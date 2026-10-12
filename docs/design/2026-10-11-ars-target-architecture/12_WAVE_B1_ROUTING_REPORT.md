# Wave B1 Routing & Precedence Execution Report

- **Date:** 2026-10-12
- **Baseline Commit:** `8bdc0df` (`docs(econ-write): add evaluation examples and ranked sources`)
- **Status:** COMPLETED
- **Decision:** `B1_COMPLETE_READY_FOR_WAVE_C_REVIEW`

---

## 1. Executive Summary

Wave B1 operationalized the accepted ARS capability ownership architecture in the existing root skill layout without physically moving components. It established a deterministic runtime routing contract across the four primary runtime components:
- `academic-paper` (Generic manuscript lifecycle owner)
- `econ-write` (Economics disciplinary writing domain policy owner)
- `academic-paper-reviewer` (Sole canonical owner of simulated external peer review)
- `academic-pipeline` (Workflow orchestrator; control plane only)

All overlapping claims (e.g. presentation slide production, simulated external refereeing, author-side vs external review) were resolved through explicit delegation statements and strict capability monopolies.

---

## 2. Routing Precedence Architecture

### 2.1 Core Capability Allocations

| Component | Semantic Role | Canonical Owned Capability | Non-Owned / Delegated Capabilities |
| :--- | :--- | :--- | :--- |
| `academic-paper` | `CORE_SKILL` | `academic_manuscript_lifecycle` (Generic paper structuring, drafting, revision, citation formatting, assembly) | Economics disciplinary style (delegates to `econ-write`); Simulated external review (delegates to `academic-paper-reviewer`); Workflow orchestration (delegates to `academic-pipeline`). |
| `econ-write` | `DOMAIN_SKILL` | `economics_prose_and_section_standards` (BLUF, triangular style, model section conventions, results presentation, identification rhetoric) | Generic paper lifecycle (owned by `academic-paper`); Simulated external peer review (delegates to `academic-paper-reviewer`); Slide deck production (delegates to `econ-slides`). |
| `academic-paper-reviewer` | `CORE_SKILL` | `simulated_external_peer_review` (5-reviewer panel, Devil's Advocate, editorial decisions, re-review verification) | Manuscript drafting or author-side revisions (owned by `academic-paper`); Advisor/committee profile storage. |
| `academic-pipeline` | `ORCHESTRATOR` | `research_workflow_orchestration` (10-stage state machine, checkpoints, Material Passport tracking) | Substantive writing, econometric analysis, or peer-review criteria ("Orchestration is not ownership"). |

### 2.2 Direct vs. Delegated Invocations

1. **Bounded Economics Writing:** Direct invocation of `econ-write` is preserved for bounded drafting/rewriting tasks (e.g. results sections, empirical strategies, model setups, abstracts).
2. **Complete Economics Manuscript Workflow:** `academic-paper` serves as the lifecycle owner and consumes `econ-write` for domain writing conventions. `econ-write` does not run a duplicate manuscript pipeline.
3. **Simulated External Peer Review:** `academic-paper-reviewer` is the sole canonical engine for simulated external journal refereeing. The internal Phase 6 in-pair evaluator in `academic-paper` is strictly an author-side pre-submission self-check gate under the v3.6.6 generator-evaluator contract.

### 2.3 Legacy Advisor & Committee Components

In accordance with the Wave B1 contract, legacy top-level components `advisor-reviewer` and `PE-phd-committee` were **not** physically decomposed (scheduled for Wave C). However, their runtime roles are formally bounded as:
- **PROFILE / CALIBRATION INPUTS**, not parallel peer-review engines.
- When an advisor perspective (Michael Ash) or committee challenge (UMass PE PhD defense) is requested, `academic-paper-reviewer` executes the review and consumes the legacy profile to calibrate its critical perspectives.

### 2.4 Runtime Path Enforcement

Until Wave F physical directory harmonization, all routing contracts resolve strictly to live existing root directories (`academic-paper`, `econ-write`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research`, `econ-slides`). Target paths (such as `skills/core/...` or `skills/domain/...`) are barred from live resolution.

---

## 3. Scope of Modifications

### 3.1 Modified Authorized Files (8 files)

1. [`academic-paper/SKILL.md`](file:///c:/ReposGitHub/academic-research-skills/academic-paper/SKILL.md): Added `Capability Ownership and Precedence Rules`, updated non-trigger table, clarified internal evaluator vs external referee review, and added disciplinary delegation to `econ-write`.
2. [`econ-write/SKILL.md`](file:///c:/ReposGitHub/academic-research-skills/econ-write/SKILL.md): Updated frontmatter and added `CAPABILITY OWNERSHIP & PRECEDENCE`, clarified domain policy ownership, bounded direct invocation vs orchestrated consumption, delegated slide production to `econ-slides`, and delegated simulated external peer review to `academic-paper-reviewer`. Preserved commit `8bdc0df` in full.
3. [`academic-paper-reviewer/SKILL.md`](file:///c:/ReposGitHub/academic-research-skills/academic-paper-reviewer/SKILL.md): Added `Capability Ownership and Precedence Rules`, established sole canonical external peer-review ownership, defined advisor/committee legacy components as calibration inputs, and updated non-trigger and related skills tables.
4. [`academic-pipeline/SKILL.md`](file:///c:/ReposGitHub/academic-research-skills/academic-pipeline/SKILL.md): Added `Capability Ownership and Precedence Rules` formalizing "Orchestration Is Not Ownership", and mapped stage delegations to `deep-research`, `academic-paper`, `econ-write`, and `academic-paper-reviewer`.
5. [`docs/governance/ars_registry.yaml`](file:///c:/ReposGitHub/academic-research-skills/docs/governance/ars_registry.yaml): Updated component and capability notes to encode routing precedence and delegation metadata while strictly preserving schema invariants.
6. [`MODE_REGISTRY.md`](file:///c:/ReposGitHub/academic-research-skills/MODE_REGISTRY.md): Reconciled `deep-research`'s `review` mode triggers and output description to prevent collision with `academic-paper-reviewer`.
7. [`UPDATE_REGISTRY.md`](file:///c:/ReposGitHub/academic-research-skills/UPDATE_REGISTRY.md): Appended `GOV-003` prospective migration entry recording Wave B1 routing precedence.
8. [`scripts/validate_ars_registry.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/validate_ars_registry.py): Extended validator with 8 deterministic routing and capability precedence invariant checks.

### 3.2 Created Authorized Files (4 files)

1. [`docs/governance/ROUTING_AND_PRECEDENCE.md`](file:///c:/ReposGitHub/academic-research-skills/docs/governance/ROUTING_AND_PRECEDENCE.md): Comprehensive human-readable routing contract, decision tree, rule catalog (R1-R7), and runtime path guidance.
2. [`evals/gold/routing/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/routing/cases.yaml): 9 canonical evaluation cases testing routing rules and delegation expectations.
3. [`scripts/test_routing_contract.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_routing_contract.py): Deterministic test script validating `cases.yaml` against `ars_registry.yaml` and precedence invariants.
4. [`docs/design/2026-10-11-ars-target-architecture/12_WAVE_B1_ROUTING_REPORT.md`](file:///c:/ReposGitHub/academic-research-skills/docs/design/2026-10-11-ars-target-architecture/12_WAVE_B1_ROUTING_REPORT.md): This report.

---

## 4. Verification & Validation Evidence

### 4.1 Registry Validation (`scripts/validate_ars_registry.py`)
```text
PASS: ars_registry.yaml is valid.
  - Components validated: 14
  - Capabilities validated: 20
```
Enforces:
1. All routing component IDs exist.
2. Runtime paths exist on disk and do not leak target path prefixes.
3. `academic_manuscript_lifecycle` is owned by `academic-paper`.
4. `economics_prose_and_section_standards` is owned by `econ-write`.
5. `simulated_external_peer_review` is owned by `academic-paper-reviewer`.
6. `academic-pipeline` is `ORCHESTRATOR` in both implementation type and semantic role.
7. Exactly one canonical external review owner exists across the monorepo.
8. Advisor and committee components are profiles, not canonical peer-review owners.

### 4.2 Deterministic Routing Test (`scripts/test_routing_contract.py`)
```text
Running ARS Wave B1 Routing Precedence Test Suite (9 cases)...
  [PASS] ROUTE-001 (R1): academic-paper -> DIRECT_EXECUTION
  [PASS] ROUTE-002 (R2): econ-write -> DIRECT_EXECUTION
  [PASS] ROUTE-003 (R3): academic-paper -> LIFECYCLE_WITH_DOMAIN_POLICY
  [PASS] ROUTE-004 (R4): academic-paper-reviewer -> DIRECT_EXECUTION
  [PASS] ROUTE-005 (R5): academic-paper-reviewer -> REVIEW_WITH_CALIBRATION
  [PASS] ROUTE-006 (R6): academic-paper-reviewer -> REVIEW_WITH_CALIBRATION
  [PASS] ROUTE-007 (R7): academic-pipeline -> WORKFLOW_ORCHESTRATION
  [PASS] ROUTE-008 (R8): econ-slides -> DIRECT_EXECUTION
  [PASS] ROUTE-009 (R9): deep-research -> DIRECT_EXECUTION

------------------------------------------------------------
Routing Test Results: 9 passed, 0 failed out of 9 cases.
PASS: All routing fixtures conform to ARS capability precedence contract.
```

### 4.3 Protected Work Verification
- `docs/design/2026-10-10-editorial-governance/`: UNCHANGED
- `evals/gold/editorial_governance/`: UNCHANGED
- `scripts/revision_guard.py` & associated tests: UNCHANGED
- `shared/contracts/passport/`: UNCHANGED
- `econ-slides/slide_deck_Fondecyt/`: UNCHANGED
- `econ-slides/tests/`: UNCHANGED
- Legacy components outside B1 (`advisor-reviewer`, `PE-phd-committee`, `umass-applied-econometrics`, etc.): UNCHANGED

---

## 5. Recommendation

Wave B1 is complete and fully verified. The repository is ready for independent review before authorizing Wave C decomposition.
