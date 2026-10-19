#!/usr/bin/env python3
"""
scripts/test_wave_d_behavioral_evals.py

Deterministic test runner & validator for Wave D cross-domain behavioral eval fixtures.
Enforces the Wave D5 Mission Charter in compliance with §17 (No Fake Behavioral Enforcement)
and Wave D5.1 Evaluation-Governance Micro-Repairs:
- D5.1-R1: Truthful runtime-contract stratification (no false 31/31 overclaim)
- D5.1-R2: E3-B inferential jurisdiction (THEORETICAL MODEL != AUTOMATIC ESTIMATOR)
- D5.1-R3: E6-D shared protocol vs. executable workflow owner distinction
- D5.1-R4: E7 strict no-owner enforcement (any existing component assignment fails)
- D5.1-R5: E9 meta-eval typing (case_kind: META_EVAL, primary_owner: N/A, no phantom capability)
- D5.1-R6: Gold-fixture schema completeness (enforcement fields cannot silently disappear)

Usage:
    python scripts/test_wave_d_behavioral_evals.py
    pytest scripts/test_wave_d_behavioral_evals.py
    python scripts/test_wave_d_behavioral_evals.py --grade E1-A --response <path_to_txt>
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = REPO_ROOT / "evals" / "gold" / "wave_d_behavioral" / "cases.yaml"

VALID_FAMILIES = {"E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"}
VALID_SEVERITIES = {"CRITICAL", "MAJOR", "MINOR"}
VALID_CASE_KINDS = {"BEHAVIORAL_EVAL", "META_EVAL"}

CANONICAL_OWNERS = {
    "political-economy-research",
    "applied-econometrics-pe",
    "heterodox-macro-modeling",
    "historical_source_criticism_protocol",
    "econ-write",
    "academic-paper",
    "academic-paper-reviewer",
    "academic-pipeline",
    "deep-research",
    "UNASSIGNED_CAPABILITY_GAP",
}

REQUIRED_CASE_FIELDS = {
    "case_id",
    "family",
    "case_kind",
    "title",
    "prompt",
    "primary_owner",
    "governing_protocol",
    "allowed_consumers",
    "forbidden_owner",
    "expected_boundary",
    "severity",
    "source_wave",
    "invariants",
    "runtime_anchors",
    "required_behaviors",
    "forbidden_behaviors",
    "bad_expected_violations",
    "good_response_exemplar",
    "bad_response_exemplar",
}

REQUIRED_META_EVAL_FIELDS = {
    "completion_report",
    "audited_artifact_violating",
    "audited_artifact_clean",
    "expected_detected_violation",
}


def load_fixtures(path: Path = CASES_PATH) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Fixture file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict) or "cases" not in data:
        raise ValueError(f"Invalid fixture format in {path}: 'cases' key missing.")
    return data


def test_schema_and_completeness():
    """Verify that every gold fixture carries all required enforcement fields and valid types."""
    data = load_fixtures()
    cases = data.get("cases", [])
    assert len(cases) == 31, f"Expected exactly 31 cases, found {len(cases)}"

    case_ids = [c.get("case_id") for c in cases]
    assert len(case_ids) == len(set(case_ids)), f"Duplicate case_ids detected: {case_ids}"

    found_families = set()
    for case in cases:
        cid = case.get("case_id")
        fam = case.get("family")
        found_families.add(fam)
        assert fam in VALID_FAMILIES, f"Case {cid} has invalid family: {fam}"

        # 1. Mandatory presence of all enforcement-relevant fields (D5.1-R6)
        for field in REQUIRED_CASE_FIELDS:
            assert field in case, f"Case {cid} missing required enforcement field: {field}"

        ckind = case.get("case_kind")
        assert ckind in VALID_CASE_KINDS, f"Case {cid} has invalid case_kind: {ckind}"

        sev = case.get("severity")
        assert sev in VALID_SEVERITIES, f"Case {cid} has invalid severity: {sev}"

        # 2. Canonical owner validation & meta-eval typing (D5.1-R5)
        owner = case.get("primary_owner")
        if ckind == "META_EVAL":
            assert owner in {"N/A", "NONE"}, (
                f"Meta-eval {cid} must have primary_owner 'N/A', got: {owner}"
            )
            for mfield in REQUIRED_META_EVAL_FIELDS:
                assert mfield in case and case[mfield], (
                    f"Meta-eval {cid} missing required meta-field: {mfield}"
                )
        else:
            assert owner in CANONICAL_OWNERS, f"Case {cid} has non-canonical primary_owner: {owner}"
            assert owner != "ARTIFACT_ADJUDICATION", (
                f"Case {cid} uses phantom capability 'ARTIFACT_ADJUDICATION'"
            )

        # 3. Invariants must be non-empty list
        invs = case.get("invariants", [])
        assert isinstance(invs, list) and len(invs) > 0, (
            f"Case {cid} invariants must be non-empty list"
        )

        # 4. Runtime anchors must be list
        anchors = case.get("runtime_anchors")
        assert isinstance(anchors, list), f"Case {cid} runtime_anchors must be list"
        for a in anchors:
            assert isinstance(a, dict) and "path" in a and "contains" in a, (
                f"Case {cid} anchor malformed: {a}"
            )
            assert a["path"] and a["contains"], f"Case {cid} anchor empty fields: {a}"

        # 5. Required behaviors validation
        rbs = case.get("required_behaviors")
        assert isinstance(rbs, list), f"Case {cid} required_behaviors must be list"
        if len(rbs) == 0:
            assert case.get("routing_assertion") is True, (
                f"Case {cid} has empty required_behaviors but routing_assertion is not True"
            )
        for b in rbs:
            assert "id" in b and "pattern" in b, f"Case {cid} required_behavior malformed: {b}"
            re.compile(b["pattern"])

        # 6. Forbidden behaviors validation
        fbs = case.get("forbidden_behaviors")
        assert isinstance(fbs, list), f"Case {cid} forbidden_behaviors must be list"
        for fb in fbs:
            assert "id" in fb and "pattern" in fb and "severity" in fb, (
                f"Case {cid} forbidden_behavior malformed: {fb}"
            )
            assert fb["severity"] in VALID_SEVERITIES, (
                f"Case {cid} forbidden_behavior has invalid severity: {fb['severity']}"
            )
            re.compile(fb["pattern"])

        # 7. Bad expected violations validation: cannot be empty, must resolve to checkable rules
        bevs = case.get("bad_expected_violations")
        assert isinstance(bevs, list) and len(bevs) > 0, (
            f"Case {cid} bad_expected_violations must be a non-empty list"
        )
        known_fb_ids = {fb["id"] for fb in fbs}
        known_rb_missing = {f"{b['id']}:missing" for b in rbs}
        known_forbidden_owners = {f"wrong_owner:{fo}" for fo in case.get("forbidden_owner", [])}
        known_routing_missing = (
            {f"primary_owner:{case.get('primary_owner')}:missing"}
            if case.get("routing_assertion")
            else set()
        )
        known_gap_violations = {
            f"assigned_unowned_gap:{fo}" for fo in case.get("forbidden_owner", [])
        }

        valid_rules = (
            known_fb_ids
            | known_rb_missing
            | known_forbidden_owners
            | known_routing_missing
            | known_gap_violations
        )
        for bev in bevs:
            assert (
                bev in valid_rules
                or bev.startswith("wrong_owner:")
                or bev.startswith("assigned_unowned_gap:")
            ), (
                f"Case {cid} bad_expected_violations contains unresolved violation rule: {bev!r}. "
                f"Valid rules for case: {valid_rules}"
            )

    assert found_families == VALID_FAMILIES, (
        f"Missing families: {VALID_FAMILIES - found_families}"
    )


def get_runtime_contract_stats(data: dict[str, Any] | None = None) -> dict[str, Any]:
    """Collect runtime contract anchor validation statistics across all cases."""
    if data is None:
        data = load_fixtures()
    cases = data.get("cases", [])
    anchored_cids = []
    unanchored_cids = []
    anchors_checked = 0

    for case in cases:
        cid = case.get("case_id")
        anchors = case.get("runtime_anchors", [])
        if anchors and isinstance(anchors, list) and len(anchors) > 0:
            for anchor in anchors:
                rel_path = anchor.get("path")
                target_str = anchor.get("contains")
                assert rel_path and target_str, f"Case {cid} anchor missing path or contains: {anchor}"

                file_path = REPO_ROOT / rel_path
                assert file_path.exists(), f"Case {cid} anchor file missing on disk: {rel_path}"

                content = file_path.read_text(encoding="utf-8")
                assert target_str in content, (
                    f"Case {cid} anchor string not found in {rel_path}: {target_str!r}"
                )
                anchors_checked += 1
            anchored_cids.append(cid)
        else:
            unanchored_cids.append(cid)

    return {
        "total_cases": len(cases),
        "anchored_cases": len(anchored_cids),
        "anchors_checked": anchors_checked,
        "unanchored_cases": len(unanchored_cids),
        "anchored_cids": anchored_cids,
        "unanchored_cids": unanchored_cids,
    }


def test_runtime_contract_anchors():
    """Verify live runtime skill/protocol files and ensure truthful stratification (D5.1-R1)."""
    stats = get_runtime_contract_stats()
    assert stats["anchors_checked"] >= 15, (
        f"Expected at least 15 runtime anchors, checked {stats['anchors_checked']}"
    )
    assert stats["anchored_cases"] > 0, "No anchored cases found"
    # D5.1-R1 honesty guard: Never assert 31/31 anchored when unanchored cases exist
    assert stats["anchored_cases"] == 22, (
        f"Expected exactly 22 anchored cases, got {stats['anchored_cases']}"
    )
    assert stats["anchors_checked"] == 28, (
        f"Expected exactly 28 anchors checked, got {stats['anchors_checked']}"
    )
    assert stats["unanchored_cases"] == 9, (
        f"Expected exactly 9 unanchored cases, got {stats['unanchored_cases']}"
    )


def grade_response(case: dict[str, Any], text: str) -> dict[str, Any]:
    """Grade a response text against a case's routing, required, and forbidden rubrics."""
    cid = case.get("case_id")
    fam = case.get("family")
    missing_required = []
    tripped_forbidden = []

    # 1. Routing assertions for E6 family (or cases with routing_assertion)
    if case.get("routing_assertion"):
        expected_owner = case.get("primary_owner")
        forbidden_owners = case.get("forbidden_owner", [])

        # Check expected owner presence (match complete kebab token)
        if expected_owner and expected_owner not in {"N/A", "NONE", "UNASSIGNED_CAPABILITY_GAP"}:
            if not re.search(
                rf"(?i)primary owner:\s*`?{re.escape(expected_owner)}(?:`|(?=[^\w-]))", text
            ):
                missing_required.append(f"primary_owner:{expected_owner}")

        # Check forbidden owner presence (match complete kebab token)
        for f_owner in forbidden_owners:
            if re.search(rf"(?i)primary owner:\s*`?{re.escape(f_owner)}(?:`|(?=[^\w-]))", text):
                tripped_forbidden.append(f"wrong_owner:{f_owner}")

    # 2. Strict unassigned capability gap enforcement (D5.1-R4)
    if case.get("primary_owner") == "UNASSIGNED_CAPABILITY_GAP":
        # Check forbidden owners explicitly
        for f_owner in case.get("forbidden_owner", []):
            if re.search(rf"(?i)primary owner:\s*`?{re.escape(f_owner)}(?:`|(?=[^\w-]))", text):
                tripped_forbidden.append(f"wrong_owner:{f_owner}")

        # Detect any attempt to assign an unauthorized primary owner
        m = re.search(r"(?i)primary owner:\s*`?([a-z0-9_-]+)`?", text)
        if m:
            claimed_owner = m.group(1).lower()
            if claimed_owner not in {"none", "n/a", "unassigned", "unassigned_capability_gap"}:
                if f"wrong_owner:{claimed_owner}" not in tripped_forbidden:
                    tripped_forbidden.append(f"assigned_unowned_gap:{claimed_owner}")

    # 3. Required behaviors
    for req in case.get("required_behaviors", []):
        rid = req.get("id")
        pat = req.get("pattern")
        if not re.search(pat, text):
            missing_required.append(rid)

    # 4. Forbidden behaviors
    for forb in case.get("forbidden_behaviors", []):
        fid = forb.get("id")
        pat = forb.get("pattern")
        if re.search(pat, text):
            tripped_forbidden.append(fid)

    passed = (len(missing_required) == 0) and (len(tripped_forbidden) == 0)
    return {
        "case_id": cid,
        "family": fam,
        "passed": passed,
        "missing_required": missing_required,
        "tripped_forbidden": tripped_forbidden,
    }


def test_exemplar_rubric_discrimination():
    """Verify that every good exemplar PASSES and every bad exemplar FAILS with expected violations."""
    data = load_fixtures()
    cases = data.get("cases", [])

    for case in cases:
        cid = case.get("case_id")
        good_text = case.get("good_response_exemplar", "")
        bad_text = case.get("bad_response_exemplar", "")
        expected_bad_violations = set(case.get("bad_expected_violations", []))

        # Test good exemplar
        good_grade = grade_response(case, good_text)
        assert good_grade["passed"], (
            f"Case {cid} good exemplar FAILED grading! "
            f"Missing required: {good_grade['missing_required']}, "
            f"Tripped forbidden: {good_grade['tripped_forbidden']}"
        )

        # Test bad exemplar
        bad_grade = grade_response(case, bad_text)
        assert not bad_grade["passed"], (
            f"Case {cid} bad exemplar unexpectedly PASSED grading!"
        )

        actual_bad_violations = set(
            bad_grade["tripped_forbidden"]
            + [f"{r}:missing" for r in bad_grade["missing_required"]]
        )
        # Check that expected bad violations were caught
        if expected_bad_violations:
            missing_detection = expected_bad_violations - actual_bad_violations
            assert not missing_detection, (
                f"Case {cid} bad exemplar failed to trigger expected violations: {missing_detection}. "
                f"Actual caught: {actual_bad_violations}"
            )


def test_e9_self_ratification_trap_meta_eval():
    """
    Executes the E9-A meta-eval:
    Tests the invariant 'SELF-REPORTED LEARNING IS NOT SELF-RATIFYING'.
    Verifies that:
    1. A completion report claiming full inheritance is NOT accepted as sufficient evidence.
    2. The underlying artifact is directly audited against the rubric.
    3. The violating artifact fails with the exact detected violation ('primary_wins').
    4. The clean artifact passes.
    """
    data = load_fixtures()
    cases_by_id = {c["case_id"]: c for c in data.get("cases", [])}
    assert "E9-A" in cases_by_id, "Case E9-A missing from fixture suite!"
    e9_case = cases_by_id["E9-A"]
    e4a_case = cases_by_id["E4-A"]

    # In E9-A, the completion report claims full inheritance:
    comp_report = e9_case["completion_report"]
    violating_artifact = e9_case["audited_artifact_violating"]
    clean_artifact = e9_case["audited_artifact_clean"]

    # If an evaluator only trusted the completion report, it would falsely pass:
    assert "All prior architectural lessons were successfully inherited" in comp_report

    # But the artifact contains a concrete violation of E4-A (primary > secondary):
    violating_grade = grade_response(e4a_case, violating_artifact)
    assert not violating_grade["passed"], "Violating artifact unexpectedly passed E4-A rubric!"
    assert "primary_wins" in violating_grade["tripped_forbidden"], (
        f"Failed to detect expected violation 'primary_wins' in violating artifact. "
        f"Detected: {violating_grade['tripped_forbidden']}"
    )

    # Auditing the clean artifact:
    clean_grade = grade_response(e4a_case, clean_artifact)
    assert clean_grade["passed"], (
        f"Clean artifact failed E4-A rubric! "
        f"Missing: {clean_grade['missing_required']}, "
        f"Tripped: {clean_grade['tripped_forbidden']}"
    )

    # Now verify that E9-A's own exemplars discriminate properly
    e9_good_grade = grade_response(e9_case, e9_case["good_response_exemplar"])
    assert e9_good_grade["passed"], f"E9-A good exemplar failed: {e9_good_grade}"

    e9_bad_grade = grade_response(e9_case, e9_case["bad_response_exemplar"])
    assert not e9_bad_grade["passed"], "E9-A bad exemplar unexpectedly passed!"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Wave D5 Cross-Domain Behavioral Eval Runner")
    parser.add_argument("--grade", help="Case ID to grade (e.g., E1-A)")
    parser.add_argument("--response", type=Path, help="Path to text response file to grade")
    args = parser.parse_args(argv)

    if args.grade:
        if not args.response or not args.response.exists():
            print(f"Error: Response file {args.response} not found.", file=sys.stderr)
            return 2
        data = load_fixtures()
        cases_by_id = {c["case_id"]: c for c in data.get("cases", [])}
        if args.grade not in cases_by_id:
            print(f"Error: Unknown case ID {args.grade}", file=sys.stderr)
            return 2
        text = args.response.read_text(encoding="utf-8")
        grade = grade_response(cases_by_id[args.grade], text)
        print(yaml.safe_dump(grade, sort_keys=False))
        return 0 if grade["passed"] else 1

    print("=" * 70)
    print("RUNNING WAVE D5 CROSS-DOMAIN BEHAVIORAL EVAL SUITE")
    print("=" * 70)

    try:
        print("[1/4] Validating schema and case completeness...")
        test_schema_and_completeness()
        print("      PASS: 31 cases across 9 families (E1–E9) validated.")

        print("[2/4] Validating runtime contract anchors on disk...")
        test_runtime_contract_anchors()
        stats = get_runtime_contract_stats()
        print(
            f"      PASS: {stats['anchored_cases']}/{stats['total_cases']} cases anchored "
            f"({stats['anchors_checked']} anchors confirmed across runtime files)."
        )
        print(
            f"      INFO: {stats['unanchored_cases']}/{stats['total_cases']} cases classified as N/A "
            f"(NOT CONTRACT-ANCHORED: {', '.join(stats['unanchored_cids'])})."
        )

        print("[3/4] Validating exemplar rubric discrimination...")
        test_exemplar_rubric_discrimination()
        print("      PASS: 31 good exemplars passed; 31 bad exemplars caught.")

        print("[4/4] Executing E9 Self-Ratification Trap meta-eval...")
        test_e9_self_ratification_trap_meta_eval()
        print("      PASS: Meta-eval confirmed; report claims do not self-ratify.")

        print("=" * 70)
        print("ALL WAVE D5 BEHAVIORAL EVAL CHECKS PASSED (DETERMINISTIC VERIFICATION)")
        print("ENFORCEMENT STATUS:")
        print("  - FIXTURE IMPLEMENTED:             31/31 CASES")
        print("  - SCHEMA ENFORCED:                 31/31 CASES")
        print(
            f"  - RUNTIME CONTRACT ANCHORED:       {stats['anchored_cases']}/{stats['total_cases']} CASES "
            f"({stats['anchors_checked']} ANCHORS CHECKED)"
        )
        print(
            f"  - RUNTIME CONTRACT UNANCHORED:     {stats['unanchored_cases']}/{stats['total_cases']} CASES "
            f"(N/A — NOT CONTRACT-ANCHORED)"
        )
        print("  - RUBRIC DISCRIMINATION VERIFIED:  31/31 CASES")
        print("  - MODEL-BEHAVIOR EXECUTION:        PENDING (NO FAKE EXECUTION)")
        print("=" * 70)
        return 0
    except AssertionError as err:
        print(f"\n[FAIL] Assertion error: {err}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"\n[ERROR] Unexpected error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
