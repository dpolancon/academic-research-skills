# ARS — Wave C5: Legacy Deprecation + Governance Reconciliation Report

**Date:** 2026-10-13
**Status:** COMPLETE
**Commit Target:** `refactor(governance): reconcile Wave C legacy surfaces`
**Governing Baseline:** `38f31af` (`feat(profiles): extract committee scholar calibrations`)
**Consolidation Status:** `C4_PROFILE_EXTRACTION_ABSORBED_BY_C3`
**Milestone:** Wave C Completion & Regression Lock

---

## 1. Baseline

* **Parent Commit:** `38f31af` (Wave C3 minimal scholar/advisor profile extraction).
* **Git Status:** Working tree clean prior to C5 reconciliation edits.
* **Protected Untracked Directories:** Preserved untouched:
  * `docs/design/2026-10-10-editorial-governance/`
  * `econ-slides/slide_deck_Fondecyt/`
  * `econ-slides/tests/`
* **Governing Architectural Decisions:** Fully adheres to `14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md`, `15_WAVE_C_EXECUTION_PLAN.md`, `16_WAVE_C_HUMAN_DECISION_LOCK.md`, and `17_WORKSPACE_CAPSULE_ARCHITECTURE.md`.

---

## 2. Purpose

The objective of Wave C5 is to reconcile repository runtime and governance truth with the modular capabilities successfully extracted during Waves C1 through C3:
1. Deprecate the three superseded legacy skill surfaces (`advisor-reviewer/`, `PE-phd-committee/`, and `prose-register-critic/`).
2. Replace their `SKILL.md` implementations with explicit, standardized compatibility redirection stubs.
3. Promote the extracted capabilities into current governance truth:
   * Shared Prose Discipline protocol and deterministic checker (Wave C1/C1.1).
   * Lightweight Editorial Governance contract and revision guard (Wave C2).
   * Scholar profiles, active advisor role, and committee composition (Wave C3).
4. Update the canonical routing contract and gold routing cases to route directly to modular substrates and profile calibrations.
5. Lock the repository governance registry to 18 total components (14 original + 4 live substrates) with strict invariant validation.
6. Record historical governance log entries (`GOV-004` through `GOV-008`) in `UPDATE_REGISTRY.md`.
7. Formally close Wave C4 as absorbed into Wave C3 (`C4_PROFILE_EXTRACTION_ABSORBED_BY_C3`).
8. Establish comprehensive integration testing (`scripts/test_wave_c_reconciliation.py`) and lock Wave C regression state.

---

## 3. Wave C4 Absorption

* **Disposition:** `C4_PROFILE_EXTRACTION_ABSORBED_BY_C3`
* **Rationale:** In the original Wave C execution plan (`15_WAVE_C_EXECUTION_PLAN.md`), Wave C3 was scoped for advisor profile extraction, while Wave C4 was planned for committee profile extraction. During Wave C3 execution, both advisor profile extraction (`Michael Ash`) and the full committee extraction (`Michael Ash`, `Deepankar Basu`, `Kevin Young`, and `umass-pe.md`) were implemented together under a unified profile schema and contract (`profiles/PROFILE_CONTRACT.md`).
* **Audit & Closure:** Wave C3 passed independent adversarial audit cleanly with zero defects (`38f31af`). Consequently, a separate Wave C4 implementation pass was unnecessary. Wave C4 is formally closed as absorbed by Wave C3, leaving zero orphaned capabilities or unextracted committee elements.

---

## 4. Legacy-Surface Reconciliation Map

The following map governs the disposition of all three legacy skill surfaces:

| Legacy Skill Directory | Status | Extracted Substrate | Runtime Canonical Executor | Deprecation Stub Location |
| :--- | :--- | :--- | :--- | :--- |
| `advisor-reviewer/` | `DEPRECATED` | `profiles/scholars/michael-ash.md`<br>`profiles/advisors/michael-ash.md` | `academic-paper-reviewer` (calibrated with profile) | `advisor-reviewer/SKILL.md` |
| `PE-phd-committee/` | `DEPRECATED` | `profiles/scholars/{michael-ash,deepankar-basu,kevin-young}.md`<br>`profiles/committees/umass-pe.md` | `academic-paper-reviewer` (calibrated with committee composition) | `PE-phd-committee/SKILL.md` |
| `prose-register-critic/` | `DEPRECATED` | `shared/protocols/prose_discipline_protocol.md`<br>`tools/prose_checks/check_prose_patterns.py` | Writing: `academic-paper` (domain general) or `econ-write` (economics writing) | `prose-register-critic/SKILL.md` |

---

## 5. `advisor-reviewer` Deprecation

* **Previous State:** Standalone skill attempting to simulate peer/advisor review, coupling candidate-specific PhD dissertation context, econometric heuristics, and Michael Ash's advisory style.
* **Extracted Artifacts:**
  * Scholar calibration: `profiles/scholars/michael-ash.md`
  * Active advisor role: `profiles/advisors/michael-ash.md`
* **Canonical Executor:** `academic-paper-reviewer` remains the sole canonical owner of peer review (`simulated_external_peer_review`). When an advisor calibration is requested, callers invoke `academic-paper-reviewer` and provide `profiles/advisors/michael-ash.md` as the calibration input.
* **Redirection Stub (`advisor-reviewer/SKILL.md`):** Replaced with a standardized compatibility stub declaring:
  * Status: DEPRECATED (Wave C5).
  * Replacement: `academic-paper-reviewer` + `profiles/advisors/michael-ash.md`.
  * Preserved directives: Econometric transparency, BLUF structure, descriptive grounding, and the punchline principle.
  * Instructions to agents/callers on how to perform review using canonical tools.
* **Governance Registry:** Lifecycle set to `DEPRECATED`, `capabilities_owned: []`, `replacement_path: profiles/advisors/michael-ash.md`.

---

## 6. `PE-phd-committee` Deprecation

* **Previous State:** Standalone skill attempting to simulate multi-member doctoral committee evaluations by hardcoding committee member traits and Chapter 1 dissertation draft checks.
* **Extracted Artifacts:**
  * Member scholar profiles: `profiles/scholars/michael-ash.md`, `profiles/scholars/deepankar-basu.md`, `profiles/scholars/kevin-young.md`.
  * Committee composition: `profiles/committees/umass-pe.md`.
* **Canonical Executor:** `academic-paper-reviewer` remains the sole canonical owner of peer review. Multi-perspective committee review is executed through `academic-paper-reviewer` by passing `profiles/committees/umass-pe.md` as input.
* **Redirection Stub (`PE-phd-committee/SKILL.md`):** Replaced with a standardized compatibility stub declaring:
  * Status: DEPRECATED (Wave C5).
  * Replacement: `academic-paper-reviewer` + `profiles/committees/umass-pe.md`.
  * Preserved committee structure: Chair (Michael Ash), Internal (Deepankar Basu), External (Kevin Young).
  * Instructions to agents/callers on sequential committee perspective reviews.
* **Governance Registry:** Lifecycle set to `DEPRECATED`, `capabilities_owned: []`, `replacement_path: profiles/committees/umass-pe.md`.

---

## 7. `prose-register-critic` Deprecation

* **Previous State:** Standalone skill combining AI clich&eacute; detection, passive voice flagging, sentence cadence checks, and academic register critique, which created ambiguous overlap with canonical writing skills.
* **Extracted Artifacts:**
  * Shared protocol: `shared/protocols/prose_discipline_protocol.md`
  * Deterministic check tool: `tools/prose_checks/check_prose_patterns.py`
  * Regression fixtures: `evals/fixtures/prose_samples/`
* **Canonical Executor:**
  * Writing ownership: Domain-general academic writing is owned by `academic-paper`; economics writing discipline is owned by `econ-write`.
  * Quality/discipline enforcement: Shared discipline protocol applied by writing owners or via deterministic CLI checks.
* **Redirection Stub (`prose-register-critic/SKILL.md`):** Replaced with a standardized compatibility stub declaring:
  * Status: DEPRECATED (Wave C5).
  * Replacement: `shared/protocols/prose_discipline_protocol.md` + `tools/prose_checks/check_prose_patterns.py`.
  * Routing direction: Call writing skills (`academic-paper` / `econ-write`) for drafting and revisions; invoke the deterministic tool for pattern checks.
* **Governance Registry:** Lifecycle set to `DEPRECATED`, `capabilities_owned: []`, `replacement_path: shared/protocols/prose_discipline_protocol.md`.

---

## 8. Prose-Discipline Canonical State

* **Artifacts:**
  * Protocol: `shared/protocols/prose_discipline_protocol.md`
  * Tool: `tools/prose_checks/check_prose_patterns.py`
  * Schema & Fixtures: `tools/prose_checks/schema.json`, `evals/fixtures/prose_samples/`
  * Test Suite: `scripts/test_prose_discipline.py` (17 tests passing).
* **Domain Boundary:** Cleanly repaired in Wave C1.1 to eliminate economics-specific terminology (`econ-write` leakage) from Section 5. Section 5 now operates in purely general academic terms ("concrete empirical anchor" / "substantive mechanism").
* **Governance Registration:** Registered in `docs/governance/ars_registry.yaml` as component `prose-discipline`:
  * Lifecycle: `ACTIVE`
  * Layer: `shared-protocol`
  * Capabilities Owned: `[prose_discipline_enforcement]`

---

## 9. Editorial-Governance Canonical State

* **Artifacts:**
  * Contract: `shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md`
  * JSON Schemas: `shared/contracts/passport/schemas/manifest.schema.json`, `shared/contracts/passport/schemas/change_log.schema.json`
  * Deterministic Tool: `scripts/revision_guard.py`
  * Test Suites: `scripts/test_editorial_governance_schema.py` (6 tests passing), `scripts/test_revision_guard.py` (15 tests passing).
* **Policy Invariant:** Operating strictly as a lightweight, optional change-control verification mechanism for packages, release manifests, and version logs. It is **not** globally mandatory for arbitrary repository edits and owns **zero** writing or review capabilities.
* **Governance Registration:** Registered in `docs/governance/ars_registry.yaml` as component `editorial-governance`:
  * Lifecycle: `ACTIVE`
  * Layer: `change-control`
  * Capabilities Owned: `[change_control_verification]`

---

## 10. Advisor/Committee Profile Calibration State

* **Artifacts:**
  * Contract: `profiles/PROFILE_CONTRACT.md`
  * Scholar Profiles: `profiles/scholars/michael-ash.md`, `profiles/scholars/deepankar-basu.md`, `profiles/scholars/kevin-young.md`
  * Active Advisor Role: `profiles/advisors/michael-ash.md`
  * Committee Composition: `profiles/committees/umass-pe.md`
  * Reusable Templates: `profiles/templates/scholar-profile.md`, `profiles/templates/advisor-role.md`, `profiles/templates/committee-composition.md`
  * Test Suite: `scripts/test_profile_contract.py` (18 tests passing).
* **Separation of Concerns:** Profiles are declarative calibration inputs, not executable review engines. They own zero review capabilities; `academic-paper-reviewer` maintains sole ownership of simulated peer review.
* **Governance Registration:**
  * Component `advisor-michael-ash`: `lifecycle: ACTIVE`, `layer: profile-calibration`, `capabilities_owned: [michael_ash_advisor_calibration]`.
  * Component `committee-umass-pe`: `lifecycle: ACTIVE`, `layer: profile-calibration`, `capabilities_owned: [umass_pe_committee_calibration]`.

---

## 11. Registry Changes

The canonical registry `docs/governance/ars_registry.yaml` was upgraded from v1.0.0 to v1.1.0, expanding from 14 to 18 registered components.

### Component Taxonomy (18 Components)

1. **Active Core Skills (11):**
   * `academic-paper` (owns `general_academic_paper_writing`)
   * `academic-paper-reviewer` (owns `simulated_external_peer_review`)
   * `econ-ark` (owns `hark_computational_modeling`)
   * `econ-slides` (owns `marxian_political_economy_presentation`)
   * `econ-write` (owns `marxian_political_economy_manuscript_drafting`)
   * `empirical-workflow` (owns `reproducible_empirical_workflow`)
   * `literature-review` (owns `academic_literature_review_and_synthesis`)
   * `math-modeling` (owns `economic_mathematical_modeling`)
   * `methodology-reviewer` (owns `methodological_evaluation`)
   * `paper-search` (owns `academic_paper_search_and_retrieval`)
   * `peer-review-evals` (owns `peer_review_evaluation_suite`)

2. **Active Shared Substrates & Profiles (4):**
   * `prose-discipline` (owns `prose_discipline_enforcement`)
   * `editorial-governance` (owns `change_control_verification`)
   * `advisor-michael-ash` (owns `michael_ash_advisor_calibration`)
   * `committee-umass-pe` (owns `umass_pe_committee_calibration`)

3. **Deprecated Legacy Compatibility Stubs (3):**
   * `advisor-reviewer` (`lifecycle: DEPRECATED`, `capabilities_owned: []`, points to `profiles/advisors/michael-ash.md`)
   * `PE-phd-committee` (`lifecycle: DEPRECATED`, `capabilities_owned: []`, points to `profiles/committees/umass-pe.md`)
   * `prose-register-critic` (`lifecycle: DEPRECATED`, `capabilities_owned: []`, points to `shared/protocols/prose_discipline_protocol.md`)

### Invariants Enforced in `scripts/validate_ars_registry.py`
* All 18 components have valid metadata and valid lifecycles (`ACTIVE` or `DEPRECATED`).
* Exactly 20 capabilities are declared; every capability has exactly one owner (strict 1:1 uniqueness).
* Deprecated components own zero capabilities (`capabilities_owned: []`).
* Deprecated components declare valid `replacement_path` targets that resolve on disk.
* All component `runtime_path` locations resolve on disk.
* `academic-paper-reviewer` maintains sole ownership of `simulated_external_peer_review`.

---

## 12. Routing Changes

`docs/governance/ROUTING_AND_PRECEDENCE.md` was upgraded to v1.1.0:
* Clarified that `advisor-reviewer`, `PE-phd-committee`, and `prose-register-critic` are deprecated compatibility stubs.
* Documented calibration routing: prompts requiring Michael Ash advisory feedback route to `academic-paper-reviewer` + `profiles/advisors/michael-ash.md`; committee feedback routes to `academic-paper-reviewer` + `profiles/committees/umass-pe.md`.
* Documented prose discipline routing: prose style critiques apply `shared/protocols/prose_discipline_protocol.md` and `tools/prose_checks/check_prose_patterns.py`, using `academic-paper` or `econ-write` for drafting.

### Gold Routing Evals (`evals/gold/routing/cases.yaml`)
Reconciled gold routing cases to point directly to canonical substrates:
* `ROUTE-005` (Michael Ash advisor review): Canonical target `academic-paper-reviewer` with calibration `profiles/advisors/michael-ash.md`.
* `ROUTE-006` (UMass PE committee review): Canonical target `academic-paper-reviewer` with calibration `profiles/committees/umass-pe.md`.
* `ROUTE-011` (Prose register check): Canonical target `tools/prose_checks/check_prose_patterns.py` & `shared/protocols/prose_discipline_protocol.md`.

### Validator Alignment (`scripts/test_routing_contract.py`)
Updated case expectation evaluation in `test_routing_contract.py` to support compound targets and profile calibrations. All 17 routing cases pass cleanly.

---

## 13. Mode-Registry Disposition

* **Status:** `UNCHANGED_NOT_REQUIRED`
* **Analysis:** `docs/governance/MODE_REGISTRY.md` was evaluated during Wave C5. It defines valid operational modes (`standard`, `exhaustive`, `rebuttal`, etc.) for mode-bearing execution engines (principally `academic-paper-reviewer` and `econ-write`).
* **Conclusion:** The three deprecated skills were never registered as mode engines. Furthermore, neither `academic-paper-reviewer` nor `econ-write` had their execution modes altered by Wave C. Therefore, `docs/governance/MODE_REGISTRY.md` remains in strict canonical alignment without modification.

---

## 14. Update-Registry Entry

`UPDATE_REGISTRY.md` was updated to document all governance events in the Wave C series:
* `GOV-004` (Wave C1): Shared Prose Discipline Protocol extraction and deterministic tooling.
* `GOV-005` (Wave C1.1): Prose discipline domain-boundary repair.
* `GOV-006` (Wave C2): Lightweight editorial governance contract and revision guard.
* `GOV-007` (Wave C3): Minimal scholar and advisor profile system extraction.
* `GOV-008` (Wave C5): Legacy skill deprecation, redirection stubs, registry v1.1.0 reconciliation, and Wave C regression lock.

---

## 15. Compatibility Behavior

The repository guarantees backwards compatibility for legacy callers:
1. **Directory Invariance:** The directories `advisor-reviewer/`, `PE-phd-committee/`, and `prose-register-critic/` remain in place at the repository root.
2. **Deterministic Redirection:** Each legacy `SKILL.md` contains clear frontmatter metadata and human/agent instructions directing callers to the corresponding active substrate.
3. **No Phantom Execution:** Deprecated stubs do not attempt to run outdated logic or compete with canonical skills; they guide the agent immediately to the canonical tools.

---

## 16. Regression Tests

All regression and validation test suites pass cleanly:

| Test Suite | Result | Details |
| :--- | :--- | :--- |
| `scripts/validate_ars_registry.py` | **PASS** | 18 components, 20 capabilities, zero orphaned capabilities, zero deprecated ownership |
| `scripts/test_routing_contract.py` | **PASS** | 17/17 gold routing cases pass |
| `scripts/test_prose_discipline.py` | **PASS** | 17/17 pattern, fixture, CLI, and boundary tests pass |
| `scripts/test_editorial_governance_schema.py` | **PASS** | 6/6 manifest and change log schema validation tests pass |
| `scripts/test_revision_guard.py` | **PASS** | 15/15 deterministic revision guard verification tests pass |
| `scripts/test_profile_contract.py` | **PASS** | 18/18 profile structure, evidence, and reference tests pass |
| `scripts/test_wave_c_reconciliation.py` | **PASS** | 11/11 structural reconciliation and invariant assertions pass |

---

## 17. Runtime Paths

All 18 registered components have validated, existing filesystem paths:

| Component ID | Declared `runtime_path` | Verified on Disk |
| :--- | :--- | :--- |
| `academic-paper` | `academic-paper/SKILL.md` | YES |
| `academic-paper-reviewer` | `academic-paper-reviewer/SKILL.md` | YES |
| `econ-ark` | `econ-ark/SKILL.md` | YES |
| `econ-slides` | `econ-slides/SKILL.md` | YES |
| `econ-write` | `econ-write/SKILL.md` | YES |
| `empirical-workflow` | `empirical-workflow/SKILL.md` | YES |
| `literature-review` | `literature-review/SKILL.md` | YES |
| `math-modeling` | `math-modeling/SKILL.md` | YES |
| `methodology-reviewer` | `methodology-reviewer/SKILL.md` | YES |
| `paper-search` | `paper-search/SKILL.md` | YES |
| `peer-review-evals` | `peer-review-evals/SKILL.md` | YES |
| `prose-discipline` | `shared/protocols/prose_discipline_protocol.md` | YES |
| `editorial-governance` | `shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md` | YES |
| `advisor-michael-ash` | `profiles/advisors/michael-ash.md` | YES |
| `committee-umass-pe` | `profiles/committees/umass-pe.md` | YES |
| `advisor-reviewer` | `advisor-reviewer/SKILL.md` | YES |
| `PE-phd-committee` | `PE-phd-committee/SKILL.md` | YES |
| `prose-register-critic` | `prose-register-critic/SKILL.md` | YES |

---

## 18. Workspace Status

* **Status:** `DEFERRED`
* **Context:** Per `16_WAVE_C_HUMAN_DECISION_LOCK.md` and `17_WORKSPACE_CAPSULE_ARCHITECTURE.md`, workspace capsule runtime infrastructure (ephemeral execution capsules, isolated execution contexts) remains deferred.
* **Invariant:** No workspace capsules, synthetic runtime harnesses, or filesystem sandbox layers were constructed during Wave C5.

---

## 19. Wave F Deferral

* **Status:** `DEFERRED`
* **Context:** Physical reorganization of skills (e.g., migrating skills from repository root into `skills/` or domain-specific subdirectories) is explicitly deferred to **Wave F**.
* **Invariant:** All core skills remain located at repository root paths (`academic-paper/`, `academic-paper-reviewer/`, etc.). Zero physical path migration was conducted.

---

## 20. Remaining Legacy Material

* The directories `advisor-reviewer/`, `PE-phd-committee/`, and `prose-register-critic/` remain present on disk solely to host the compatibility redirection stubs (`SKILL.md`).
* Candidate-specific dissertation notes, Chapter 1 draft spreadsheets, and historic dissertation matrices from legacy prompts were intentionally omitted from profile extraction and remain safely quarantined in repository history without polluting runtime profiles.
* The protected untracked directories (`docs/design/2026-10-10-editorial-governance/`, `econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`) remain completely untouched.

---

## 21. Wave C Final State

With the completion of Wave C5, the overarching Wave C milestone is **COMPLETE**:
1. **Wave C0:** Legacy component decomposition design review completed.
2. **Wave C0.1:** Human decision lock and workspace capsule architecture completed.
3. **Wave C1 / C1.1:** Shared prose discipline protocol extracted, deterministic pattern checker implemented, and domain boundary repaired.
4. **Wave C2:** Lightweight editorial governance ported, schemas established, and revision guard implemented.
5. **Wave C3:** Minimal evidence-grounded profile system extracted (3 scholars, 1 active advisor role, 1 committee composition, 3 templates) and validated.
6. **Wave C4:** Formally absorbed by Wave C3.
7. **Wave C5:** Legacy surfaces deprecated, compatibility stubs deployed, governance registry reconciled to 18 components, routing updated, and regression locked.

---

## 22. Post-Wave-C Recommendations

1. **Independent Adversarial Audit:** Conduct an independent adversarial audit of Wave C5 / Wave C final state to verify compliance against all Wave C architectural locks.
2. **No Physical Migration Until Wave F:** Maintain the root directory layout for all runtime skills until the dedicated physical migration pass in Wave F.
3. **Workspace Preparation:** When workspace capsule implementation begins in future waves, leverage the Material Passport schema and revision guard tooling established in Wave C2.
4. **Profile Expansion Protocol:** If additional scholar profiles are added in future personalization waves, strictly follow `profiles/PROFILE_CONTRACT.md` and use the templates in `profiles/templates/`.
