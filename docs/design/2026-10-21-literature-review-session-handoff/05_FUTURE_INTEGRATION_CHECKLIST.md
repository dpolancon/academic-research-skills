# ARS LITERATURE-REVIEW SESSION HANDOFF — FUTURE INTEGRATION CHECKLIST

**Document Location:** `docs/design/2026-10-21-literature-review-session-handoff/05_FUTURE_INTEGRATION_CHECKLIST.md`  
**Target Audience:** Future Agent / Human Operator executing final branch reconciliation  
**Active Worktree:** `C:\ReposGitHub\academic-research-skills-literature-review` (`feat/literature-review`)  
**Canonical Repository:** `C:\ReposGitHub\academic-research-skills` (`main`)  
**Date:** 2026-10-21, America/Santiago  

---

## 1. Pre-Integration Verification Protocol

Before initiating any merge or rebase operation between `feat/literature-review` and canonical `main`, the operator must complete the following 12-step verification protocol:

```text
[ ] Step 1: Inspect Canonical ARS Main
    - Verify working tree status: Ensure no uncommitted or dirty files remain on canonical main.
    - Inspect git log: Identify all commits landed by parallel sprints (Wave E/F, dissemination, public-scholarship).

[ ] Step 2: Inspect Parallel Workflow Branches
    - Identify if parallel refactoring has completed and landed on main or remains on a feature branch.
    - If parallel work is still active, HALT immediately. Do not merge until parallel work reaches freeze.

[ ] Step 3: Read This Session Bundle
    - Read `00_SESSION_INDEX.md` through `06_SESSION_CLOSURE.md` in this directory to understand the full context.

[ ] Step 4: Inspect Literature-Review Integration Reports
    - Read `docs/design/2026-10-20-literature-review-consolidation/08_FINAL_INTEGRATION_REPORT.md` on main.
    - Confirm the baseline integration hash matches commit `5333e06`.

[ ] Step 5: Identify Overlapping Components
    - Run diff check between `feat/literature-review` and `main`:
      `git diff --stat feat/literature-review main`
    - Check for file collisions in `docs/governance/ars_registry.yaml`, `pyproject.toml`, or test harnesses.

[ ] Step 6: Distinguish Mechanical from Semantic Conflicts
    - Mechanical conflicts (e.g., adjacent entries in `ars_registry.yaml` or lists in documentation) may be resolved mechanically.
    - Semantic conflicts (e.g., changes to skill interfaces, registry schemas, or validation protocols) require careful reconciliation.

[ ] Step 7: Preserve Human-Sovereignty Invariants
    - Verify that no automated workflow removes human gates ($L_{13}$) or allows agents to self-ratify scholarly locks.

[ ] Step 8: Preserve Retrieval Backend Agnosticism
    - Ensure `notebooklm_adapter.py` and extraction utilities retain abstract interfaces (`ExtractionBackendBase`, `MockExtractionBackend`, `LocalNotesBackend`).

[ ] Step 9: Preserve Evidence -> Argument -> Prose Separation
    - Ensure the 3-tier sequence (Ledgers $L_6 \to$ Argument Assembly $L_7 \to$ Staged Prose $L_8 \to$ Manuscript $L_9$) is not collapsed into a single prompting shortcut.

[ ] Step 10: Run Full Registry & Literature-Review Tests
    - Execute pytest in the reconciled environment:
      `pytest literature-review/tests` -> MUST PASS 30/30.
    - Validate registry integrity:
      `python scripts/validate_ars_registry.py` -> MUST PASS.

[ ] Step 11: Reconcile Documentation
    - Ensure the session handoff bundle (`docs/design/2026-10-21-literature-review-session-handoff/`) is copied/preserved in canonical `main`.

[ ] Step 12: Merge and Freeze
    - Execute fast-forward or clean merge into main.
    - Tag or log the reconciled state.
```

---

## 2. Anticipated Conflict Classes & Resolution Rules

| Conflict Class | Manifestation | Resolution Rule |
|---|---|---|
| **Class A: Registry Schema Evolution** | Parallel redesign may have restructured `ars_registry.yaml` syntax or section headers. | Re-map the `literature-review` skill entries to conform to the new registry schema while preserving all declared components (`scripts`, `schemas`, `templates`, `references`). |
| **Class B: Skill Directory Re-namespacing** | Parallel redesign may have moved standalone skills into `skills/research/` or `skills/domain/`. | Move `literature-review/` to the new namespace path without altering internal relative links or test paths. |
| **Class C: Centralized Test Harness Changes** | Test root configuration in `pyproject.toml` or `conftest.py` altered. | Ensure `literature-review/tests` are included in root test discovery without breaking relative imports to `scripts/`. |
| **Class D: CLI or Shell Integration Changes** | Global CLI tooling updated in `tools/` or `scripts/`. | Ensure `control_bundle_validator.py`, `style_risk_auditor.py`, and `claim_immobility_auditor.py` remain standalone, zero-dependency executable Python scripts. |
