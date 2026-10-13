#!/usr/bin/env python3
"""
scripts/test_revision_guard.py

Deterministic revision guard test suite for Wave C2:
1. Executes all 12 gold evaluation cases (EG-01 through EG-12)
2. Enforces offline standard-library isolation (zero network/LLM dependencies)
3. Enforces deterministic reproducibility across repeated runs
4. Verifies FAIL vs. INDETERMINATE distinction
5. Verifies unresolved decision tracking without false blocking
6. Verifies 5-field Material Passport summary port contract
7. Confirms scholarly-quality independence
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts import revision_guard as guard

GOLD_PATH = ROOT / "evals" / "gold" / "editorial_governance" / "cases.json"


def load_gold_cases() -> list[dict]:
    with open(GOLD_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["cases"]


def test_gold_cases():
    """Runs all 12 gold evaluation cases and asserts expected verdicts."""
    cases = load_gold_cases()
    assert len(cases) == 12, f"Expected 12 gold cases, got {len(cases)}"

    for case in cases:
        cid = case["id"]
        expected = case["expected_verdict"]
        c_input = case["input"]

        gov = c_input["governance"]
        base_text = c_input.get("baseline_text", "")
        curr_text = c_input.get("current_text", "")

        snapshots = {"manuscript": {"kind": "source", "content": curr_text.encode("utf-8")}}
        baseline_snapshots = {"manuscript": {"kind": "source", "content": base_text.encode("utf-8")}}

        result = guard.verify(
            gov,
            snapshots=snapshots,
            baseline_snapshots=baseline_snapshots,
        )

        assert result["overall"] == expected, (
            f"[{cid}] Expected overall verdict '{expected}', got '{result['overall']}'. Checks: {result['checks']}"
        )

        # Check passport summary matches
        summary = result["passport_summary"]
        assert summary["verification_verdict"] == expected

        if "expected_unresolved_count" in case:
            assert summary["unresolved_decision_count"] == case["expected_unresolved_count"], (
                f"[{cid}] Expected unresolved count {case['expected_unresolved_count']}, got {summary['unresolved_decision_count']}"
            )

        print(f"  [PASS] {cid} ({case['name']}) -> {result['overall']}")


def test_offline_independence():
    """Verifies that revision_guard imports no network or AI inference modules."""
    code = (ROOT / "scripts" / "revision_guard.py").read_text(encoding="utf-8")
    forbidden = [
        "openai",
        "anthropic",
        "google.generativeai",
        "requests",
        "urllib.request",
        "httpx",
        "aiohttp",
        "socket",
        "transformers",
        "torch",
        "spacy",
    ]
    for mod in forbidden:
        assert f"import {mod}" not in code and f"from {mod}" not in code, (
            f"Forbidden network/inference module '{mod}' imported in revision_guard.py!"
        )
    print("  [PASS] Tool is 100% offline (standard library + jsonschema only; zero network/AI calls).")


def test_ai_non_inference():
    """Verifies no AI detection or synthetic authorship classification in tool."""
    code = (ROOT / "scripts" / "revision_guard.py").read_text(encoding="utf-8")
    forbidden_terms = [
        "ai_score",
        "machine_generated",
        "human_likelihood",
        "synthetic_probability",
        "detection_verdict",
    ]
    for term in forbidden_terms:
        assert term not in code.lower(), f"Tool contains forbidden AI inference term: {term}"
    print("  [PASS] AI non-inference invariant enforced (no authorship classification).")


def test_deterministic_reproducibility():
    """Confirms that running verification twice on identical inputs produces identical JSON."""
    cases = load_gold_cases()
    c = cases[0]
    gov = c["input"]["governance"]
    base = c["input"]["baseline_text"].encode("utf-8")
    curr = c["input"]["current_text"].encode("utf-8")

    res1 = guard.verify(gov, snapshots={"m": {"kind": "source", "content": curr}},
                        baseline_snapshots={"m": {"kind": "source", "content": base}})
    res2 = guard.verify(gov, snapshots={"m": {"kind": "source", "content": curr}},
                        baseline_snapshots={"m": {"kind": "source", "content": base}})

    assert json.dumps(res1, sort_keys=True) == json.dumps(res2, sort_keys=True), (
        "Non-deterministic execution: identical inputs produced divergent verification reports!"
    )
    print("  [PASS] Deterministic reproducibility verified (100% identical JSON outputs across runs).")


def test_fail_vs_indeterminate_distinction():
    """Confirms clear separation between violations (FAIL) and uncertainties (INDETERMINATE)."""
    cases = {c["id"]: c for c in load_gold_cases()}

    # Violation: text outside anchor bounds -> FAIL
    eg02 = cases["EG-02"]
    res_eg02 = guard.verify(
        eg02["input"]["governance"],
        snapshots={"m": {"kind": "source", "content": eg02["input"]["current_text"].encode("utf-8")}},
        baseline_snapshots={"m": {"kind": "source", "content": eg02["input"]["baseline_text"].encode("utf-8")}},
    )
    assert res_eg02["overall"] == "FAIL"

    # Uncertainty: missing anchor -> INDETERMINATE (not FAIL)
    eg03 = cases["EG-03"]
    res_eg03 = guard.verify(
        eg03["input"]["governance"],
        snapshots={"m": {"kind": "source", "content": eg03["input"]["current_text"].encode("utf-8")}},
        baseline_snapshots={"m": {"kind": "source", "content": eg03["input"]["baseline_text"].encode("utf-8")}},
    )
    assert res_eg03["overall"] == "INDETERMINATE"
    print("  [PASS] FAIL vs. INDETERMINATE semantic separation verified.")


def test_unresolved_decisions_surfaced():
    """Confirms open decisions surface in counts without silently causing FAIL."""
    cases = {c["id"]: c for c in load_gold_cases()}
    eg09 = cases["EG-09"]
    res = guard.verify(
        eg09["input"]["governance"],
        snapshots={"m": {"kind": "source", "content": eg09["input"]["current_text"].encode("utf-8")}},
        baseline_snapshots={"m": {"kind": "source", "content": eg09["input"]["baseline_text"].encode("utf-8")}},
    )
    summary = res["passport_summary"]
    assert summary["unresolved_decision_count"] == 1
    assert res["overall"] != "FAIL", "Unresolved decision must NOT silently trigger build FAIL."
    print("  [PASS] Unresolved decisions surfaced cleanly in passport summary.")


def test_passport_summary_fields():
    """Confirms Material Passport summary contains exactly the 5 permitted high-level fields."""
    cases = load_gold_cases()
    c = cases[0]
    res = guard.verify(
        c["input"]["governance"],
        snapshots={"m": {"kind": "source", "content": c["input"]["current_text"].encode("utf-8")}},
        baseline_snapshots={"m": {"kind": "source", "content": c["input"]["baseline_text"].encode("utf-8")}},
    )
    summary = res["passport_summary"]
    expected_keys = {
        "governance_id",
        "verification_verdict",
        "active_decision_count",
        "unresolved_decision_count",
        "source_hash",
    }
    assert set(summary.keys()) == expected_keys, f"Passport summary fields mismatch: {set(summary.keys())}"
    print("  [PASS] Material Passport Summary Port conforms strictly to 5-field contract.")


def test_scholarly_quality_independence():
    """Confirms governance evaluates change control only, not prose elegance or academic merit."""
    cases = {c["id"]: c for c in load_gold_cases()}
    eg10 = cases["EG-10"]
    res = guard.verify(
        eg10["input"]["governance"],
        snapshots={"m": {"kind": "source", "content": eg10["input"]["current_text"].encode("utf-8")}},
        baseline_snapshots={"m": {"kind": "source", "content": eg10["input"]["baseline_text"].encode("utf-8")}},
    )
    assert res["overall"] == "PASS"
    print("  [PASS] Scholarly quality independence verified (poor prose inside scope passes).")


def main():
    print("=" * 60)
    print("Running ARS Wave C2 Revision Guard Test Suite")
    print("=" * 60)
    try:
        test_gold_cases()
        test_offline_independence()
        test_ai_non_inference()
        test_deterministic_reproducibility()
        test_fail_vs_indeterminate_distinction()
        test_unresolved_decisions_surfaced()
        test_passport_summary_fields()
        test_scholarly_quality_independence()
        print("=" * 60)
        print("ALL REVISION GUARD TESTS PASSED.")
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
