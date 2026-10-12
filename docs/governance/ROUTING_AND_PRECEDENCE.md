# ARS Runtime Routing & Capability Precedence Contract

- **Version:** 1.0.0
- **Wave:** Wave B1 (Routing & Precedence Implementation)
- **Baseline:** `8bdc0df`
- **Authoritative Governance Reference:** `docs/governance/ars_registry.yaml`

---

## 1. Ownership Principles

The Academic Research Skills (ARS) repository enforces deterministic capability precedence across its component suite:

1. **Strict Capability Monopoly:** Every capability in ARS has exactly one canonical operational owner (`forbidden_duplicate_owners: true`).
2. **Orchestration Is Not Ownership:** `academic-pipeline` manages workflow sequencing, stage transitions, and Material Passport tracking; it does not own substantive disciplinary writing, econometrics, or peer-review criteria.
3. **Disciplinary Policy Consumption:** Generic paper production is owned by `academic-paper`. Disciplinary conventions for economics manuscripts are owned by `econ-write` and consumed by `academic-paper` during economics paper drafting and revision.
4. **Sole Peer-Review Ownership:** `academic-paper-reviewer` is the sole canonical owner of simulated external peer review, referee reports, and editorial decision synthesis.
5. **Profiles Are Inputs, Not Review Engines:** Legacy persona components (`advisor-reviewer`, `PE-phd-committee`) serve strictly as calibration profile inputs to `academic-paper-reviewer` when persona angles are requested; they are not independent peer-review engines.
6. **Runtime Path Rule:** Until Wave F physical directory harmonization, all routing contracts MUST resolve to live root directories (`academic-paper`, `econ-write`, `academic-paper-reviewer`, `academic-pipeline`), never to target paths (`skills/core/...`, `skills/domain/...`).

---

## 2. Routing Decision Tree

```
USER REQUEST
    │
    ├── Full research→publication lifecycle?
    │       └── academic-pipeline (orchestrates stages; delegates substantive work)
    │
    ├── External/referee review simulation?
    │       └── academic-paper-reviewer (sole canonical review engine)
    │
    ├── Advisor/committee perspective simulation?
    │       └── academic-paper-reviewer
    │              + legacy calibration input (advisor-reviewer / PE-phd-committee)
    │
    ├── Bounded economics writing or section drafting?
    │       └── econ-write (direct domain skill invocation)
    │
    ├── Slide deck presentation production?
    │       └── econ-slides (Beamer deck generation and verification)
    │
    └── Generic academic paper lifecycle?
            └── academic-paper
                   │
                   └── If economics paper → consumes econ-write for disciplinary policy
```

---

## 3. Core Precedence Rules

### Rule R1 — Generic Academic Manuscript
- **Trigger Examples:** `"Write an academic paper from these materials"`, `"Help me draft this paper"`, `"Organize my manuscript outline"`.
- **Primary Owner:** `academic-paper`.
- **Scope:** Full manuscript architecture, section drafting, citation integration, authoring state machine, and journal formatting.

### Rule R2 — Economics-Specific Writing Task (Bounded)
- **Trigger Examples:** `"Rewrite this economics results section"`, `"Fix the model section of this economics paper"`, `"Improve identification language"`, `"Apply BLUF to this economics abstract"`.
- **Primary Owner:** `econ-write`.
- **Scope:** Disciplinary economics conventions (BLUF, triangular style, concrete magnitudes, model and mechanism exposition, identification strategies, causal claim discipline, economics table/figure rhetoric).

### Rule R3 — Full Economics Paper Workflow
- **Trigger Examples:** `"Help me write an economics paper from outline to submission"`, `"Revise this entire economics manuscript"`.
- **Primary Lifecycle Owner:** `academic-paper`.
- **Required Domain Policy:** `econ-write`.
- **Relationship:** `academic-paper` orchestrates the manuscript lifecycle and consumes `econ-write` for disciplinary standards. `econ-write` does not run an independent second manuscript lifecycle.

### Rule R4 — Simulated External Peer Review
- **Trigger Examples:** `"Peer review this paper"`, `"Act as a journal referee"`, `"Evaluate whether this paper would survive submission"`, `"Verify revisions against reviewer comments"`.
- **Primary Owner:** `academic-paper-reviewer`.
- **Scope:** Sole canonical owner of referee panel simulation (EIC, methodology, domain, perspective, Devil's Advocate), editorial decisions, revision roadmaps, and re-review verification. Neither `academic-paper` nor `econ-write` owns simulated external peer review.

### Rule R5 — Advisor-Specific Perspective
- **Trigger Examples:** `"Review this paper as Michael Ash would"`, `"What would my advisor object to in this chapter?"`.
- **Routing:** `academic-paper-reviewer` + `advisor-reviewer` calibration input.
- **Contract:** `advisor-reviewer` provides persona heuristics and research preferences; it does not operate as an independent review engine.

### Rule R6 — Committee / Defense Simulation
- **Trigger Examples:** `"Simulate my PhD defense committee challenging Chapter 2"`, `"How would the UMass political economy committee critique this?"`.
- **Routing:** `academic-paper-reviewer` + `PE-phd-committee` calibration input.
- **Contract:** Committee personas (Ash, Basu, Young) calibrate the review panel's critical angle; `academic-paper-reviewer` remains the execution engine.

### Rule R7 — Full Research-to-Publication Workflow
- **Trigger Examples:** `"Run the academic pipeline"`, `"Take this project from research through review"`.
- **Primary Owner:** `academic-pipeline`.
- **Delegation Contract:**
  - Stage 1 (RESEARCH) → `deep-research`
  - Stage 2, 4, 4', 5 (WRITE, REVISE, FINALIZE) → `academic-paper`
  - Disciplinary Writing Policy → `econ-write` (consumed during Stage 2 & 4 for economics papers)
  - Stage 3, 3' (REVIEW, RE-REVIEW) → `academic-paper-reviewer`
  - Slide Presentation Production → `econ-slides`
- **Boundary:** Orchestration is not ownership. The pipeline does not duplicate substantive rules.

---

## 4. Key Architectural Distinctions

### Generic Paper vs. Economics Writing
- `academic-paper` owns the universal manuscript workflow across all academic disciplines.
- `econ-write` owns disciplinary policy specifically for economics (e.g. BLUF, triangular structure, model section protocols, empirical identification rhetoric).
- For economics papers, `academic-paper` delegates section-level style and identification discipline to `econ-write`.

### Author-Side Self-Check vs. External Peer Review
- `academic-paper` includes an in-pair Phase 6 evaluator under the v3.6.6 generator-evaluator contract. This is strictly an **author-side internal self-quality check** to prevent premature submission.
- `academic-paper-reviewer` owns **simulated external peer review**, running an independent 5-referee panel, Devil's Advocate stress-testing, and editorial decision synthesis.

### Advisor/Committee Components as Profiles
- `advisor-reviewer` and `PE-phd-committee` currently exist as top-level skill directories (scheduled for physical extraction into `profiles/` in Wave C).
- In Wave B1, they are formally defined as **calibration inputs**, never as competing peer-review engines.

---

## 5. Runtime Path vs. Target Path Warning

> ⚠️ **CRITICAL RUNTIME WARNING (Wave B1 through Wave E):**
> All live prompts, dispatch calls, tests, and configuration MUST refer to the existing runtime paths:
> - `academic-paper`
> - `econ-write`
> - `academic-paper-reviewer`
> - `academic-pipeline`
> - `deep-research`
> - `econ-slides`
>
> Target paths such as `skills/core/academic-paper` or `skills/domain/econ-write` are architectural destinations scheduled for Wave F physical migration. Routing to nonexistent target paths during runtime is an immediate error.
