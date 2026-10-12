#!/usr/bin/env python3
"""
scripts/test_routing_contract.py

Deterministic test runner for ARS Wave B1 routing precedence contract.
Validates evals/gold/routing/cases.yaml against docs/governance/ars_registry.yaml
and verifies capability ownership invariants without invoking LLMs.
"""

import sys
from pathlib import Path
import yaml

TARGET_PATH_PREFIXES = ("skills/", "profiles/", "orchestrator/", "tools/", "shared/")


def test_routing_contract(repo_root: Path) -> bool:
    cases_path = repo_root / "evals" / "gold" / "routing" / "cases.yaml"
    registry_path = repo_root / "docs" / "governance" / "ars_registry.yaml"

    if not cases_path.exists():
        print(f"FAIL: Fixture file not found: {cases_path}")
        return False

    if not registry_path.exists():
        print(f"FAIL: Registry file not found: {registry_path}")
        return False

    try:
        with open(cases_path, "r", encoding="utf-8") as f:
            cases_data = yaml.safe_load(f)
        with open(registry_path, "r", encoding="utf-8") as f:
            reg_data = yaml.safe_load(f)
    except Exception as e:
        print(f"FAIL: YAML parsing error: {e}")
        return False

    components = {c["component_id"]: c for c in reg_data.get("components", [])}
    capabilities = {cap["capability_id"]: cap for cap in reg_data.get("capabilities", [])}

    cases = cases_data.get("cases", [])
    if not cases:
        print("FAIL: No cases found in cases.yaml")
        return False

    print(f"Running ARS Wave B1 Routing Precedence Test Suite ({len(cases)} cases)...")
    passed = 0
    failed = 0

    for case in cases:
        case_id = case.get("id")
        rule = case.get("rule")
        owner = case.get("primary_owner")
        delegates = case.get("delegates_to", [])
        calib = case.get("calibration_input")
        prompt = case.get("prompt")

        errors = []

        # 1. Primary owner existence and target-path check
        if owner not in components:
            errors.append(f"primary_owner '{owner}' does not exist in registry components.")
        else:
            owner_comp = components[owner]
            rpath = owner_comp.get("runtime_path", "")
            if any(rpath.startswith(p) for p in TARGET_PATH_PREFIXES):
                errors.append(f"primary_owner '{owner}' uses future target path format as runtime_path: '{rpath}'.")

        # 2. Delegates existence and target-path check
        if delegates:
            for d in delegates:
                if d not in components:
                    errors.append(f"delegated component '{d}' does not exist in registry components.")
                else:
                    d_rpath = components[d].get("runtime_path", "")
                    if any(d_rpath.startswith(p) for p in TARGET_PATH_PREFIXES):
                        errors.append(f"delegated component '{d}' has future target path: '{d_rpath}'.")

        # 3. Calibration input check
        if calib:
            if calib not in components:
                errors.append(f"calibration_input '{calib}' does not exist in registry components.")
            else:
                calib_comp = components[calib]
                if calib_comp.get("semantic_role") != "PROFILE":
                    errors.append(f"calibration_input '{calib}' must have semantic_role 'PROFILE', got '{calib_comp.get('semantic_role')}'.")

        # 4. Rule-specific governance assertions
        if rule == "R1":  # Generic manuscript
            if owner != "academic-paper":
                errors.append(f"R1 primary owner must be 'academic-paper', got '{owner}'.")
            if capabilities.get("academic_manuscript_lifecycle", {}).get("current_owner") != "academic-paper":
                errors.append("Registry capability 'academic_manuscript_lifecycle' owner mismatch.")

        elif rule == "R2":  # Bounded economics writing
            if owner != "econ-write":
                errors.append(f"R2 primary owner must be 'econ-write', got '{owner}'.")
            if capabilities.get("economics_prose_and_section_standards", {}).get("current_owner") != "econ-write":
                errors.append("Registry capability 'economics_prose_and_section_standards' owner mismatch.")

        elif rule == "R3":  # Full economics workflow
            if owner != "academic-paper":
                errors.append(f"R3 primary owner must be 'academic-paper', got '{owner}'.")
            if "econ-write" not in delegates:
                errors.append("R3 full economics workflow must delegate domain policy to 'econ-write'.")

        elif rule == "R4":  # External peer review
            if owner != "academic-paper-reviewer":
                errors.append(f"R4 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") != "academic-paper-reviewer":
                errors.append("Registry capability 'simulated_external_peer_review' owner mismatch.")

        elif rule == "R5":  # Advisor calibration
            if owner != "academic-paper-reviewer":
                errors.append(f"R5 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if calib != "advisor-reviewer":
                errors.append(f"R5 calibration_input must be 'advisor-reviewer', got '{calib}'.")

        elif rule == "R6":  # Committee calibration
            if owner != "academic-paper-reviewer":
                errors.append(f"R6 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if calib != "PE-phd-committee":
                errors.append(f"R6 calibration_input must be 'PE-phd-committee', got '{calib}'.")

        elif rule == "R7":  # Orchestration
            if owner != "academic-pipeline":
                errors.append(f"R7 primary owner must be 'academic-pipeline', got '{owner}'.")
            if components.get("academic-pipeline", {}).get("semantic_role") != "ORCHESTRATOR":
                errors.append("academic-pipeline must have semantic_role 'ORCHESTRATOR'.")

        elif rule == "R8":  # Slides
            if owner != "econ-slides":
                errors.append(f"R8 primary owner must be 'econ-slides', got '{owner}'.")

        elif rule == "R9":  # Deep research / evidence check
            if owner != "deep-research":
                errors.append(f"R9 primary owner must be 'deep-research', got '{owner}'.")

        if errors:
            print(f"  [FAIL] {case_id} ({rule}): {prompt}")
            for err in errors:
                print(f"         - {err}")
            failed += 1
        else:
            print(f"  [PASS] {case_id} ({rule}): {owner} -> {case.get('expected_action')}")
            passed += 1

    print("\n------------------------------------------------------------")
    print(f"Routing Test Results: {passed} passed, {failed} failed out of {len(cases)} cases.")
    if failed == 0:
        print("PASS: All routing fixtures conform to ARS capability precedence contract.")
        return True
    else:
        print("FAIL: One or more routing fixtures violated precedence contract.")
        return False


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    success = test_routing_contract(root)
    sys.exit(0 if success else 1)
