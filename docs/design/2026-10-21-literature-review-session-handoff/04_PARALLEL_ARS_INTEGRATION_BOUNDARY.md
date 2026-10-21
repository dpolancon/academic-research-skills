# ARS LITERATURE-REVIEW SESSION HANDOFF — PARALLEL INTEGRATION BOUNDARY

**Document Location:** `docs/design/2026-10-21-literature-review-session-handoff/04_PARALLEL_ARS_INTEGRATION_BOUNDARY.md`  
**Governing Principle:** Strict Isolation between Feature Branches and Parallel Architecture Sprints  
**Active Worktree:** `C:\ReposGitHub\academic-research-skills-literature-review` (`feat/literature-review`)  
**Canonical Repository:** `C:\ReposGitHub\academic-research-skills` (`main`)  
**Date:** 2026-10-21, America/Santiago  

---

## 1. The Core Governance Rule

> [!CAUTION] Critical Boundary Rule
> **THIS SESSION HANDOFF IS AN INTEGRATION INPUT, NOT AN INSTRUCTION TO MERGE IMMEDIATELY.**  
> 
> The current branch (`feat/literature-review`) MUST NOT be merged into canonical `main`, nor may changes from active uncommitted working copies on `main` be pulled into this worktree.  
> 
> The canonical ARS repository is currently undergoing parallel architecture sprints (Wave E closure, Wave F restart, dissemination / public-scholarship refactoring, and editorial governance design). Any premature merge or cross-branch rebase will create catastrophic context pollution and merge collisions.

---

## 2. Ownership Demarcation

### What THIS Branch (`feat/literature-review`) Owns:
1. **The Complete `literature-review/` Skill Directory:**
   - Full specification (`literature-review/SKILL.md`);
   - Reference protocols (`references/argument_assembly_protocol.md`, `references/staged_prose_protocol.md`, `references/manuscript_prose_protocol.md`, `references/structural_style_risk_guidelines.md`, `references/humanization_and_claim_immobility_protocol.md`, `references/cross_literature_hinge_protocol.md`, `references/human_sovereignty_and_repair_loops.md`, `references/workflow_specification.md`);
   - JSON schemas (`schemas/control_bundle_manifest_schema.json`, `schemas/governance_state_schema.json`, `schemas/paragraph_ledger_schema.json`, `schemas/argument_assembly_schema.json`, `schemas/staged_prose_schema.json`, `schemas/manuscript_prose_contract_schema.json`, `schemas/post_humanization_audit_schema.json`);
   - Deterministic CLI scripts (`scripts/control_bundle_validator.py`, `scripts/style_risk_auditor.py`, `scripts/claim_immobility_auditor.py`, `scripts/notebooklm_adapter.py`);
   - Control bundle and prose templates (`templates/`);
   - Automated unit test suite (`tests/` — 30 tests);
2. **Consolidation & Session Reports:**
   - `docs/design/2026-10-20-literature-review-consolidation/` (Reports 01–07);
   - `docs/design/2026-10-21-literature-review-session-handoff/` (This handoff bundle, Artifacts 00–06);
3. **The Literature-Review Capability Registration:**
   - Literature-review entry and component declarations in `docs/governance/ars_registry.yaml`.

### What THIS Branch Does NOT Own (Belongs Exclusively to Canonical `main` / Parallel Work):
1. **Wave E / Wave F Architectural Redesign:**
   - Active work in `docs/design/wave-e/` and `docs/design/wave-f/`;
2. **Public Scholarship & Dissemination Skills:**
   - Refactoring of `public-scholarship/` and `skills/dissemination/public-scholarship/`;
   - `evals/gold/wave_e_dissemination/cases.yaml`;
3. **Editorial Governance & Columna Auditing:**
   - `docs/design/2026-10-10-editorial-governance/`;
   - `editor-jacobin-lat/` scripts and tests;
   - `tools/audit_columna/` and `tests/test_audit_columna.py`;
4. **General Repository Infrastructure:**
   - `scripts/install-local.ps1`, `scripts/validate_ars_registry.py`, `econ-slides/`.

---

## 3. What Has Already Landed on Canonical `main`

Prior to this session, the literature-review skill consolidation was officially merged into canonical `main` under explicit human ratification:
- **Consolidation Commit:** `d53be45` (Feature implementation)
- **Merge Commit:** `f99c85d` (`merge: integrate governed literature-review workflow`)
- **Canonical Report Commit:** `5333e06` (`docs(literature-review): record canonical integration report` adding `08_FINAL_INTEGRATION_REPORT.md`)

Therefore, the core functionality of the literature-review skill is **already present** in canonical ARS `main`. This session's work in the worktree adds the session handoff documentation, production findings, and future integration guidelines without modifying the already-landed runtime code.

---

## 4. Conflict Surface & Future Reconciliation Analysis

When the parallel architecture sprint concludes and ARS is ready for final synchronization, the future integration operator should anticipate the following potential conflict surfaces:

| Component | Potential Collision Class | Preservation Instruction |
|---|---|---|
| `docs/governance/ars_registry.yaml` | Syntactic merge conflict | Preserve both the literature-review capability entries AND the parallel dissemination / public-scholarship entries. |
| Skill Directory Layout | File reorganization | If ARS adopts a nested namespace layout (e.g., `skills/research/literature-review/`), move the directory contents as a unit without breaking relative references to `schemas/`, `scripts/`, or `references/`. |
| Script Shared Dependencies | Environment / packaging | Ensure `style_risk_auditor.py` and `claim_immobility_auditor.py` remain zero-external-dependency pure Python (using only `sys`, `json`, `re`, `argparse`). |

---

## 5. Invariant Semantic Commitments

Even if the future ARS refactoring alters directory paths, YAML keys, or test runners, the following semantic principles of the literature-review skill must remain permanently intact:
1. **Authority Separation:** The 4-tier hierarchy (External Literature, Internal Lineage, Executable Code, Current Manuscript Governance) must never be collapsed.
2. **Cluster Invariant:** $\text{Cluster Membership} \neq \text{Common Claim Membership}$.
3. **Three-Tier Separation:** Ledgers ($L_6$) $\to$ Argument Assembly ($L_7$) $\to$ Staged Prose ($L_8$) $\to$ Manuscript ($L_9$).
4. **Claim-Immobility Law:** Humanization may polish rhythm and syntax, but may never strengthen causality or broaden scope.
5. **Human Sovereignty:** No agent or automated pass may grant a scholarly `LOCK` or alter paragraph sequence without explicit human authorization.
