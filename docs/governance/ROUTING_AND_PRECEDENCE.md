# ARS Runtime Routing & Capability Precedence Contract

- **Version:** 1.1.0
- **Wave:** Wave C5 (Legacy Deprecation & Governance Reconciliation)
- **Baseline Parent:** `38f31af`
- **Authoritative Governance Reference:** `docs/governance/ars_registry.yaml`

---

## 1. Ownership Principles

The Academic Research Skills (ARS) repository enforces deterministic capability precedence across its component suite:

1. **Strict Capability Monopoly:** Every capability in ARS has exactly one canonical operational owner (`forbidden_duplicate_owners: true`).
2. **Orchestration Is Not Ownership:** `academic-pipeline` manages workflow sequencing, stage transitions, and Material Passport tracking; it does not own substantive disciplinary writing, econometrics, or peer-review criteria.
3. **Disciplinary Policy Consumption:** Generic paper production is owned by `academic-paper`. Disciplinary conventions for economics manuscripts are owned by `econ-write` and consumed by `academic-paper` during economics paper drafting and revision.
4. **Sole Peer-Review Ownership:** `academic-paper-reviewer` is the sole canonical owner of simulated external peer review, referee reports, and editorial decision synthesis.
5. **Profiles Are Inputs, Not Review Engines:** Scholar and committee profiles (`profiles/advisors/michael-ash.md`, `profiles/committees/umass-pe.md`) serve strictly as calibration inputs to `academic-paper-reviewer`; they are not independent peer-review engines.
6. **Shared Protocol Substrate:** Reusable cross-domain prose discipline is codified in `shared/protocols/prose_discipline_protocol.md` and verified offline via `tools/prose_checks/check_prose_patterns.py`; it does not own manuscript authoring or editing tasks.
7. **Change Control Is Not Review:** Editorial governance (`shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md`, `scripts/revision_guard.py`) owns change-control verification only; it does not evaluate scholarly quality or authorize substantive prose changes. Default release policy is `optional`.
8. **Runtime Path Rule:** Until Wave F physical directory harmonization, all routing contracts MUST resolve to live root directories (`academic-paper`, `econ-write`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research`, `econ-slides`) and live extracted substrates (`profiles/`, `shared/`, `tools/`), never to future target paths (`skills/core/...`, `skills/domain/...`, `orchestrator/...`).

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
    ├── Advisor perspective simulation (Michael Ash)?
    │       └── academic-paper-reviewer
    │              + calibration input: profiles/advisors/michael-ash.md
    │
    ├── Committee / defense simulation (UMass PE)?
    │       └── academic-paper-reviewer
    │              + calibration input: profiles/committees/umass-pe.md
    │
    ├── Bounded economics writing or section drafting?
    │       └── econ-write (direct domain skill invocation)
    │
    ├── Slide deck presentation production?
    │       └── econ-slides (Beamer deck generation and verification)
    │
    ├── Prose discipline / pattern scan?
    │       ├── Diagnostic scan: tools/prose_checks/check_prose_patterns.py
    │       └── Manuscript revision: academic-paper or econ-write
    │              consuming shared/protocols/prose_discipline_protocol.md
    │
    ├── Revision verification / change control audit?
    │       └── scripts/revision_guard.py (Material Passport Port)
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
- **Primary Owner:** `academic-paper-reviewer`.
- **Calibration Input:** `profiles/advisors/michael-ash.md` (referencing `profiles/scholars/michael-ash.md`).
- **Contract:** The advisor wrapper supplies supervisory calibration parameters; it does not operate as an independent review engine.

### Rule R6 — Committee / Defense Simulation
- **Trigger Examples:** `"Simulate my PhD defense committee challenging Chapter 2"`, `"How would the UMass political economy committee critique this?"`.
- **Primary Owner:** `academic-paper-reviewer`.
- **Calibration Input:** `profiles/committees/umass-pe.md` (referencing Ash, Basu, and Young scholar profiles).
- **Contract:** The committee composition calibrates the panel roster; `academic-paper-reviewer` remains the sole execution engine.

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

### Rule R8 — Dissemination Slide Production
- **Trigger Examples:** `"Create Beamer slides for my economics seminar"`, `"Generate conference presentation deck"`.
- **Primary Owner:** `econ-slides`.
- **Scope:** Authoritative production and verification of academic economics Beamer presentation slide decks.

### Rule R9 — Evidence Discovery & Source Assessment
- **Trigger Examples:** `"Fact-check the evidence behind these claims"`, `"Find systematic literature on this topic"`.
- **Primary Owner:** `deep-research`.
- **Scope:** Systematic literature discovery, multi-agent query synthesis, PRISMA reporting, and source-level claim assessment.

### Rule R10 — Shared Prose Discipline & Pattern Audit
- **Trigger Examples:** `"Audit this draft for AI scaffolding"`, `"Check prose patterns"`, `"Audit lexical discipline"`.
- **Routing:**
  - Diagnostic scan → offline tool `tools/prose_checks/check_prose_patterns.py`.
  - Generic manuscript revision → `academic-paper` consuming `shared/protocols/prose_discipline_protocol.md`.
  - Economics manuscript revision → `econ-write` consuming `shared/protocols/prose_discipline_protocol.md`.
- **Boundary:** The shared protocol and checker do not own writing tasks; writing remains canonically owned by `academic-paper` or `econ-write`.

### Rule R11 — Editorial Governance & Change Control Verification
- **Trigger Examples:** `"Verify changes against reviewer decisions"`, `"Check revision sidecar compliance"`.
- **Primary Owner:** `shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md` executed via `scripts/revision_guard.py`.
- **Boundary:** Owns change-control verification only. Does not own peer review, writing, orchestration, or release quality judgment. Default release policy is `optional`.

---

## 4. Deprecated Compatibility Redirects

The following legacy skill surfaces are deprecated as of Wave C5. Calls to these surfaces are routed to canonical components:

| Legacy Surface | Status | Canonical Replacement |
|:---------------|:-------|:----------------------|
| `advisor-reviewer` | DEPRECATED | `academic-paper-reviewer` + `profiles/advisors/michael-ash.md` |
| `PE-phd-committee` | DEPRECATED | `academic-paper-reviewer` + `profiles/committees/umass-pe.md` |
| `prose-register-critic` | DEPRECATED | `shared/protocols/prose_discipline_protocol.md` + `tools/prose_checks/check_prose_patterns.py` (writing: `academic-paper` / `econ-write`) |

---

## 5. Runtime Path vs. Target Path Warning

> ⚠️ **CRITICAL RUNTIME WARNING (Wave C5 through Wave E):**<br>
> All live prompts, dispatch calls, tests, and configuration MUST refer to the existing runtime paths:
> - `academic-paper`
> - `econ-write`
> - `academic-paper-reviewer`
> - `academic-pipeline`
> - `deep-research`
> - `econ-slides`
> - `profiles/`
> - `shared/`
> - `tools/`
>
> Target paths such as `skills/core/academic-paper` or `skills/domain/econ-write` are architectural destinations scheduled for Wave F physical migration. Routing to nonexistent target paths during runtime is an immediate error.
