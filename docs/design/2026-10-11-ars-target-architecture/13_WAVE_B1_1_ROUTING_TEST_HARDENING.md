# Wave B1.1 Adversarial Routing Test Hardening Report

- **Date:** 2026-10-12
- **Baseline Commit:** `a87e8b2` (`feat(routing): enforce ARS capability precedence`)
- **Status:** COMPLETED
- **Decision:** `B1_ROUTING_HARDENED_READY_FOR_WAVE_C`

---

## 1. Purpose & Audit Finding Closed

The Wave B1 independent audit concluded `B1_AUDIT_PASS` with a single bounded gap:
`ROUTING_FIXTURE_COVERAGE = PARTIAL`
While the initial test suite validated all 9 positive canonical routing mappings, it lacked adversarial fixtures to verify boundary disambiguation when user requests carry overlapping keywords or compound intents.

Wave B1.1 closes this gap by introducing 8 adversarial test fixtures and hardening the deterministic test runner with negative ownership assertions, required delegation checks, and orchestration boundary validation.

---

## 2. Adversarial Categories Added (8 cases)

| Case ID | Rule | Prompt | Primary Owner | Negative Constraint | Architectural Boundary Verified |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ROUTE-010` | `ADV-A1` | `"Peer review this economics paper."` | `academic-paper-reviewer` | `must_not: [academic-paper, econ-write]` | Disciplinary economics review remains owned by reviewer; `econ-write` informs criteria but does not own review. |
| `ROUTE-011` | `ADV-A2` | `"Review this paper as Michael Ash might."` | `academic-paper-reviewer` | `must_not: [advisor-reviewer]` | Advisor profile is strictly calibration input; `advisor-reviewer` is not an independent review engine. |
| `ROUTE-012` | `ADV-A3` | `"Write and referee my economics paper."` | `academic-pipeline` | `must_not: [econ-write]` | Compound multi-stage request sequenced by pipeline; pipeline does not own substantive writing or review capabilities. |
| `ROUTE-013` | `ADV-A4` | `"Improve the economics prose but do not rewrite the paper."` | `econ-write` | `must_not: [academic-paper, academic-pipeline]` | Bounded economics prose refinement belongs directly to `econ-write`, avoiding unnecessary escalation to full paper lifecycle. |
| `ROUTE-014` | `ADV-A5` | `"Assess whether this cited source supports my claim."` | `deep-research` | `must_not: [academic-paper-reviewer, academic-paper]` | Source-level factual verification belongs to `deep-research`, not manuscript-level peer review. |
| `ROUTE-015` | `ADV-A6` | `"Review this paper."` | `academic-paper-reviewer` | `must_not: [deep-research, academic-paper]` | Ambiguous paper review where the target is a manuscript resolves to `academic-paper-reviewer`, not `deep-research`. |
| `ROUTE-016` | `ADV-A7` | `"Review the evidence behind these historical claims."` | `deep-research` | `must_not: [academic-paper-reviewer]` | Research evidence and claim review belongs to `deep-research`. |
| `ROUTE-017` | `ADV-A8` | `"Revise this economics manuscript for journal submission."` | `academic-paper` | `must_not: [academic-paper-reviewer]` | Author-side manuscript revision belongs to `academic-paper` consuming `econ-write`, distinct from external peer review. |

---

## 3. Test Runner Enhancements (`scripts/test_routing_contract.py`)

The test runner was hardened to enforce:
1. **Negative Ownership Assertions:** Asserts that forbidden components are not selected as primary owners, and cross-checks against `docs/governance/ars_registry.yaml` to verify forbidden owners do not hold canonical ownership of the underlying capability.
2. **Domain Policy Verification:** Validates that declared `domain_policy` components exist and carry `semantic_role == "DOMAIN_SKILL"`.
3. **Required Delegation Enforcement:** Confirms that multi-component workflows include all mandatory delegates.
4. **Orchestrator Boundary Checks:** Enforces that `academic-pipeline` never holds substantive capabilities (`academic_manuscript_lifecycle`, `economics_prose_and_section_standards`, or `simulated_external_peer_review`).
5. **Target-Path Safety:** Confirms no fixture references future target path prefixes (`skills/`, `profiles/`, etc.).

---

## 4. Verification Evidence

### 4.1 Registry Validation
```text
PASS: ars_registry.yaml is valid.
  - Components validated: 14
  - Capabilities validated: 20
```

### 4.2 Routing Precedence Test Suite
```text
Running ARS Routing Precedence Test Suite (17 cases)...
  [PASS] ROUTE-001 (R1): academic-paper -> DIRECT_EXECUTION
  [PASS] ROUTE-002 (R2): econ-write -> DIRECT_EXECUTION
  [PASS] ROUTE-003 (R3): academic-paper -> LIFECYCLE_WITH_DOMAIN_POLICY
  [PASS] ROUTE-004 (R4): academic-paper-reviewer -> DIRECT_EXECUTION
  [PASS] ROUTE-005 (R5): academic-paper-reviewer -> REVIEW_WITH_CALIBRATION
  [PASS] ROUTE-006 (R6): academic-paper-reviewer -> REVIEW_WITH_CALIBRATION
  [PASS] ROUTE-007 (R7): academic-pipeline -> WORKFLOW_ORCHESTRATION
  [PASS] ROUTE-008 (R8): econ-slides -> DIRECT_EXECUTION
  [PASS] ROUTE-009 (R9): deep-research -> DIRECT_EXECUTION
  [PASS] ROUTE-010 (ADV-A1): academic-paper-reviewer -> REVIEW_WITH_DOMAIN_STANDARDS
  [PASS] ROUTE-011 (ADV-A2): academic-paper-reviewer -> REVIEW_WITH_CALIBRATION
  [PASS] ROUTE-012 (ADV-A3): academic-pipeline -> SEQUENCED_ORCHESTRATION
  [PASS] ROUTE-013 (ADV-A4): econ-write -> DIRECT_EXECUTION
  [PASS] ROUTE-014 (ADV-A5): deep-research -> DIRECT_EXECUTION
  [PASS] ROUTE-015 (ADV-A6): academic-paper-reviewer -> DIRECT_EXECUTION
  [PASS] ROUTE-016 (ADV-A7): deep-research -> DIRECT_EXECUTION
  [PASS] ROUTE-017 (ADV-A8): academic-paper -> LIFECYCLE_WITH_DOMAIN_POLICY

------------------------------------------------------------
Routing Test Results: 17 passed, 0 failed out of 17 cases.
  - Positive invariant cases: 9
  - Adversarial disambiguation cases: 8
PASS: All positive and adversarial routing fixtures conform to ARS capability precedence contract.
```

---

## 5. Scope Confirmation & Wave C Readiness

- **Routing Ownership Unchanged:** No capability ownership, runtime paths, or skill contents were modified.
- **Scope Confined:** Modifications strictly confined to `evals/gold/routing/cases.yaml`, `scripts/test_routing_contract.py`, and this report.
- **Protected Work Intact:** Editorial governance and Fondecyt econ-slides remain untouched.
- **Wave C Readiness:** Routing precedence is fully hardened against adversarial overlap. The repository is ready to proceed to Wave C decomposition.
