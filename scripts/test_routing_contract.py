#!/usr/bin/env python3
"""
scripts/test_routing_contract.py

Deterministic test runner for ARS Wave B1, B1.1, and C5 routing precedence contract.
Validates evals/gold/routing/cases.yaml against docs/governance/ars_registry.yaml
and enforces positive ownership, delegation, calibration, and adversarial negative
exclusion invariants without invoking LLMs.
"""

import sys
from pathlib import Path
import yaml

TARGET_PATH_PREFIXES = ("skills/", "orchestrator/")


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
    deprecated_components = {
        c["component_id"] for c in reg_data.get("components", [])
        if c.get("lifecycle_status") == "DEPRECATED"
    }
    capabilities = {cap["capability_id"]: cap for cap in reg_data.get("capabilities", [])}

    cases = cases_data.get("cases", [])
    if not cases:
        print("FAIL: No cases found in cases.yaml")
        return False

    print(f"Running ARS Routing Precedence Test Suite ({len(cases)} cases)...")
    passed = 0
    failed = 0
    pos_count = 0
    adv_count = 0

    for case in cases:
        case_id = case.get("id")
        rule = case.get("rule")
        owner = case.get("primary_owner")
        delegates = case.get("delegates_to", [])
        calib = case.get("calibration_input")
        domain_policy = case.get("domain_policy")
        must_not_owner = case.get("must_not_primary_owner", [])
        must_include_del = case.get("must_include_delegates", [])
        orchestrator_allowed = case.get("orchestrator_allowed", False)
        prompt = case.get("prompt")

        if rule.startswith("ADV-"):
            adv_count += 1
        else:
            pos_count += 1

        errors = []

        # 1. Primary owner existence and target-path check
        if owner not in components:
            errors.append(f"primary_owner '{owner}' does not exist in registry components.")
        else:
            owner_comp = components[owner]
            rpath = owner_comp.get("runtime_path", "")
            if any(rpath.startswith(p) for p in TARGET_PATH_PREFIXES):
                errors.append(f"primary_owner '{owner}' uses future target path format as runtime_path: '{rpath}'.")
            if owner in deprecated_components:
                errors.append(f"primary_owner '{owner}' is a deprecated component; deprecated aliases cannot be primary owners.")

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
            if calib.startswith("profiles/") or "/" in calib:
                if not (repo_root / calib).exists():
                    errors.append(f"calibration_input profile path '{calib}' does not exist on disk.")
            elif calib not in components:
                errors.append(f"calibration_input '{calib}' does not exist in registry components.")
            else:
                calib_comp = components[calib]
                if calib_comp.get("semantic_role") != "PROFILE":
                    errors.append(f"calibration_input '{calib}' must have semantic_role 'PROFILE', got '{calib_comp.get('semantic_role')}'.")

        # 4. Domain policy check
        if domain_policy:
            if domain_policy not in components:
                errors.append(f"domain_policy '{domain_policy}' does not exist in registry components.")
            else:
                dp_comp = components[domain_policy]
                if dp_comp.get("semantic_role") != "DOMAIN_SKILL":
                    errors.append(f"domain_policy '{domain_policy}' must have semantic_role 'DOMAIN_SKILL', got '{dp_comp.get('semantic_role')}'.")

        # 5. Negative owner assertions
        if must_not_owner:
            if owner in must_not_owner:
                errors.append(f"Negative assertion violated: primary_owner '{owner}' is in must_not_primary_owner {must_not_owner}.")

        # 6. Required delegates check
        if must_include_del:
            for req_d in must_include_del:
                if req_d not in delegates:
                    errors.append(f"Required delegate '{req_d}' missing from delegates_to list: {delegates}.")

        # 7. Orchestration constraint check
        if orchestrator_allowed:
            if components.get(owner, {}).get("semantic_role") != "ORCHESTRATOR":
                errors.append(f"orchestrator_allowed is true, but '{owner}' is not an ORCHESTRATOR.")
            # Verify orchestrator does not own substantive capabilities
            for sub_cap in ("academic_manuscript_lifecycle", "economics_prose_and_section_standards", "simulated_external_peer_review"):
                if capabilities.get(sub_cap, {}).get("current_owner") == owner:
                    errors.append(f"Orchestrator '{owner}' illegally claims substantive capability '{sub_cap}'.")

        # 8. Rule-specific assertions
        # Positive Rules R1-R9
        if rule == "R1":
            if owner != "academic-paper":
                errors.append(f"R1 primary owner must be 'academic-paper', got '{owner}'.")
            if capabilities.get("academic_manuscript_lifecycle", {}).get("current_owner") != "academic-paper":
                errors.append("Registry capability 'academic_manuscript_lifecycle' owner mismatch.")

        elif rule == "R2":
            if owner != "econ-write":
                errors.append(f"R2 primary owner must be 'econ-write', got '{owner}'.")
            if capabilities.get("economics_prose_and_section_standards", {}).get("current_owner") != "econ-write":
                errors.append("Registry capability 'economics_prose_and_section_standards' owner mismatch.")

        elif rule == "R3":
            if owner != "academic-paper":
                errors.append(f"R3 primary owner must be 'academic-paper', got '{owner}'.")
            if "econ-write" not in delegates:
                errors.append("R3 full economics workflow must delegate domain policy to 'econ-write'.")

        elif rule == "R4":
            if owner != "academic-paper-reviewer":
                errors.append(f"R4 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") != "academic-paper-reviewer":
                errors.append("Registry capability 'simulated_external_peer_review' owner mismatch.")

        elif rule == "R5":
            if owner != "academic-paper-reviewer":
                errors.append(f"R5 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if calib != "profiles/advisors/michael-ash.md":
                errors.append(f"R5 calibration_input must be 'profiles/advisors/michael-ash.md', got '{calib}'.")
            if not (repo_root / calib).exists():
                errors.append(f"R5 calibration_input path '{calib}' does not exist on disk.")

        elif rule == "R6":
            if owner != "academic-paper-reviewer":
                errors.append(f"R6 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if calib != "profiles/committees/umass-pe.md":
                errors.append(f"R6 calibration_input must be 'profiles/committees/umass-pe.md', got '{calib}'.")
            if not (repo_root / calib).exists():
                errors.append(f"R6 calibration_input path '{calib}' does not exist on disk.")

        elif rule == "R7":
            if owner != "academic-pipeline":
                errors.append(f"R7 primary owner must be 'academic-pipeline', got '{owner}'.")
            if components.get("academic-pipeline", {}).get("semantic_role") != "ORCHESTRATOR":
                errors.append("academic-pipeline must have semantic_role 'ORCHESTRATOR'.")

        elif rule == "R8":
            if owner != "econ-slides":
                errors.append(f"R8 primary owner must be 'econ-slides', got '{owner}'.")

        elif rule == "R9":
            if owner != "deep-research":
                errors.append(f"R9 primary owner must be 'deep-research', got '{owner}'.")

        # Adversarial Rules ADV-A1 to ADV-A8
        elif rule == "ADV-A1":  # Econ paper peer review
            if owner != "academic-paper-reviewer":
                errors.append(f"ADV-A1 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") != "academic-paper-reviewer":
                errors.append("simulated_external_peer_review must be owned by 'academic-paper-reviewer'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") == "econ-write":
                errors.append("econ-write must NOT own simulated_external_peer_review.")

        elif rule == "ADV-A2":  # Advisor calibrated review
            if owner != "academic-paper-reviewer":
                errors.append(f"ADV-A2 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if calib != "profiles/advisors/michael-ash.md":
                errors.append(f"ADV-A2 calibration_input must be 'profiles/advisors/michael-ash.md', got '{calib}'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") == "advisor-reviewer":
                errors.append("advisor-reviewer must NOT be canonical owner of simulated_external_peer_review.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") != "academic-paper-reviewer":
                errors.append("simulated_external_peer_review must be owned by 'academic-paper-reviewer'.")

        elif rule == "ADV-A3":  # Compound write + review
            if owner != "academic-pipeline":
                errors.append(f"ADV-A3 primary owner must be 'academic-pipeline', got '{owner}'.")
            if capabilities.get("academic_manuscript_lifecycle", {}).get("current_owner") != "academic-paper":
                errors.append("academic_manuscript_lifecycle must be owned by 'academic-paper'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") != "academic-paper-reviewer":
                errors.append("simulated_external_peer_review must be owned by 'academic-paper-reviewer'.")

        elif rule == "ADV-A4":  # Bounded economics prose
            if owner != "econ-write":
                errors.append(f"ADV-A4 primary owner must be 'econ-write', got '{owner}'.")
            if capabilities.get("economics_prose_and_section_standards", {}).get("current_owner") != "econ-write":
                errors.append("economics_prose_and_section_standards must be owned by 'econ-write'.")

        elif rule == "ADV-A5":  # Source / claim verification
            if owner != "deep-research":
                errors.append(f"ADV-A5 primary owner must be 'deep-research', got '{owner}'.")
            if capabilities.get("literature_synthesis_search", {}).get("current_owner") != "deep-research":
                errors.append("literature_synthesis_search must be owned by 'deep-research'.")

        elif rule == "ADV-A6":  # Ambiguous paper review
            if owner != "academic-paper-reviewer":
                errors.append(f"ADV-A6 primary owner must be 'academic-paper-reviewer', got '{owner}'.")
            if capabilities.get("simulated_external_peer_review", {}).get("current_owner") != "academic-paper-reviewer":
                errors.append("simulated_external_peer_review must be owned by 'academic-paper-reviewer'.")

        elif rule == "ADV-A7":  # Research evidence review
            if owner != "deep-research":
                errors.append(f"ADV-A7 primary owner must be 'deep-research', got '{owner}'.")

        elif rule == "ADV-A8":  # Economics manuscript revision
            if owner != "academic-paper":
                errors.append(f"ADV-A8 primary owner must be 'academic-paper', got '{owner}'.")
            if domain_policy != "econ-write":
                errors.append(f"ADV-A8 domain_policy must be 'econ-write', got '{domain_policy}'.")
            if capabilities.get("academic_manuscript_lifecycle", {}).get("current_owner") != "academic-paper":
                errors.append("academic_manuscript_lifecycle must be owned by 'academic-paper'.")

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
    print(f"  - Positive invariant cases: {pos_count}")
    print(f"  - Adversarial disambiguation cases: {adv_count}")
    if failed == 0:
        print("PASS: All positive and adversarial routing fixtures conform to ARS capability precedence contract.")
        return True
    else:
        print("FAIL: One or more routing fixtures violated precedence contract.")
        return False


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    success = test_routing_contract(root)
    sys.exit(0 if success else 1)
