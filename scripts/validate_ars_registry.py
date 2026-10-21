#!/usr/bin/env python3
"""
scripts/validate_ars_registry.py

Deterministic validation script for docs/governance/ars_registry.yaml.
Enforces the architectural invariants of the ARS Governance Foundation (Wave B0 & Wave C5).
"""

import os
import sys
from pathlib import Path
import yaml

# Controlled Vocabularies
ALLOWED_IMPLEMENTATION_TYPES = {
    "SKILL", "LEGACY_SKILL", "ORCHESTRATOR", "TOOL", "SHARED_PROTOCOL", "PROFILE"
}
ALLOWED_SEMANTIC_ROLES = {
    "CORE_SKILL", "DOMAIN_SKILL", "DISSEMINATION_SKILL",
    "ORCHESTRATOR", "PROFILE", "TOOL", "SHARED_PROTOCOL"
}
ALLOWED_LIFECYCLE_STATUSES = {"ACTIVE", "PLANNED_MIGRATION", "CANDIDATE_DECOMPOSITION", "DEPRECATED"}
ALLOWED_MIGRATION_STATUSES = {"CURRENT", "MIGRATING", "PLANNED", "CANDIDATE", "DEPRECATED"}

REQUIRED_COMPONENT_FIELDS = {
    "component_id", "display_name", "runtime_path", "current_implementation_type",
    "semantic_role", "lifecycle_status", "mode_bearing", "target_path",
    "provenance_source", "notes"
}

REQUIRED_CAPABILITY_FIELDS = {
    "capability_id", "description", "current_owner", "target_owner",
    "migration_status", "consumers", "forbidden_duplicate_owners", "provenance"
}


def validate_registry_data(data: dict, repo_root: Path) -> list[str]:
    errors = []

    # Check top-level structure
    if not isinstance(data, dict):
        return ["Root of registry must be a mapping/dict."]

    components_list = data.get("components")
    capabilities_list = data.get("capabilities")

    if not isinstance(components_list, list):
        errors.append("Top-level 'components' section must be a list.")
        components_list = []

    if not isinstance(capabilities_list, list):
        errors.append("Top-level 'capabilities' section must be a list.")
        capabilities_list = []

    # 1. Validate Components
    component_ids = set()
    components_by_id = {}
    deprecated_component_ids = set()

    # Load optional migration state for Wave F physical directory harmonization
    migration_state_path = repo_root / "docs" / "governance" / "migration_state.json"
    migration_state = {}
    if migration_state_path.exists():
        try:
            import json
            with open(migration_state_path, "r", encoding="utf-8") as mf:
                m_data = json.load(mf)
            migration_state = m_data.get("components", {})
        except Exception as e:
            errors.append(f"Failed to parse migration_state.json: {e}")

    # Negative assertion: Only authorized pilot components permitted in migration_state
    AUTHORIZED_PILOT_COMPONENTS = {"public-scholarship", "editor-jacobin-lat"}
    for mc_id in migration_state:
        if mc_id not in AUTHORIZED_PILOT_COMPONENTS:
            errors.append(f"Component '{mc_id}' found in migration_state.json but is outside the authorized pilot envelope.")

    for idx, comp in enumerate(components_list):
        if not isinstance(comp, dict):
            errors.append(f"Component at index {idx} is not a dictionary.")
            continue

        cid = comp.get("component_id")
        if not cid:
            errors.append(f"Component at index {idx} missing 'component_id'.")
            continue

        # Rule 1: component_id uniqueness
        if cid in component_ids:
            errors.append(f"Duplicate component_id found: '{cid}'.")
        component_ids.add(cid)
        components_by_id[cid] = comp

        # Required fields
        missing_fields = REQUIRED_COMPONENT_FIELDS - set(comp.keys())
        if missing_fields:
            errors.append(f"Component '{cid}' missing required fields: {missing_fields}")

        # Rule 11: mode_bearing is boolean
        mode_bearing = comp.get("mode_bearing")
        if not isinstance(mode_bearing, bool):
            errors.append(f"Component '{cid}' field 'mode_bearing' must be boolean, got {type(mode_bearing)}.")

        # Rule 8: lifecycle_status vocabulary
        l_status = comp.get("lifecycle_status")
        if l_status not in ALLOWED_LIFECYCLE_STATUSES:
            errors.append(f"Component '{cid}' has invalid lifecycle_status '{l_status}'. Allowed: {ALLOWED_LIFECYCLE_STATUSES}")
        if l_status == "DEPRECATED":
            deprecated_component_ids.add(cid)

        # Vocabulary checks for implementation_type and semantic_role
        impl_type = comp.get("current_implementation_type")
        if impl_type not in ALLOWED_IMPLEMENTATION_TYPES:
            errors.append(f"Component '{cid}' has invalid current_implementation_type '{impl_type}'. Allowed: {ALLOWED_IMPLEMENTATION_TYPES}")

        sem_role = comp.get("semantic_role")
        if sem_role not in ALLOWED_SEMANTIC_ROLES:
            errors.append(f"Component '{cid}' has invalid semantic_role '{sem_role}'. Allowed: {ALLOWED_SEMANTIC_ROLES}")

        # Rule 4 & 12: runtime_path exists on disk, reconciled with migration_state
        r_path = comp.get("runtime_path")
        if not r_path:
            errors.append(f"Component '{cid}' missing runtime_path.")
        else:
            disk_path = repo_root / r_path
            if cid in migration_state:
                c_info = migration_state[cid]
                c_state = c_info.get("state")
                expected_canonical = c_info.get("canonical_runtime_path")
                if c_state == "MIGRATED_TARGET":
                    if r_path != expected_canonical:
                        errors.append(f"Component '{cid}' has state MIGRATED_TARGET but runtime_path '{r_path}' does not match canonical '{expected_canonical}'.")
                    if not disk_path.exists():
                        errors.append(f"Component '{cid}' migrated target path '{r_path}' does not exist on disk.")
                    if cid == "public-scholarship":
                        baseline_root = repo_root / "public-scholarship"
                        if baseline_root.is_dir():
                            ref_dir = baseline_root / "references"
                            skill_file = baseline_root / "SKILL.md"
                            is_substantive = False
                            if ref_dir.is_dir() and any(ref_dir.iterdir()):
                                is_substantive = True
                            elif skill_file.exists():
                                content = skill_file.read_text(encoding="utf-8")
                                if "COMPATIBILITY_TRANSITION_STUB" not in content:
                                    is_substantive = True
                            if is_substantive:
                                errors.append(f"Forbidden duplicate: baseline root path '{baseline_root}' still exists as a substantive skill directory after MIGRATED_TARGET.")
                elif c_state == "DEPRECATED_ALIAS":
                    if r_path != expected_canonical:
                        errors.append(f"Component '{cid}' has state DEPRECATED_ALIAS but runtime_path '{r_path}' does not match canonical '{expected_canonical}'.")
                    if not disk_path.exists():
                        errors.append(f"Component '{cid}' alias runtime_path '{r_path}' does not exist on disk.")

                # Validate required compatibility entries
                for entry in c_info.get("allowed_compatibility_entries", []):
                    entry_p = repo_root / entry["path"]
                    if not entry_p.exists():
                        errors.append(f"Component '{cid}' required compatibility entry '{entry['path']}' missing on disk.")
            else:
                # Rule 12: Check for accidental future target paths
                if any(r_path.startswith(prefix) for prefix in ("skills/", "orchestrator/")):
                    errors.append(f"Component '{cid}' has future target path format as runtime_path: '{r_path}', but is not MIGRATED_TARGET.")

                if not disk_path.exists():
                    errors.append(f"Component '{cid}' runtime_path '{r_path}' does not exist on disk at {disk_path}.")

        # Check replacement_path if present
        rep_path = comp.get("replacement_path")
        if rep_path:
            disk_rep = repo_root / rep_path
            if not disk_rep.exists():
                errors.append(f"Component '{cid}' replacement_path '{rep_path}' does not exist on disk.")

    if len(component_ids) < 14:
        errors.append(f"Expected at least 14 components in registry, found {len(component_ids)}.")

    # 2. Validate Capabilities
    capability_ids = set()
    capabilities_by_id = {}

    for idx, cap in enumerate(capabilities_list):
        if not isinstance(cap, dict):
            errors.append(f"Capability at index {idx} is not a dictionary.")
            continue

        cap_id = cap.get("capability_id")
        if not cap_id:
            errors.append(f"Capability at index {idx} missing 'capability_id'.")
            continue

        # Rule 2: capability_id uniqueness
        if cap_id in capability_ids:
            errors.append(f"Duplicate capability_id found: '{cap_id}'.")
        capability_ids.add(cap_id)
        capabilities_by_id[cap_id] = cap

        # Required fields
        missing_cap_fields = REQUIRED_CAPABILITY_FIELDS - set(cap.keys())
        if missing_cap_fields:
            errors.append(f"Capability '{cap_id}' missing required fields: {missing_cap_fields}")

        # Rule 7: migration_status vocabulary
        m_status = cap.get("migration_status")
        if m_status not in ALLOWED_MIGRATION_STATUSES:
            errors.append(f"Capability '{cap_id}' has invalid migration_status '{m_status}'. Allowed: {ALLOWED_MIGRATION_STATUSES}")

        # Rule 3: every non-null current_owner exists in components
        cur_owner = cap.get("current_owner")
        if cur_owner is not None:
            if cur_owner not in component_ids:
                errors.append(f"Capability '{cap_id}' has current_owner '{cur_owner}' which is not a recognized component_id.")
            # Wave C5 Invariant: Deprecated aliases own zero canonical capabilities
            if cur_owner in deprecated_component_ids:
                errors.append(f"Capability '{cap_id}' is owned by deprecated component '{cur_owner}'. Deprecated aliases must own zero capabilities.")

        # Rule 6 & 10: No capability has two current canonical owners; no CANDIDATE capability is active current owner
        if m_status == "CANDIDATE":
            if cur_owner is not None:
                errors.append(f"Capability '{cap_id}' has status CANDIDATE but defines active current_owner '{cur_owner}'.")

        # Rule 9: current_owner and target_owner semantics are distinguishable
        tgt_owner = cap.get("target_owner")
        if cur_owner is not None and tgt_owner is not None:
            if cur_owner == tgt_owner and any(cur_owner.startswith(p) for p in ("skills/", "orchestrator/")):
                errors.append(f"Capability '{cap_id}' conflates target path as current_owner: '{cur_owner}'.")

    # 3. Validate Wave B1 / Wave C5 Routing & Precedence Invariants
    routing_components = {
        "academic-paper", "econ-write", "academic-paper-reviewer",
        "academic-pipeline", "deep-research", "econ-slides"
    }
    missing_rc = routing_components - component_ids
    if missing_rc:
        errors.append(f"Missing essential routing component(s): {missing_rc}")

    # B1 Invariant 1 & 2: runtime paths exist and never resolve to future target path prefixes
    for cid in routing_components:
        comp = components_by_id.get(cid)
        if comp:
            rpath = comp.get("runtime_path", "")
            if not (repo_root / rpath).exists():
                errors.append(f"Routing component '{cid}' runtime path '{rpath}' does not exist on disk.")
            if any(rpath.startswith(prefix) for prefix in ("skills/", "orchestrator/")):
                errors.append(f"Routing component '{cid}' leaked future target path into runtime_path: '{rpath}'.")

    # B1 Invariant 3: academic-paper owns generic manuscript lifecycle
    aml_cap = capabilities_by_id.get("academic_manuscript_lifecycle")
    if not aml_cap or aml_cap.get("current_owner") != "academic-paper":
        errors.append("Invariant violation: 'academic_manuscript_lifecycle' must be currently owned by 'academic-paper'.")

    # B1 Invariant 4: econ-write owns economics writing standards
    econ_cap = capabilities_by_id.get("economics_prose_and_section_standards")
    if not econ_cap or econ_cap.get("current_owner") != "econ-write":
        errors.append("Invariant violation: 'economics_prose_and_section_standards' must be currently owned by 'econ-write'.")

    # B1 Invariant 5: academic-paper-reviewer owns external peer review
    review_cap = capabilities_by_id.get("simulated_external_peer_review")
    if not review_cap or review_cap.get("current_owner") != "academic-paper-reviewer":
        errors.append("Invariant violation: 'simulated_external_peer_review' must be currently owned by 'academic-paper-reviewer'.")

    # B1 Invariant 6: academic-pipeline is ORCHESTRATOR
    pipe_comp = components_by_id.get("academic-pipeline")
    pipe_cap = capabilities_by_id.get("research_workflow_orchestration")
    if not pipe_comp or pipe_comp.get("semantic_role") != "ORCHESTRATOR" or pipe_comp.get("current_implementation_type") != "ORCHESTRATOR":
        errors.append("Invariant violation: 'academic-pipeline' component must have semantic_role and implementation_type 'ORCHESTRATOR'.")
    if not pipe_cap or pipe_cap.get("current_owner") != "academic-pipeline":
        errors.append("Invariant violation: 'research_workflow_orchestration' must be currently owned by 'academic-pipeline'.")

    # B1 Invariant 7: No second canonical external-review owner exists
    review_owners = [
        cap.get("current_owner") for cap in capabilities_list
        if "peer_review" in cap.get("capability_id", "") and cap.get("current_owner") is not None
    ]
    if len(review_owners) != 1 or review_owners[0] != "academic-paper-reviewer":
        errors.append(f"Invariant violation: Exactly one peer review owner permitted, found {review_owners}.")

    # Wave C5 Invariant: Advisor and committee components are profiles, not canonical peer-review owners
    for prof_id in ("advisor-reviewer", "PE-phd-committee", "advisor-michael-ash", "committee-umass-pe"):
        prof_comp = components_by_id.get(prof_id)
        if prof_comp:
            if prof_comp.get("semantic_role") != "PROFILE":
                errors.append(f"Invariant violation: Profile component '{prof_id}' must have semantic_role 'PROFILE'.")
            if review_cap and review_cap.get("current_owner") == prof_id:
                errors.append(f"Invariant violation: Profile component '{prof_id}' cannot be canonical owner of peer review.")

    # Wave C5 Invariant: Editorial governance is active change-control, does not own review or writing
    eg_comp = components_by_id.get("editorial-governance")
    if not eg_comp or eg_comp.get("lifecycle_status") != "ACTIVE":
        errors.append("Wave C5 violation: 'editorial-governance' must be an ACTIVE component in registry.")
    eg_cap = capabilities_by_id.get("editorial_decision_persistence")
    if not eg_cap or eg_cap.get("current_owner") != "editorial-governance":
        errors.append("Wave C5 violation: 'editorial_decision_persistence' must be owned by 'editorial-governance'.")

    # Wave C5 Invariant: Prose discipline is active shared protocol
    pd_comp = components_by_id.get("prose-discipline")
    if not pd_comp or pd_comp.get("lifecycle_status") != "ACTIVE":
        errors.append("Wave C5 violation: 'prose-discipline' must be an ACTIVE component in registry.")
    pd_cap = capabilities_by_id.get("prose_discipline_and_lexical_audit")
    if not pd_cap or pd_cap.get("current_owner") != "prose-discipline":
        errors.append("Wave C5 violation: 'prose_discipline_and_lexical_audit' must be owned by 'prose-discipline'.")

    # 4. Validate Wave D6 Domain Governance Invariants
    # Invariant D6-1: political-economy-research is an ACTIVE domain skill owning political_economy_research_methodology
    pe_comp = components_by_id.get("political-economy-research")
    if not pe_comp or pe_comp.get("lifecycle_status") != "ACTIVE" or pe_comp.get("semantic_role") != "DOMAIN_SKILL":
        errors.append("Wave D6 violation: 'political-economy-research' must be an ACTIVE DOMAIN_SKILL in registry.")
    pe_cap = capabilities_by_id.get("political_economy_research_methodology")
    if not pe_cap or pe_cap.get("current_owner") != "political-economy-research" or pe_cap.get("migration_status") != "CURRENT":
        errors.append("Wave D6 violation: 'political_economy_research_methodology' must be currently owned by 'political-economy-research'.")

    # Invariant D6-2: historical-source-criticism is an ACTIVE shared protocol owning claim_relative_source_criticism
    hsc_comp = components_by_id.get("historical-source-criticism")
    if not hsc_comp or hsc_comp.get("lifecycle_status") != "ACTIVE" or hsc_comp.get("semantic_role") != "SHARED_PROTOCOL":
        errors.append("Wave D6 violation: 'historical-source-criticism' must be an ACTIVE SHARED_PROTOCOL in registry.")
    hsc_cap = capabilities_by_id.get("claim_relative_source_criticism")
    if not hsc_cap or hsc_cap.get("current_owner") != "historical-source-criticism" or hsc_cap.get("migration_status") != "CURRENT":
        errors.append("Wave D6 violation: 'claim_relative_source_criticism' must be owned by 'historical-source-criticism'.")

    # Invariant D6-3: umass-applied-econometrics owns applied_econometrics_political_economy with CURRENT migration_status
    ae_comp = components_by_id.get("umass-applied-econometrics")
    if not ae_comp or ae_comp.get("lifecycle_status") != "ACTIVE" or ae_comp.get("semantic_role") != "DOMAIN_SKILL":
        errors.append("Wave D6 violation: 'umass-applied-econometrics' must be an ACTIVE DOMAIN_SKILL in registry.")
    ae_cap = capabilities_by_id.get("applied_econometrics_political_economy")
    if not ae_cap or ae_cap.get("current_owner") != "umass-applied-econometrics" or ae_cap.get("migration_status") != "CURRENT":
        errors.append("Wave D6 violation: 'applied_econometrics_political_economy' must be currently owned by 'umass-applied-econometrics'.")

    # Invariant D6-4: heterodox-economics-review owns heterodox_macro_modeling with CURRENT migration_status
    macro_comp = components_by_id.get("heterodox-economics-review")
    if not macro_comp or macro_comp.get("lifecycle_status") != "ACTIVE" or macro_comp.get("semantic_role") != "DOMAIN_SKILL":
        errors.append("Wave D6 violation: 'heterodox-economics-review' must be an ACTIVE DOMAIN_SKILL in registry.")
    macro_cap = capabilities_by_id.get("heterodox_macro_modeling")
    if not macro_cap or macro_cap.get("current_owner") != "heterodox-economics-review" or macro_cap.get("migration_status") != "CURRENT":
        errors.append("Wave D6 violation: 'heterodox_macro_modeling' must be currently owned by 'heterodox-economics-review'.")

    # Invariant D6-5: causal_inference_microeconometrics is preserved as unassigned capability gap (CANDIDATE, current_owner: null)
    ci_cap = capabilities_by_id.get("causal_inference_microeconometrics")
    if not ci_cap:
        errors.append("Wave D6 violation: 'causal_inference_microeconometrics' capability must exist in registry.")
    elif ci_cap.get("current_owner") is not None or ci_cap.get("migration_status") != "CANDIDATE":
        errors.append("Wave D6 violation: 'causal_inference_microeconometrics' must have current_owner: null and migration_status: CANDIDATE.")

    # 5. Validate Wave E Dissemination Governance Invariants
    # Invariant E-1: public-scholarship is an ACTIVE DISSEMINATION_SKILL owning public_scholarship_translation
    ps_comp = components_by_id.get("public-scholarship")
    if not ps_comp or ps_comp.get("lifecycle_status") != "ACTIVE" or ps_comp.get("semantic_role") != "DISSEMINATION_SKILL":
        errors.append("Wave E violation: 'public-scholarship' must be an ACTIVE DISSEMINATION_SKILL in registry.")
    ps_cap = capabilities_by_id.get("public_scholarship_translation")
    if not ps_cap or ps_cap.get("current_owner") != "public-scholarship" or ps_cap.get("migration_status") != "CURRENT":
        errors.append("Wave E violation: 'public_scholarship_translation' must be currently owned by 'public-scholarship'.")

    # Invariant E-2: venue-jacobin-lat is an ACTIVE PROFILE owning venue_jacobin_lat_editorial
    vj_comp = components_by_id.get("venue-jacobin-lat")
    if not vj_comp or vj_comp.get("lifecycle_status") != "ACTIVE" or vj_comp.get("semantic_role") != "PROFILE":
        errors.append("Wave E violation: 'venue-jacobin-lat' must be an ACTIVE PROFILE in registry.")
    vj_cap = capabilities_by_id.get("venue_jacobin_lat_editorial")
    if not vj_cap or vj_cap.get("current_owner") != "venue-jacobin-lat" or vj_cap.get("migration_status") != "CURRENT":
        errors.append("Wave E violation: 'venue_jacobin_lat_editorial' must be owned by 'venue-jacobin-lat'.")

    # Invariant E-3: editor-jacobin-lat is a DEPRECATED LEGACY_SKILL delegating to public-scholarship
    ej_comp = components_by_id.get("editor-jacobin-lat")
    if not ej_comp or ej_comp.get("lifecycle_status") != "DEPRECATED" or ej_comp.get("current_implementation_type") != "LEGACY_SKILL":
        errors.append("Wave E violation: 'editor-jacobin-lat' must be a DEPRECATED LEGACY_SKILL in registry.")
    if ej_comp and ej_comp.get("delegates_to") != "public-scholarship":
        errors.append("Wave E violation: 'editor-jacobin-lat' must delegate_to 'public-scholarship'.")
    if ej_comp and ej_comp.get("replacement_path") != "profiles/venues/jacobin-lat.md":
        errors.append("Wave E violation: 'editor-jacobin-lat' replacement_path must be 'profiles/venues/jacobin-lat.md'.")

    return errors


def validate_registry(repo_root: Path) -> bool:
    registry_path = repo_root / "docs" / "governance" / "ars_registry.yaml"
    if not registry_path.exists():
        print(f"FAIL: Registry file not found at {registry_path}")
        return False

    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"FAIL: YAML parsing error: {e}")
        return False

    errors = validate_registry_data(data, repo_root)

    if errors:
        print(f"FAIL: {len(errors)} validation errors found in ars_registry.yaml:")
        for err in errors:
            print(f"  - {err}")
        return False

    component_ids = {
        c["component_id"] for c in data.get("components", [])
        if isinstance(c, dict) and "component_id" in c
    }
    capability_ids = {
        c["capability_id"] for c in data.get("capabilities", [])
        if isinstance(c, dict) and "capability_id" in c
    }
    print("PASS: ars_registry.yaml is valid.")
    print(f"  - Components validated: {len(component_ids)}")
    print(f"  - Capabilities validated: {len(capability_ids)}")
    return True


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent
    success = validate_registry(root_dir)
    sys.exit(0 if success else 1)
