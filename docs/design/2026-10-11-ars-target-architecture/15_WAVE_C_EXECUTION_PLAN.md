# ARS Wave C Legacy Component Decomposition Execution Plan

**Document ID:** `15_WAVE_C_EXECUTION_PLAN.md`
**Status:** PROPOSED EXECUTION PLAN (Wave C0 Review)
**Date:** 2026-10-12
**Governing Design Document:** `14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md`
**Target Baseline:** `a797db9`
**Scope:** Staged, reversible implementation plan across Subwaves C1 through C5
**Execution Authority:** Implementation PLAN only. No execution or modifications during Wave C0.

---

## 1. Execution Principles & Guardrails

The execution of Wave C decomposes legacy skills and candidate modules into canonical profiles, shared protocols, and deterministic tools. The following constraints govern all subwaves:

1. **Reversible Subwave Boundaries:** Every subwave must be small, independently testable, and capable of clean git rollback without affecting adjacent components.
2. **Strict File Scoping:** Each subwave specifies an explicit whitelist of authorized file paths. Modifying unauthorized files immediately triggers a rollback.
3. **No Premature Physical Reorganization:** Root directories (`academic-paper`, `econ-write`, `academic-paper-reviewer`, `academic-pipeline`) remain executable truth. Directory tree re-rooting into `skills/core/` and `skills/domain/` is deferred to Wave F.
4. **MIGRATE_FIRST Before Deprecation:** Legacy surfaces are maintained in working order until their extracted destinations are verified by automated tests.
5. **No Blind Deletions:** Legacy components are replaced by clear redirection headers and marked `DEPRECATED` in the governance registry; physical file removal occurs only in Wave F.

---

## 2. Subwave Sequencing & Dependency Architecture

```
[Baseline: a797db9]
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│ Subwave C1: Shared Prose Discipline Protocol & Tooling      │
│ Target: shared/protocols/ + tools/prose_checks/             │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Subwave C2: Lightweight Editorial Governance & Passport     │
│ Target: shared/contracts/passport/ + scripts/               │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Subwave C3: Advisor Profile Extraction (Michael Ash)        │
│ Target: profiles/advisors/ + projects/dissertation-ch1/     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Subwave C4: Committee Profiles & Composition Extraction    │
│ Target: profiles/scholars/ + profiles/committees/           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Subwave C5: Legacy Deprecation, Registry Update & Regression │
│ Target: docs/governance/ + legacy SKILL.md wrappers         │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Granular Subwave Execution Specifications

### Subwave C1 — Shared Prose Discipline Protocol & Tool Extraction

- **Objective:** Extract the Category A/B/C lexical taxonomy, 11 auditing pattern families, and evidential verb rules from `prose-register-critic` into a shared reusable protocol, accompanied by a deterministic Python regex scanner.
- **Input Baseline:** `a797db9` (post-Wave B1.1).
- **Authorized Paths:**
  - `shared/protocols/prose_discipline_protocol.md` (new)
  - `tools/prose_checks/check_jargon_leakage.py` (new)
  - `tools/prose_checks/tests/test_check_jargon_leakage.py` (new)
  - `tools/prose_checks/README.md` (new)
- **Forbidden Paths:**
  - `prose-register-critic/*` (no edits in C1)
  - `academic-paper/*`, `econ-write/*`, `academic-paper-reviewer/*`
  - `docs/governance/*`
- **Migration Action:**
  - Standardize Category A technical protection rules, Category B review clustering, and Category C scaffolding definitions in `shared/protocols/prose_discipline_protocol.md`.
  - Implement deterministic CLI scanner `tools/prose_checks/check_jargon_leakage.py` validating against Category C patterns without external dependencies.
- **Tests Required:**
  - Unit test suite verifying zero false positives on Category A terms (`rate of exploitation`, `companion matrix eigenvalues`, `Johansen trace test`, `supermultiplier`).
  - Unit test verifying 100% true positive detection on Category C scaffolding (`empirical tournament`, `admissibility gates`, `crucially`, `profound institutional divergence`).
- **Stop Conditions:**
  - Any failure in prose check unit tests.
  - Modification of any file outside authorized scope.
- **Commit Boundary:**
  - Commit message: `feat(protocol): extract shared prose discipline protocol and verification tools`
- **Rollback Condition:** `git checkout main && git clean -fd` if scanner false-positive rate on gold academic text exceeds 0%.
- **Human-Review Gate:** Verify that Category A technical terms in political economy remain strictly protected.

---

### Subwave C2 — Lightweight Editorial Governance & Passport Integration

- **Objective:** Formalize the 3-axis decision state model, scoped source-role contract, and bounded-diff anchor verification from the candidate bundle into an optional Material Passport sidecar port. Release gating is strictly workspace-scoped (`optional | recommended | required`, default `optional`, gating only `RELEASE_READY`).
- **Input Baseline:** Post-Subwave C1 commit.
- **Authorized Paths:**
  - `shared/contracts/passport/editorial_governance.schema.json` (stage candidate)
  - `shared/contracts/passport/revision_verification.schema.json` (stage candidate)
  - `scripts/revision_guard.py` (stage candidate)
  - `scripts/test_editorial_governance_schema.py` (stage candidate)
  - `scripts/test_revision_guard.py` (stage candidate)
  - `evals/gold/editorial_governance/cases.json` (stage candidate)
  - `evals/gold/editorial_governance/manifest.yaml` (stage candidate)
  - `docs/design/2026-10-10-editorial-governance/*` (stage candidate)
- **Forbidden Paths:**
  - `shared/contracts/passport/passport.yaml` (do not alter core passport schema in C2)
  - `academic-pipeline/*`, `academic-paper/*`
  - Any file in `econ-slides/`
- **Migration Action:**
  - Validate candidate schemas against Schema Draft 2020-12 / Draft-07 standards.
  - Simplify schema to purge cryptographic DAG parent-hashing dependencies and multi-party receipt verification requirements.
  - Run deterministic test suites.
- **Tests Required:**
  - `python scripts/test_editorial_governance_schema.py` (must pass 100%).
  - `python scripts/test_revision_guard.py` (must pass 100%).
- **Stop Conditions:**
  - Any validation failure in synthetic gold test cases.
  - Any alteration to untracked `econ-slides/` candidate files.
- **Commit Boundary:**
  - Commit message: `feat(governance): integrate lightweight editorial governance and revision guard`
- **Rollback Condition:** Reset uncommitted candidate staging if tests fail or if core passport contracts break.
- **Human-Review Gate:** Confirm that the simplified protocol functions as an optional sidecar without imposing cryptographic DAG overhead.

---

### Subwave C3 — Advisor / Scholar Profile Extraction (Michael Ash)

- **Objective:** Extract reusable research guidance, econometrics simplicity principles, and Marglin descriptive macro grounding from `advisor-reviewer` into a canonical durable scholar profile (`profiles/scholars/michael-ash.md`) and an active contextual advisor role wrapper (`profiles/advisors/michael-ash.md`), while recording Chapter 1 extraction notes in documentation only.
- **Input Baseline:** Post-Subwave C2 commit.
- **Authorized Paths:**
  - `profiles/scholars/michael-ash.md` (new)
  - `profiles/advisors/michael-ash.md` (new)
- **Forbidden Paths:**
  - `advisor-reviewer/*` (no edits in C3; legacy preserved until C5)
  - `academic-paper-reviewer/*`
  - `docs/governance/*`
  - Any substantive project directory (e.g. `projects/dissertation-ch1/`)
- **Migration Action:**
  - Author canonical scholar profile `profiles/scholars/michael-ash.md` with durable methodological priors, empirical standards, and Marglin descriptive grounding heuristics.
  - Author contextual advisor wrapper `profiles/advisors/michael-ash.md` referencing the scholar profile and defining active supervisory review constraints (active until dissertation completion).
  - Quarantine Diego Polanco Chapter 1 specific references (Section 4.3, Table 1, Shaikh dataset constants, Feedback Matrix items) to documentation-only extraction notes. No substantive project folder is created in ARS.
  - Purge references to phantom skills (`umass-applied-econometrics`, `heterodox-economics-review`).
- **Tests Required:**
  - Markdown syntax and schema frontmatter linting on `profiles/scholars/michael-ash.md` and `profiles/advisors/michael-ash.md`.
  - Anti-loss check: Verify all 6 core Ash methodological directives from `advisor-reviewer/SKILL.md` are present in the new profiles.
- **Stop Conditions:**
  - Omission of any substantive research guidance from Michael Ash.
  - Inclusion of project-specific equation proofs or chapter files in the shared profile.
- **Commit Boundary:**
  - Commit message: `feat(profiles): extract Michael Ash scholar profile and advisor role wrapper`
- **Rollback Condition:** Revert profile commit if advisor guidance is truncated or distorted.
- **Human-Review Gate:** Verify that all durable supervisory advice from Michael Ash is fully preserved without chapter-specific contamination.

---

### Subwave C4 — Committee Profiles & Composition Extraction

- **Objective:** Decompose `PE-phd-committee` into individual scholar profiles (Deepankar Basu, Kevin Young), referencing canonical scholar Michael Ash, and author a declarative committee composition profile (`umass-pe`).
- **Input Baseline:** Post-Subwave C3 commit.
- **Authorized Paths:**
  - `profiles/scholars/deepankar-basu.md` (new)
  - `profiles/scholars/kevin-young.md` (new)
  - `profiles/committees/umass-pe.md` (new)
  - `academic-paper-reviewer/references/defense_mode_protocol.md` (new reference protocol)
- **Forbidden Paths:**
  - `PE-phd-committee/*` (no edits in C4; legacy preserved until C5)
  - `academic-paper/*`, `econ-write/*`
- **Migration Action:**
  - Author `profiles/scholars/deepankar-basu.md` (Marxian theory, Leontief microfoundations, dimensional analysis, ODE stability).
  - Author `profiles/scholars/kevin-young.md` (Historical institutional analysis, class struggle, 1956/1974/1980 structural breaks).
  - Author `profiles/committees/umass-pe.md` defining committee roster referencing scholar profiles (`michael-ash`, `deepankar-basu`, `kevin-young`), Chair synthesis protocol, and defense modes (`pre-defense`, `oral-defense`).
  - Add defense simulation protocol documentation under `academic-paper-reviewer/references/defense_mode_protocol.md`.
- **Tests Required:**
  - Profile schema validation for all newly created scholar and committee profiles.
  - Anti-loss check: Verify Basu mathematical checks and Young historical shocks are preserved.
- **Stop Conditions:**
  - Incomplete scholar profile definitions.
  - Modification of `academic-paper-reviewer/SKILL.md` core code (reference additions only permitted).
- **Commit Boundary:**
  - Commit message: `feat(profiles): extract UMass PE committee scholar profiles and composition`
- **Rollback Condition:** Revert if persona distinctions are merged or diluted.
- **Human-Review Gate:** Confirm that Basu mathematical criteria and Young historical shock criteria are accurately represented.

---

### Subwave C5 — Legacy Deprecation, Registry Update & Regression Lock

- **Objective:** Formally update the ARS registry to recognize newly extracted profiles and protocols, mark legacy component SKILL.md files as deprecated redirection stubs, and freeze routing regression tests.
- **Input Baseline:** Post-Subwave C4 commit.
- **Authorized Paths:**
  - `docs/governance/ars_registry.yaml`
  - `docs/governance/ROUTING_AND_PRECEDENCE.md`
  - `MODE_REGISTRY.md`
  - `advisor-reviewer/SKILL.md` (update to redirection stub)
  - `PE-phd-committee/SKILL.md` (update to redirection stub)
  - `prose-register-critic/SKILL.md` (update to redirection stub)
  - `scripts/validate_ars_registry.py` (extend validation for profiles/protocols)
  - `scripts/test_routing_contract.py` (add legacy redirection assertions)
- **Forbidden Paths:**
  - `academic-paper/*`, `econ-write/*`, `deep-research/*`
  - Physical file deletions of legacy directories (directories retained until Wave F)
- **Migration Action:**
  - Update `docs/governance/ars_registry.yaml`:
    - Reclassify `advisor-reviewer` and `PE-phd-committee` as `status: deprecated` / `migrated_to: profiles/...`.
    - Reclassify `prose-register-critic` as `status: deprecated` / `migrated_to: shared/protocols/prose_discipline_protocol.md`.
    - Register new profiles and protocols under governance tracking.
  - Update legacy `SKILL.md` files with clear deprecation notices directing users and agents to canonical routing paths (`academic-paper-reviewer` with profile flags).
  - Update `MODE_REGISTRY.md` to reflect defense simulation modes under `academic-paper-reviewer`.
  - Extend routing test suite to verify that attempts to invoke legacy skills route correctly to canonical owners.
- **Tests Required:**
  - `python scripts/validate_ars_registry.py` (must pass 100%).
  - `python scripts/test_routing_contract.py` (must pass 100%).
  - Pre-commit check: `git diff --check`.
- **Stop Conditions:**
  - Any failure in registry validation or routing contract tests.
  - Premature physical deletion of legacy directories.
- **Commit Boundary:**
  - Commit message: `feat(governance): deprecate legacy surfaces and lock post-Wave-C routing`
- **Rollback Condition:** Full rollback to post-C4 baseline if any routing contract fails.
- **Human-Review Gate:** Final audit confirming 0 duplicate canonical owners and 100% test pass rate.

---

## 4. Governance Decision Boundaries

To maintain strict alignment with established architecture, decisions across Wave C are categorized into four authoritative classes:

### 4.1 LOCKED_BY_EXISTING_ARCHITECTURE
*These principles are non-negotiable foundations established in Waves A through B1:*
1. **Single Capability Monopoly:** Every capability in ARS has exactly one canonical operational owner (`forbidden_duplicate_owners: true`).
2. **Canonical Core Roles:** `academic-paper` owns manuscript lifecycle; `econ-write` owns economics disciplinary policy; `academic-paper-reviewer` owns simulated external review; `academic-pipeline` owns orchestration.
3. **Profiles Are Inputs Only:** Advisor and committee personas operate strictly as calibration inputs to `academic-paper-reviewer`; they are forbidden from acting as independent review engines.
4. **Current-Path Execution Rule:** All live runtime paths continue resolving to existing repository roots until Wave F physical migration.

### 4.2 RECOMMENDED_FOR_WAVE_C
*Architectural recommendations submitted for human approval in this review:*
1. **Semantic De-escalation:** Reclassify `prose-register-critic` from a top-level skill into a shared protocol (`shared/protocols/prose_discipline_protocol.md`) and deterministic tools (`tools/prose_checks/`).
2. **Passport Sidecar Port:** Adopt Option C for Editorial Governance, packaging it as a lightweight contract in `shared/contracts/passport/` backed by `scripts/revision_guard.py`.
3. **Scholar-Committee Decoupling:** Separate individual scholar profiles (`Ash`, `Basu`, `Young`) from the committee composition contract (`umass-pe`).
4. **Project Overlay Quarantine:** Isolate Chapter 1 dissertation specifics to external project overlays rather than embedding them in reusable profiles.
5. **Execution Order:** Execute subwaves in strict sequence C1 $\to$ C2 $\to$ C3 $\to$ C4 $\to$ C5 to ensure shared infrastructure is available before persona extraction.

### 4.3 RESOLVED_HUMAN_DECISIONS (Wave C0.1 Lock)
*All previously open architectural choices have been formally decided and locked:*
1. **Scholar Identity & Active Advisor Role (RESOLVED):**
   - Dual representation model locked: canonical durable scholar identity in `profiles/scholars/<person>.md`, paired with contextual active role wrappers (`profiles/advisors/<person>.md` and `profiles/committees/<committee>.md`).
   - Michael Ash remains an active advisor and committee member until dissertation completion. Post-dissertation, the active advisor role may be deactivated while the scholar identity remains durable.
2. **Project Overlay & Chapter 1 Quarantine (RESOLVED):**
   - Chapter 1 is frozen. No substantive project folder `projects/dissertation-ch1/` is created inside ARS.
   - Chapter 1 specific references, constants, and the 68-item feedback matrix are preserved exclusively as documentation-only migration provenance and extraction notes.
3. **Editorial Governance Release Gate Policy (RESOLVED):**
   - There is no globally mandatory ARS release gate.
   - Editorial governance release policy is strictly workspace-scoped (`optional | recommended | required`, default `optional`).
   - A `required` gate affects ONLY the transition to `RELEASE_READY` and never blocks drafting, editing, compiling, or reviewing.
4. **Workspace Abstraction (RESOLVED):**
   - Formalized the `WORKSPACE` abstraction as the bounded research object upon which skills, tools, profiles, and protocols operate, governed by strict source-of-truth and external repository read-only invariants.

### 4.4 DEFERRED
*Capabilities explicitly out of scope for Wave C, preserved in future backlogs:*
1. **Automated Corpus Profiling (`10_FUTURE_PERSONALIZATION_BACKLOG.md`):** Automated extraction of advisor or referee profiles from scholarly PDF papers.
2. **Dynamic Author Persona Inference:** Algorithmic inference of user writing style or political economy priors.
3. **Physical Repository Harmonization:** Moving top-level skills into nested directories `skills/core/`, `skills/domain/` (strictly scheduled for Wave F).
4. **Distributed Cryptographic Infrastructure:** Merkle trees, multi-party signature servers, or external identity verification harnesses.
5. **Workspace Runtime Implementation:** Physical workspace infrastructure, CLI commands, and runner integrations remain a separate future wave after Wave C decomposition.

---

## 5. Pre-Execution Checklist for Subwave C1

Before authorizing Subwave C1 execution, verify:
- [x] Wave B1.1 adversarial routing test lock passed (`a797db9`).
- [x] Design review document `14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md` authored and approved.
- [x] Execution plan document `15_WAVE_C_EXECUTION_PLAN.md` authored and approved.
- [x] Human decisions on persona taxonomy, Chapter 1 quarantine, and workspace model locked (`16_WAVE_C_HUMAN_DECISION_LOCK.md`).
- [x] Conceptual workspace architecture specified (`17_WORKSPACE_CAPSULE_ARCHITECTURE.md`).
- [ ] Working tree clean (no tracked modifications; protected candidate work untouched).
- [ ] Subwave C1 branch or local working pass authorized.
