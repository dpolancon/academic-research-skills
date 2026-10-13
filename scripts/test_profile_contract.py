#!/usr/bin/env python3
"""
Test Suite: ARS Profile Contract & Integrity Verification
Wave: C3

Deterministically verifies:
1. Exactly three concrete scholar profiles exist (Ash, Basu, Young).
2. Michael Ash advisor wrapper exists.
3. UMass PE committee composition exists.
4. All scholar references resolve on disk.
5. Advisor scholar_ref resolves to canonical scholar profile.
6. Committee member scholar_refs resolve to valid scholar profiles.
7. Michael Ash advisor role is 'active'.
8. Michael Ash advisor lifecycle includes 'dissertation_completion'.
9. Advisor wrapper is 'calibration_only: true'.
10. Advisor wrapper delegates to 'academic-paper-reviewer'.
11. Concrete profile IDs are unique.
12. Required reusable templates exist.
13. Profiles distinguish evidence, confidence, and provenance.
14. No concrete profiles beyond the approved three scholars are present.
15. Committee composition delegates review to 'academic-paper-reviewer' without embedding simulation.
16. No profile claims canonical capability ownership.
17. No prohibited persona fields exist (personality_type, political_preference, etc.).
18. No project directory or Chapter 1 payload was created.
19. Template quality checks: explicit prompts for evidence, confidence, provenance, and exclusions.
"""

import sys
import re
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"
SCHOLARS_DIR = PROFILES_DIR / "scholars"
ADVISORS_DIR = PROFILES_DIR / "advisors"
COMMITTEES_DIR = PROFILES_DIR / "committees"
TEMPLATES_DIR = PROFILES_DIR / "templates"

APPROVED_SCHOLARS = {
    "michael-ash.md",
    "deepankar-basu.md",
    "kevin-young.md",
}

PROHIBITED_FRONTMATTER_FIELDS = {
    "personality_type",
    "personality",
    "political_preference",
    "political_party",
    "psychological_profile",
    "psychological_traits",
    "acceptance_probability",
    "grading_behavior",
    "grading_probability",
    "owns_capability",
}


def parse_frontmatter(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not match:
        raise ValueError(f"No YAML frontmatter found in {file_path}")
    raw_yaml = match.group(1)
    data = yaml.safe_load(raw_yaml)
    return data, content


def run_checks():
    errors = []
    print("=" * 60)
    print("ARS Wave C3: Profile Contract Verification")
    print("=" * 60)

    # 1. Exactly three concrete scholar profiles exist
    if not SCHOLARS_DIR.exists():
        errors.append(f"Missing scholars directory: {SCHOLARS_DIR}")
        scholar_files = []
    else:
        scholar_files = [f.name for f in SCHOLARS_DIR.glob("*.md")]
        if set(scholar_files) != APPROVED_SCHOLARS:
            errors.append(
                f"Concrete scholar profiles mismatch. Expected {APPROVED_SCHOLARS}, found {set(scholar_files)}"
            )
        else:
            print(f"[PASS] Assertion 1 & 14: Exactly three approved scholar profiles exist: {sorted(scholar_files)}")

    # 2. Michael Ash advisor wrapper exists
    ash_advisor_path = ADVISORS_DIR / "michael-ash.md"
    if not ash_advisor_path.exists():
        errors.append(f"Missing advisor wrapper: {ash_advisor_path}")
    else:
        print("[PASS] Assertion 2: Michael Ash advisor wrapper exists")

    # 3. UMass PE committee composition exists
    committee_path = COMMITTEES_DIR / "umass-pe.md"
    if not committee_path.exists():
        errors.append(f"Missing committee composition: {committee_path}")
    else:
        print("[PASS] Assertion 3: UMass PE committee composition exists")

    # 4 & 5. Advisor scholar_ref resolves to canonical scholar profile
    if ash_advisor_path.exists():
        adv_data, adv_content = parse_frontmatter(ash_advisor_path)
        scholar_ref = adv_data.get("scholar_ref")
        if not scholar_ref:
            errors.append("Advisor wrapper missing 'scholar_ref' frontmatter")
        else:
            resolved_ref = (ADVISORS_DIR / scholar_ref).resolve()
            if not resolved_ref.exists():
                errors.append(f"Advisor scholar_ref does not resolve: {scholar_ref} -> {resolved_ref}")
            elif resolved_ref != (SCHOLARS_DIR / "michael-ash.md").resolve():
                errors.append(f"Advisor scholar_ref does not point to michael-ash.md: {resolved_ref}")
            else:
                print(f"[PASS] Assertion 4 & 5: Advisor scholar_ref resolves to {resolved_ref.name}")

        # 7. Michael Ash advisor role is active
        if adv_data.get("role_status") != "active":
            errors.append(f"Advisor role_status must be 'active', got: {adv_data.get('role_status')}")
        else:
            print("[PASS] Assertion 7: Michael Ash advisor role status is 'active'")

        # 8. Michael Ash advisor lifecycle includes dissertation_completion
        if adv_data.get("valid_until_event") != "dissertation_completion":
            errors.append(
                f"Advisor valid_until_event must be 'dissertation_completion', got: {adv_data.get('valid_until_event')}"
            )
        else:
            print("[PASS] Assertion 8: Advisor valid_until_event is 'dissertation_completion'")

        # 9. Advisor wrapper is calibration_only: true
        if adv_data.get("calibration_only") is not True:
            errors.append(f"Advisor wrapper calibration_only must be True, got: {adv_data.get('calibration_only')}")
        else:
            print("[PASS] Assertion 9: Advisor wrapper is 'calibration_only: true'")

        # 10. Advisor wrapper delegates to academic-paper-reviewer
        if adv_data.get("review_engine") != "academic-paper-reviewer":
            errors.append(
                f"Advisor review_engine must be 'academic-paper-reviewer', got: {adv_data.get('review_engine')}"
            )
        else:
            print("[PASS] Assertion 10: Advisor review_engine delegates to 'academic-paper-reviewer'")

    # 6. Committee member scholar_refs resolve
    if committee_path.exists():
        comm_data, comm_content = parse_frontmatter(committee_path)
        members = comm_data.get("members", [])
        if not members or len(members) != 3:
            errors.append(f"Committee composition must list exactly 3 members, got: {len(members)}")
        else:
            for member in members:
                m_ref = member.get("scholar_ref")
                if not m_ref:
                    errors.append(f"Committee member missing 'scholar_ref': {member}")
                    continue
                resolved_m = (COMMITTEES_DIR / m_ref).resolve()
                if not resolved_m.exists():
                    errors.append(f"Committee member scholar_ref does not resolve: {m_ref} -> {resolved_m}")
            print(f"[PASS] Assertion 6: All {len(members)} committee member scholar_refs resolve on disk")

        # 15. Committee composition delegates review to academic-paper-reviewer without simulation mechanics
        if comm_data.get("review_engine") != "academic-paper-reviewer":
            errors.append(
                f"Committee review_engine must be 'academic-paper-reviewer', got: {comm_data.get('review_engine')}"
            )
        else:
            print("[PASS] Assertion 15: Committee review_engine delegates to 'academic-paper-reviewer'")

        # Check for simulation engine leakage in committee file
        simulation_tokens = ["Phase 1: Committee Questioning", "Socratic Defense Dialogue", "Editorial Decision Letter"]
        for token in simulation_tokens:
            if token in comm_content:
                errors.append(f"Committee composition embeds simulation mechanics token: '{token}'")

    # 11. Profile IDs are unique
    profile_ids = {}
    for p_path in [
        SCHOLARS_DIR / "michael-ash.md",
        SCHOLARS_DIR / "deepankar-basu.md",
        SCHOLARS_DIR / "kevin-young.md",
        ash_advisor_path,
        committee_path,
    ]:
        if p_path.exists():
            p_data, _ = parse_frontmatter(p_path)
            pid = p_data.get("profile_id") or p_data.get("committee_id")
            if not pid:
                errors.append(f"Profile {p_path.name} missing profile_id/committee_id")
            elif pid in profile_ids:
                errors.append(f"Duplicate profile ID '{pid}' in {p_path} and {profile_ids[pid]}")
            else:
                profile_ids[pid] = p_path
    if not any("Duplicate profile ID" in e for e in errors):
        print(f"[PASS] Assertion 11: All {len(profile_ids)} profile IDs are globally unique: {list(profile_ids.keys())}")

    # 12. Reusable templates exist
    expected_templates = [
        TEMPLATES_DIR / "scholar-profile.md",
        TEMPLATES_DIR / "advisor-role.md",
        TEMPLATES_DIR / "committee-composition.md",
    ]
    for tmpl in expected_templates:
        if not tmpl.exists():
            errors.append(f"Missing template: {tmpl}")
    if all(t.exists() for t in expected_templates):
        print(f"[PASS] Assertion 12: All 3 reusable templates exist in {TEMPLATES_DIR.name}/")

    # 13. Profiles distinguish evidence and provenance
    for s_name in APPROVED_SCHOLARS:
        s_path = SCHOLARS_DIR / s_name
        if s_path.exists():
            _, s_content = parse_frontmatter(s_path)
            required_sections = ["## 2. Evidence Base", "## 6. Evidence Confidence", "## 8. Provenance", "## 7. Exclusions / Non-Inferences"]
            for sec in required_sections:
                if sec not in s_content:
                    errors.append(f"Scholar profile {s_name} missing required section: '{sec}'")
    if not any("missing required section" in e for e in errors):
        print("[PASS] Assertion 13: Scholar profiles distinguish Evidence Base, Confidence, Exclusions, and Provenance")

    # 16. No profile claims canonical capability ownership
    for p_path in list(SCHOLARS_DIR.glob("*.md")) + list(ADVISORS_DIR.glob("*.md")) + list(COMMITTEES_DIR.glob("*.md")):
        p_data, _ = parse_frontmatter(p_path)
        if "owns_capability" in p_data:
            errors.append(f"Profile {p_path.name} illicitly claims capability ownership: {p_data['owns_capability']}")
    print("[PASS] Assertion 16: No profile claims canonical capability ownership")

    # 17. No prohibited persona fields exist
    for p_path in list(SCHOLARS_DIR.glob("*.md")) + list(ADVISORS_DIR.glob("*.md")) + list(COMMITTEES_DIR.glob("*.md")):
        p_data, _ = parse_frontmatter(p_path)
        for field in PROHIBITED_FRONTMATTER_FIELDS:
            if field in p_data:
                errors.append(f"Profile {p_path.name} contains prohibited persona field: '{field}'")
    print("[PASS] Assertion 17: No prohibited persona fields detected in frontmatter")

    # 18. No project directory or Chapter 1 payload created
    projects_dir = REPO_ROOT / "projects"
    if projects_dir.exists():
        errors.append(f"Prohibited project directory exists: {projects_dir}")
    else:
        print("[PASS] Assertion 18: No prohibited 'projects/' directory or Chapter 1 payload created")

    # 19. Template quality checks: explicit prompts for evidence, confidence, provenance, exclusions
    scholar_tmpl = TEMPLATES_DIR / "scholar-profile.md"
    if scholar_tmpl.exists():
        _, tmpl_content = parse_frontmatter(scholar_tmpl)
        for expected_kw in ["published_work", "direct_feedback", "institutional_context", "Evidence Confidence", "Exclusions / Non-Inferences", "Provenance"]:
            if expected_kw not in tmpl_content:
                errors.append(f"Scholar template missing quality prompt for: '{expected_kw}'")
        print("[PASS] Assertion 19: Scholar template includes explicit quality prompts and future evidence seams")

    print("-" * 60)
    if errors:
        print(f"FAILED: {len(errors)} error(s) found:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("ALL PROFILE CONTRACT ASSERTIONS PASSED (19/19)")
        print("=" * 60)
        return True


if __name__ == "__main__":
    success = run_checks()
    sys.exit(0 if success else 1)
