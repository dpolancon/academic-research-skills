#!/usr/bin/env python3
"""
scripts/revision_guard.py

Lightweight deterministic editorial governance revision verification engine.
Enforces change-control boundaries, source identity, and unresolved decision tracking.

Does NOT evaluate scholarly validity, econometric identification, or literary quality.
Runs strictly offline using Python standard library and jsonschema.
"""

from __future__ import annotations

import os
import sys
import json
import hashlib
import datetime
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Set

from jsonschema import Draft202012Validator, FormatChecker

VERSION = "1.0.0"
REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = REPO_ROOT / "shared" / "contracts" / "passport"
EXIT_CODES = {"PASS": 0, "FAIL": 1, "INDETERMINATE": 2}


def make_format_checker() -> FormatChecker:
    """Creates a FormatChecker with ISO-8601 date-time support."""
    fc = FormatChecker()

    @fc.checks("date-time")
    def check_datetime(val: Any) -> bool:
        if not isinstance(val, str):
            return True
        try:
            # Handle standard ISO-8601 timestamps
            datetime.datetime.fromisoformat(val.replace("Z", "+00:00"))
            return True
        except Exception:
            return False

    return fc


def validator(name: str) -> Draft202012Validator:
    """Loads a JSON schema from shared/contracts/passport and returns a validator."""
    schema_path = SCHEMAS / f"{name}.schema.json"
    if not schema_path.is_file():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=make_format_checker())


def canonical_digest(value: Any) -> str:
    """Computes a deterministic SHA-256 digest of a JSON-serializable structure."""
    data = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def _normalize_content(item: Any) -> bytes:
    """Converts a snapshot content entry to raw bytes."""
    if isinstance(item, bytes):
        return item
    if isinstance(item, str):
        return item.encode("utf-8")
    if isinstance(item, dict):
        if "content" in item:
            return _normalize_content(item["content"])
        if "content_text" in item:
            return item["content_text"].encode("utf-8")
    raise ValueError(f"Cannot normalize snapshot content of type {type(item)}")


def verify(
    governance: Optional[Dict[str, Any]],
    *,
    snapshots: Optional[Dict[str, Any]] = None,
    baseline_snapshots: Optional[Dict[str, Any]] = None,
    previous: Optional[Dict[str, Any]] = None,
    trusted_approvals: Optional[List[Any]] = None,
    evidence: Optional[List[Any]] = None,
    prior_verification: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Pure deterministic revision verification.
    Evaluates change-control compliance against the governance sidecar contract.
    """
    checks: List[Dict[str, str]] = []
    bindings: Dict[str, str] = {}
    accepted_evidence: List[Dict[str, Any]] = []
    active_invariants: List[str] = []
    freshness = "NOT_EVALUATED"

    def add_check(cid: str, status: str, detail: str) -> None:
        checks.append({"check_id": cid, "status": status, "detail": detail})

    # 1. Governance contract presence
    if governance is None:
        add_check("governance_presence", "INDETERMINATE", "No governance sidecar provided.")
        return _build_result("INDETERMINATE", "optional", "unknown", 0, 0, None, checks, bindings, active_invariants, accepted_evidence, freshness)

    # 2. Schema validation
    gv = validator("editorial_governance")
    errors = list(gv.iter_errors(governance))
    if errors:
        first_err = errors[0]
        err_path = "/".join(map(str, first_err.absolute_path)) or "root"
        add_check("schema_validation", "FAIL", f"Schema violation at {err_path}: {first_err.message}")
        gov_id = governance.get("governance_id", "malformed")
        return _build_result("FAIL", "optional", gov_id, 0, 0, None, checks, bindings, active_invariants, accepted_evidence, freshness)

    gov_id = governance["governance_id"]
    release_policy = governance.get("release_policy", "optional")
    expected_source_hash = governance.get("source_hash")
    bindings["governance"] = canonical_digest(governance)

    # 3. Decision extraction & three-axis analysis
    raw_decisions = governance.get("decisions", [])
    active_decision_count = len(raw_decisions)
    unresolved_decisions: List[str] = []
    normalized_decisions: List[Dict[str, Any]] = []

    for d in raw_decisions:
        did = d.get("decision_id", "unknown")
        # Handle nested payload if present (candidate legacy) or flat decision
        p = d.get("payload", d)

        # Three-axis extraction
        res = d.get("resolution") or p.get("concern_resolution_status")
        auth = d.get("authorization") or p.get("authorization_status")
        act = d.get("action") or p.get("adjudicated_action")

        # Normalize resolution
        if res in ("ACCEPT", "RESOLVED", "DELIBERATE_LIMITATION"):
            norm_res = "ACCEPT"
        elif res in ("REJECT", "UNRESOLVABLE", "REVIEWER_DISAGREE"):
            norm_res = "REJECT"
        elif res in ("DEFER",):
            norm_res = "DEFER"
        else:
            norm_res = "UNRESOLVED"

        # Normalize authorization
        if auth in ("ALLOWED", "AUTHORIZED"):
            norm_auth = "ALLOWED"
        elif auth in ("FORBIDDEN", "HELD", "BLOCKED"):
            norm_auth = "FORBIDDEN"
        elif auth in ("CONDITIONAL",):
            norm_auth = "CONDITIONAL"
        else:
            norm_auth = "NOT_SPECIFIED"

        # Normalize action
        if act in ("IMPLEMENTED", "REWRITE", "REMOVE", "RELOCATE"):
            norm_act = "IMPLEMENTED"
        elif act in ("NOT_IMPLEMENTED", "RETAIN"):
            norm_act = "NOT_IMPLEMENTED"
        elif act in ("PARTIAL",):
            norm_act = "PARTIAL"
        elif act in ("OUT_OF_SCOPE_CHANGE",):
            norm_act = "OUT_OF_SCOPE_CHANGE"
        else:
            norm_act = "NOT_IMPLEMENTED"

        if norm_res == "UNRESOLVED" or norm_auth in ("NOT_SPECIFIED",) or norm_auth == "CONDITIONAL":
            unresolved_decisions.append(did)

        normalized_decisions.append({
            "decision_id": did,
            "resolution": norm_res,
            "authorization": norm_auth,
            "action": norm_act,
            "scope": p.get("scope", {}),
            "rationale": p.get("rationale", ""),
            "invariants": p.get("invariants", []),
            "permitted_changes": p.get("permitted_changes", []),
        })

    unresolved_decision_count = len(unresolved_decisions)

    # If unresolved decisions exist, surface info check
    if unresolved_decision_count > 0:
        add_check(
            "unresolved_decisions",
            "INDETERMINATE",
            f"{unresolved_decision_count} unresolved or conditional decision(s) remaining: {', '.join(unresolved_decisions)}",
        )

    # 4. Snapshot normalization & source identity check
    current_bytes: Optional[bytes] = None
    baseline_bytes: Optional[bytes] = None
    observed_source_hash: Optional[str] = None

    if baseline_snapshots:
        first_key = next(iter(baseline_snapshots))
        baseline_bytes = _normalize_content(baseline_snapshots[first_key])
        observed_source_hash = hashlib.sha256(baseline_bytes).hexdigest()
        bindings["baseline_source_hash"] = observed_source_hash

        if expected_source_hash and observed_source_hash != expected_source_hash:
            add_check(
                "source_identity",
                "INDETERMINATE",
                f"Source hash mismatch: contract expected {expected_source_hash}, baseline observed {observed_source_hash}",
            )

    if snapshots:
        first_key = next(iter(snapshots))
        current_bytes = _normalize_content(snapshots[first_key])
        bindings["current_source_hash"] = hashlib.sha256(current_bytes).hexdigest()

    # 5. Bounded Diff & Change Authorization Checks
    if baseline_bytes is not None and current_bytes is not None:
        try:
            base_text = baseline_bytes.decode("utf-8")
            curr_text = current_bytes.decode("utf-8")
        except UnicodeDecodeError:
            add_check("text_encoding", "INDETERMINATE", "Artifact content is not valid UTF-8.")
            base_text = ""
            curr_text = ""

        if base_text and curr_text:
            authorized_base_spans: List[Tuple[int, int]] = []
            authorized_curr_spans: List[Tuple[int, int]] = []
            whole_doc_authorized = False
            anchor_missing_encountered = False

            for nd in normalized_decisions:
                did = nd["decision_id"]
                scope = nd.get("scope", {})
                locations = scope.get("locations") or scope.get("anchors") or []

                # Mandatory unimplemented decision check
                if nd["resolution"] == "ACCEPT" and nd["action"] == "NOT_IMPLEMENTED":
                    # Check if decision was mandatory
                    add_check(
                        "unimplemented_mandatory_decision",
                        "FAIL",
                        f"Accepted mandatory decision was not implemented: {did}",
                    )

                # Check forbidden additions / rejected changes
                if nd["resolution"] == "REJECT" or nd["authorization"] == "FORBIDDEN":
                    for loc in locations:
                        forbidden_txt = loc.get("forbidden_text")
                        if forbidden_txt and forbidden_txt in curr_text:
                            add_check(
                                "forbidden_change",
                                "FAIL",
                                f"Forbidden text appears in revision ({did}): '{forbidden_txt}'",
                            )

                if scope.get("whole_document"):
                    if nd["authorization"] == "ALLOWED" and nd["action"] in ("IMPLEMENTED", "REWRITE"):
                        whole_doc_authorized = True

                # Process location anchors
                for loc in locations:
                    start_anchor = loc.get("start")
                    end_anchor = loc.get("end")

                    if start_anchor is None and end_anchor is None:
                        continue

                    # Anchor presence check
                    in_base = (start_anchor in base_text) and (end_anchor in base_text)
                    in_curr = (start_anchor in curr_text) and (end_anchor in curr_text)

                    if not in_base or not in_curr:
                        anchor_missing_encountered = True
                        add_check(
                            "scope_anchor_missing",
                            "INDETERMINATE",
                            f"Location anchor missing or moved ({loc.get('location_id', did)}): start={start_anchor!r}, end={end_anchor!r}",
                        )
                        continue

                    b_lo = base_text.index(start_anchor) + len(start_anchor)
                    b_hi = base_text.index(end_anchor)
                    c_lo = curr_text.index(start_anchor) + len(start_anchor)
                    c_hi = curr_text.index(end_anchor)

                    if b_hi >= b_lo and c_hi >= c_lo:
                        if nd["authorization"] == "ALLOWED" and nd["action"] in ("IMPLEMENTED", "REWRITE", "REMOVE"):
                            authorized_base_spans.append((b_lo, b_hi))
                            authorized_curr_spans.append((c_lo, c_hi))

            # Mask authorized regions and check outside text only if anchors were intact
            has_conditional = any(nd["authorization"] == "CONDITIONAL" for nd in normalized_decisions)
            if has_conditional:
                add_check(
                    "conditional_authorization",
                    "INDETERMINATE",
                    "Conditional authorization requires human interpretation to verify compliance.",
                )

            if not whole_doc_authorized and not anchor_missing_encountered and not has_conditional:
                unmasked_base = _mask_spans(base_text, authorized_base_spans)
                unmasked_curr = _mask_spans(curr_text, authorized_curr_spans)

                if unmasked_base != unmasked_curr:
                    add_check(
                        "unauthorized_change_outside_scope",
                        "FAIL",
                        "Source document modified outside authorized anchor regions.",
                    )

    # 6. Legacy structural / trusted_approvals compatibility
    if trusted_approvals is not None and isinstance(trusted_approvals, list):
        bindings["trusted_approvals"] = canonical_digest(trusted_approvals)
    if previous is not None and isinstance(previous, dict):
        bindings["previous"] = canonical_digest(previous)
        if previous.get("governance_id") != gov_id:
            add_check("history", "FAIL", "Governance identity changed across revisions.")

    # 7. Aggregate overall verdict
    statuses = {c["status"] for c in checks}
    if "FAIL" in statuses:
        overall = "FAIL"
    elif "INDETERMINATE" in statuses:
        overall = "INDETERMINATE"
    else:
        overall = "PASS"

    if not checks:
        add_check("change_control", "PASS", "All change-control conditions satisfied.")

    return _build_result(
        overall,
        release_policy,
        gov_id,
        active_decision_count,
        unresolved_decision_count,
        observed_source_hash or expected_source_hash,
        checks,
        bindings,
        active_invariants,
        accepted_evidence,
        freshness,
    )


def _mask_spans(text: str, spans: List[Tuple[int, int]]) -> str:
    """Replaces spans of text with a deterministic sentinel to isolate outside text."""
    if not spans:
        return text
    merged: List[List[int]] = []
    for lo, hi in sorted(spans):
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    parts = []
    idx = 0
    for lo, hi in merged:
        parts.append(text[idx:lo])
        parts.append("\x00AUTHORIZED_REGION\x00")
        idx = hi
    parts.append(text[idx:])
    return "".join(parts)


def _build_result(
    overall: str,
    release_policy: str,
    governance_id: str,
    active_count: int,
    unresolved_count: int,
    source_hash: Optional[str],
    checks: List[Dict[str, str]],
    bindings: Dict[str, str],
    active_invariants: List[str],
    evidence: List[Dict[str, Any]],
    freshness: str,
) -> Dict[str, Any]:
    """Assembles structured verification report compliant with revision_verification.schema.json."""
    passport_summary = {
        "governance_id": governance_id,
        "verification_verdict": overall,
        "active_decision_count": active_count,
        "unresolved_decision_count": unresolved_count,
        "source_hash": source_hash,
    }

    result = {
        "schema_version": "1.0",
        "verifier_version": VERSION,
        "governance_id": governance_id,
        "assurance_scope": "CHANGE_CONTROL",
        "release_certified": False,
        "release_policy": release_policy,
        "overall": overall,
        "verdict": overall,
        "passport_summary": passport_summary,
        "summary": passport_summary,
        "freshness": freshness,
        "bindings": bindings,
        "active_invariant_ids": active_invariants,
        "unresolved_decisions": [],
        "checks": checks,
        "evidence": evidence,
    }

    # Validate output report against revision_verification.schema.json
    rv = validator("revision_verification")
    out_errors = list(rv.iter_errors(result))
    if out_errors:
        sys.stderr.write(f"Warning: verification result schema validation error: {out_errors[0].message}\n")

    return result


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="ARS Lightweight Editorial Governance Revision Guard (Deterministic & Offline)"
    )
    parser.add_argument(
        "--request",
        type=Path,
        help="Path to JSON verification request file.",
    )
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path("."),
        help="Workspace directory for relative artifact paths.",
    )
    parser.add_argument(
        "--governance",
        type=Path,
        help="Path to editorial governance sidecar JSON file.",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        help="Path to baseline source document.",
    )
    parser.add_argument(
        "--current",
        type=Path,
        help="Path to revised current source document.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit output strictly as formatted JSON.",
    )

    args = parser.parse_args(argv)

    request_data: Dict[str, Any] = {}

    if args.request:
        if not args.request.is_file():
            sys.stderr.write(f"Error: request file '{args.request}' not found.\n")
            return 2
        with open(args.request, "r", encoding="utf-8") as f:
            request_data = json.load(f)
    elif args.governance:
        if not args.governance.is_file():
            sys.stderr.write(f"Error: governance file '{args.governance}' not found.\n")
            return 2
        with open(args.governance, "r", encoding="utf-8") as f:
            request_data["governance"] = json.load(f)
        if args.baseline and args.baseline.is_file():
            request_data["baseline_snapshots"] = {
                "manuscript": {"kind": "source", "content": args.baseline.read_bytes()}
            }
        if args.current and args.current.is_file():
            request_data["snapshots"] = {
                "manuscript": {"kind": "source", "content": args.current.read_bytes()}
            }
    else:
        if sys.stdin.isatty():
            parser.print_help()
            return 0
        try:
            request_data = json.load(sys.stdin)
        except Exception as e:
            sys.stderr.write(f"Error reading JSON from stdin: {e}\n")
            return 2

    # Execute verification
    result = verify(**request_data)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return EXIT_CODES.get(result["overall"], 2)


if __name__ == "__main__":
    sys.exit(main())
