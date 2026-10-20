#!/usr/bin/env python3
"""
scripts/test_wave_e_dissemination.py

Deterministic test runner & validator for Wave E public scholarship & dissemination eval fixtures.
Enforces the Wave E Dissemination Architecture Charter in compliance with §6.1
(Epistemic Honesty: Tier 3 Static Behavioral Verification):

- Validates schema completeness of evals/gold/wave_e_dissemination/cases.yaml.
- Verifies physical runtime contract anchors on disk.
- Verifies deterministic rubric discrimination (good exemplar passes, bad exemplar caught).
- Epistemically transparent: declares MODEL_BEHAVIOR_EXECUTION_PENDING.

Usage:
    python scripts/test_wave_e_dissemination.py
    pytest scripts/test_wave_e_dissemination.py
    python scripts/test_wave_e_dissemination.py --grade WAVE-E-NEG-01 --response <path_to_txt>
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = REPO_ROOT / "evals" / "gold" / "wave_e_dissemination" / "cases.yaml"

VALID_FAMILIES = {
    "VENUE_LEAKAGE",
    "COMMISSION_LEAKAGE",
    "CAUSAL_INTEGRITY",
    "COMPATIBILITY_REDIRECT",
    "VENUE_CALIBRATION",
}
VALID_SEVERITIES = {"CRITICAL", "MAJOR", "MINOR"}
VALID_CASE_KINDS = {"BEHAVIORAL_EVAL"}

REQUIRED_CASE_FIELDS = {
    "case_id",
    "family",
    "case_kind",
    "title",
    "prompt",
    "primary_owner",
    "calibration_profile",
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
    assert len(cases) >= 5, f"Expected at least 5 cases, found {len(cases)}"

    case_ids = [c.get("case_id") for c in cases]
    assert len(case_ids) == len(set(case_ids)), f"Duplicate case_ids detected: {case_ids}"

    for case in cases:
        cid = case.get("case_id", "UNKNOWN")
        missing = REQUIRED_CASE_FIELDS - set(case.keys())
        assert not missing, f"[{cid}] Missing required schema fields: {missing}"

        assert case["family"] in VALID_FAMILIES, f"[{cid}] Invalid family: {case['family']}"
        assert case["case_kind"] in VALID_CASE_KINDS, f"[{cid}] Invalid case_kind: {case['case_kind']}"
        assert case["severity"] in VALID_SEVERITIES, f"[{cid}] Invalid severity: {case['severity']}"
        assert case["primary_owner"] == "public-scholarship", (
            f"[{cid}] Expected primary_owner 'public-scholarship', got '{case['primary_owner']}'"
        )
        assert isinstance(case["runtime_anchors"], list) and len(case["runtime_anchors"]) > 0, (
            f"[{cid}] runtime_anchors must be non-empty list"
        )
        assert isinstance(case["required_behaviors"], list) and len(case["required_behaviors"]) > 0, (
            f"[{cid}] required_behaviors must be non-empty list"
        )
        assert isinstance(case["forbidden_behaviors"], list) and len(case["forbidden_behaviors"]) > 0, (
            f"[{cid}] forbidden_behaviors must be non-empty list"
        )
        assert isinstance(case["bad_expected_violations"], list) and len(case["bad_expected_violations"]) > 0, (
            f"[{cid}] bad_expected_violations must be non-empty list"
        )

        # Check regex compilability
        for req in case["required_behaviors"]:
            re.compile(req["pattern"])
        for forb in case["forbidden_behaviors"]:
            assert forb.get("severity") in VALID_SEVERITIES, f"[{cid}] Invalid forbidden severity: {forb}"
            re.compile(forb["pattern"])


def test_runtime_contract_anchoring():
    """Verify that all referenced runtime documents exist and anchor the cited rules."""
    data = load_fixtures()
    cases = data.get("cases", [])

    for case in cases:
        cid = case.get("case_id")
        for anchor in case.get("runtime_anchors", []):
            path_str = anchor["path"]
            contains_str = anchor["contains"]
            full_path = REPO_ROOT / path_str
            assert full_path.exists(), f"[{cid}] Anchor path does not exist on disk: {path_str}"

            text = full_path.read_text(encoding="utf-8")
            assert contains_str in text, (
                f"[{cid}] Target string not found in {path_str}:\n  Expected: {contains_str[:60]}..."
            )


def grade_response(case: dict[str, Any], text: str) -> tuple[bool, list[str], list[str]]:
    """
    Grades an arbitrary response against a case fixture.
    Returns: (passed, matched_required_ids, caught_forbidden_ids)
    """
    matched_req = []
    for req in case.get("required_behaviors", []):
        if re.search(req["pattern"], text):
            matched_req.append(req["id"])

    caught_forb = []
    for forb in case.get("forbidden_behaviors", []):
        if re.search(forb["pattern"], text):
            caught_forb.append(forb["id"])

    all_req_ids = [r["id"] for r in case.get("required_behaviors", [])]
    passed = (set(matched_req) == set(all_req_ids)) and (len(caught_forb) == 0)
    return passed, matched_req, caught_forb


def test_rubric_discrimination():
    """Verify that good exemplar passes completely and bad exemplar triggers expected violations."""
    data = load_fixtures()
    cases = data.get("cases", [])

    for case in cases:
        cid = case.get("case_id")
        good_text = case["good_response_exemplar"]
        bad_text = case["bad_response_exemplar"]

        # 1. Good exemplar must pass cleanly
        passed_good, matched_req, caught_forb = grade_response(case, good_text)
        all_req_ids = [r["id"] for r in case["required_behaviors"]]
        missing_req = set(all_req_ids) - set(matched_req)

        assert not missing_req, f"[{cid}] Good exemplar failed to match required behaviors: {missing_req}"
        assert not caught_forb, f"[{cid}] Good exemplar tripped forbidden behaviors: {caught_forb}"
        assert passed_good, f"[{cid}] Good exemplar did not pass cleanly"

        # 2. Bad exemplar must trigger all bad_expected_violations
        _, _, bad_caught_forb = grade_response(case, bad_text)
        expected_violations = set(case["bad_expected_violations"])
        caught_violations = set(bad_caught_forb)

        missing_violations = expected_violations - caught_violations
        assert not missing_violations, (
            f"[{cid}] Bad exemplar failed to trigger expected forbidden violations:\n"
            f"  Expected: {expected_violations}\n"
            f"  Caught:   {caught_violations}\n"
            f"  Missing:  {missing_violations}"
        )


def run_full_suite() -> bool:
    print("=" * 70)
    print("ARS WAVE E — DISSEMINATION ARCHITECTURE STATIC BEHAVIORAL EVAL SUITE")
    print("=" * 70)

    try:
        data = load_fixtures()
        cases = data.get("cases", [])
        print(f"Loaded {len(cases)} behavioral fixtures from {CASES_PATH.relative_to(REPO_ROOT)}")

        print("\n1. Testing Schema and Completeness...")
        test_schema_and_completeness()
        print(f"   [PASS] {len(cases)}/{len(cases)} cases comply with strict schema.")

        print("\n2. Testing Runtime Contract Physical Anchoring...")
        test_runtime_contract_anchoring()
        total_anchors = sum(len(c.get("runtime_anchors", [])) for c in cases)
        print(f"   [PASS] {total_anchors}/{total_anchors} runtime anchors physically verified on disk.")

        print("\n3. Testing Rubric Discrimination (Good vs Bad Exemplars)...")
        test_rubric_discrimination()
        print(f"   [PASS] {len(cases)}/{len(cases)} rubrics discriminate good from bad exemplars cleanly.")

        print("\n" + "-" * 70)
        print("EPISTEMIC HONESTY STATUS REPORT (Wave E §6.1 / D5 §17):")
        print("  - FIXTURE_IMPLEMENTED:              YES (5/5 cases)")
        print("  - SCHEMA_ENFORCED:                  YES (strict types & fields)")
        print("  - RUNTIME_CONTRACT_ANCHORED:        YES (verified on disk)")
        print("  - RUBRIC_DISCRIMINATION_VERIFIED:   YES (clean separation)")
        print("  - MODEL_BEHAVIOR_EXECUTION_PENDING: YES (offline static verification only)")
        print("-" * 70)
        print("\nALL WAVE E STATIC EVAL CHECKS PASSED.")
        return True

    except AssertionError as e:
        print(f"\n[FAIL] Assertion failed: {e}")
        return False
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Wave E Dissemination Behavioral Eval Runner")
    parser.add_argument("--grade", type=str, help="Case ID to grade against")
    parser.add_argument("--response", type=Path, help="Path to text response to grade")
    args = parser.parse_args()

    if args.grade:
        if not args.response or not args.response.exists():
            print(f"Error: --response file '{args.response}' does not exist.")
            sys.exit(1)
        data = load_fixtures()
        matches = [c for c in data.get("cases", []) if c.get("case_id") == args.grade]
        if not matches:
            print(f"Error: Case ID '{args.grade}' not found.")
            sys.exit(1)
        case = matches[0]
        text = args.response.read_text(encoding="utf-8")
        passed, matched_req, caught_forb = grade_response(case, text)
        print(f"Grade Result for {args.grade}: {'PASS' if passed else 'FAIL'}")
        print(f"  Matched Required: {matched_req}")
        print(f"  Caught Forbidden: {caught_forb}")
        sys.exit(0 if passed else 1)

    success = run_full_suite()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
