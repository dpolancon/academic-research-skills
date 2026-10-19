# ARS Runtime Routing & Capability Precedence Contract

- **Version:** 1.2.0
- **Wave:** Wave D6 (Domain Architecture & Governance Reconciliation)
- **Baseline Checkpoint:** `aa5283ecd4cf49c377a3a96ba8d57c3c0257ab65`
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
8. **Runtime Path Rule:** Until Wave F physical directory harmonization, all routing contracts MUST resolve to live root directories (`academic-paper`, `econ-write`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research`, `econ-slides`, `political-economy-research`, `umass-applied-econometrics`, `heterodox-economics-review`) and live extracted substrates (`profiles/`, `shared/`, `tools/`), never to future target paths (`skills/core/...`, `skills/domain/...`, `orchestrator/...`).
9. **Inferential-Task Jurisdiction:** Task allocation is governed by the specific inferential operation requested, not the topical framing of the prompt. A political-economy paper requesting unit-root tests routes to applied econometrics (`umass-applied-econometrics`), not political economy; an accumulation model requesting historical strike records routes to deep research / political economy, not macro modeling.
10. **Theoretical Model ≠ Automatic Estimator (`THEORY → EMPIRICAL METHOD → INTERPRETATION`):** Theoretical macro models (`heterodox-economics-review`) derive mechanisms, theoretical state variables, and testable restrictions. Empirical strategy and estimator selection belong strictly to the applicable empirical capability (`umass-applied-econometrics`). A theoretical model does not select an estimator; historical evidence cannot establish stochastic admissibility; econometric non-findings cannot be overridden by theoretical fit or narrative.
11. **Shared Protocol Standard vs. Executable Workflow Owner (`BEHAVIOR, NOT PATH, DETERMINES COMPONENT TYPE`):** `shared/protocols/historical_source_criticism_protocol.md` is a shared diagnostic standard governing claim-relative source warrant (14 diagnostic dimensions, 4 canonical verdicts: SUPPORTS, UNDERMINES, SILENT, INDETERMINATE; no universal hierarchy; no causal inference leak). It is NOT an autonomous routable skill or agent; it is executed conditionally within a requesting workflow (`political-economy-research` or `deep-research`).
12. **Preserved Causal-Inference Gap (`UNRESOLVED CAPABILITY OWNERSHIP ≠ LICENSE TO ASSIGN TO NEAREST SKILL`):** Micro-econometric causal inference (DID, IV, RDD, synthetic controls, staggered adoption) currently has `NO CURRENT CANONICAL OWNER`. It is bounded out of `umass-applied-econometrics` (time-series only) and `econ-write` (writing only). Requests for causal identification must acknowledge this gap and must NOT be misrouted to existing skills.

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
    ├── Comparative-historical PE, mechanism adjudication, or periodization?
    │       └── political-economy-research (sole canonical PE methodology owner)
    │
    ├── Heterodox macro modeling, dynamical systems, stability, or SFC closures?
    │       └── heterodox-economics-review (formal modeling; derives restrictions)
    │
    ├── Applied time-series econometrics, cointegration, or lag selection?
    │       └── umass-applied-econometrics (stochastic admissibility & testing)
    │
    ├── Historical documentary source assessment relative to claim?
    │       └── Requesting workflow (political-economy-research or deep-research)
    │              consuming shared/protocols/historical_source_criticism_protocol.md
    │
    ├── Micro-econometric causal inference (DID / IV / RDD / synthetic control)?
    │       └── UNASSIGNED_CAPABILITY_GAP (NO CURRENT CANONICAL OWNER)
    │
    ├── Systematic literature search / archival retrieval?
    │       └── deep-research (discovery & retrieval; PE never searches)
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

### Rule R12 — Comparative-Historical Political Economy & Mechanism Adjudication
- **Trigger Examples:** `"Explain which mechanism best explains this historical sequence"`, `"Periodize the transition in the labor-relations regime"`, `"Adjudicate between rival institutional explanations"`.
- **Primary Owner:** `political-economy-research`.
- **Scope:** Comparative-historical political economy, qualitative mechanism reasoning, periodization, and institutional analysis.
- **Boundaries:** Delegates formal dynamic modeling to `heterodox-economics-review`, econometric testing to `umass-applied-econometrics`, source retrieval to `deep-research`, and manuscript drafting to `academic-paper` consuming `econ-write`. Never searches archives or invents sources.

### Rule R13 — Heterodox Macroeconomic Modeling & Dynamic Systems
- **Trigger Examples:** `"Derive local stability conditions for this accumulation model"`, `"Build a Goodwin predator-prey model with debt dynamics"`, `"Check SFC accounting closures for this open-economy model"`.
- **Primary Owner:** `heterodox-economics-review`.
- **Scope:** Formal mathematical modeling, dynamical systems (2D Jacobian, trace/determinant stability, Hopf conditionality), SFC balance-sheet and transactions-flow consistency, and derivation of testable restrictions.
- **Boundaries:** Derives theoretical state variables and restrictions; does not own econometric estimator selection or stochastic admissibility testing (delegated to `umass-applied-econometrics`). Does not own historical evidence (delegated to `political-economy-research`).

### Rule R14 — Applied Time-Series Econometrics (Political Economy)
- **Trigger Examples:** `"Determine whether these series are cointegrated"`, `"Test whether wage share has a unit root"`, `"Run Toda-Yamamoto lag selection mapping"`, `"Audit VECM rank and specification"`.
- **Primary Owner:** `umass-applied-econometrics`.
- **Scope:** Applied time-series econometrics in political economy: integration order testing (ADF/KPSS), Toda-Yamamoto (k + d_max) lag selection, cointegration rank audits, forensic replication, and linear VAR/VECM estimation.
- **Boundaries:** Governs statistical admissibility and empirical non-findings; cannot be overridden by historical narrative or theoretical fit. Bounded strictly to implemented time-series methods; does not claim micro causal inference (DID, IV, RDD) or non-linear state-space estimators.

### Rule R15 — Historical Source Assessment (Claim-Relative Shared Protocol)
- **Trigger Examples:** `"Assess whether this cabinet memo supports the claim that policy X was considered"`, `"Evaluate documentary warrant for this signing date"`.
- **Requesting Workflow Owner:** `political-economy-research` (or `deep-research`).
- **Governing Protocol:** `shared/protocols/historical_source_criticism_protocol.md`.
- **Scope:** Claim-relative evidentiary warrant calibration across relevant diagnostic dimensions (authenticity, access, incentives, temporality, corroboration, silence).
- **Boundaries:** The protocol is a shared standard, NOT an autonomous executable skill or agent. It cannot be routed to as a primary owner. It does NOT assess stochastic admissibility or econometric validity.

### Rule R16 — Unassigned Causal-Inference Capability Gap
- **Trigger Examples:** `"Estimate minimum-wage employment effects using staggered DID"`, `"Compare IV vs synthetic control for this regional reform"`.
- **Owner:** `UNASSIGNED_CAPABILITY_GAP` (`NO CURRENT CANONICAL OWNER`).
- **Scope:** Micro-econometric causal identification (difference-in-differences, instrumental variables, regression discontinuity, synthetic controls).
- **Enforcement:** Requests must identify and report the capability gap. Must NOT be routed to `econ-write` (writing only) or `umass-applied-econometrics` (time-series only).

---

## 4. Adversarial Disambiguation Rules

| Rule ID | Operation / Dispute | Primary Owner | Excluded Owners | Architectural Principle |
|:---|:---|:---|:---|:---|
| **ADV-A1** | Peer review of economics manuscript | `academic-paper-reviewer` | `academic-paper`, `econ-write` | Disciplinary writing is not peer review |
| **ADV-A2** | Advisor-calibrated evaluation | `academic-paper-reviewer` | `advisor-reviewer`, `academic-paper` | Profiles are calibration inputs, not review engines |
| **ADV-A3** | Compound write + referee request | `academic-pipeline` | `econ-write` | Orchestration is not capability ownership |
| **ADV-A4** | Bounded economics prose revision | `econ-write` | `academic-paper`, `academic-pipeline` | Bounded prose does not escalate to full lifecycle |
| **ADV-A5** | Source-claim fact verification | `deep-research` | `academic-paper-reviewer`, `academic-paper` | Evidence fact-checking is not manuscript review |
| **ADV-A6** | Ambiguous manuscript review | `academic-paper-reviewer` | `deep-research`, `academic-paper`, `econ-write` | Paper review belongs strictly to review engine |
| **ADV-A7** | Research evidence review | `deep-research` | `academic-paper-reviewer` | Factual verification of claims belongs to deep-research |
| **ADV-A8** | Economics manuscript revision | `academic-paper` | `academic-paper-reviewer` | Author-side revision distinct from refereeing |
| **ADV-D1** | Archival source retrieval | `deep-research` | `political-economy-research`, `historical-source-criticism` | Retrieval belongs to deep-research; PE never searches |
| **ADV-D2** | Documentary claim support | `political-economy-research` | `academic-paper-reviewer`, `umass-applied-econometrics`, `historical-source-criticism` | Shared protocol executed in requesting workflow; not skill |
| **ADV-D3** | Multi-step cross-domain coordination | `academic-pipeline` | `political-economy-research`, `umass-applied-econometrics` | Pipeline sequences and delegates; owns no method |
| **ADV-D4** | PE topic with econometric operation | `umass-applied-econometrics` | `political-economy-research` | Operation, not topic, selects the capability owner |
| **ADV-D5** | Historical section drafting | `academic-paper` | `political-economy-research`, `heterodox-economics-review` | Manuscript lifecycle belongs to academic-paper consuming econ-write; analytical skills supply outputs |
| **ADV-D6** | Unassigned causal inference method | `UNASSIGNED_CAPABILITY_GAP` | All registered components | Causal inference has no current owner; reject all components |

---

## 5. Deprecated Compatibility Redirects

The following legacy skill surfaces are deprecated as of Wave C5. Calls to these surfaces are routed to canonical components:

| Legacy Surface | Status | Canonical Replacement |
|:---------------|:-------|:----------------------|
| `advisor-reviewer` | DEPRECATED | `academic-paper-reviewer` + `profiles/advisors/michael-ash.md` |
| `PE-phd-committee` | DEPRECATED | `academic-paper-reviewer` + `profiles/committees/umass-pe.md` |
| `prose-register-critic` | DEPRECATED | `shared/protocols/prose_discipline_protocol.md` + `tools/prose_checks/check_prose_patterns.py` (writing: `academic-paper` / `econ-write`) |

---

## 6. Runtime Path vs. Target Path Warning

> ⚠️ **CRITICAL RUNTIME WARNING (Wave C5 through Wave E):**<br>
> All live prompts, dispatch calls, tests, and configuration MUST refer to the existing runtime paths:
> - `academic-paper`
> - `econ-write`
> - `academic-paper-reviewer`
> - `academic-pipeline`
> - `deep-research`
> - `econ-slides`
> - `political-economy-research`
> - `umass-applied-econometrics`
> - `heterodox-economics-review`
> - `profiles/`
> - `shared/`
> - `tools/`
>
> Target paths such as `skills/core/academic-paper` or `skills/domain/econ-write` are architectural destinations scheduled for Wave F physical migration. Routing to nonexistent target paths during runtime is an immediate error.
