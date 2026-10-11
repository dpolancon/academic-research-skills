# ARS Human Review Decision & Pre-Wave-A Architecture Reconciliation

**Status:** Architecture Accepted & Pre-Wave-A Reconciliation Complete  
**Date:** 2026-10-11  
**Repository:** `c:\ReposGitHub\academic-research-skills` (`dpolancon/academic-research-skills`)  
**Scope:** Formal record of accepted architecture, bounded repairs (R1–R5), explicit hold items, and Wave A execution readiness  

---

## 1. Accepted Architecture

The target architecture has been formally confirmed with revisions (`CONFIRMED_WITH_REVISIONS`):

1. **One Capability, One Canonical Owner:** Authoritative logic lives in exactly one component. Multiple consumers may invoke it, but parallel implementations of the same capability are prohibited.
2. **`academic-pipeline` Typed as Orchestrator:** The pipeline is strictly the workflow state machine and control plane (governing gates, checkpoints, handoffs, and Material Passport persistence). It does not accumulate substantive disciplinary reasoning.
3. **Logical Architecture Before Physical Migration:** Layering (Core, Domain, Dissemination, Profiles, Tools, Shared Protocols) is governed logically via registries and client adapters before any physical directory restructuring.
4. **Distinct Component Ontology:** Profiles (author voice, advisor preferences, committee personas, venue guides), Tools (deterministic scripts, verifiers, plotters), and Shared Protocols (invariants, contracts) are strictly distinguished from standalone Skills.
5. **Quarantine of Project Overlays:** Manuscript-specific, dissertation-specific, and grant-specific files (`paper_refutation_SSM/`, `user_testings/`, `editing_memos/`, `writings_testing/`, `slide_deck_Fondecyt/`) are quarantined from core library infrastructure.
6. **Epistemic Safeguard Principle:** Heterodox economic theory expands candidate hypotheses and interpretive options; it must never encode conclusions as axioms or force empirical verdicts.

---

## 2. Accepted Migration Sequence

The repository evolves through six staged, dependency-ordered migration waves:
- **WAVE A:** Hygiene, Identity & Canonical Source Integrity (`G01–G05`)
- **WAVE B:** Ontology, Registry & Capability Ownership Stabilization (`G06–G09`, `G15–G16`)
- **WAVE C:** Shared Protocols & Duplicated Capability Consolidation (`G10–G11`, `G13–G14`, `G18`, `G27`, `G29`)
- **WAVE D:** Domain Intellectual Architecture & Epistemic Safeguards (`G17`, `G19–G24`)
- **WAVE E:** Dissemination Architecture & Public Scholarship (`G12`, `G25–G26`, `G28`)
- **WAVE F:** Physical Tree Harmonization & Client Packaging (`G31–G34`)

---

## 3. Repairs Imposed by Human Review (R1–R5)

### R1 — Capability Registry: Current vs. Target Owner Distinction
- **Issue:** Future components (e.g., `skills/domain/applied-econometrics-pe`, `profiles/advisors/michael-ash`) were prematurely marked "active", creating false-state operational risk.
- **Resolution:** `capability_registry.yaml` was redesigned to explicitly distinguish `current_owner` and `current_owner_type` from `target_owner` and `target_owner_type`. It implements a strict migration state vocabulary: `CURRENT`, `MIGRATING`, `PLANNED`, `CANDIDATE`, `DEPRECATED`. No non-existent component is labeled active.

### R2 — Removal of Capability-Registry Promotion from Wave A
- **Issue:** `06_WAVE_A_P0_P1_EXECUTION_PLAN.md` included Action A.6 (promoting `capability_registry.yaml` and updating `MODE_REGISTRY.md`), violating the boundary where Wave A is strictly repository hygiene and Wave B owns capability governance.
- **Resolution:** Action A.6 has been completely removed from Wave A. The capability registry remains a design artifact under `docs/design/2026-10-11-ars-target-architecture/` until Wave B.

### R3 — License Action Replaced by License & Provenance Audit
- **Issue:** Prior design prematurely authorized automatic dual-licensing without tracing the legal origins of inherited files. The upstream author name was also misspelled.
- **Resolution:** Action A.3 is now strictly a License and Provenance Audit. Material is categorized into:
  1. *Inherited from Imbad0202 upstream* (Author: **Cheng-I Wu**, CC BY-NC 4.0, noncommercial academic copilot core);
  2. *Inherited/adapted from hanlulong upstream* (Author: **Han Lulong**, MIT License, permissive slide/writing foundations);
  3. *Independently authored locally* (Author: **Diego Polanco**, author-owned original works);
  4. *Mixed/derived infrastructure* (Root `README.md`, sync harnesses).
  - Upstream author name corrected to **Cheng-I Wu** across all documentation.
  - No legal advice is provided, and no files are re-licensed in this pass; human decisions are documented for future action.

### R4 — Secret Hygiene: Historical Exposure as a Conditional Branch
- **Issue:** Prior plan treated `git rm --cached .env` as the sole fix, ignoring potential historical credential exposure in prior commits.
- **Resolution:** Action A.1 now explicitly separates:
  - *Branch A (Current Tracking):* Ensure `.gitignore` coverage, create safe `.env.example` with placeholders, untrack `.env` via `git rm --cached`.
  - *Branch B (Historical Exposure):* Assess commit history where `.env` was committed without printing secret values. If live credentials entered history, mandate credential rotation at provider dashboards (Together AI, Gemini). History rewriting is treated as an independent, non-automatic human decision.

### R5 — Narrowed Mirror Cleanup Acceptance Criteria
- **Issue:** Prior acceptance test required `git ls-files .agents .claude` to return empty, which would forbid legitimate thin client adapter and configuration files.
- **Resolution:** The acceptance test is narrowed to the core invariant: **No complete skill implementation is tracked more than once.** The test specifically verifies that `git ls-files .agents/skills .claude/skills` returns empty, while permitting thin client configs (e.g. `.claude/CLAUDE.md`, `.claude-plugin/`) where justified.

---

## 4. Explicit HOLD Items

The following items are strictly on **HOLD** and must NOT be executed until their designated wave:
1. **Final Licensing Reassignment:** Awaiting human review of the License and Provenance Audit.
2. **Git History Rewriting:** Held; requires independent evaluation and is not part of standard Wave A execution.
3. **Physical Tree Migration:** Held until Wave F (preserves client runner discovery).
4. **Substantive Skill Refactoring:** Held until Waves C, D, and E (`econ-write`, `umass-applied-econometrics`, `heterodox-economics-review`).
5. **Editorial Governance Integration:** Held until Wave C (simplification and Material Passport integration).
6. **Creation of New Skills:** Held until Wave D/E (`political-economy-research`, `public-scholarship`).

---

## 5. Authorization After This Pass

### **WAVE A IS READY FOR EXECUTION**

### Rationale:
1. **All Pre-Wave-A Contradictions Resolved:** The five human review findings (R1–R5) are completely resolved in the design artifacts.
2. **Authoritative Boundaries Restored:** Wave A is strictly bounded to `G01–G05` repository hygiene, secret cleanup, provenance auditing, and mirror untracking.
3. **Zero Runtime / Skill Disruption:** Wave A modifies zero academic writing rules, zero econometric logic, and zero theoretical models.
4. **Reversible & Safe:** Every planned operation has verified rollback commands and requires human approval before modifying the git index.
