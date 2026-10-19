#!/usr/bin/env python3
"""
scripts/test_routing_contract.py

Deterministic test runner for ARS Wave B1, B1.1, C5, and D6 routing precedence contract.
Validates evals/gold/routing/cases.yaml against docs/governance/ars_registry.yaml
and enforces positive ownership, delegation, calibration, and adversarial negative
exclusion invariants without invoking LLMs.
"""

import copy
import sys
from pathlib import Path
import yaml

TARGET_PATH_PREFIXES = ("skills/", "orchestrator/")

# D5 Conceptual Name Resolution Mapping
# Ensures conceptual names from D5 evaluations resolve explicitly to registered runtime components
D5_CONCEPTUAL_TO_REGISTERED = {
    "applied-econometrics-pe": "umass-applied-econometrics",
    "heterodox-macro-modeling": "heterodox-economics-review",
    "historical_source_criticism_protocol": "historical-source-criticism",
}


def validate_single_case(
    case: dict,
    components: dict,
    deprecated_components: set,
    capabilities: dict,
    repo_root: Path,
) -> list[str]:
    """
    Validates a single routing case fixture against registry invariants and rules.
    Returns a list of error strings (empty list indicates a valid case).
    """
    rule = case.get("rule", "")
    owner = case.get("primary_owner")
    delegates = case.get("delegates_to", [])
    calib = case.get("calibration_input")
    domain_policy = case.get("domain_policy")
    gov_protocol = case.get("governing_protocol")
    must_not_owner = case.get("must_not_primary_owner", [])
    must_include_del = case.get("must_include_delegates", [])
    orchestrator_allowed = case.get("orchestrator_allowed", False)

    errors = []

    # 1. Primary owner existence and target-path check
    if owner == "UNASSIGNED_CAPABILITY_GAP":
        # The unassigned capability gap must NOT exist as a registered component
        if owner in components:
            errors.append("UNASSIGNED_CAPABILITY_GAP must not exist as a registered component.")
    elif owner not in components:
        errors.append(f"primary_owner '{owner}' does not exist in registry components.")
    else:
        owner_comp = components[owner]
        rpath = owner_comp.get("runtime_path", "")
        if any(rpath.startswith(p) for p in TARGET_PATH_PREFIXES):
            errors.append(f"primary_owner '{owner}' uses future target path format as runtime_path: '{rpath}'.")
        if owner in deprecated_components:
            errors.append(f"primary_owner '{owner}' is a deprecated component; deprecated aliases cannot be primary owners.")
        if owner_comp.get("semantic_role") == "SHARED_PROTOCOL":
            errors.append(f"primary_owner '{owner}' has semantic_role 'SHARED_PROTOCOL'; shared protocols cannot be autonomous executable primary owners.")

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

    # 4b. Governing protocol check
    if gov_protocol:
        resolved_gov = D5_CONCEPTUAL_TO_REGISTERED.get(gov_protocol, gov_protocol)
        if resolved_gov not in components:
            errors.append(f"governing_protocol '{gov_protocol}' (resolved: '{resolved_gov}') does not exist in registry components.")
        else:
            gov_comp = components[resolved_gov]
            if gov_comp.get("semantic_role") != "SHARED_PROTOCOL":
                errors.append(f"governing_protocol '{gov_protocol}' must have semantic_role 'SHARED_PROTOCOL', got '{gov_comp.get('semantic_role')}'.")

    # 5. Negative owner assertions
    if must_not_owner:
        for mno in must_not_owner:
            resolved_mno = D5_CONCEPTUAL_TO_REGISTERED.get(mno, mno)
            if owner == mno or owner == resolved_mno:
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

    # Wave D Domain Rules (R12 to R14)
    elif rule == "R12":  # Political economy mechanism adjudication
        if owner != "political-economy-research":
            errors.append(f"R12 primary owner must be 'political-economy-research', got '{owner}'.")
        if capabilities.get("political_economy_research_methodology", {}).get("current_owner") != "political-economy-research":
            errors.append("political_economy_research_methodology must be owned by 'political-economy-research'.")

    elif rule == "R13":  # Heterodox macro stability derivation
        if owner != "heterodox-economics-review":
            errors.append(f"R13 primary owner must be 'heterodox-economics-review', got '{owner}'.")
        if capabilities.get("heterodox_macro_modeling", {}).get("current_owner") != "heterodox-economics-review":
            errors.append("heterodox_macro_modeling must be owned by 'heterodox-economics-review'.")

    elif rule == "R14":  # Applied econometrics cointegration
        if owner != "umass-applied-econometrics":
            errors.append(f"R14 primary owner must be 'umass-applied-econometrics', got '{owner}'.")
        if capabilities.get("applied_econometrics_political_economy", {}).get("current_owner") != "umass-applied-econometrics":
            errors.append("applied_econometrics_political_economy must be owned by 'umass-applied-econometrics'.")

    # Wave D Adversarial Disambiguation Rules (ADV-D1 to ADV-D6)
    elif rule == "ADV-D1":  # Archival retrieval vs PE
        if owner != "deep-research":
            errors.append(f"ADV-D1 primary owner must be 'deep-research', got '{owner}'.")
        if "political-economy-research" not in must_not_owner:
            errors.append("ADV-D1 must exclude 'political-economy-research' from primary owner.")

    elif rule == "ADV-D2":  # Documentary source claim support
        if owner != "political-economy-research":
            errors.append(f"ADV-D2 primary owner must be 'political-economy-research', got '{owner}'.")
        if not gov_protocol or D5_CONCEPTUAL_TO_REGISTERED.get(gov_protocol, gov_protocol) != "historical-source-criticism":
            errors.append(f"ADV-D2 governing_protocol must resolve to 'historical-source-criticism', got '{gov_protocol}'.")
        if "historical-source-criticism" not in must_not_owner:
            errors.append("ADV-D2 must exclude 'historical-source-criticism' from primary owner.")

    elif rule == "ADV-D3":  # Multi-step cross-domain coordination
        if owner != "academic-pipeline":
            errors.append(f"ADV-D3 primary owner must be 'academic-pipeline', got '{owner}'.")
        for req_d in ("deep-research", "political-economy-research", "umass-applied-econometrics", "heterodox-economics-review"):
            if req_d not in delegates:
                errors.append(f"ADV-D3 missing required delegate '{req_d}'.")

    elif rule == "ADV-D4":  # Disciplinary topic vs econometric operation
        if owner != "umass-applied-econometrics":
            errors.append(f"ADV-D4 primary owner must be 'umass-applied-econometrics', got '{owner}'.")
        if "political-economy-research" not in must_not_owner:
            errors.append("ADV-D4 must exclude 'political-economy-research' from primary owner.")

    elif rule == "ADV-D5":  # Historical background drafting
        if owner != "academic-paper":
            errors.append(f"ADV-D5 primary owner must be 'academic-paper', got '{owner}'.")
        if domain_policy != "econ-write":
            errors.append(f"ADV-D5 domain_policy must be 'econ-write', got '{domain_policy}'.")
        for ex in ("political-economy-research", "heterodox-economics-review"):
            if ex not in must_not_owner:
                errors.append(f"ADV-D5 must exclude '{ex}' from primary owner.")

    elif rule == "ADV-D6":  # Unassigned causal inference gap
        if owner != "UNASSIGNED_CAPABILITY_GAP":
            errors.append(f"ADV-D6 primary owner must be 'UNASSIGNED_CAPABILITY_GAP', got '{owner}'.")
        ci_cap = capabilities.get("causal_inference_microeconometrics", {})
        if ci_cap.get("current_owner") is not None:
            errors.append("causal_inference_microeconometrics must have current_owner: null.")
        if ci_cap.get("migration_status") != "CANDIDATE":
            errors.append("causal_inference_microeconometrics must have migration_status: 'CANDIDATE'.")

    return errors


def verify_unassigned_capability_and_negative_invariants(
    cases: list,
    reg_data: dict,
    components: dict,
    deprecated_components: set,
    capabilities: dict,
    repo_root: Path,
) -> None:
    """
    Exhaustive regression test verifying unassigned causal-inference capability and negative invariants:
    - Reads component IDs dynamically from registry (no hardcoded count or list).
    - For ROUTE-026, tests assigning each registered component as primary owner.
      Every assignment must fail because the causal-inference capability has no owner.
    - Asserts original unassigned case passes.
    - Asserts registry's causal_inference_microeconometrics.current_owner remains null.
    - Asserts assigning a current owner to that capability fails registry validation.
    - Asserts assigning historical-source protocol as executable owner fails.
    - Asserts assigning unit-root task to political-economy methodology fails.
    - Asserts the corresponding valid cases pass.
    """
    sys.path.insert(0, str(repo_root / "scripts"))
    from validate_ars_registry import validate_registry_data

    print("\n--- Running Exhaustive Dynamic Invariant Regressions (Wave D6) ---")

    # 1. Dynamic component enumeration
    dynamic_components = [
        c["component_id"] for c in reg_data.get("components", [])
        if isinstance(c, dict) and "component_id" in c
    ]
    assert len(dynamic_components) > 0, "No components found in registry."

    # 2. ROUTE-026 exhaustive component rejection
    r026_matches = [c for c in cases if c.get("id") == "ROUTE-026"]
    assert len(r026_matches) == 1, "Expected exactly one ROUTE-026 case fixture."
    r026 = r026_matches[0]

    # Verify original unassigned case passes
    orig_r026_errs = validate_single_case(r026, components, deprecated_components, capabilities, repo_root)
    assert len(orig_r026_errs) == 0, f"Original ROUTE-026 unexpectedly failed: {orig_r026_errs}"

    # Verify assigning each registered component as primary owner fails
    rejected_count = 0
    for comp_id in dynamic_components:
        tampered_case = copy.deepcopy(r026)
        tampered_case["primary_owner"] = comp_id
        errs = validate_single_case(tampered_case, components, deprecated_components, capabilities, repo_root)
        assert len(errs) > 0, (
            f"Regression assertion failed: Assigning registered component '{comp_id}' as primary owner "
            f"to ROUTE-026 should have failed, but passed without error!"
        )
        rejected_count += 1

    assert rejected_count == len(dynamic_components), (
        f"Expected to test {len(dynamic_components)} components, tested {rejected_count}."
    )
    print(f"  [PASS] ROUTE-026: Rejected all {rejected_count}/{len(dynamic_components)} dynamically enumerated components as primary owner.")

    # 3. Verify registry causal_inference_microeconometrics.current_owner is null and status is CANDIDATE
    ci_cap = capabilities.get("causal_inference_microeconometrics")
    assert ci_cap is not None, "causal_inference_microeconometrics missing from registry capabilities."
    assert ci_cap.get("current_owner") is None, (
        f"Registry invariant failed: causal_inference_microeconometrics.current_owner must be null, got '{ci_cap.get('current_owner')}'."
    )
    assert ci_cap.get("migration_status") == "CANDIDATE", (
        f"Registry invariant failed: causal_inference_microeconometrics.migration_status must be 'CANDIDATE', got '{ci_cap.get('migration_status')}'."
    )
    print("  [PASS] causal_inference_microeconometrics: current_owner is null and migration_status is CANDIDATE.")

    # 4. Verify assigning a current owner to causal_inference_microeconometrics fails validation
    # A) In-memory registry data validation
    tampered_reg = copy.deepcopy(reg_data)
    for cap in tampered_reg.get("capabilities", []):
        if cap.get("capability_id") == "causal_inference_microeconometrics":
            cap["current_owner"] = "econ-write"
            cap["current_owner_type"] = "DOMAIN_SKILL"
            break
    reg_errs = validate_registry_data(tampered_reg, repo_root)
    assert any("causal_inference_microeconometrics" in e for e in reg_errs), (
        "Registry validation failed to catch non-null owner on causal_inference_microeconometrics!"
    )
    # B) In-memory routing case validation
    tampered_caps = copy.deepcopy(capabilities)
    tampered_caps["causal_inference_microeconometrics"]["current_owner"] = "econ-write"
    tampered_r026_errs = validate_single_case(r026, components, deprecated_components, tampered_caps, repo_root)
    assert any("causal_inference_microeconometrics must have current_owner: null" in e for e in tampered_r026_errs), (
        "Routing validation failed to catch non-null owner on causal_inference_microeconometrics!"
    )
    print("  [PASS] Tampering causal_inference_microeconometrics.current_owner reliably fails registry and routing validation.")

    # 5. Verify assigning historical-source protocol as executable owner fails, while valid case passes
    r022_matches = [c for c in cases if c.get("id") == "ROUTE-022"]
    assert len(r022_matches) == 1, "Expected exactly one ROUTE-022 case fixture."
    r022 = r022_matches[0]

    # Valid case passes
    orig_r022_errs = validate_single_case(r022, components, deprecated_components, capabilities, repo_root)
    assert len(orig_r022_errs) == 0, f"Original valid ROUTE-022 failed: {orig_r022_errs}"

    # Tampered case: assigning protocol as primary owner
    tampered_r022 = copy.deepcopy(r022)
    tampered_r022["primary_owner"] = "historical-source-criticism"
    proto_errs = validate_single_case(tampered_r022, components, deprecated_components, capabilities, repo_root)
    assert len(proto_errs) > 0, "Assigning historical-source-criticism as executable primary owner should have failed!"
    assert any("has semantic_role 'SHARED_PROTOCOL'" in e for e in proto_errs), (
        f"Expected protocol typing error, got: {proto_errs}"
    )
    print("  [PASS] ROUTE-022: Protocol-as-executable-owner assignment fails; valid requesting workflow passes.")

    # 6. Verify assigning unit-root task to political-economy methodology fails, while valid case passes
    r024_matches = [c for c in cases if c.get("id") == "ROUTE-024"]
    assert len(r024_matches) == 1, "Expected exactly one ROUTE-024 case fixture."
    r024 = r024_matches[0]

    # Valid case passes
    orig_r024_errs = validate_single_case(r024, components, deprecated_components, capabilities, repo_root)
    assert len(orig_r024_errs) == 0, f"Original valid ROUTE-024 failed: {orig_r024_errs}"

    # Tampered case: assigning political-economy-research as primary owner
    tampered_r024 = copy.deepcopy(r024)
    tampered_r024["primary_owner"] = "political-economy-research"
    pe_unit_root_errs = validate_single_case(tampered_r024, components, deprecated_components, capabilities, repo_root)
    assert len(pe_unit_root_errs) > 0, "Assigning unit-root task to political-economy-research should have failed!"
    assert any("ADV-D4 primary owner must be 'umass-applied-econometrics'" in e for e in pe_unit_root_errs), (
        f"Expected ADV-D4 violation error, got: {pe_unit_root_errs}"
    )
    print("  [PASS] ROUTE-024: Unit-root assignment to PE fails; valid econometric assignment passes.")


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

    components = {c["component_id"]: c for c in reg_data.get("components", []) if isinstance(c, dict) and "component_id" in c}
    deprecated_components = {
        c["component_id"] for c in reg_data.get("components", [])
        if isinstance(c, dict) and c.get("lifecycle_status") == "DEPRECATED"
    }
    capabilities = {cap["capability_id"]: cap for cap in reg_data.get("capabilities", []) if isinstance(cap, dict) and "capability_id" in cap}

    # Verify D5 Conceptual Name Mapping
    mapping_errors = []
    for conceptual, registered in D5_CONCEPTUAL_TO_REGISTERED.items():
        if registered not in components:
            mapping_errors.append(f"Conceptual D5 name '{conceptual}' maps to '{registered}', which does not exist in registry.")
        elif components[registered].get("lifecycle_status") != "ACTIVE":
            mapping_errors.append(f"Registered component '{registered}' mapped from '{conceptual}' is not ACTIVE.")
        if conceptual in components and conceptual != registered:
            mapping_errors.append(f"Conceptual D5 name '{conceptual}' illegally exists as a duplicate component in registry.")
    if mapping_errors:
        print("FAIL: D5 conceptual name mapping verification failed:")
        for merr in mapping_errors:
            print(f"  - {merr}")
        return False

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
        rule = case.get("rule", "")
        owner = case.get("primary_owner")
        prompt = case.get("prompt")

        if rule.startswith("ADV-"):
            adv_count += 1
        else:
            pos_count += 1

        errors = validate_single_case(case, components, deprecated_components, capabilities, repo_root)

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
    if failed != 0:
        print("FAIL: One or more routing fixtures violated precedence contract.")
        return False

    # Execute dynamic regression invariants
    try:
        verify_unassigned_capability_and_negative_invariants(
            cases, reg_data, components, deprecated_components, capabilities, repo_root
        )
    except AssertionError as e:
        print(f"\nFAIL: Dynamic regression assertion failed: {e}")
        return False

    print("\nPASS: All positive, adversarial, and dynamic regression fixtures conform to ARS capability precedence contract.")
    return True


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    success = test_routing_contract(root)
    sys.exit(0 if success else 1)
