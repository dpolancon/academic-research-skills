#!/usr/bin/env python3
"""
scripts/validate_ars_registry.py

Deterministic validation script for docs/governance/ars_registry.yaml.
Enforces the architectural invariants of the ARS Integrated Governance Foundation (Wave B0).
"""

import os
import sys
from pathlib import Path
import yaml

# Controlled Vocabularies
ALLOWED_IMPLEMENTATION_TYPES = {"SKILL", "LEGACY_SKILL", "ORCHESTRATOR", "TOOL"}
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

    errors = []

    # Check top-level structure
    if not isinstance(data, dict):
        print("FAIL: Root of registry must be a mapping/dict.")
        return False

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

        # Vocabulary checks for implementation_type and semantic_role
        impl_type = comp.get("current_implementation_type")
        if impl_type not in ALLOWED_IMPLEMENTATION_TYPES:
            errors.append(f"Component '{cid}' has invalid current_implementation_type '{impl_type}'.")

        sem_role = comp.get("semantic_role")
        if sem_role not in ALLOWED_SEMANTIC_ROLES:
            errors.append(f"Component '{cid}' has invalid semantic_role '{sem_role}'.")

        # Rule 4 & 12: runtime_path exists on disk and is not a future target path
        r_path = comp.get("runtime_path")
        if not r_path:
            errors.append(f"Component '{cid}' missing runtime_path.")
        else:
            # Check for accidental target paths (e.g. skills/core/..., profiles/..., tools/...)
            if any(r_path.startswith(prefix) for prefix in ("skills/", "profiles/", "orchestrator/", "tools/", "shared/")):
                errors.append(f"Component '{cid}' has future target path format as runtime_path: '{r_path}'.")

            disk_path = repo_root / r_path
            if not disk_path.exists():
                errors.append(f"Component '{cid}' runtime_path '{r_path}' does not exist on disk at {disk_path}.")

    if len(component_ids) != 14:
        errors.append(f"Expected exactly 14 components in registry, found {len(component_ids)}.")

    # 2. Validate Capabilities
    capability_ids = set()

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

        # Rule 6 & 10: No capability has two current canonical owners; no CANDIDATE capability is active current owner
        if m_status == "CANDIDATE":
            if cur_owner is not None:
                errors.append(f"Capability '{cap_id}' has status CANDIDATE but defines active current_owner '{cur_owner}'.")

        # Rule 9: current_owner and target_owner semantics are distinguishable
        tgt_owner = cap.get("target_owner")
        if cur_owner is not None and tgt_owner is not None:
            # If current_owner and target_owner have the exact same string when paths are involved
            if cur_owner == tgt_owner and any(cur_owner.startswith(p) for p in ("skills/", "tools/", "profiles/")):
                errors.append(f"Capability '{cap_id}' conflates target path as current_owner: '{cur_owner}'.")

    # Final summary output
    if errors:
        print(f"FAIL: {len(errors)} validation errors found in ars_registry.yaml:")
        for err in errors:
            print(f"  - {err}")
        return False

    print("PASS: ars_registry.yaml is valid.")
    print(f"  - Components validated: {len(component_ids)}")
    print(f"  - Capabilities validated: {len(capability_ids)}")
    return True


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent
    success = validate_registry(root_dir)
    sys.exit(0 if success else 1)
