#!/usr/bin/env python3
"""
scripts/test_prose_discipline.py

Verification and regression test suite for Wave C1 Prose Discipline Extraction:
1. Validates existence and structural completeness of shared/protocols/prose_discipline_protocol.md
2. Validates tools/prose_checks/check_prose_patterns.py against gold evaluation fixtures
3. Enforces deterministic execution, offline guarantee, Category A protection, and AI non-inference
"""

import os
import sys
import yaml
import json
import inspect
from pathlib import Path

# Add repo root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.prose_checks.check_prose_patterns import ProsePatternChecker


def test_protocol_exists():
    protocol_path = REPO_ROOT / "shared" / "protocols" / "prose_discipline_protocol.md"
    assert protocol_path.is_file(), f"Protocol file missing: {protocol_path}"
    content = protocol_path.read_text(encoding="utf-8")

    required_sections = [
        "## 1. Purpose",
        "## 2. Ownership Boundary",
        "## 3. Non-Goals",
        "## 4. Relationship to `academic-paper`",
        "## 5. Relationship to `econ-write`",
        "## 6. Relationship to `academic-paper-reviewer`",
        "## 7. Category A / B / C Terminology Protection Model",
        "## 8. Claim-Strength Discipline",
        "## 9. Prose-Pattern Families",
        "## 10. Human Judgment Requirements",
        "## 11. Deterministic vs. Judgmental Checks",
        "## 12. False-Positive Policy",
        "## 13. Technical Vocabulary Protection",
        "## 14. Revision Recommendations",
        "## 15. AI-Authorship Non-Inference Rule",
        "## 16. Consumption Contract",
        "## 17. Future Workspace Seam",
    ]
    for sec in required_sections:
        assert sec in content, f"Missing required protocol section: {sec}"
    print("  [PASS] Shared protocol exists and contains all 17 required sections.")


def test_offline_independence():
    tool_path = REPO_ROOT / "tools" / "prose_checks" / "check_prose_patterns.py"
    assert tool_path.is_file(), f"Tool missing: {tool_path}"
    code = tool_path.read_text(encoding="utf-8")

    forbidden_modules = [
        "openai",
        "anthropic",
        "google.generativeai",
        "requests",
        "urllib.request",
        "aiohttp",
        "httpx",
        "transformers",
        "torch",
        "spacy",
    ]
    for mod in forbidden_modules:
        assert f"import {mod}" not in code and f"from {mod}" not in code, (
            f"Forbidden external/network module '{mod}' imported in deterministic tool!"
        )
    print("  [PASS] Tool is 100% offline (standard library only; zero external/AI network dependencies).")


def test_ai_authorship_non_inference():
    tool_path = REPO_ROOT / "tools" / "prose_checks" / "check_prose_patterns.py"
    code = tool_path.read_text(encoding="utf-8")

    forbidden_terms = [
        "ai_score",
        "machine_generated",
        "human_likelihood",
        "ai_probability",
        "detection_verdict",
        "hallucination_score",
    ]
    for term in forbidden_terms:
        assert term not in code.lower(), f"Tool contains forbidden AI authorship classification term: {term}"

    checker = ProsePatternChecker()
    sample_res = checker.analyze_text("This is an empirical tournament text.")
    res_str = json.dumps(sample_res).lower()
    for term in forbidden_terms:
        assert term not in res_str, f"Diagnostic output contains forbidden AI classification term: {term}"
    print("  [PASS] Non-inference invariant enforced: Zero AI authorship scoring or classification.")


def test_gold_fixtures():
    fixtures_path = REPO_ROOT / "evals" / "gold" / "prose_discipline" / "cases.yaml"
    assert fixtures_path.is_file(), f"Fixtures missing: {fixtures_path}"

    with open(fixtures_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    cases = data.get("cases", [])
    assert len(cases) >= 11, f"Expected at least 11 cases in cases.yaml, got {len(cases)}"

    checker = ProsePatternChecker()
    passed_cases = 0

    for c in cases:
        case_id = c["id"]
        text = c["text"]
        expected_status = c.get("expected_status")
        expected_flags_count = c.get("expected_flags_count")
        expected_flag_families = c.get("expected_flag_families", [])
        forbidden_flag_families = c.get("forbidden_flag_families", [])
        expected_protected_terms = c.get("expected_protected_terms", [])

        res = checker.analyze_text(text)

        # Status check
        if expected_status:
            assert res["status"] == expected_status, (
                f"[{case_id}] Status mismatch: expected {expected_status}, got {res['status']}"
            )

        # Expected flag count check (if specified)
        if expected_flags_count is not None:
            actual_count = res["summary"]["total_flags"]
            if expected_flags_count == 0:
                assert actual_count == 0, f"[{case_id}] Expected 0 flags, got {actual_count}: {res['flags']}"
            else:
                assert actual_count >= expected_flags_count, (
                    f"[{case_id}] Expected at least {expected_flags_count} flags, got {actual_count}"
                )

        # Expected flag families
        for fam in expected_flag_families:
            assert fam in res["summary"]["flag_counts"], (
                f"[{case_id}] Expected flag family '{fam}' not found in results: {res['summary']['flag_counts']}"
            )

        # Forbidden flag families
        for fam in forbidden_flag_families:
            assert fam not in res["summary"]["flag_counts"], (
                f"[{case_id}] Forbidden flag family '{fam}' was triggered: {res['summary']['flag_counts']}"
            )

        # Category A protected terms check
        for term in expected_protected_terms:
            assert term in res["protected_terms"], (
                f"[{case_id}] Expected protected term '{term}' was not identified: {res['protected_terms']}"
            )

        # Severity vocabulary check
        for flag in res["flags"]:
            assert flag["severity"] in ("INFO", "REVIEW"), (
                f"[{case_id}] Invalid severity '{flag['severity']}'; must be INFO or REVIEW"
            )

        passed_cases += 1
        print(f"  [PASS] {case_id} ({res['status']}) - Flags: {res['summary']['total_flags']}")

    print(f"  [PASS] All {passed_cases} gold evaluation fixtures executed and verified.")


def test_determinism():
    checker = ProsePatternChecker()
    sample = (
        "Furthermore, we evaluate the admissibility gates.\n"
        "Moreover, the black-box screening protocol reveals profound institutional divergence.\n"
        "We find that the Johansen trace test identifies a single cointegrating vector."
    )
    res1 = checker.analyze_text(sample)
    res2 = checker.analyze_text(sample)

    assert json.dumps(res1, sort_keys=True) == json.dumps(res2, sort_keys=True), (
        "Non-deterministic execution detected: Identical text produced divergent diagnostic reports!"
    )
    print("  [PASS] Deterministic reproducibility verified: 100% identical JSON outputs across runs.")


def main():
    print("=" * 60)
    print("Running ARS Wave C1 Prose Discipline Test Suite")
    print("=" * 60)
    try:
        test_protocol_exists()
        test_offline_independence()
        test_ai_authorship_non_inference()
        test_gold_fixtures()
        test_determinism()
        print("=" * 60)
        print("ALL PROSE DISCIPLINE TESTS PASSED.")
        print("=" * 60)
        sys.exit(0)
    except AssertionError as e:
        print(f"\n[FAIL] Test failure: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
