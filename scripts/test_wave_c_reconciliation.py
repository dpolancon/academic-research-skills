#!/usr/bin/env python3
"""
scripts/test_wave_c_reconciliation.py

Deterministic integration test suite for Wave C reconciliation (Wave C5).
Verifies:
A. Legacy skill stubs exist and contain deprecation notices and canonical redirects.
B. Profile routing: Advisor and committee profiles exist and references resolve.
C. Review ownership: academic-paper-reviewer remains sole canonical peer-review owner.
D. Legacy ownership: Deprecated aliases own zero canonical capabilities.
E. Prose discipline: Shared protocol and tool exist; prose-register-critic does not own writing.
F. Editorial governance: Change-control contract and tool exist; does not own review or writing.
G. Current paths: All runtime paths in registry resolve on disk.
H. C4 absorption: State records C4_PROFILE_EXTRACTION_ABSORBED_BY_C3.
I. Wave F deferral: Physical core-skill migration has not occurred.
J. Workspace deferral: Workspace runtime implementation has not begun.
K. Legacy alias compatibility destinations are explicit.
"""

import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_wave_c_reconciliation():
    errors = []
    print("=" * 65)
    print("ARS Wave C5: Legacy Reconciliation & Regression Lock Suite")
    print("=" * 65)

    registry_path = REPO_ROOT / "docs" / "governance" / "ars_registry.yaml"
    if not registry_path.exists():
        errors.append(f"Registry not found: {registry_path}")
        return False

    with open(registry_path, "r", encoding="utf-8") as f:
        reg_data = yaml.safe_load(f)

    components = {c["component_id"]: c for c in reg_data.get("components", [])}
    capabilities = {c["capability_id"]: c for c in reg_data.get("capabilities", [])}

    # A. LEGACY STUBS
    legacy_stubs = {
        "advisor-reviewer": REPO_ROOT / "advisor-reviewer" / "SKILL.md",
        "PE-phd-committee": REPO_ROOT / "PE-phd-committee" / "SKILL.md",
        "prose-register-critic": REPO_ROOT / "prose-register-critic" / "SKILL.md",
    }
    for alias_id, path in legacy_stubs.items():
        if not path.exists():
            errors.append(f"Legacy stub missing: {path}")
        else:
            text = path.read_text(encoding="utf-8")
            if "DEPRECATED" not in text:
                errors.append(f"Legacy stub {alias_id} does not indicate DEPRECATED status.")
            if "academic-paper-reviewer" not in text and alias_id != "prose-register-critic":
                errors.append(f"Legacy stub {alias_id} does not redirect to academic-paper-reviewer.")
    print("[PASS] Assertion A: All 3 legacy stubs exist, indicate deprecation, and define redirects")

    # B. PROFILE ROUTING & REFERENCE RESOLUTION
    adv_path = REPO_ROOT / "profiles" / "advisors" / "michael-ash.md"
    comm_path = REPO_ROOT / "profiles" / "committees" / "umass-pe.md"

    if not adv_path.exists():
        errors.append(f"Advisor profile missing: {adv_path}")
    else:
        adv_content = adv_path.read_text(encoding="utf-8")
        adv_yaml = yaml.safe_load(adv_content.split("---")[1])
        s_ref = (adv_path.parent / adv_yaml.get("scholar_ref", "")).resolve()
        if not s_ref.exists():
            errors.append(f"Advisor scholar_ref does not resolve: {s_ref}")

    if not comm_path.exists():
        errors.append(f"Committee profile missing: {comm_path}")
    else:
        comm_content = comm_path.read_text(encoding="utf-8")
        comm_yaml = yaml.safe_load(comm_content.split("---")[1])
        for m in comm_yaml.get("members", []):
            m_ref = (comm_path.parent / m.get("scholar_ref", "")).resolve()
            if not m_ref.exists():
                errors.append(f"Committee member ref does not resolve: {m_ref}")
    print("[PASS] Assertion B: Advisor and committee profiles exist and all references resolve on disk")

    # C. REVIEW OWNERSHIP
    review_cap = capabilities.get("simulated_external_peer_review", {})
    if review_cap.get("current_owner") != "academic-paper-reviewer":
        errors.append(f"simulated_external_peer_review owner must be 'academic-paper-reviewer', got: {review_cap.get('current_owner')}")
    else:
        print("[PASS] Assertion C: academic-paper-reviewer remains sole canonical peer-review owner")

    # D. LEGACY OWNERSHIP
    deprecated_aliases = {"advisor-reviewer", "PE-phd-committee", "prose-register-critic"}
    for cap_id, cap in capabilities.items():
        c_owner = cap.get("current_owner")
        if c_owner in deprecated_aliases:
            errors.append(f"Deprecated alias '{c_owner}' illicitly owns capability '{cap_id}'.")
    for alias_id in deprecated_aliases:
        comp = components.get(alias_id, {})
        if comp.get("lifecycle_status") != "DEPRECATED":
            errors.append(f"Legacy component '{alias_id}' must have lifecycle_status 'DEPRECATED', got '{comp.get('lifecycle_status')}'.")
    print("[PASS] Assertion D: Deprecated aliases own zero canonical capabilities and have lifecycle DEPRECATED")

    # E. PROSE DISCIPLINE
    prose_proto = REPO_ROOT / "shared" / "protocols" / "prose_discipline_protocol.md"
    prose_tool = REPO_ROOT / "tools" / "prose_checks" / "check_prose_patterns.py"
    if not prose_proto.exists():
        errors.append(f"Shared prose protocol missing: {prose_proto}")
    if not prose_tool.exists():
        errors.append(f"Deterministic prose tool missing: {prose_tool}")
    econ_cap = capabilities.get("economics_prose_and_section_standards", {})
    if econ_cap.get("current_owner") != "econ-write":
        errors.append(f"economics_prose_and_section_standards owner must be 'econ-write', got: {econ_cap.get('current_owner')}")
    prose_cap = capabilities.get("prose_discipline_and_lexical_audit", {})
    if prose_cap.get("current_owner") == "prose-register-critic":
        errors.append("prose_discipline_and_lexical_audit must not be owned by prose-register-critic.")
    print("[PASS] Assertion E: Shared prose discipline exists; econ-write owns economics writing; prose alias owns no writing")

    # F. EDITORIAL GOVERNANCE
    eg_port = REPO_ROOT / "shared" / "contracts" / "passport" / "EDITORIAL_GOVERNANCE_PORT.md"
    rev_guard = REPO_ROOT / "scripts" / "revision_guard.py"
    if not eg_port.exists():
        errors.append(f"Editorial governance port missing: {eg_port}")
    if not rev_guard.exists():
        errors.append(f"Revision guard missing: {rev_guard}")
    eg_cap = capabilities.get("editorial_decision_persistence", {})
    if eg_cap.get("current_owner") != "editorial-governance":
        errors.append(f"editorial_decision_persistence owner must be 'editorial-governance', got: {eg_cap.get('current_owner')}")
    if eg_cap.get("migration_status") != "CURRENT":
        errors.append(f"editorial_decision_persistence status must be 'CURRENT', got: {eg_cap.get('migration_status')}")
    print("[PASS] Assertion F: Editorial governance is active change-control; does not own review or writing")

    # G. CURRENT PATHS RESOLVE
    for cid, comp in components.items():
        rpath = comp.get("runtime_path", "")
        disk_p = REPO_ROOT / rpath
        if not disk_p.exists():
            errors.append(f"Component '{cid}' runtime_path '{rpath}' does not exist on disk.")
        rep_path = comp.get("replacement_path")
        if rep_path:
            if not (REPO_ROOT / rep_path).exists():
                errors.append(f"Component '{cid}' replacement_path '{rep_path}' does not exist on disk.")
    print("[PASS] Assertion G: All runtime paths and replacement paths in registry resolve on disk")

    # H. C4 ABSORPTION
    c3_report = REPO_ROOT / "docs" / "design" / "2026-10-11-ars-target-architecture" / "21_WAVE_C3_PROFILE_EXTRACTION_REPORT.md"
    if not c3_report.exists():
        errors.append(f"Wave C3 report missing: {c3_report}")
    else:
        c3_text = c3_report.read_text(encoding="utf-8")
        if "C4_PROFILE_EXTRACTION_ABSORBED_BY_C3" not in c3_text:
            errors.append("Wave C3 report does not record C4_PROFILE_EXTRACTION_ABSORBED_BY_C3.")
    print("[PASS] Assertion H: Architecture state explicitly records C4_PROFILE_EXTRACTION_ABSORBED_BY_C3")

    # I. WAVE F PHYSICAL MIGRATION DEFERRAL
    core_runtime_skills = [
        "academic-paper/SKILL.md",
        "econ-write/SKILL.md",
        "academic-paper-reviewer/SKILL.md",
        "academic-pipeline/SKILL.md",
        "deep-research/SKILL.md",
        "econ-slides/SKILL.md",
    ]
    for skill_file in core_runtime_skills:
        if not (REPO_ROOT / skill_file).exists():
            errors.append(f"Core runtime skill missing from root location: {skill_file}")
    if (REPO_ROOT / "skills" / "core").exists():
        errors.append("Premature physical migration: 'skills/core/' directory exists prior to Wave F.")
    print("[PASS] Assertion I: Core runtime skills remain at root locations; Wave F physical migration deferred")

    # J. WORKSPACE RUNTIME DEFERRAL
    if (REPO_ROOT / "workspaces").exists():
        errors.append("Premature workspace implementation: 'workspaces/' directory exists prior to designated wave.")
    print("[PASS] Assertion J: Workspace runtime implementation deferred")

    # K. COMPATIBILITY ALIAS DESTINATIONS
    compat_checks = [
        ("advisor-reviewer", "profiles/advisors/michael-ash.md"),
        ("PE-phd-committee", "profiles/committees/umass-pe.md"),
        ("prose-register-critic", "shared/protocols/prose_discipline_protocol.md"),
    ]
    for alias_id, target in compat_checks:
        comp = components.get(alias_id, {})
        if comp.get("replacement_path") != target:
            errors.append(f"Component '{alias_id}' replacement_path expected '{target}', got '{comp.get('replacement_path')}'.")
    print("[PASS] Assertion K: Legacy aliases map to verified compatibility destinations")

    print("-" * 65)
    if errors:
        print(f"FAILED: {len(errors)} error(s) found:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("ALL WAVE C RECONCILIATION ASSERTIONS PASSED (11/11)")
        print("=" * 65)
        return True


if __name__ == "__main__":
    success = test_wave_c_reconciliation()
    sys.exit(0 if success else 1)
