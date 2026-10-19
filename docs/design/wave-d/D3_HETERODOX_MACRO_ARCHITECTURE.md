# ARS Wave D3-A — Heterodox Macro Modeling Architecture & Goodwin Validation

- **Date:** 2026-10-17
- **Status:** `HUMAN-RATIFIED BINDING MACRO MODELING ARCHITECTURE — WAVE D3 CLOSED`
- **Primary Artifact:** `docs/design/wave-d/D3_HETERODOX_MACRO_ARCHITECTURE.md`
- **Companion Validated Candidate Artifact:** `docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md`
- **Governing Checkpoint / Inspected HEAD:** `917ee2f2332cef92015937bddd7337a52ef4b12d` (`refactor(governance): reconcile Wave C legacy surfaces`)
- **Upstream Ratified Wave-D Contracts Consumed:**
  - `docs/design/wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md` (D0 / D0.1)
  - `docs/design/wave-d/D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md` (D1 / D1.1 — CLOSED & RATIFIED)
  - `docs/design/wave-d/D2_APPLIED_ECONOMETRICS_BOUNDARY_REFACTOR.md` (D2 / D2.1 — CLOSED & RATIFIED)
- **Current Runtime Surface (Inspected Only; Unmodified in D3-A):** `heterodox-economics-review/SKILL.md` (29 lines)
- **Future Semantic Target (Wave F Physical Move):** `skills/domain/heterodox-macro-modeling`
- **Write Scope:** `docs/design/wave-d/D3_HETERODOX_MACRO_ARCHITECTURE.md` and `docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` only. Zero edits to runtime skills, registry, routing, profiles, protocols, tests, or repository topology.

---

## 0. EXECUTIVE VERDICT

Wave D3-A establishes the binding architectural design for **`heterodox-macro-modeling`** (currently at runtime path `heterodox-economics-review/`) and validates the candidate Goodwin (1967) knowledge input into a source-disciplined benchmark artifact (`docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md`).

### Core Architectural Conclusions:
1. **Canonical Capability Ownership:** `heterodox-macro-modeling` is the sole canonical owner of **`heterodox_macro_modeling`**—an author-side domain reasoning capability governing the formal construction, accounting verification, closure analysis, state-space reduction, dynamical stability analysis, and model-derived theoretical implications of heterodox macroeconomic models across traditions (Marxian, Classical/Sraffian, Kaleckian/Post-Keynesian, Harrodian, Kaldorian, Minskyan, Structuralist/Center–Periphery, Ecological, and Stock-Flow Consistent [SFC]).
2. **Contamination Diagnosis of Live `heterodox-economics-review/SKILL.md`:** The existing 29-line skill is a narrow, paper-specific checklist written for a single Sraffian Supermultiplier (SSM) / Harrodian instability critique. It suffers from five distinct architectural contaminations:
   - *Review-language leakage* in its name and framing (competing with `academic-paper-reviewer`);
   - *LaTeX/prose duplication* in §4 (`amsthm` proposition/proof formatting owned by `econ-write`);
   - *Project-specific SSM leakage* elevated to universal rules ($\mu = 1$ singularity in $\frac{1}{\mu-1}\hat{\mu}$ and $\theta \neq 1$ capacity-to-capital elasticity tautology);
   - *Sub-school doctrinal narrowing* in §3 (presenting a specific Serrano–Freitas–Lavoie–Nikiforos debate as the sole literature alignment requirement);
   - *Absence of general modeling architecture* (no general closure audit, no SFC accounting framework, no state-space/Jacobian/stability contract, and no model extension grammar).
3. **Validated General Modeling Grammar:** A formal heterodox macro model is defined structurally as:
   $$\text{MODEL} = \text{State Space} + \text{Accounting Structure} + \text{Behavioral Relations} + \text{Closure} + \text{Feedback Architecture} + \text{Institutional Regime}$$
   where **Exogenous Processes** and **Technological Assumptions** are explicitly separated from **Accounting Identities**, **Behavioral Equations**, and **Closure Rules**. This grammar passes all ten Adversarial Architecture Tests (`A` through `J`), handling models with or without a wage-share state, demand-led utilization models, SFC balance-sheet models, multi-sector models, linear and nonlinear Hopf systems, and models whose empirical implications are contradicted by data.
4. **Goodwin (1967) Validated as Pedagogical Exemplar, Never Root Ontology:** The candidate Goodwin knowledge input has been rigorously validated against Goodwin (1967) and separated from `LATER GOODWIN LITERATURE` (such as explicit capital depreciation $\delta > 0$, nominal wage-price equations, or Minskyan debt extensions). Goodwin (1967) is locked as an **exemplar reference** (`goodwin_baseline.md`) illustrating state reduction, equation-to-primitive traceability, and the distinction between a conservative Lotka–Volterra center (continuum of closed orbits) and a dissipative limit cycle. It is **not** the master template of heterodox macroeconomics.
5. **SFC Analytical Ownership vs. Tool Restraint:** Stock-Flow Consistency (balance-sheet matrices, transaction-flow matrices, row/column zero-sum laws, flow-stock accumulation and capital-gains revaluation, and redundant-equation verification) is canonically owned as **SFC analytical reasoning** inside `heterodox-macro-modeling`. In accordance with D1-LOCK-04 and Inherited Lesson L1, **no deterministic SFC matrix-verification tool** is created in Wave D3.
6. **Unbreachable Cross-Domain Boundaries (D1 & D2 Preserved):**
   - *Macro $\leftrightarrow$ Econometrics (D2):* `heterodox-macro-modeling` derives theoretical comparative statics, dynamic signs, phase relationships, stability conditions, and observable mappings. It **never** rules on stochastic admissibility, integration order, estimator selection, or empirical verdicts. Dynamic econometric frameworks (VAR, VECM, SVAR, state-space, threshold/TVP) are candidate empirical strategies owned by `applied-econometrics-pe`, never automatic consequences of a theoretical model.
   - *Macro $\leftrightarrow$ Political Economy (D1):* `heterodox-macro-modeling` owns formal equations, closures, accounting consistency, and dynamical systems (including formal open-economy and center–periphery equations). `political-economy-research` owns historical sequences, periodization, institutional coalitions, relational comparison, and historical mechanism adjudication. Neither overrides the other.

---

## 1. GOVERNING LOCKS

### 1.1 Inherited Architectural & Epistemic Invariants

| Lock ID | Invariant | Governing Source | Binding Implication for Wave D3 |
|:---|:---|:---|:---|
| **INV-1** | `ONE CAPABILITY → ONE CANONICAL OWNER` | Wave C5 (`ROUTING_AND_PRECEDENCE.md` §1.1) | `heterodox-macro-modeling` is the sole owner of formal heterodox macro modeling. It must shed peer-review language (owned by `academic-paper-reviewer`) and LaTeX/prose rules (owned by `econ-write` and `prose-discipline`). |
| **INV-2** | `INFERENTIAL-TASK JURISDICTION` | Wave D1 (`D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md` §19.2) | Primary analytic jurisdiction belongs to the component owning the requested inferential operation (formal derivation/stability vs. historical process tracing vs. statistical estimation), not the topical noun ("profit rate", "center–periphery", "instability"). |
| **INV-3** | `NO CROSS-METHOD OVERRIDE` | Wave D1 (§9.3, §10.2) & Wave D2 (§1.2) | A formal macro model cannot establish that a historical mechanism operated in a concrete case, nor can it override an econometric non-finding. Conversely, historical narrative or statistical correlation cannot repair an algebraically inconsistent or stock-flow inconsistent formal model. |
| **INV-4** | `THEORY → EMPIRICAL METHOD → INTERPRETATION` | Wave D2 (`D2_APPLIED_ECONOMETRICS_BOUNDARY_REFACTOR.md` §0) | Formal macro models operate at the `THEORY` layer (proposing mechanisms, equilibrium conditions, phase relations, and testable sign/precedence restrictions) and re-enter at `INTERPRETATION` conditioned on what empirical evidence supports. |
| **INV-5** | `BEHAVIOR, NOT PATH, DETERMINES COMPONENT TYPE` | Wave B / C / D2.1 | Methodological reasoning references inside a domain skill are skill references/protocols, not executable tools. Analytical SFC auditing is a reasoning obligation, not a software script. |
| **INV-6** | `USEFUL IMPLEMENTATION != UNIVERSAL ARCHITECTURAL RULE` | Wave D1 / D2 | A mathematical check useful in one paper (e.g., $\mu = 1$ singularity or Lotka–Volterra first integrals) must not be frozen as a universal requirement for models where that structure does not exist. |
| **INV-7** | `PROJECT-SPECIFIC SUCCESS DOES NOT CREATE CANONICAL DOCTRINE` | Wave D0 / D1 / D2 | Results from the author's Sraffian Supermultiplier critique or Goodwin modeling papers may serve as clearly labeled illustrative examples, never as mandatory doctrinal conclusions. |
| **INV-8** | `LOCK REASONING OBLIGATIONS, NOT ARBITRARY SERIALIZATION OR NOTATION` | Wave D1.1 / D2 | Mathematical obligations (explicit state space, closure audit, accounting identity check, Jacobian/stability proof) are binding; specific variable symbols ($e, \omega, \sigma$) are locally scoped to individual models. |
| **INV-9** | `SELF-REPORTED LEARNING IS NOT SELF-RATIFYING` | Wave D2.1 / D3 Governance Invariant | Claiming in the Learning Delta that a prior lesson was inherited is insufficient. Every claimed lesson must be verified via an explicit **Artifact Consistency Check** pointing to the exact sections and rules in this document that demonstrate compliance (§25). |
| **INV-10** | `PHYSICAL TOPOLOGY LOCK FOR WAVE D` | Wave C5 (`ROUTING_AND_PRECEDENCE.md` Rule 8) | During Wave D, the live component remains at root path `heterodox-economics-review/`. Physical rename to `skills/domain/heterodox-macro-modeling/` is reserved exclusively for Wave F. |

---

## 2. CURRENT MACRO SKILL AUDIT (`heterodox-economics-review/SKILL.md`)

The live file `heterodox-economics-review/SKILL.md` consists of 29 lines containing frontmatter, a header, and 7 bulleted rules across 4 sections. Every normative element is audited below against the six required contamination classes:
- `C1 — GENERIC MACRO MODELING PRINCIPLE`
- `C2 — GOODWIN / DYNAMIC-SYSTEM RELEVANT`
- `C3 — PROJECT-SPECIFIC SSM CONTENT`
- `C4 — PROSE / LATEX DUPLICATION`
- `C5 — REVIEW-LANGUAGE LEAKAGE`
- `C6 — UNSUPPORTED UNIVERSAL RULE`

### 2.1 Complete Line-by-Line Contamination Ledger

| Item ID | Lines | Current Wording Summary | Primary Classification | Secondary Classification | Architectural Defect / Contamination Diagnosis | D3-B Disposition | Target Owner / Module |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **M-R01** | 1–4 | Frontmatter `name: heterodox-economics-review`; `description: Guidelines and checklists for writing, formatting, and reviewing heterodox economics papers (e.g., Metroeconomica, JPKE) focusing on post-Keynesian and Sraffian growth models.` | `C5 — REVIEW-LANGUAGE LEAKAGE` | `C4 — PROSE / LATEX DUPLICATION` | Conflates formal macro modeling with "writing, formatting, and reviewing" (encroaching on `academic-paper`, `econ-write`, and `academic-paper-reviewer`) and narrows scope to PK/Sraffian growth models. | `GENERALIZE` / `REWRITE` (preserve `name:` key until Wave F) | `heterodox-macro-modeling` (`SKILL.md` frontmatter) |
| **M-R02** | 6–8 | `# Heterodox Economics Review & Drafting Guidelines` / `Use this skill when drafting, reviewing, or revising theoretical macroeconomics papers, particularly Sraffian Supermultiplier (SSM) models and Harrodian instability dynamics.` | `C5 — REVIEW-LANGUAGE LEAKAGE` | `C3 — PROJECT-SPECIFIC SSM CONTENT` | Frames the skill as a review/drafting checklist centered on SSM and Harrodian instability rather than an author-side formal macro modeling capability. | `GENERALIZE` / `REWRITE` | `heterodox-macro-modeling` (`SKILL.md` purpose contract) |
| **M-R03** | 10–11 | **§1 Singularity Checks:** Verify if equations contain singularities at normal values (e.g., capacity utilization $\mu = 1$). Check if term coefficients diverge (such as $\frac{1}{\mu - 1}\hat{\mu}$) and handle using L'Hôpital's rule or phase-plane analyses. | `C1 — GENERIC MACRO MODELING PRINCIPLE` (singularity & domain check) | `C3 — PROJECT-SPECIFIC SSM CONTENT` ($\mu=1$, $\frac{1}{\mu-1}\hat{\mu}$) | The general rule (check denominators and undefined manifolds inside the economically admissible state space $\Omega$) is sound dynamical systems practice. However, the $\mu=1$ singularity in $\frac{1}{\mu-1}\hat{\mu}$ comes directly from a specific SSM critique specification. | `GENERALIZE` rule; `DEMOTE TO EXAMPLE` the $\mu=1$ singularity | `dynamic_systems_and_stability.md` |
| **M-R04** | 12 | **§1 Boundary Conditions:** Ensure proofs of stability or divergence do not simply assume limits, but rigorously check vector fields near boundary conditions ($\mu \to 0$ or $\mu \to \infty$). | `C2 — GOODWIN / DYNAMIC-SYSTEM RELEVANT` | `C1 — GENERIC MACRO MODELING PRINCIPLE` | Essential dynamical-systems discipline (checking vector-field behavior, invariance, and economically admissible bounds at boundary manifolds such as $e \to 0, 1$, $\omega \to 0, 1$, $u \to 0$). | `PRESERVE` & `GENERALIZE` across arbitrary state bounds | `dynamic_systems_and_stability.md` |
| **M-R05** | 13 | **§1 Logarithmic Derivatives:** Double-check time derivatives of ratios (e.g., investment share $\phi = I/Y$). Ensure variables like capital-capacity ratio $\nu = K/Y^p$ are mapped correctly from accounting identities rather than assumed constant. | `C1 — GENERIC MACRO MODELING PRINCIPLE` | `C2 — GOODWIN / DYNAMIC-SYSTEM RELEVANT` | High-value modeling invariant: intensive ratios must be differentiated via exact logarithmic derivatives ($\widehat{X/Y} = \hat{X} - \hat{Y}$) and grounded in accounting/technological identities. | `PRESERVE` & `GENERALIZE` | `model_architecture_and_closures.md` |
| **M-R06** | 15–16 | **§2 Behavioral vs. Technological Instability:** Do not model instability by fixing the capacity-to-capital elasticity $\theta \neq 1$ in a way that forces $\nu \to \infty$. That creates a technological tautology. | `C3 — PROJECT-SPECIFIC SSM CONTENT` ($\theta \neq 1$ critique) | `C1 — GENERIC MACRO MODELING PRINCIPLE` (no specification tautologies) | The underlying principle—do not manufacture dynamic instability or stability by hardcoding arbitrary non-homogeneous technological elasticities that violate accounting/production coherence—is general. The $\theta \neq 1 \implies \nu \to \infty$ case is a project-specific SSM critique. | `GENERALIZE` into Anti-Tautology Rule; `DEMOTE TO EXAMPLE` $\theta \neq 1$ | `model_architecture_and_closures.md` |
| **M-R07** | 17 | **§2 Induced Technical Change:** Under unbalanced growth, model changes in the capital-output ratio as the result of induced technical change or factor substitution (e.g., letting $\nu_n$ evolve endogenously relative to distribution) rather than using an exogenous constant $\theta$. | `C2 — GOODWIN / DYNAMIC-SYSTEM RELEVANT` | `C6 — UNSUPPORTED UNIVERSAL RULE` (if read as banning exogenous tech change) | While induced technical change (Marx–Hicks / Kennedy–Weizsäcker / Shah–Desai) is a major heterodox mechanism, mandating endogenous $\nu_n$ universally would outlaw canonical baseline models (including `GOODWIN-1967` where $\sigma$ is constant). Must be framed as a conditional modeling choice when capital-output ratios vary. | `GENERALIZE` into Technical Change Interface | `model_architecture_and_closures.md` & `extensions_and_accounting.md` |
| **M-R08** | 19–20 | **§3 Harrodian Instability:** Ensure Harrodian instability is defined as a behavioral/expectational phenomenon (animal spirits and investment responsiveness) rather than a technological discrepancy. | `C1 — GENERIC MACRO MODELING PRINCIPLE` (conceptual accuracy of named mechanisms) | `C3 — PROJECT-SPECIFIC SSM CONTENT` | Accurately distinguishes Harrod's warranted-growth behavioral instability from technological misspecification, but currently presented as if every heterodox paper is about Harrodian instability. | `GENERALIZE` to Tradition & Closure Taxonomy | `model_architecture_and_closures.md` |
| **M-R09** | 21–23 | **§3 Core Debates:** Actively engage with: distinction between Smithian and Harrodian investment functions; taming of Harrodian instability via expected growth rate adjustments (Serrano, Freitas, Lavoie, Nikiforos). | `C6 — UNSUPPORTED UNIVERSAL RULE` | `C3 — PROJECT-SPECIFIC SSM CONTENT` | Mandates engagement with one specific sub-school debate (SSM vs. Harrodian/Kaleckian investment functions) across all heterodox macro papers. A Marxian reproduction model, Goodwin cycle model, or Minskyan SFC model need not engage Serrano/Nikiforos. | `DEMOTE TO EXAMPLE` within Closure & Demand-Led Growth taxonomy | `model_architecture_and_closures.md` |
| **M-R10** | 25–28 | **§4 LaTeX Standards:** Statically structure theorems and proofs using `amsthm` (`\begin{proposition}`, `\begin{proof}` immediately after); use `align` and `equation` for numbered derivations. | `C4 — PROSE / LATEX DUPLICATION` | — | Direct duplication of `econ-write/SKILL.md` (lines 160–178) and `econ-write/latex-tips.md` (lines 92–102), which already govern `\begin{proposition}` and `\begin{proof}` formatting for theoretical economics papers. | `DELEGATE` to `econ-write` / `REMOVE IN D3-B` | `econ-write` |

---

## 3. CANONICAL MACRO CAPABILITY DEFINITION

```text
CAPABILITY ID:   heterodox_macro_modeling
CANONICAL OWNER: heterodox-macro-modeling (runtime path in Wave D: heterodox-economics-review)
TYPE:            DOMAIN_SKILL (author-side formal modeling & mathematical analysis capability)

DEFINITION:
The reusable author-side reasoning required to formulate, audit, reduce, solve,
analyze, and extend formal macroeconomic models within and across heterodox
economic traditions. Specifically:

  (a) defining stocks, flows, ratios, prices, and intensive state variables with
      dimensional and accounting consistency;
  (b) separating accounting identities, technological assumptions, behavioral
      relations, institutional assumptions, exogenous processes, and closure rules;
  (c) auditing and comparing alternative macroeconomic closures at the equation level
      without doctrinal favoritism;
  (d) enforcing Stock-Flow Consistency (SFC) across sectoral balance sheets,
      transaction flows, and stock accumulation/revaluation identities;
  (e) reducing multi-equation systems to explicit autonomous dynamical systems
      on economically admissible state spaces;
  (f) deriving stationary states / balanced growth paths, nullclines, Jacobians,
      local stability conditions (trace/determinant, Routh–Hurwitz), and nonlinear
      global dynamics (conservative centers vs. dissipative limit cycles, bifurcations,
      and traverse paths);
  (g) executing structured model extensions via the 8-step re-derivation protocol; and
  (h) deriving testable theoretical implications (comparative statics, dynamic signs,
      phase relationships, stability regimes) for downstream empirical or historical evaluation.

It CONSUMES, and never owns: literature retrieval, historical/institutional evidence
adjudication, econometric estimation and stochastic admissibility, manuscript drafting,
economics prose and LaTeX formatting conventions, simulated peer review, workflow
orchestration, and scholar/committee calibration profiles.
```

### 3.1 Ownership Test (Three-Part Predicate)

A task is `OWNED` by `heterodox-macro-modeling` when **all three** of the following hold:
1. **Analytical Object:** The task concerns the formal mathematical structure, accounting consistency, closure mechanics, equilibrium properties, or dynamical behavior of a macroeconomic system (whether closed-form analytical or symbolic/structural).
2. **Inferential Operation:** Answering the request requires formal equation manipulation, accounting identity verification, closure classification, state-space derivation, Jacobian/eigenvalue calculation, phase-diagram/bifurcation analysis, or comparative-static derivation.
3. **Deliverable:** The required output is a formal model specification, closure audit table, SFC accounting matrix, state-space derivation, stability proof/diagnosis, model extension re-derivation, or theoretical implication map—not a literature review, historical narrative, econometric estimate, drafted manuscript section, or referee report.

### 3.2 Evaluation of the 25-Item Required Domain Capability Envelope

Prompt §8 requires evaluating whether `heterodox-macro-modeling` canonically owns 25 specific modeling capabilities and mapping them into a cohesive module architecture (`Few strong modules > many shallow modules`):

| # | Capability Item | Ownership Decision | Assigned Logical Module (§22) | Architectural Scope & Qualification |
|:---|:---|:---|:---|:---|
| 1 | State-variable definition | `OWNED` | `M1: model_architecture_and_closures.md` | Explicit declaration of state vector $\mathbf{x} \in \Omega \subseteq \mathbb{R}^n$, distinguishing predetermined states from jump/algebraic variables. |
| 2 | Stock / flow / ratio distinction | `OWNED` | `M1: model_architecture_and_closures.md` | Dimensional homogeneity check (stocks $[X]$, flows $[X/T]$, growth rates $[1/T]$, dimensionless shares/ratios $[1]$). |
| 3 | Accounting identities | `OWNED` | `M1: model_architecture_and_closures.md` & `M3: extensions_and_accounting.md` | Income-expenditure, saving-investment, cost-price, and stock-flow accumulation identities. |
| 4 | Behavioral equations | `OWNED` | `M1: model_architecture_and_closures.md` | Investment, saving, wage/price bargaining, consumption, financial portfolio, and expectations equations. |
| 5 | Exogenous processes | `OWNED` | `M1: model_architecture_and_closures.md` | Explicit specification of autonomous time trends, external growth rates, or policy parameters. |
| 6 | Closure identification | `OWNED` | `M1: model_architecture_and_closures.md` | Equation-counting and causal-ordering audit identifying which variables clear or adjust to close each balance. |
| 7 | Equilibrium concepts | `OWNED` | `M1: model_architecture_and_closures.md` & `M2: dynamic_systems_and_stability.md` | Distinction among short-run equilibrium, stationary state, balanced growth path, and classical center of gravitation. |
| 8 | Steady states / stationary states | `OWNED` | `M2: dynamic_systems_and_stability.md` | Solving $\dot{\mathbf{x}} = \mathbf{0}$, checking existence, uniqueness/multiplicity, and interior admissibility $\mathbf{x}^* \in \Omega$. |
| 9 | Nullclines | `OWNED` | `M2: dynamic_systems_and_stability.md` | Zero-motion loci $\dot{x}_i = 0$, vector-field sign partitioning across regions, and phase-plane orientation. |
| 10 | Jacobians | `OWNED` | `M2: dynamic_systems_and_stability.md` | Symbolic differentiation $J(\mathbf{x}) = \partial \mathbf{F} / \partial \mathbf{x}$ both in general form and evaluated at $\mathbf{x}^*$. |
| 11 | Local stability | `OWNED` | `M2: dynamic_systems_and_stability.md` | Hyperbolic stability conditions ($\operatorname{tr} J < 0, \det J > 0$ in 2D) and saddle-path conditions ($\det J < 0$). |
| 12 | Eigenvalue interpretation | `OWNED` | `M2: dynamic_systems_and_stability.md` | Real vs. complex conjugate roots, damping/explosion rates, oscillation frequency, and non-hyperbolic zero/imaginary cases. |
| 13 | Routh–Hurwitz where dimension warrants | `OWNED` | `M2: dynamic_systems_and_stability.md` | Principal minor conditions ($a_1 > 0, a_2 > 0, a_3 > 0, a_1 a_2 - a_3 > 0$ for 3D; Hurwitz determinants for $n \ge 4$). |
| 14 | Nonlinear dynamics | `OWNED` | `M2: dynamic_systems_and_stability.md` | Global invariance of $\Omega$, boundary manifolds, singularities, Lyapunov/first-integral functions, and basins of attraction. |
| 15 | Conservative vs dissipative systems | `OWNED` | `M2: dynamic_systems_and_stability.md` | Divergence/trace test ($\nabla \cdot \mathbf{F}$ or Bendixson–Dulac criterion) separating conservative centers from dissipative attractors/repellors. |
| 16 | Limit-cycle analysis | `OWNED` | `M2: dynamic_systems_and_stability.md` | Isolated periodic orbits vs. closed-orbit families; Poincaré–Bendixson theorem and orbital stability. |
| 17 | Bifurcations where justified | `OWNED` | `M2: dynamic_systems_and_stability.md` | Hopf (supercritical/subcritical), saddle-node, and transcritical bifurcations as structural parameters cross critical values. |
| 18 | Traverse / adjustment paths | `OWNED` | `M2: dynamic_systems_and_stability.md` | Out-of-equilibrium transition dynamics between short-run equilibria and long-run normal positions. |
| 19 | Distribution–accumulation feedbacks | `OWNED` | `M1: model_architecture_and_closures.md` & `M4: goodwin_baseline.md` | Profit-squeeze vs. profit-led vs. wage-led feedbacks linking $\omega, r, u, e$, and $g_K$. |
| 20 | Capacity-utilization dynamics | `OWNED` | `M1: model_architecture_and_closures.md` | Endogenous $u = Y/Y^p$ adjustment, Keynesian stability condition, paradox of thrift/costs, and Harrodian instability vs. normal utilization $u_n$. |
| 21 | Endogenous technical change | `OWNED` | `M3: extensions_and_accounting.md` | Kaldor–Verdoorn scale effects, Marx–Hicks induced technical bias, and endogenous capital-output ratio $\sigma$ dynamics. |
| 22 | Demand-led growth mechanisms | `OWNED` | `M1: model_architecture_and_closures.md` | Autonomous vs. induced demand, Kaleckian growth closures, Kaldorian export-led growth, and Sraffian Supermultiplier closures. |
| 23 | Stock-flow consistency (SFC) | `OWNED` (analytical) | `M3: extensions_and_accounting.md` | Balance-sheet and transaction-flow matrices, accounting closures, stock-flow norms, and debt/wealth state dynamics. |
| 24 | Center–periphery / open-economy formal extensions | `OWNED` (formal equations) | `M3: extensions_and_accounting.md` | BOP-constrained growth (Thirlwall's Law), Prebisch–Singer terms-of-trade dynamics, external debt states, and currency-hierarchy interest parity wedges. |
| 25 | Model-derived comparative statics & dynamic implications | `OWNED` | `M2: dynamic_systems_and_stability.md` & `M3: extensions_and_accounting.md` | Partial derivatives $\partial \mathbf{x}^* / \partial \boldsymbol{\theta}$, phase lead/lag relations, and testable observable predictions for econometrics/PE. |

---

## 4. EXPLICIT NON-OWNERSHIP

| Task / Domain | Canonical Owner | `heterodox-macro-modeling` Relationship | Boundary Rule |
|:---|:---|:---|:---|
| **Simulated peer review, referee reports, accept/reject verdicts, scored evaluations** | `academic-paper-reviewer` | `OUT OF SCOPE` (Reviewer may consume macro standards as domain criteria) | Author-side math verification produces diagnostic derivations and consistency ledgers, **never** referee reports or editorial verdicts. |
| **Encyclopedic history of economic thought or doctrinal advocacy** | None (`OUT OF SCOPE` as canonical doctrine; literature synthesis owned by `deep-research`) | Theory enters as formal equations and explicit closures | The skill never preaches school orthodoxy or writes ideological essays; it translates theoretical traditions into auditable mathematical closures. |
| **Econometric estimation, unit-root/cointegration testing, lag selection, bootstrap, statistical verdicts** | `applied-econometrics-pe` (runtime: `umass-applied-econometrics`) | `COMPOSED` downstream via §20 | Theoretical models propose hypotheses and parameter sign restrictions; they never certify stochastic admissibility or empirical truth. |
| **Comparative-historical research design, periodization, process tracing, archival source adjudication** | `political-economy-research` (planned D4) | `COMPOSED` via §19 (D1 §10) | Macro formalizes structural relations and closures; PE adjudicates whether historical institutions and sequences match those assumptions. |
| **Claim-relative historical source criticism** | `shared/protocols/historical_source_criticism_protocol.md` (planned D4) | `OUT OF SCOPE` | Formal derivations do not evaluate archival documents. |
| **Literature search, citation verification, bibliographic synthesis** | `deep-research` | `CONSUMED` | Macro does not execute bibliographic searches or invent citations; unverified attributions are marked `SOURCE VALIDATION REQUIRED`. |
| **Manuscript lifecycle, section drafting, citation integration** | `academic-paper` | Supplies formal model artifacts | `academic-paper` drafts the manuscript prose consuming macro derivations. |
| **Economics writing style, BLUF, model-section exposition prose, LaTeX `amsthm` formatting** | `econ-write` | `DELEGATED` | `econ-write` (`SKILL.md` lines 160–178, `latex-tips.md` lines 92–102) owns theorem/proposition LaTeX environments and prose exposition. |
| **Cross-domain prose discipline and lexical rules** | `shared/protocols/prose_discipline_protocol.md` | `CONSUMED` when prose is written | Macro owns mathematical precision, not sentence-level syntax rules. |
| **Beamer slide deck generation** | `econ-slides` | Supplies mathematical content | Slide layout and compilation belong to `econ-slides`. |
| **Scholar, advisor, and committee calibration** | `profiles/*` (`deepankar-basu.md`, `michael-ash.md`, `umass-pe.md`) | Calibration input only (consumed by reviewer/authoring) | Faculty preferences (e.g., Basu's preference for Marxian profitability decomposition) remain in `profiles/` and must not lock canonical macro rules. |
| **Project-specific parameter values, dissertation critiques, or country calibrations** | Workspace Project Overlay | Parameter/specification input only | Project-specific SSM critiques ($\mu=1$ singularity, $\theta \neq 1$) may appear only as labeled illustrative examples. |

---

## 5. GENERAL MODEL ARCHITECTURE & MODELING GRAMMAR TEST

Prompt §7 requires testing whether the following structural decomposition should become domain-level macro-modeling doctrine:

$$\text{MODEL} = \text{State Space} + \text{Accounting Structure} + \text{Behavioral Relations} + \text{Closure} + \text{Feedback Architecture} + \text{Institutional Regime}$$

### 5.1 Multi-Tradition Validation of the Modeling Grammar

To ensure this grammar is not a disguised Goodwin template, we test each component across five distinct heterodox modeling families:
1. **Marxian / Classical (`GOODWIN-1967` / Foley Circuit of Capital)**
2. **Kaleckian / Post-Keynesian Demand-Led (Rowthorn–Dutt–Amadeo–Bhaduri–Marglin)**
3. **Sraffian Supermultiplier (Serrano–Freitas)**
4. **Godley–Lavoie Stock-Flow Consistent (SFC)**
5. **Structuralist / Thirlwall Open-Economy Center–Periphery**

| Grammar Element | Formal Definition | How It Instantiates Across Non-Goodwin Traditions | Scope Classification |
|:---|:---|:---|:---|
| **1. State Space ($\mathbf{x} \in \Omega$)** | The minimal vector of predetermined stocks or intensive stock-flow/distributional ratios whose time derivatives $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x}; \boldsymbol{\theta})$ (or discrete transitions $\mathbf{x}_{t+1} = \mathbf{G}(\mathbf{x}_t; \boldsymbol{\theta})$) govern system evolution, together with its economically admissible domain $\Omega$. | - *Goodwin:* $\mathbf{x} = (e, \omega) \in (0,1)^2$<br>- *Kaleckian short-run/medium-run:* $\mathbf{x} = (u, \omega)$ or $(k, d)$ (no $e$ state)<br>- *SSM:* $\mathbf{x} = (u, \gamma_Z)$ where $\gamma_Z = Z/K$ is autonomous demand-to-capital ratio (no $\omega$ or $e$ state)<br>- *SFC:* $\mathbf{x} = (v_h, d_f, b_g)$ (sectoral wealth/debt ratios)<br>- *Center–Periphery:* $\mathbf{x} = (q_{\text{rer}}, f_d)$ (real exchange rate, external debt ratio) | `HETERODOX-MACRO DOMAIN PRINCIPLE` |
| **2. Accounting Structure** | The system of identities holding by definition at every instant/period (national income-expenditure, cost-income decomposition, sectoral budget constraints, stock-flow accumulation $\dot{S} = F - \delta S + \text{revaluation}$, and intensive ratio definitions). | Present in **all** formal macro models. In 2D analytical models, consists of national income and growth-rate identities ($\widehat{X/Y} = \hat{X} - \hat{Y}$); in SFC models, expands to full Balance-Sheet and Transaction-Flow matrices. | `HETERODOX-MACRO DOMAIN PRINCIPLE` |
| **3. Technological & Exogenous Processes** *(Explicit refinement added by D3-A)* | Production-technology mappings (e.g., potential output $Y^p = K/\sigma_{\text{cap}}$, labor productivity $a = Y/L$) and exogenous laws of motion ($\hat{a} = \alpha$, autonomous demand growth $\hat{Z} = g_Z$, world income growth $\hat{Y}^*$). | Explicitly required so technological relations are neither confused with accounting identities nor conflated with behavioral equations. | `HETERODOX-MACRO DOMAIN PRINCIPLE` |
| **4. Behavioral Relations** | Equations describing purposeful or routine responses of economic agents/classes (investment functions $g_K(\cdot)$, consumption/saving functions, wage-price conflict curves, credit supply/portfolio allocation, import/export demand elasticities). | Universal across traditions, though functional forms and arguments differ by school (e.g., profit-share vs. utilization arguments in $g_K$). | `HETERODOX-MACRO DOMAIN PRINCIPLE` |
| **5. Closure** | The mathematical and economic assignment of which variables are endogenous vs. exogenous/predetermined, and which adjustment mechanism brings planned magnitudes into consistency with accounting identities ($n$ independent equations for $n$ endogenous variables). | - *Classical/Goodwin:* Saving drives investment ($I \equiv S$), full capacity ($u=1$).<br>- *Kaleckian:* Investment drives saving via endogenous capacity utilization $u$ ($S(u, \omega) = I(u, \omega)$).<br>- *Kaldor–Pasinetti:* Full capacity ($u=\bar{u}$), income distribution $\omega$ adjusts so $S(\omega) = I$.<br>- *BOP-constrained:* Output growth adjusts to balance trade/payments ($\hat{Y} = \hat{Y}_{BOP}$). | `HETERODOX-MACRO DOMAIN PRINCIPLE` |
| **6. Feedback Architecture** | The directed signed causal graph and Jacobian structure ($J_{ij} = \partial \dot{x}_i / \partial x_j$) linking states to their own rates of change (diagonal self-stabilizing/destabilizing loops) and to other states (off-diagonal coupling loops). | Captures both predator-prey cross-coupling ($J_{12} J_{21} < 0$), cumulative causation ($J_{ii} > 0$ or $J_{12} J_{21} > 0$), Keynesian multiplier-accelerator damping/instability, and debt-service snowballs ($r > g$). | `HETERODOX-MACRO DOMAIN PRINCIPLE` |
| **7. Institutional Regime** | The historically or structurally conditioned parameter constraints, bargaining rules, monetary/fiscal policy regimes, exchange-rate arrangements, and financial regulations that parameterize behavioral relations and select the operative closure. | Connects formal macro parameters ($\boldsymbol{\theta}$) and closure selection to institutional political economy without collapsing formal math into historical narrative. | `CROSS-DOMAIN PRINCIPLE` (bridges `heterodox-macro-modeling` and `political-economy-research`) |

**Grammar Verdict:** With the explicit inclusion of **Technological & Exogenous Processes** alongside **Accounting Structure**, the refined grammar:
$$\text{MODEL} = \text{State Space} + \text{Accounting Structure} + \text{Technology \& Exogenous Processes} + \text{Behavioral Relations} + \text{Closure} + \text{Feedback Architecture} + \text{Institutional Regime}$$
is validated and locked as a **`HETERODOX-MACRO DOMAIN PRINCIPLE`**.

### 5.2 Notation Discipline Contract

To prevent Goodwin or SSM notation from polluting unrelated models, `heterodox-macro-modeling` enforces four strict notation rules:
1. **No Universal Symbol Lock Across the Skill:** While individual reference exemplars (such as `goodwin_baseline.md`) locally lock their symbols, the domain skill allows model-specific notation appropriate to each subfield.
2. **Mandatory Symbol Table Before Derivation:** Every formal model derivation must define every symbol before or upon first use, specifying its mathematical domain and economic meaning.
3. **Zero Intra-Model Symbol Collisions:** A single model may never use the same symbol for two distinct quantities (e.g., using $\pi$ for both the profit share and the inflation rate, or $\mu$ for both capacity utilization and the markup, within the same system).
4. **Explicit Dimensional & Type Tagging:** Every variable in the symbol table must be typed as one of:
   - `Stock` (measured at an instant in time, units $[X]$);
   - `Flow` (measured per unit of time, units $[X / T]$);
   - `Level / Rate / Price` (e.g., wage rate, exchange rate, interest rate);
   - `Intensive Ratio / Share` (dimensionless stock-to-stock, flow-to-flow, or stock-to-flow ratio, specifying units $[1]$ or $[T]$);
   - `State Variable` vs. `Algebraic Endogenous Variable` vs. `Exogenous Parameter`.

---

## 6. ACCOUNTING VS. BEHAVIOR VS. CLOSURE

A foundational failure mode in informal macroeconomic modeling is conflating definitional identities with behavioral hypotheses or closure assumptions. `heterodox-macro-modeling` enforces a six-way equation taxonomy:

### 6.1 Six-Way Primitive Equation Taxonomy

| Equation Category | Definition | Falsifiability / Epistemic Status | Canonical Example |
|:---|:---|:---|:---|
| **1. Accounting Identity (`ID`)** | Holds by definition of the variables or double-entry bookkeeping across all possible worlds. | **True by definition** (cannot be empirically rejected; violation is an algebraic error). | $Y \equiv W + \Pi$; $\dot{K} \equiv I - \delta K$; $\widehat{(X/Y)} \equiv \hat{X} - \hat{Y}$; $\sum_j \text{Financial Net Lending}_j \equiv 0$. |
| **2. Technological Assumption (`TECH`)** | Specifies the physical transformation between inputs, productive capacity, and output. | **Structural approximation** (can be relaxed via induced technical change or variable proportions). | $Y^p = K / \sigma_{\text{cap}}$ with constant $\sigma_{\text{cap}}$; $a \equiv Y/L$ growing at $\hat{a} = \alpha$. |
| **3. Behavioral Relation (`BEH`)** | Describes how economic agents, classes, or sectors form plans or react to incentives/states. | **Theoretically contested & empirically testable** (core locus of economic theory). | Kaleckian investment $g_K = \gamma_0 + \gamma_u u + \gamma_\pi \pi$; real-wage bargaining $\hat{w} = -\gamma + \rho e$. |
| **4. Institutional Assumption (`INST`)** | Encodes legal, monetary, class, or policy rules governing distribution, finance, or market structure. | **Historically/institutionally contingent** (valid within a specific institutional regime; interfaces with PE). | Classical class saving ($s_w = 0, s_\pi > 0$); Taylor rule; central bank accommodation of reserves; fixed peg. |
| **5. Closure Rule (`CLOS`)** | Specifies which endogenous variable adjusts to reconcile independent plans with accounting identities, or equates planned magnitudes directly. | **System-level modeling choice** (defines the causal ordering and macro regime of the model). | Say's Law closure ($I \equiv S, u = 1$) vs. Keynesian/Kaleckian goods-market closure ($I(u,\pi) = S(u,\pi)$ solved for endogenous $u$). |
| **6. Exogenous Process (`EXOG`)** | Specifies the trajectory of variables determined outside the model's feedback loops. | **Boundary condition** (can be endogenized in model extensions). | $\hat{N} = \beta$; autonomous non-capacity-creating expenditure growth $\hat{Z} = g_Z$; world demand growth $\hat{Y}^*$. |

### 6.2 Anti-Tautology Guard (Generalizing Live Rules §1.3 and §2.1)

The live skill's warnings against assuming $\nu = K/Y^p$ constant without checking accounting identities (§1.3) and against manufacturing instability via a fixed non-unitary capacity-to-capital elasticity $\theta \neq 1$ (§2.1) are generalized into two binding domain rules:

1. **Identity-Consistent Ratio Differentiation Rule (`ID-DIFF`):**
   Whenever a model defines an intensive ratio $z \equiv X / Y$, its time derivative **must** be derived directly from the laws of motion of $X$ and $Y$:
   $$\hat{z} = \frac{\dot{z}}{z} = \hat{X} - \hat{Y} \implies \dot{z} = z (\hat{X} - \hat{Y})$$
   A modeler may set $\dot{z} = 0$ **only** by explicitly declaring a closure or technological assumption $\hat{X} = \hat{Y}$ and verifying that no other equation in the system implies $\hat{X} \neq \hat{Y}$.
2. **No Specification Tautology Rule (`NO-TAUTOLOGY`):**
   Dynamic instability, cyclicality, or convergence must arise from explicit **behavioral feedbacks and closure interactions**, never from an unexamined dimensional or technological exponent that mechanically forces a ratio to zero or infinity along any steady growth path.
   - *Illustrative Example (demoted from live §2.1):* In capacity-utilization models, defining potential output via a non-homogeneous function $Y^p = A K^\theta$ with constant $\theta \neq 1$ mechanically forces the capital-capacity ratio $\nu = K/Y^p = A^{-1} K^{1-\theta}$ to drift toward $0$ or $\infty$ under any positive capital growth $\hat{K} > 0$, manufacturing secular divergence by technological definition rather than behavioral Harrodian instability.

---

## 7. STATE-SPACE AND DYNAMIC-SYSTEM CONTRACT

Every dynamic model formulated or audited by `heterodox-macro-modeling` must satisfy the following five state-space obligations:

### 7.1 Intensive State Reduction Obligation
1. **Extensive vs. Intensive Variables:** Growing economies feature trending extensive levels ($Y, K, L, N, D, Z$). To analyze stationary states and cyclical dynamics, extensive variables must be normalized into **intensive ratios or shares** (e.g., $e = L/N$, $\omega = wL/Y$, $u = Y/Y^p$, $d = D/K$, $\gamma_Z = Z/K$) that remain bounded along a balanced growth path.
2. **Explicit State Vector Declaration:** The model must explicitly declare the dimension $n$ and components of the state vector:
   $$\mathbf{x}(t) = \left( x_1(t), x_2(t), \dots, x_n(t) \right)^T \in \Omega \subseteq \mathbb{R}^n$$
   distinguishing **dynamic state variables** (governed by differential equations $\dot{x}_i = F_i(\mathbf{x}; \boldsymbol{\theta})$ or difference equations $x_{i,t+1} = G_i(\mathbf{x}_t; \boldsymbol{\theta})$) from **static/algebraic endogenous variables** $y_j = H_j(\mathbf{x}; \boldsymbol{\theta})$ solved instantaneously at each point in time via short-run equilibrium closures.
3. **Autonomous vs. Non-Autonomous Verification:** After intensive normalization, the reduced system $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x}; \boldsymbol{\theta})$ must be checked for explicit time dependence $t$. If time $t$ remains on the right-hand side, the model does **not** admit a time-invariant intensive stationary state unless a further balanced-growth restriction (such as Harrod-neutral technical change or asymptotically constant growth rates) is imposed.

### 7.2 Admissible Domain $\Omega$, Boundary Behavior, and Singularity Contract
1. **Economic Admissibility Domain $\Omega$:** For every state variable $x_i$, the economically meaningful interval must be declared prior to stability analysis (e.g., shares $\omega \in (0, 1)$, employment rate $e \in (0, 1)$, capacity utilization $u \in (0, u_{\max})$ or $\mathbb{R}_{++}$, capital-output ratio $\sigma \in \mathbb{R}_{++}$, net debt ratio $d \in \mathbb{R}$).
2. **Positivity and Forward Invariance Check:** The vector field $\mathbf{F}(\mathbf{x})$ must be checked at the boundaries $\partial \Omega$:
   - If $x_i = 0$ is a multiplicative boundary ($\dot{x}_i = x_i f_i(\mathbf{x})$), then $x_i = 0$ is an invariant manifold (trajectories starting in $x_i > 0$ cannot cross $x_i = 0$ in finite time).
   - For upper bounds (such as $e = 1$ or $\omega = 1$), the audit must state whether the functional forms enforce invariance of $\Omega$ globally (e.g., via nonlinear asymptotes $\lim_{e \to 1^-} f(e) = +\infty$) or only locally in a neighborhood of $\mathbf{x}^*$.
3. **Singularity & Zero-Denominator Audit (Generalizing Live Rule §1.1):**
   Whenever a reduced-form differential equation contains rational expressions $\dot{x}_i = \frac{N_i(\mathbf{x}; \boldsymbol{\theta})}{D_i(\mathbf{x}; \boldsymbol{\theta})}$, the singular locus $\mathcal{S} = \{ \mathbf{x} \in \Omega : D_i(\mathbf{x}; \boldsymbol{\theta}) = 0 \}$ must be solved explicitly:
   - Determine whether $\mathcal{S}$ intersects the interior admissible domain $\Omega$ or normal equilibrium values.
   - Check whether numerator $N_i$ vanishes simultaneously on $\mathcal{S}$ (removable singularity evaluable via L'Hôpital's rule / Taylor expansion) or does not vanish (non-removable singularity / impasse curve / relaxation oscillation manifold).
   - *Illustrative Example (demoted from live §1.1):* If a dynamical specification contains $\frac{1}{\mu - 1}\hat{\mu}$, evaluating trajectories as capacity utilization approaches normal utilization ($\mu \to 1$) requires checking whether $\hat{\mu} \to 0$ at the same order or whether the equation exhibits a genuine singularity at $\mu = 1$.

---

## 8. STABILITY ANALYSIS CONTRACT

`heterodox-macro-modeling` enforces a complete, mathematically rigorous stability workflow that prevents linearizing non-hyperbolic systems blindly or confusing local stability with global behavior.

### 8.1 Step-by-Step Stability Audit Protocol

1. **Nullclines & Phase-Space Partitioning:**
   - Solve $F_i(\mathbf{x}; \boldsymbol{\theta}) = 0$ for each $i = 1, \dots, n$ to identify all trivial (boundary) and non-trivial (interior) nullclines.
   - Determine the sign of $\dot{x}_i$ on either side of each nullcline to establish directional arrows in phase space.
2. **Stationary-State Derivation & Admissibility Gate:**
   - Solve the simultaneous system $\mathbf{F}(\mathbf{x}^*; \boldsymbol{\theta}) = \mathbf{0}$.
   - Explicitly write the parameter inequalities required for $\mathbf{x}^* \in \operatorname{int}(\Omega)$. An equilibrium that violates $\mathbf{x}^* \in \Omega$ (e.g., $\omega^* < 0$ or $e^* > 1$) is classified as **economically inadmissible** regardless of its formal eigenvalues.
3. **Jacobian Matrix Construction:**
   - Derive the general symbolic Jacobian $J(\mathbf{x}) = \left[ \frac{\partial F_i}{\partial x_j}(\mathbf{x}) \right]_{i,j=1}^n$.
   - Evaluate $J^* \equiv J(\mathbf{x}^*)$ at each admissible stationary state, explicitly noting which terms simplify to zero because $F_i(\mathbf{x}^*) = 0$.
4. **Local Stability Characterization by System Dimension:**
   - **Dimension $n = 1$:** $\dot{x} = F(x)$; locally asymptotically stable if $F'(x^*) < 0$, unstable if $F'(x^*) > 0$, non-hyperbolic if $F'(x^*) = 0$.
   - **Dimension $n = 2$ (Planar Systems):** Characteristic polynomial $\lambda^2 - \operatorname{tr}(J^*)\lambda + \det(J^*) = 0$ with discriminant $\Delta = (\operatorname{tr} J^*)^2 - 4 \det J^*$:
     - $\det J^* < 0$: **Hyperbolic Saddle Point** (one positive real eigenvalue, one negative real eigenvalue; 1D stable manifold and 1D unstable manifold).
     - $\det J^* > 0$ and $\operatorname{tr} J^* < 0$: **Locally Asymptotically Stable** (stable node if $\Delta \ge 0$; stable focus / damped oscillations if $\Delta < 0$).
     - $\det J^* > 0$ and $\operatorname{tr} J^* > 0$: **Locally Unstable** (unstable node if $\Delta \ge 0$; unstable focus / explosive oscillations if $\Delta < 0$).
     - $\det J^* > 0$ and $\operatorname{tr} J^* = 0$: **Non-Hyperbolic Purely Imaginary Pair** ($\lambda = \pm i \sqrt{\det J^*}$). **Linearization is inconclusive** by Hartman–Grobman; mandatory escalation to Step 5 (Nonlinear Center vs. Limit Cycle analysis).
   - **Dimension $n = 3$ (Three-State Systems, e.g., Goodwin–Minsky $(e, \omega, d)$ or SSM $(u, \gamma_Z, \omega)$):**
     Characteristic polynomial $\lambda^3 + a_1 \lambda^2 + a_2 \lambda + a_3 = 0$, where:
     $$a_1 = -\operatorname{tr}(J^*), \qquad a_2 = M_{11} + M_{22} + M_{33} \text{ (sum of principal } 2\times 2 \text{ minors)}, \qquad a_3 = -\det(J^*)$$
     By the **Routh–Hurwitz Theorem**, all three eigenvalues have strictly negative real parts ($\operatorname{Re}(\lambda_i) < 0$) if and only if:
     $$a_1 > 0, \qquad a_2 > 0, \qquad a_3 > 0, \qquad \text{and} \qquad a_1 a_2 - a_3 > 0$$
   - **Dimension $n \ge 4$:** Apply general Hurwitz determinant conditions $\Delta_k > 0$ ($k = 1, \dots, n$) or block-triangular decomposition where the system is recursive.
5. **Global & Nonlinear Dynamical Analysis:**
   - **Conservative vs. Dissipative Classification:** Compute vector-field divergence $\nabla \cdot \mathbf{F}$ (or weighted divergence $\nabla \cdot (g(\mathbf{x})\mathbf{F}(\mathbf{x}))$ via Bendixson–Dulac). If the system admits a smooth first integral $V(\mathbf{x}) = \text{const}$ with definite Hessian at $\mathbf{x}^*$, it is a **conservative center** (family of closed orbits whose amplitude depends permanently on initial conditions).
   - **Limit-Cycle Verification:** Distinguish a conservative family of closed orbits from an **isolated limit cycle** (dissipative periodic attractor/repellor). Use the **Poincaré–Bendixson Theorem** (trapping region $D \subset \Omega$ containing a unique unstable focus/node and no other equilibria) or **Hopf Bifurcation Theorem** (verify eigenvalue crossing speed $\left.\frac{d \operatorname{Re}\lambda(\mu)}{d\mu}\right|_{\mu=\mu_H} \neq 0$ and sign of the first Lyapunov coefficient $\ell_1$ to distinguish supercritical stable limit cycles from subcritical unstable limit cycles).

---

## 9. EQUILIBRIUM / STATIONARY-STATE CONCEPTS

Because heterodox traditions use the word "equilibrium" in fundamentally different ways, `heterodox-macro-modeling` requires every model analysis to specify which equilibrium concept is being invoked:

| Equilibrium Concept | Time Horizon & Adjustment Mechanism | Mathematical Representation | Traditions Where Central |
|:---|:---|:---|:---|
| **1. Short-Run Temporary Equilibrium** | Fast market-clearing or quantity adjustment (e.g., goods-market multiplier adjustment of output $Y$ or utilization $u$) with capital stock $K$, technology $a$, debt $D$, and distribution $\omega$ held temporarily fixed. | Algebraic subsystem $\mathbf{0} = \mathbf{G}(\mathbf{y}, \mathbf{x}; \boldsymbol{\theta})$ solved for fast variables $\mathbf{y} = \mathbf{H}(\mathbf{x}; \boldsymbol{\theta})$. | Kaleckian, Post-Keynesian, Structuralist, Temporary SFC equilibria. |
| **2. Medium-Run Stationary State / Steady-State Equilibrium** | State vector of intensive ratios ceases to change ($\dot{\mathbf{x}} = \mathbf{0}$), though extensive levels ($Y, K, L$) grow at constant rates (or oscillate around $\mathbf{x}^*$). | Fixed point $\mathbf{x}^*$ of $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x}; \boldsymbol{\theta})$. | Goodwin / Marxian cycles, Kaleckian–Goodwin syntheses, Minskyan debt cycles. |
| **3. Long-Run Balanced Growth Path (BGP) / Normal Position** | All extensive stocks and flows grow at a common steady rate $g^*$, capacity utilization equals normal/desired utilization ($u^* = u_n$), and intersectoral profit rates equalize around prices of production. | $\hat{Y} = \hat{K} = \hat{Z} = g^*$ with $\dot{u} = 0, u^* = u_n$. | Classical / Sraffian, Sraffian Supermultiplier, Kaldor–Pasinetti, Harrodian warranted growth. |
| **4. Classical / Marxian Center of Gravitation** | Market prices and turbulent accumulation paths fluctuate persistently around—without necessarily resting at—a structural attractor (such as prices of production or $(e^*, \omega^*)$). | Time-average property $\lim_{T\to\infty} \frac{1}{T}\int_0^T \mathbf{x}(t)\,dt = \mathbf{x}^*$ (holds along Goodwin closed orbits and ergodic attractors). | Classical political economy, Marxian value/price and accumulation dynamics. |
| **5. Path-Dependent / Hysteretic Moving Equilibrium** | The long-run stationary state itself depends on the traverse path or initial conditions (zero root / continuum of equilibria, or endogenous natural rate $g_n = g_n(g)$). | Non-isolated fixed-point manifold or history-dependent parameter evolution. | Kaldor–Verdoorn cumulative causation, hysteretic Post-Keynesian growth models. |

---

## 10. CLOSURE ANALYSIS FRAMEWORK

In accordance with Prompt §9, `heterodox-macro-modeling` **prohibits** treating simplistic school labels ("the Keynesian closure", "the Marxian closure", "the Sraffian closure") as self-sufficient mathematical specifications. School labels may describe candidate **families** of closure, but they never replace equation-level specification.

### 10.1 The Mandatory 14-Question Equation-Level Closure Audit

For every macroeconomic model constructed or analyzed, the skill requires executing the following 14-question audit to establish how the system closes mathematically and economically:

| # | Audit Question | What Must Be Specified at the Equation Level |
|:---|:---|:---|
| **Q1** | **What determines output ($Y$)?** | Is output determined by productive capacity ($Y = K/\sigma$), by effective demand ($Y = C + I + G + NX$), by labor supply ($Y = a L$), or by a balance-of-payments constraint ($Y = Y_{BOP}$)? |
| **Q2** | **What determines capacity utilization ($u$)?** | Is utilization fixed at full/normal capacity ($u = 1$ or $u = u_n$), an endogenous short-run adjusting variable ($u = Y/Y^p$), or a dynamic state variable adjusting to excess demand/supply? |
| **Q3** | **What determines investment ($I$ or $g_K$)?** | Is investment passively determined by saving ($I \equiv S$), or driven by an independent behavioral investment function $g_K(u, \pi, r, i, \gamma_Z)$? |
| **Q4** | **What determines saving ($S$)?** | How do household, worker, capitalist, firm retained-earning, government, and foreign saving propensities ($s_w, s_\pi, s_f$) map income and wealth into aggregate saving? |
| **Q5** | **What determines income distribution ($\omega, \pi, r$)?** | Is distribution fixed exogenously (markup), determined by a classical conventional subsistence wage ($w = \bar{w}$), adjusted endogenously to equate saving and investment (Kaldor–Pasinetti), or driven dynamically by labor-market conflict/bargaining ($\dot{\omega} = F_2(e, \omega)$)? |
| **Q6** | **What determines wages and prices ($W, P, w$)?** | Are wages bargained in real terms ($\hat{w}$) or nominal terms ($\hat{W}$) with separate price-setting ($\hat{P}$) and conflict inflation? |
| **Q7** | **What determines employment ($L, e$)?** | Does employment clear the labor market ($e = \bar{e}$), or is labor demand derived residually from output and productivity ($L = Y/a$, making $e = L/N$ endogenous)? |
| **Q8** | **What determines technical change ($a, \sigma$)?** | Are labor productivity growth ($\hat{a}$) and the capital-output ratio ($\sigma$) exogenous constants, or endogenous functions of output growth (Kaldor–Verdoorn) and distribution (Marx–Hicks induced bias)? |
| **Q9** | **What adjusts when planned magnitudes conflict?** | When planned investment $I^p$ differs from planned saving $S^p$, or wage claims conflict with target profit markups, does adjustment occur through output/utilization $u$, price inflation $\hat{P}$ (forced saving), inventories, rationed credit, or expectations revision? |
| **Q10** | **Which variables are predetermined at time $t$?** | Which stocks ($K, N, D, a$) and intensive state ratios are fixed at the instant $t$ (moving only via $\dot{\mathbf{x}}$), and which variables jump/clear instantaneously? |
| **Q11** | **Which variables clear markets or accounting balances?** | Explicit mapping of each equilibrium condition or accounting identity to the specific endogenous variable it determines. |
| **Q12** | **What is exogenous?** | Complete list of exogenous parameters $\boldsymbol{\theta}$ and autonomous forcing processes (e.g., $\alpha, \beta, g_Z, \hat{Y}^*, i_{cb}$). |
| **Q13** | **What is endogenous?** | Complete list of $M$ endogenous variables ($n$ dynamic states $\mathbf{x}$ + $m$ algebraic variables $\mathbf{y}$). |
| **Q14** | **What closes the system mathematically?** | Verification that the number of independent equations equals $M = n + m$, the algebraic subsystem Jacobian $\partial \mathbf{G}/\partial \mathbf{y}$ is nonsingular (Implicit Function Theorem), and no redundant identity is double-counted as an independent equation. |

### 10.2 Comparative Reference Matrix of Classic Closure Families (Illustrative, Non-Dogmatic)

Following Sen (1963), Marglin (1984), Dutt (1990), and Foley, Michl, & Tavani (2019), classic heterodox closure families represent different assignments in the 14-question audit above:

| Closure Family Label | Utilization $u$ | Real Wage $w$ / Wage Share $\omega$ | Investment $I$ vs. Saving $S$ | Employment Rate $e$ | Adjusting Variable Closing $I = S$ |
|:---|:---|:---|:---|:---|:---|
| **Classical / Marxian Baseline (`GOODWIN-1967`)** | Fixed at full capacity ($u = 1$) | Dynamic state ($\dot{\omega} = \omega(\hat{w}(e) - \alpha)$) | Say's Law: Saving drives investment ($I \equiv S(\omega)$) | Dynamic state ($\dot{e} = e(g_K(\omega) - g_n)$) | Investment $I$ adjusts passively to available profit saving $S$. |
| **Kaldor–Pasinetti (Cambridge Growth)** | Fixed at full/normal capacity ($u = 1$) | Endogenous adjusting variable ($\omega^*$) | Independent investment $g_K = \bar{g}$ drives saving | Often full employment ($g_K = g_n$) or reserve army | Income distribution $\omega$ (via price markup relative to money wages) adjusts so $s_\pi(1-\omega) = \sigma \bar{g}$. |
| **Canonical Kaleckian / Post-Keynesian** | Endogenous adjusting variable ($u^*$) | Exogenous/institutional markup ($\omega = \bar{\omega}$) or dynamic conflict state | Independent investment $g_K(u, \pi)$ drives saving $g_S(u, \pi)$ | Residual ($e$ follows $u$ and $K/N$) | Capacity utilization $u$ adjusts via the goods-market multiplier ($I(u) = S(u)$). |
| **Sraffian Supermultiplier (SSM)** | Short-run endogenous ($u$); long-run gravitates to exogenous $u_n$ | Exogenous/institutional ($\omega = \bar{\omega}$) | Induced investment $I = h Y$ ($\dot{h} = h \gamma (u - u_n)$) + autonomous demand $Z$ | Residual unless labor constraints added | Short run: $u$ adjusts; Long run: investment share $h^*$ adjusts so $\hat{Y}^* = \hat{K}^* = g_Z$ at $u^* = u_n$. |
| **Thirlwall / Structuralist BOP-Constrained** | Endogenous (below full capacity) | Institutional or terms-of-trade linked | Constrained by foreign-exchange availability | Residual (structural underemployment) | Domestic output growth $\hat{Y}$ adjusts to maintain current-account / capital-flow balance ($\hat{Y}_{BOP} = \frac{\varepsilon \hat{Y}^*}{\pi_M}$). |

---

## 11. GOODWIN VALIDATION SUMMARY

Wave D3-A validated the candidate Goodwin knowledge input and produced the standalone candidate artifact [`docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md`](file:///c:/ReposGitHub/academic-research-skills/docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md).

### 11.1 Summary of Source-Disciplined Validation Findings (Items A–P)
1. **Strict Separation of `GOODWIN-1967` from `LATER GOODWIN LITERATURE`:**
   - **Original Notation vs. Modern Convention:** Original `GOODWIN-1967` (pp. 54–58) denotes the workers' share of product by $u$ and the employment ratio by $v$. Modern heterodox literature (`LATER GOODWIN LITERATURE`) standardizes on $(\omega, e)$ to prevent collision with capacity utilization $u$. This is documented explicitly in the candidate artifact's Local Notation Lock.
   - **Depreciation $\delta$:** Original `GOODWIN-1967` defines output $q$ and capital $k$ in real net terms (implicitly $\delta = 0$), yielding $\hat{k} = (1-\omega)/\sigma$ and stationary wage share $\omega^* = 1 - \sigma(\alpha + \beta)$. Including explicit depreciation $\delta > 0$ ($\hat{k} = \frac{1-\omega}{\sigma} - \delta$ and $\omega^* = 1 - \sigma(\alpha + \beta + \delta)$) is a textbook generalization from `LATER GOODWIN LITERATURE`. Both are presented transparently without retroactive attribution.
   - **Real vs. Nominal Phillips Relation:** Original `GOODWIN-1967` specifies the wage curve directly in **real** terms ($\dot{w}/w = f(e) \approx -\gamma + \rho e$). Separating nominal wage bargaining from price inflation belongs to `LATER GOODWIN LITERATURE` (e.g., Desai 1973).
2. **Mathematical Verification of the 2D System:**
   - Reduced system: $\dot{e} = e\left[\frac{1-\omega}{\sigma} - (\alpha + \beta + \delta)\right]$ and $\dot{\omega} = \omega\left[-(\alpha + \gamma) + \rho e\right]$.
   - Unique interior equilibrium: $(e^*, \omega^*) = \left(\frac{\alpha+\gamma}{\rho}, 1 - \sigma(\alpha+\beta+\delta)\right)$, admissible on $(0,1)^2$ iff $0 < \alpha + \gamma < \rho$ and $0 < \alpha + \beta + \delta < 1/\sigma$.
   - Jacobian at $(e^*, \omega^*)$: $J^* = \begin{bmatrix} 0 & -e^*/\sigma \\ \rho\omega^* & 0 \end{bmatrix}$, with $\operatorname{tr}(J^*) = 0$ and $\det(J^*) = \frac{\rho}{\sigma}e^*\omega^* > 0$, giving purely imaginary eigenvalues $\lambda = \pm i \sqrt{\frac{\rho}{\sigma}e^*\omega^*}$.
   - Global nonlinear proof: Because $\operatorname{tr}(J^*) = 0$ is non-hyperbolic, local eigenvalues alone cannot prove closed orbits. The proof rests on the separable Lotka–Volterra structure and closed-form first integral $V(e, \omega) = \frac{1}{\sigma}(\omega^* \ln \omega - \omega) + \rho(e^* \ln e - e) = C_0$, establishing a **conservative nonlinear center** (a continuum of initial-condition-dependent closed orbits), which is structurally unstable and mathematically distinct from an isolated dissipative **limit cycle**.
3. **Goodwin Terminology Guardrail (`ARS ANALYTICAL SYNTHESIS`):**
   - `GOODWIN BASELINE`: The exact 1967 2D conservative closure.
   - `GOODWIN-FAMILY MODEL`: Retains the core accumulation–employment–distribution loop while modifying closures or adding states (e.g., Goodwin–Minsky 3D $(e, \omega, d)$ or induced technical change).
   - `GOODWIN-INSPIRED MODEL`: Borrows selected state variables or distributive concepts within a materially different causal architecture (e.g., Kaleckian demand-led models or Sraffian Supermultiplier models).

---

## 12. GOODWIN-SPECIFIC VS. GENERALIZABLE LESSONS

To ensure Goodwin (1967) serves as a pedagogical exemplar without becoming the ontology of `heterodox-macro-modeling`, every candidate rule extracted from the Goodwin validation is classified below across the five required scope tiers:
- `LOCAL TO GOODWIN`
- `MODEL-FAMILY LEVEL`
- `HETERODOX-MACRO DOMAIN PRINCIPLE`
- `CROSS-DOMAIN PRINCIPLE`
- `NOT SUPPORTED`

| Candidate Rule / Property | Scope Classification | Architectural Rationale & Handling in D3 |
|:---|:---|:---|
| **Exact state vector $\mathbf{x} = (e, \omega)$** | `MODEL-FAMILY LEVEL` (Goodwin baseline & 2D Goodwin-family models) | Many heterodox models have no $e$ state (Kaleckian/SSM) or no $\omega$ state (fixed-markup models). Must **never** be required outside Goodwin-family models. |
| **Notation lock $(e, \omega, a, w, q, k, \sigma, \alpha, \beta, \gamma, \rho)$** | `LOCAL TO GOODWIN` | Locked solely inside `goodwin_baseline.md`. General models define their own symbol tables (§5.2). |
| **Say's Law full-capacity profit-driven accumulation ($\hat{k} = (1-\omega)/\sigma$)** | `LOCAL TO GOODWIN` / Classical full-capacity baseline | Directly rejected by Kaleckian, Post-Keynesian, Harrodian, and Sraffian demand-led closures. |
| **Zero Jacobian trace ($\operatorname{tr} J^* = 0$) and separable Lotka–Volterra first integral $V(e,\omega) = C_0$** | `LOCAL TO GOODWIN` | Arises from the knife-edge absence of diagonal self-feedback ($\partial \dot{e}/\partial e = 0, \partial \dot{\omega}/\partial \omega = 0$). Vanishes as soon as utilization, debt, or induced technical change is added. |
| **Predator-prey profit-squeeze feedback ($J_{12} < 0, J_{21} > 0$)** | `MODEL-FAMILY LEVEL` | Shared across Goodwin-family and profit-led Kaleckian–Goodwin syntheses, but reversed or modified in wage-led Kaleckian models. |
| **Logarithmic differentiation of intensive ratios ($\widehat{X/Y} = \hat{X} - \hat{Y}$)** | `HETERODOX-MACRO DOMAIN PRINCIPLE` | Universal mathematical law for reducing extensive growth systems to intensive state variables across all macro traditions. |
| **Traceability of every reduced-form ODE to primitives (`ID`, `TECH`, `BEH`, `INST`, `CLOS`, `EXOG`)** | `HETERODOX-MACRO DOMAIN PRINCIPLE` | Universal modeling audit standard preventing hidden assumptions and specification tautologies. |
| **Explicit interior admissibility gate ($\mathbf{x}^* \in \operatorname{int}(\Omega)$) before stability analysis** | `HETERODOX-MACRO DOMAIN PRINCIPLE` | Universal dynamical-systems requirement: parameter inequalities ensuring economically meaningful shares/ratios must be proved explicitly. |
| **Non-hyperbolic escalation rule ($\operatorname{tr} J^* = 0$ or $\det J^* = 0 \implies$ nonlinear analysis required)** | `HETERODOX-MACRO DOMAIN PRINCIPLE` | Universal dynamical-systems theorem (Hartman–Grobman boundary): linear eigenvalues cannot classify a center vs. nonlinear spiral. |
| **Strict distinction between conservative closed orbits (center) and dissipative limit cycles** | `HETERODOX-MACRO DOMAIN PRINCIPLE` | Prevents widespread mathematical confusion across all oscillatory macro models. |
| **8-Step Model Extension Re-Derivation Protocol (changing one equation changes multiple feedbacks)** | `HETERODOX-MACRO DOMAIN PRINCIPLE` | Universal safeguard when extending any formal macroeconomic model (§21). |
| **Source provenance discipline (`PRIMARY SOURCE` vs. `LATER LITERATURE` vs. `ARS SYNTHESIS`)** | `CROSS-DOMAIN PRINCIPLE` | Applies across all theoretical and historical domain skills to prevent retroactive attribution. |
| **Every heterodox macro model must exhibit endogenous cycles around a natural growth rate** | `NOT SUPPORTED` | Rejected: many heterodox models exhibit steady-state convergence, saddle-path instability, cumulative causation, or hysteresis rather than cycles. |

---

## 13. HETERODOX TRADITION BOUNDARY MAP

Heterodox macroeconomics is **not** a single unified theory; it is a pluralist ecosystem of distinct research traditions with different ontologies, closures, and focal mechanisms. In accordance with Prompt §11, the table below maps all ten traditions across five analytical relationship categories:
- `GENEALOGICAL CONNECTION`: Shared intellectual lineage in classical political economy or effective-demand critiques of Walrasian/neoclassical orthodoxy.
- `FORMAL SIMILARITY`: Use of shared mathematical machinery (intensive differential equations, accounting matrices, input-output or class-income decompositions).
- `CLOSURE DIFFERENCE`: Incompatible or contrasting choices of which variables are exogenous, endogenous, or adjusting in the 14-question closure audit.
- `LATER SYNTHESIS`: Hybrid models documented in post-1980 literature that combine mechanisms from two or more traditions.
- `MODEL FAMILY WITH DISTINCT ONTOLOGY`: Core conceptual commitments that cannot be reduced to parameter special cases of another tradition.

| Tradition | Core Ontology & Focal Variables (`MODEL FAMILY WITH DISTINCT ONTOLOGY`) | `CLOSURE DIFFERENCE` | `GENEALOGICAL CONNECTION` & `FORMAL SIMILARITY` | Major `LATER SYNTHESIS` Bridges |
|:---|:---|:---|:---|:---|
| **1. Marxian** | Exploitation/surplus value, class conflict over wage share $\omega$ and working day/intensity, reserve army of labor $e$, organic composition / capital productivity $\sigma$, profit rate $r = (1-\omega)/\sigma$ driving capital accumulation. | Accumulation is fundamentally profitability-driven ($g_K = f(r)$); output is typically capacity-constrained in the long run rather than purely demand-determined; technical change is labor-saving / capital-using (Marx-biased). | Shares surplus approach with Classical/Sraffian; `GOODWIN-1967` formalizes Marx's *Capital* Vol. I Ch. 25 reserve-army cycle via Lotka–Volterra ODEs. | Marxian–Kaleckian syntheses (Marglin & Bhaduri 1990; Barbosa-Filho & Taylor 2006) adding utilization $u$; Foley–Michl induced technical change models. |
| **2. Classical / Sraffian** | Production of commodities by means of commodities; physical reproduction and social surplus; prices of production equalizing profit rates across sectors; separation of distribution, output levels, and relative prices. | Treats one distributive variable ($w$ or $r$) as exogenous/institutionally determined outside the price system; long-run utilization must gravitate to normal capacity ($u^* = u_n$). | Genealogical root of both Marxian and modern surplus-approach macro; linear input-output algebra ($\mathbf{p} = (1+r)\mathbf{p}\mathbf{A} + w\mathbf{l}$) and Pasinetti vertically integrated sectors. | Sraffian Supermultiplier (Serrano 1995; Cesaratto et al. 2003; Freitas & Serrano 2015) coupling classical normal utilization with Keynesian autonomous demand growth $g_Z$. |
| **3. Kaleckian / Post-Keynesian** | Principle of effective demand in both short and long run; oligopolistic mark-up pricing ($\omega = 1/(1+\tau)$); underutilized productive capacity ($u < 1$) as the normal state of monetary production economies. | Investment is independent of prior saving; capacity utilization $u$ is an **endogenous adjusting variable** in both short and long run ($u^* \neq u_n$); growth can be **wage-led** ($\partial u^*/\partial \omega > 0, \partial g^*/\partial \omega > 0$) or **profit-led** (Bhaduri–Marglin). | Genealogical roots in Kalecki (1939, 1954), Robinson (1956, 1962), Steindl (1952); shares class-saving differential ($s_w < s_\pi$) with Classical/Kaldorian models. | Kaleckian–Goodwin conflict cycles (endogenizing $\dot{\omega}$ alongside $\dot{u}$); Post-Keynesian SFC models (Godley & Lavoie 2007). |
| **4. Harrodian** | Dual role of investment (demand generation vs. capacity creation) and knife-edge instability of the warranted growth path ($g_w = s/\nu_n$) when entrepreneurs react behaviorally to utilization gaps ($u - u_n$). | Normal utilization $u_n$ is a structural target; deviations $u \neq u_n$ trigger cumulative investment acceleration ($\dot{g}_K = \phi(u - u_n)$ with $\phi > 0$), rendering the warranted path locally unstable (**Harrodian instability**). | Originates in Harrod (1939); shares effective-demand foundation with Keynes/Kalecki but rejects permanent passive departure of $u^*$ from $u_n$. | Shaikh (2009, 2016) classical-Harrodian adjustment via retention ratio; Skott (1989, 2010) Kaldorian–Harrodian labor-market cycles; SSM taming via autonomous demand $Z$ when $\gamma$ is sufficiently small. |
| **5. Kaldorian / Verdoorn** | Cumulative causation, dynamic increasing returns to scale in manufacturing, endogenous productivity growth driven by output expansion (**Kaldor–Verdoorn Law**: $\hat{a} = a_0 + \eta \hat{Y}, \eta \in (0,1)$), and export-led growth. | Technical progress $\hat{a}$ is **endogenous to demand growth** rather than exogenous ($\alpha$); in Kaldor (1956)/Pasinetti (1962) early closures, full employment holds and distribution $\omega$ adjusts to equate $S = I$, whereas later Kaldor (1966, 1970) is demand- and export-led. | Formal similarity in linear growth-rate feedback loops; connects technological change directly to effective demand and trade competitiveness. | Kaldor–Goodwin models (endogenizing $\hat{a} = a_0 + \eta \hat{q}$ in the Goodwin cycle); Thirlwall–Kaldor BOP-constrained cumulative causation (Dixon & Thirlwall 1975). |
| **6. Minskyan** | Financial instability hypothesis: endogenous evolution of balance sheets from **hedge** to **speculative** to **Ponzi** finance during tranquil booms; endogenous money, asset-price valuation ratios ($p_K/p_Y$), leverage, and debt-deflation crises. | Rejects neutral finance and pure internal profit financing ($I = \Pi$); investment exceeds retained profits via debt creation ($\dot{D} = I - \Pi_{\text{ret}}$), making debt-to-income $d$ or interest coverage a core state variable. | Rooted in Keynes's Ch. 12/17 and Kalecki's principle of increasing risk; formally expressed through nonlinear coupled ODEs (3D+ state spaces) or SFC balance sheets. | Keen (1995) and Grasselli & Costa Lima (2012) 3D Goodwin–Minsky $(e, \omega, d)$ models; Taylor & O'Connell (1985); Nikolarea/Nikiforos/Dafermos Minsky–SFC models. |
| **7. Institutional / Regulationist** | Historically contingent regimes of accumulation and modes of regulation (wage-labor nexus, monetary regime, competition form, state form, international insertion) that temporarily stabilize macroeconomic contradictions. | Parameters and functional forms (e.g., wage indexation to productivity, credit elasticity) are **regime-specific constants** that hold within an era (e.g., Fordism) and break down during structural crises. | Genealogical bridge between Marxian/Kaleckian macro and comparative-historical political economy (Boyer 1988; Aglietta 1979; SSA school: Gordon, Edwards, Reich). | Formal Regulationist growth models (Boyer 1988) mapping wage-formation regimes against productivity regimes; direct interface to `political-economy-research` (§19). |
| **8. Structuralist / Center–Periphery** | Asymmetric global division of labor, productive heterogeneity, Prebisch–Singer terms-of-trade deterioration, structural inflation, foreign-exchange bottlenecks, and international currency hierarchy. | Domestic accumulation and utilization are bounded or closed by the **external balance / FX constraint** ($\hat{Y} \le \hat{Y}_{BOP}$) and external debt dynamics, with exchange-rate depreciation redistributing income away from wages (Díaz-Alejandro contractionary devaluation). | Rooted in ECLAC/CEPAL (Prebisch, Furtado, Sunkel, Noyola) and Taylor (1983, 1991) structuralist macroeconomics; formal similarity in multi-sector/two-country accounting matrices. | North–South uneven development models (Dutt 1990; Cimoli & Porcile 2014); BOP-constrained Goodwin/Kaleckian open-economy models (Blecker 1989; Vera 2006). |
| **9. Ecological / Biophysical** | Economy embedded in a finite biosphere; thermodynamic laws (energy/material throughput, entropy), natural capital depletion, carbon/ecological debt stocks, and planetary boundaries limiting material growth. | Adds physical stock-flow identities (materials balance, atmospheric carbon concentration $\dot{C}_{atm} = E(Y) - \delta_C C_{atm}$) and damage/abatement feedbacks or degrowth/post-growth steady-state constraints ($\hat{Y} = 0$). | Connects classical physical reproduction (Quesnay/Sraffa) and Georgescu-Roegen bioeconomics with dynamical systems and SFC accounting. | Ecological SFC models (Dafermos, Nikolaidi, & Galanis 2017; Jackson & Victor 2016) and Ecological Goodwin–Keen models (Rezai, Taylor, & Mechler 2013). |
| **10. Stock-Flow Consistent (SFC)** | Double-entry quadruple accounting across institutional sectors (households, firms, banks, central bank, government, rest of world); every financial asset has a counterpart liability; no black holes between flows and stocks. | Requires explicit **accounting closure** in every sector's budget constraint and portfolio matrix (Tobin Brainard-Tobin adding-up conditions; one buffer-stock asset per sector, and one redundant system-wide identity dropped by Walras's Law analogue). | Synthesizes Godley (Cripps & Godley 1976; Godley & Lavoie 2007), Tobin (1969), and Post-Keynesian endogenous money; serves as an accounting discipline usable across multiple heterodox closures. | Kaleckian–SFC, Minskyan–SFC, Sraffian–SFC, Open-Economy Currency-Hierarchy SFC, and Ecological SFC models. |

---

## 14. DEMAND-LED MODELING INTERFACE

To handle demand-led growth models rigorously without taking doctrinal sides in the Kaleckian vs. Harrodian vs. Sraffian Supermultiplier debates (resolving Contamination Items M-R06, M-R08, and M-R09), `heterodox-macro-modeling` enforces the following analytical interface:

1. **Short-Run Goods-Market Equilibrium & Keynesian Stability Condition:**
   - When capacity utilization $u \equiv Y / Y^p$ (or $u \equiv Y / K$) adjusts to clear the goods market $g_I(u, \pi, \dots) = g_S(u, \pi, \dots)$, the model must explicitly check the **Keynesian stability condition**:
     $$\frac{\partial g_S}{\partial u} - \frac{\partial g_I}{\partial u} > 0$$
     *(Marginal propensity to save out of utilization exceeds marginal propensity to invest out of utilization).*
   - If the Keynesian stability condition fails ($\partial g_I/\partial u > \partial g_S/\partial u$), short-run multiplier adjustment is unstable unless bounded by nonlinearities or embedded in a higher-dimensional dynamical system.
2. **Wage-Led vs. Profit-Led Regimes (Bhaduri–Marglin Decomposition):**
   - Distinguish clearly between:
     - **Demand regime ($\partial u^* / \partial \omega$):** Whether a higher wage share expands or contracts equilibrium capacity utilization (depending on whether differential consumption $(s_\pi - s_w)u$ outweighs profit-Margin sensitivity of investment $\partial g_I / \partial \pi$).
     - **Accumulation / Growth regime ($\partial g_K^* / \partial \omega$):** Even in a wage-led *demand* regime ($\partial u^*/\partial \omega > 0$), capital accumulation $g_K^*$ can be either wage-led or **conflictual/profit-led** if the direct negative profit-share effect on investment outweighs the positive utilization effect.
3. **Harrodian Instability vs. Normal Utilization ($u_n$) Debates:**
   - **Definition:** Harrodian instability is a **behavioral/expectational feedback** wherein firms adjust their desired accumulation rate or investment share $h \equiv I/Y$ in response to deviations of actual utilization $u$ from normal/desired utilization $u_n$ (e.g., $\dot{h} = h \gamma_h (u - u_n)$ with $\gamma_h > 0$).
   - **Pluralist Analytical Treatment:** When a model includes $u$ and $u_n$, the skill must identify which of the four literature closures the author is employing and verify its exact stability conditions:
     1. *Canonical Kaleckian:* $u^*$ remains endogenous in the long run ($u^* \neq u_n$), or $u_n$ adapts endogenously towards $u^*$ ($\dot{u}_n = \xi(u - u_n)$, Lavoie 1995/Nikiforos).
     2. *Harrodian / Classical-Harrodian (Skott / Shaikh):* $u \to u_n$ via labor-market discipline, financial/retention-rate adjustments, or limit cycles around $u_n$.
     3. *Sraffian Supermultiplier (Serrano / Freitas):* Autonomous non-capacity-creating demand $Z$ grows at $\hat{Z} = g_Z$; intensive state $\gamma_Z \equiv Z/K$ evolves alongside $h \equiv I/Y$; local asymptotic stability around $(u^* = u_n, h^*)$ holds if and only if the reaction parameter $\gamma_h$ satisfies the upper bound (the "taming of Harrodian instability" condition $\operatorname{tr} J^* < 0, \det J^* > 0$).
     4. *Marxian / Goodwin Full-Capacity Baseline:* $u$ is fixed at $1$ by Say's Law closure.
   - **Neutrality Rule:** The skill **never** forces a Kaleckian model to adopt a Supermultiplier closure, nor forces a Supermultiplier model to adopt a Kaleckian closure. It audits the mathematical stability and economic assumptions of whichever closure is under analysis.

---

## 15. DISTRIBUTION / ACCUMULATION INTERFACE

1. **Exact Profit-Rate Decomposition Identity:**
   In any model with variable capacity utilization $u \equiv Y / Y^p$ and potential output-to-capital ratio $1/\sigma_{\text{cap}} \equiv Y^p / K$, the rate of profit $r \equiv \Pi / K$ must be decomposed via the three-factor identity:
   $$r \equiv \frac{\Pi}{Y} \cdot \frac{Y}{Y^p} \cdot \frac{Y^p}{K} = \frac{(1 - \omega) u}{\sigma_{\text{cap}}}$$
   - Taking logarithmic derivatives yields the exact dynamic relation:
     $$\hat{r} = \widehat{(1 - \omega)} + \hat{u} - \hat{\sigma}_{\text{cap}} = -\frac{\omega}{1 - \omega}\hat{\omega} + \hat{u} - \hat{\sigma}_{\text{cap}}$$
   - Setting $u \equiv 1$ and $\hat{\sigma}_{\text{cap}} \equiv 0$ recovers the `GOODWIN-1967` special case $r = (1-\omega)/\sigma$.
2. **Distributional Dynamics & Conflict Inflation:**
   - When wages and prices are set in nominal terms, $\omega = W / (P a) \implies \hat{\omega} = \hat{W} - \hat{P} - \hat{a}$.
   - If workers bargain for nominal wage growth $\hat{W} = \Omega_w(\omega_w^T - \omega) + \eta_w \hat{P}^e + \phi_w \hat{a}$ based on a target wage share $\omega_w^T(e)$ and firms set price inflation $\hat{P} = \Omega_p(\omega - \omega_f^T(u)) + \eta_p \hat{W}$ based on a target profit share $1 - \omega_f^T$, the audit must derive both the resulting inflation rate $\hat{P}$ and the real distributional law of motion $\dot{\omega}$ from the underlying nominal equations rather than asserting $\dot{\omega}$ ad hoc.
3. **Class-Saving & Wealth Distribution (Pasinetti vs. Anti-Pasinetti):**
   - Whenever worker saving is positive ($s_w > 0$), accounting consistency requires tracking whether workers accumulate earning assets/capital $K_w$ (generating rental/interest income flows to worker households) or whether worker saving is absorbed solely into non-interest money/consumption loans. Assuming $s_w > 0$ while ignoring worker asset accumulation over the long run is flagged as a **stock-flow omission** unless explicitly scoped to a short-run horizon where stocks are fixed.

---

## 16. TECHNICAL-CHANGE INTERFACE

Technical change enters heterodox macro models through labor productivity $a \equiv Y/L$ and potential capital productivity $1/\sigma_{\text{cap}} \equiv Y^p/K$. `heterodox-macro-modeling` supports both exogenous and endogenous specifications:

1. **Classification of Technical Change Forms:**
   - **Harrod-Neutral (Purely Labor-Augmenting):** $\hat{a} > 0$, $\hat{\sigma}_{\text{cap}} = 0$. Required for a stationary wage share $\omega^*$ and stationary profit rate $r^*$ along a constant-utilization balanced growth path.
   - **Marx-Biased (Labor-Saving, Capital-Using):** $\hat{a} > 0$ and $\hat{\sigma}_{\text{cap}} > 0$ (rising technical/organic composition of capital). Under constant $\omega$ and $u$, this drives a falling maximum rate of profit $r_{\max} = 1/\sigma_{\text{cap}} \downarrow$, preventing a stationary interior steady state unless offset by counteracting tendencies or asymptotic stabilization of $\sigma_{\text{cap}}$.
   - **Solow-Neutral (Capital-Augmenting) / Hicks-Neutral.**
2. **Endogenous Technical Change Closures:**
   - **Kaldor–Verdoorn Dynamic Scale Effect:** $\hat{a} = \alpha_0 + \eta \hat{Y}$ (with Verdoorn coefficient $\eta \in (0, 1)$). Couples productivity growth directly to demand/accumulation growth.
   - **Marx–Hicks / Kennedy–Weizsäcker Induced Bias:** Firms choose or innovate along a technical-change frontier $(\hat{a}, -\hat{\sigma}_{\text{cap}})$ to maximize the rate of change of the profit rate $\hat{r}$, making $\hat{a} = \phi(\omega)$ with $\phi'(\omega) > 0$ (rising labor costs induce faster mechanization).
   - **Labor-Market Tightness Effect:** $\hat{a} = \alpha(e)$ with $\alpha'(e) > 0$ or $< 0$ (reserve-army discipline vs. labor-shortage induced automation).
3. **Stabilizing Feedback of Induced Technical Change:**
   - As proved in the Goodwin validation (`Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` §4.P), replacing exogenous $\hat{a} = \alpha$ with $\hat{a} = \phi(\omega)$ ($\phi'(\omega) > 0$) introduces a negative diagonal entry $J_{22}^* = -\omega^* \phi'(\omega^*) < 0$ into the Jacobian, shifting $\operatorname{tr}(J^*)$ from $0$ to $< 0$ and converting a conservative center into an asymptotically stable focus.

---

## 17. SFC / ACCOUNTING INTERFACE

In accordance with Prompt §12 and D1-LOCK-04, `heterodox-macro-modeling` treats **Stock-Flow Consistency (SFC)** not as "adding debt as one state variable," but as a comprehensive double-entry accounting architecture.

### 17.1 Core SFC Analytical Requirements Owned by `heterodox-macro-modeling`

Whenever a model includes financial assets, liabilities, money, government deficits, or sectoral balance sheets, the skill requires auditing six structural layers:

1. **Balance-Sheet Matrix (Stocks at Instant/End of Period $t$):**
   - Columns represent institutional sectors (e.g., Worker Households, Capitalist Households, Production Firms, Commercial Banks, Central Bank, Government, Rest of World).
   - Rows represent tangible capital ($+K$) and financial assets ($+$) / liabilities ($-$) (e.g., deposits $+M$, loans $-L$, government bills $+B_h / -B_g$, equities $+E_h / -E_f$, foreign reserves).
   - **Horizontal Financial Zero-Sum Law:** Every financial asset row must sum identically to zero across all sectors ($\sum_j A_{ij} \equiv 0$). Tangible capital plus net financial worth equals sectoral net worth ($NW_j$), and aggregate net worth equals tangible capital ($\sum_j NW_j \equiv K$).
2. **Transaction-Flow Matrix (Current & Capital Account Flows over Period $t$):**
   - **Row Consistency:** Every transaction row (wages, consumption, investment, taxes, interest payments $i_{t-1} B_{t-1}$, dividends, net lending, and flow-of-funds asset changes $\Delta M, \Delta L, \Delta B$) must sum identically to zero across columns ($\sum_j F_{kj} \equiv 0$).
   - **Column Consistency (Sectoral Budget Constraints):** Every sector column must sum identically to zero (Current Saving $-$ Physical Investment $\equiv$ Net Financial Lending $\equiv \sum_i \Delta \text{Assets}_i - \sum_i \Delta \text{Liabilities}_i$).
3. **Sectoral Financial Balances Identity (Godley Fundamental Identity):**
   - In any three-sector open economy (Private Domestic $S - I$, Government $T - G$, External Current Account $NX + NFI = CAB$):
     $$(S - I) + (T - G) - CAB \equiv 0 \iff (S - I) \equiv (G - T) + CAB$$
   - No model may postulate simultaneous trajectories for private net saving, fiscal deficits, and current-account balances that violate this identity.
4. **Flow-Stock Reconciliation & Revaluation Matrix:**
   - Every stock $S_{ij}(t)$ must evolve according to the exact reconciliation law:
     $$S_{ij}(t) = S_{ij}(t-1) + \text{Net Transaction Flow}_{ij}(t) - \text{Depreciation/Default}_{ij}(t) + \text{Capital Gains Revaluation}_{ij}(t)$$
     (or in continuous time: $\dot{S}_{ij} = F_{ij} - \delta S_{ij} + \dot{p}_i Q_{ij}$).
5. **Portfolio Adding-Up Conditions (Brainard–Tobin Conditions):**
   - When a sector allocates wealth $V_h$ across $K$ assets via portfolio shares $\mathbf{\lambda}_h = \boldsymbol{\lambda}_0 + \boldsymbol{\Lambda} \mathbf{r}_a + \boldsymbol{\gamma}(Y_h/V_h)$, parameters must satisfy vertical adding-up ($\sum_k \lambda_{0k} = 1$) and horizontal symmetry/zero-sum across return sensitivities ($\sum_k \lambda_{kj} = 0$ for each $j$, $\sum_k \gamma_k = 0$).
6. **Accounting Closure & Redundant Equation Verification (Walras's Law Analogue):**
   - Each sector's budget constraint requires designating **one buffer-stock asset or liability** (e.g., household bank deposits $M_h$, firm bank loans $L_f$, central bank advances $A_{cb}$) determined residually by its budget identity rather than by an independent demand equation.
   - Because all rows and columns of the Transaction-Flow Matrix sum to zero, **one system-wide accounting identity is mathematically redundant** (implied by all the others). In a complete SFC model, one equation (typically the equality of central bank reserve supply and demand, or equality of aggregate asset holdings and issue) is omitted from estimation/solution and used as the **redundant-equation consistency check** (`A_redundant_LHS - A_redundant_RHS == 0`).

### 17.2 Separation of `SFC ANALYTICAL REASONING` vs. `DETERMINISTIC MATRIX VERIFICATION`

```text
SFC ANALYTICAL REASONING (OWNED BY heterodox-macro-modeling IN WAVE D3):
    Constructing balance-sheet and transaction-flow tables; verifying row/column
    symbolic zero-sum identities; deriving intensive debt/wealth differential
    equations; checking Brainard–Tobin adding-up conditions; identifying buffer
    stocks and the redundant accounting equation.

DETERMINISTIC MATRIX VERIFICATION (FUTURE CANDIDATE TOOL — NOT CREATED IN WAVE D3):
    A deterministic Symbolic/SymPy or numerical script that parses a serialized
    SFC matrix specification and verifies row/column symbolic sums equal zero.
    Per Prompt §12, D1-LOCK-04, and Lesson L1, this is NOT created in D3-A or D3-B
    and may be proposed as a tool in a later wave only if recurrent operational
    need is demonstrated.
```

---

## 18. OPEN-ECONOMY / CENTER–PERIPHERY INTERFACE

`heterodox-macro-modeling` owns the **formal mathematical representation** of open-economy and center–periphery mechanisms:

1. **Balance-of-Payments Constrained Growth (Thirlwall's Law & Extensions):**
   - Starting from the trade balance $P_d X = E P_f M$ (or with capital flows $P_d X + F = E P_f M$) and isoelastic export/import functions $X = (E P_f / P_d)^{\eta_X} (Y^*)^{\varepsilon_X}$, $M = (P_d / (E P_f))^{\eta_M} Y^{\pi_M}$:
   - Under constant real exchange rate ($\hat{q}_{rer} = \hat{E} + \hat{P}_f - \hat{P}_d = 0$) and balanced trade, derive Thirlwall's baseline growth rate:
     $$\hat{Y}_{BOP} = \frac{\varepsilon_X \hat{Y}^*}{\pi_M} = \frac{\hat{X}}{\pi_M}$$
   - Under sustainable external debt-to-GDP stabilization (Moreno-Brid 1998/2003; Barbosa-Filho 2001), incorporate net foreign interest payments $i^* D_{ext}$ and sustainable current-account deficit ratios.
2. **Structuralist Center–Periphery (North–South) Formal Models:**
   - Coupled two-region dynamical systems where the **Center (North)** operates under a Kaleckian, Goodwin, or Kaldorian closure with endogenous innovation ($\varepsilon_X^N > \varepsilon_X^S$), while the **Periphery (South)** faces a structural BOP or capital-goods import constraint ($\pi_M^S > \pi_M^N$), terms-of-trade dynamics ($\hat{p}_{tot} = \hat{P}_S - \hat{P}_N$), or Lewis-type dual labor markets.
3. **Real Exchange Rate, Distribution, and Contractionary Devaluation (Krugman–Taylor / Blecker):**
   - Formalizing the link between the real exchange rate $q_{rer} = E P^* / P$, imported intermediate input costs, the domestic price markup, and the real wage share $\omega = \omega(q_{rer})$ with $\partial \omega / \partial q_{rer} < 0$.
   - Auditing whether currency depreciation is **expansionary** (Marshall–Lerner export/import substitution dominates) or **contractionary** (redistributive shift from high-propensity-to-consume wages to profits/foreign costs reduces aggregate demand more than net exports rise).
4. **International Currency Hierarchy & External Debt Dynamics:**
   - Formalizing uncovered interest parity with an endogenous sovereign/currency risk premium and liquidity premium ($\text{liquidity premium } \rho_N > \rho_S$):
     $$i_S = i_N + \hat{E}^e + \xi(d_{ext}, f_{res}) - (\rho_S - \rho_N)$$
   - Auditing the external debt-to-output differential equation $\dot{d}_{ext} = (i^* + \hat{q}_{rer} - \hat{Y}) d_{ext} - nx(q_{rer}, u, Y^*)$ for debt-trap saddle or unstable thresholds ($i^* + \hat{q}_{rer} > \hat{Y}$).

---

## 19. POLITICAL-ECONOMY INTERFACE (`heterodox-macro-modeling` $\leftrightarrow$ `political-economy-research`)

This section preserves and enforces the ratified **Wave D1 Lock** (`D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md` §10).

### 19.1 Strict Division of Ownership

| Analytical Dimension | `heterodox-macro-modeling` OWNS | `political-economy-research` OWNS |
|:---|:---|:---|
| **Core Object** | Formal mathematical equations, closures, accounting matrices, dynamical systems, and stability proofs. | Comparative-historical research design, periodization, process tracing, actor/coalition analysis, and relational comparison. |
| **Institutions & Regimes** | How an institutional rule is parameterized as a behavioral equation or closure constraint ($\boldsymbol{\theta}$, closure choice). | How that institutional arrangement emerged, persisted, or broke down historically through state, class, and coalition struggles. |
| **Center–Periphery / Dependency** | Formal 2-region North–South models, Thirlwall BOP equations, external debt ODEs, and currency-hierarchy interest-parity wedges. | Historical dependency relations, transnational elite/state negotiations, IMF conditionality episodes, and relational case comparison. |
| **Mechanisms** | Deductive derivation of how variables co-move or cycle *within the formal model* ($\partial \mathbf{x}^*/\partial \boldsymbol{\theta}$, phase lead/lag). | Empirical/archival adjudication of *whether* a hypothesized mechanism actually operated in a historical case (A3/A4/A6). |

### 19.2 Bidirectional Interface Rules (Consistent with D1 §10.2 & §10.3)

- **MI-1 (Model $\neq$ Historical Evidence):** A formal macroeconomic model generates candidate mechanisms, consistency constraints, and observable implications. Showing that a formal model can reproduce a stylized fact establishes **theoretical plausibility / institutional compatibility**, never proof that the mechanism operated historically.
- **MI-2 (Closure Justification Flow):** When an author justifies a model's closure (e.g., wage-led vs. profit-led, fixed peg vs. crawling peg, wage indexation) by appealing to a specific historical period (e.g., US 1948–1973 or Chile 1975–1989), `political-economy-research` owns the historical evidence and periodization (A2/A3); `heterodox-macro-modeling` consumes that justification as an `Institutional Regime` input and owns the formal specification.
- **MI-3 (Observable Implication Export for D1 §10.3):** To satisfy the obligation handed to D3 by D1 §10.3, `heterodox-macro-modeling` exports model-derived implications in a structured summary (equilibrium comparative statics, predicted dynamic phase ordering, and stability boundary conditions) that PE's Mechanism Specification (`A3.implications_by_method`) and Econometrics can directly reference.
- **MI-4 (No Cross-Method Override):** Macro must never embed contested historical interpretations as universal mathematical axioms; PE must never claim a formal model is algebraically or dynamically invalid on purely narrative grounds without an equation-level critique.

---

## 20. ECONOMETRICS INTERFACE (`heterodox-macro-modeling` $\leftrightarrow$ `applied-econometrics-pe`)

This section preserves and enforces the ratified **Wave D2 Lock** (`D2_APPLIED_ECONOMETRICS_BOUNDARY_REFACTOR.md` §0, §11, §18).

### 20.1 The Four-Step Theory-to-Empirics Translation Pipeline

```text
1. THEORETICAL MODEL (Owned by heterodox-macro-modeling)
       Explicit state space, accounting identities, behavioral equations,
       and closure -> Stationary states, Jacobian, stability conditions.
           ↓
2. DERIVED THEORETICAL IMPLICATIONS (Owned by heterodox-macro-modeling)
       - Comparative statics signs: ∂x*/∂θ
       - Dynamic cross-effects / Jacobian signs: J_ij = ∂(dx_i/dt)/∂x_j
       - Phase relationships: e.g., e leads ω by π/2 in a counterclockwise cycle
       - Long-run equilibrium / cointegrating restrictions: F(x*) = 0
           ↓
3. OBSERVABLE MAPPING & IDENTIFICATION REQUIREMENTS (Shared Seam)
       - Mapping latent theoretical constructs (e.g., normal utilization u_n,
         potential output Y^p, profit rate r) to candidate empirical proxies.
       - Specifying what structural restrictions or directional precedence
         hypotheses (H_A vs. H_B) are implied by rival closures.
           ↓
4. EMPIRICAL ADMISSIBILITY, ESTIMATION & VERDICT (Owned by applied-econometrics-pe)
       - Stochastic admissibility screening (ADF/KPSS integration order, I(2) check,
         collinearity screening).
       - Estimator selection, lag-space mapping, Toda–Yamamoto / VECM / ARDL / SVAR
         estimation, small-sample bootstrap, and residual diagnostics.
       - Empirical disposition: supported, contradicted, or non-finding.
```

### 20.2 Hard Epistemic Guardrails on Macro $\to$ Econometrics

1. **No Automatic Estimator Dictation (`NO-AUTO-ESTIMATOR`):**
   `heterodox-macro-modeling` **must never** state that a VAR, VECM, SVAR, Toda–Yamamoto levels VAR, state-space / Kalman filter, nonlinear threshold VAR (TVAR), or time-varying parameter (TVP) model "automatically follows" from a theoretical differential/difference equation system. Those are **candidate empirical strategies** whose validity depends on data frequency, sample size $T$, integration order $I(d)$, cointegration rank, and identification assumptions governed by `applied-econometrics-pe`.
2. **Respecting Empirical Non-Findings (`NO-EPISTEMIC-INVERSION`):**
   If `heterodox-macro-modeling` derives a long-run equilibrium relation (e.g., $\omega^* = 1 - \sigma(\alpha+\beta)$ or a supermultiplier relation between $Y$ and $Z$) and `applied-econometrics-pe` finds **no cointegration** or **statistically insignificant/opposite-signed** effects in the data, the theoretical model **may not** override the empirical verdict or declare that the rejection proves "structural regime switching." Instead, the discrepancy must be reported transparently, motivating either:
   - a formal model extension (e.g., relaxing a closure assumption via §21 and deriving new testable implications), or
   - an independently tested empirical hypothesis in `applied-econometrics-pe`.

---

## 21. MODEL EXTENSION GRAMMAR

When researchers extend a baseline macroeconomic model, a common mathematical error is modifying a single equation in isolation while leaving the stationary states, Jacobian, or accounting identities of the baseline model unchanged.

### 21.1 Fundamental Extension Guard

```text
FUNDAMENTAL EXTENSION INVARIANT:
CHANGING ONE EQUATION DOES NOT NECESSARILY CHANGE ONLY ONE MECHANISM.

In a coupled dynamical system with accounting identities, modifying a single
behavioral, technological, or closure equation alters:
  - the substitution path into every reduced-form state equation;
  - the location and admissibility conditions of the stationary state x*;
  - diagonal and off-diagonal entries of the Jacobian J(x*);
  - the trace, determinant, or Routh–Hurwitz conditions; and
  - potentially the dimension n of the state vector itself.
```

### 21.2 Catalog of the Nine Canonical Extension Operations

| Op ID | Extension Operation | Structural Description | Example Across Heterodox Traditions | Typical Impact on State Space & Dynamics |
|:---|:---|:---|:---|:---|
| **EXT-1** | `REPLACE A CLOSURE` | Swap which variable adjusts to clear an identity while keeping the accounting framework intact. | Replace Goodwin's Say's Law ($I \equiv S, u=1$) with a Kaleckian goods-market multiplier ($I(u,\omega) = S(u,\omega)$ solved for endogenous $u(\omega)$). | Alters the reduced-form accumulation rate $g_K(\omega)$ and can flip $\partial \dot{e}/\partial \omega$ from profit-led ($<0$) to wage-led ($>0$). |
| **EXT-2** | `ENDOGENIZE AN EXOGENOUS PROCESS` | Replace a constant parameter with a behavioral or technological function of existing state variables. | Replace exogenous productivity growth $\hat{a} = \alpha$ with Marx–Hicks induced technical change $\hat{a} = \phi(\omega)$ or Kaldor–Verdoorn $\hat{a} = \alpha_0 + \eta \hat{q}$. | Often preserves state dimension $n$, but adds diagonal feedback $J_{ii}^* \neq 0$, converting a neutral center into a stable or unstable focus. |
| **EXT-3** | `ADD A STATE VARIABLE` | Convert a previously constant ratio or algebraic variable into a dynamic state with its own law of motion $\dot{x}_{n+1}$. | Allow capital-output ratio $\sigma$ to evolve ($\dot{\sigma} = \sigma(\hat{k} - \hat{q})$) or investment share $h$ to evolve ($\dot{h} = h\gamma(u - u_n)$). | Increases state dimension $n \to n+1$; requires upgrading stability analysis from 2D $(\operatorname{tr}, \det)$ to 3D Routh–Hurwitz ($a_1 a_2 - a_3 > 0$). |
| **EXT-4** | `ADD A SECTOR` | Disaggregate a 1-good / 1-sector economy into multiple productive or institutional sectors. | Disaggregate into Marxian Department I (capital goods) and Department II (consumption goods), or tradable vs. non-tradable sectors. | Introduces relative prices ($p_1/p_2$) and intersectoral allocation shares ($L_1/L, K_1/K$) as additional algebraic or dynamic variables. |
| **EXT-5** | `ADD A BALANCE SHEET` | Introduce explicit financial stocks (debt, deposits, bills, equities) and interest/dividend payment flows between sectors. | Extend Goodwin $(e, \omega)$ to Keen (1995) Goodwin–Minsky $(e, \omega, d)$ by financing $I - \Pi_{\text{ret}}$ via bank loans $\dot{D} = I - (\Pi - i D)$. | Requires SFC transaction-flow check; adds debt ratio $d = D/Y$ as state variable; subtracts debt service $i d$ from retained profit share; introduces crisis boundary ($d \to \infty$). |
| **EXT-6** | `ADD AN INSTITUTIONAL NONLINEARITY` | Replace a globally linear behavioral function with a nonlinear function reflecting institutional ceilings, floors, or saturation. | Replace linear Phillips curve $-\gamma + \rho e$ with nonlinear asymptote $\phi(e) = \frac{\rho_0}{(1-e)^2} - \gamma_0$, or nonlinear investment function $I(\pi)$ in Keen. | Preserves state dimension $n$, enforces boundary invariance ($e < 1$), can create multiple equilibria, and enables global limit cycles via Poincaré–Bendixson or Hopf bifurcation. |
| **EXT-7** | `ADD REGIME DEPENDENCE` | Make parameters or closures switch across state thresholds or institutional regimes (piecewise-smooth / Filippov or threshold systems). | Inflation-targeting central bank reaction that switches above an inflation threshold $\pi > \bar{\pi}$, or downward nominal wage rigidity floor. | Partitions phase space $\Omega = \Omega_1 \cup \Omega_2$ across switching manifold $\Sigma$; requires checking stability in each regime and sliding/crossing behavior on $\Sigma$. |
| **EXT-8** | `ADD AN EXTERNAL CONSTRAINT` | Open a closed economy to trade, real exchange rate dynamics, capital flows, and foreign debt/reserve constraints. | Couple domestic accumulation and distribution with a balance-of-payments constraint or endogenous real exchange rate $q_{rer}$. | Links domestic wage share $\omega$ to international competitiveness $q_{rer}$; constrains steady-state growth to $\hat{Y}_{BOP}$ or adds external debt state $d_{ext}$. |
| **EXT-9** | `ADD TECHNICAL CHANGE FEEDBACK` | Couple factor-augmenting rates $(\hat{a}, -\hat{\sigma}_{\text{cap}})$ dynamically to profitability, utilization, or ecological constraints. | Foley–Michl / Duménil–Lévy endogenous technical change trajectory where $\hat{a}$ and $\hat{\sigma}$ respond to $\omega$ and $r$. | Couples distribution and capital productivity; determines whether long-run profit rate $r$ stabilizes or trends downward. |

### 21.3 The Mandatory 8-Step Extension Re-Derivation Protocol

Whenever any extension operation (`EXT-1` through `EXT-9`) is applied to a baseline model, `heterodox-macro-modeling` enforces the following sequential 8-step re-derivation checklist:

```text
STEP 1 — IDENTIFY ALTERED ASSUMPTION:
    State explicitly which baseline assumption (ID, TECH, BEH, INST, CLOS, or EXOG)
    is relaxed or replaced, and write the new primitive equation(s).

STEP 2 — IDENTIFY ALL EQUATIONS AFFECTED:
    Trace the substitution chain through the entire system. Never assume a change
    in one primitive equation affects only one reduced-form state equation.

STEP 3 — IDENTIFY FEEDBACKS ADDED OR REMOVED:
    Determine which partial derivatives ∂(dx_i/dt)/∂x_j are newly created, eliminated,
    or rendered sign-ambiguous (especially diagonal self-feedback terms J_ii).

STEP 4 — UPDATE STATE VECTOR & ADMISSIBILITY DOMAIN IF NECESSARY:
    Declare the new state vector x_new ∈ Ω_new (dimension n_new) and any new
    intensive ratio definitions.

STEP 5 — UPDATE ACCOUNTING & SFC CONSISTENCY:
    Verify that any newly introduced flows (e.g., interest payments, retained earnings,
    net exports, worker savings) have exact counterpart stocks and satisfy sectoral
    budget constraints.

STEP 6 — RE-DERIVE STATIONARY STATES & ADMISSIBILITY BOUNDS:
    Solve F_new(x*) = 0 from scratch. Compare the new equilibrium coordinates x*_new
    and parameter admissibility inequalities against the baseline x*_base.

STEP 7 — RE-ANALYZE LOCAL & GLOBAL STABILITY:
    Recompute the Jacobian J_new(x*_new), trace/determinant or Routh–Hurwitz conditions,
    and determine whether the extension stabilizes, destabilizes, or bifurcates the
    baseline dynamics.

STEP 8 — REASSESS ECONOMIC INTERPRETATION & EMPIRICAL IMPLICATIONS:
    State how the extension changes comparative statics, regime classifications
    (e.g., wage-led vs. profit-led), and testable predictions for downstream work.
```

---

## 22. CANDIDATE LOGICAL MODULE STRUCTURE & ADVERSARIAL ARCHITECTURE TESTS

### 22.1 Evaluation of the Candidate 6-Reference Structure (Prompt §18)

Prompt §18 proposes evaluating the following six-reference candidate structure under the principle `Few strong modules > many shallow modules`:
- `model_architecture.md`
- `closure_analysis.md`
- `dynamic_systems.md`
- `accounting_and_sfc.md`
- `goodwin_baseline.md`
- `extension_design.md`

#### Consolidation Analysis & Module Disposition

| Candidate File | Evaluation of Overlap / Cohesion | D3-A Architectural Decision | Resulting Consolidated Module |
|:---|:---|:---|:---|
| `model_architecture.md` | Defines the 7-part modeling grammar, 6-way equation taxonomy, and equilibrium concepts. | **MERGE** with `closure_analysis.md` | **`M1: references/model_architecture_and_closures.md`**<br>*Rationale:* In heterodox macro, a model's architecture *is* inseparable from its closure. Keeping equation taxonomy, the 14-question closure audit, and the tradition/closure comparison matrix (Classical, Kaleckian, Harrodian, SSM, Kaldorian, Structuralist) in one cohesive reference eliminates circular cross-references. |
| `closure_analysis.md` | Contains the 14-question closure audit, demand-led vs. profit-led closures, and tradition boundary map. | **MERGED into M1** | See above. |
| `dynamic_systems.md` | Owns state-space reduction, admissibility $\Omega$, singularities, nullclines, Jacobians, 2D trace/det, 3D+ Routh–Hurwitz, centers vs. limit cycles, Poincaré–Bendixson, and Hopf bifurcations. | **ACCEPT AS STANDALONE** | **`M2: references/dynamic_systems_and_stability.md`**<br>*Rationale:* Distinct, high-density mathematical reasoning load that applies across all dynamical models regardless of closure. |
| `accounting_and_sfc.md` | Owns stock-flow ratios, Balance-Sheet & Transaction-Flow matrices, Godley sectoral balances, Brainard–Tobin conditions, redundant-equation check, and open-economy/BOP accounting. | **MERGE** with `extension_design.md` | **`M3: references/extensions_and_accounting.md`**<br>*Rationale:* Most complex extensions (`EXT-1` through `EXT-9`: adding debt/balance sheets, adding sectors, adding open-economy BOP constraints, or endogenizing technical change) directly require updating the accounting and SFC matrices (Step 5 of the 8-step extension protocol). Merging SFC/open-economy accounting with the 8-step Extension Grammar yields a single powerhouse reference for model building and expansion. |
| `extension_design.md` | Owns `EXT-1` through `EXT-9` and the 8-step re-derivation protocol. | **MERGED into M3** | See above. |
| `goodwin_baseline.md` | Validated candidate artifact (`Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md`) with Items A–P, source discipline, terminology guardrail, and local notation lock. | **ACCEPT AS EXEMPLAR REFERENCE** | **`M4: references/goodwin_baseline.md`**<br>*Rationale:* Kept strictly as a worked benchmark exemplar showing how M1, M2, and M3 apply to a concrete canonical model, without polluting M1–M3 as the root ontology. |

#### Resulting Target Logical Structure for D3-B (`SKILL.md` + 4 Strong References)

```text
heterodox-economics-review/               (Runtime path in Wave D; renamed to skills/domain/heterodox-macro-modeling/ in Wave F)
├── SKILL.md                              (Canonical Entrypoint: ownership contract, 7-part grammar, 14-question closure audit summary, 8-step extension checklist, PE/Econometrics boundaries, routing pointers to M1–M4)
└── references/
    ├── model_architecture_and_closures.md (M1: 6-way equation taxonomy, notation contract, 14-question closure audit, tradition boundary map, Kaleckian/Harrodian/SSM/Classical/Kaldorian closures)
    ├── dynamic_systems_and_stability.md   (M2: Intensive state reduction, domain Ω & singularity checks, equilibrium concepts, Jacobians, 2D trace/det, 3D+ Routh–Hurwitz, conservative centers vs. limit cycles, Hopf bifurcations)
    ├── extensions_and_accounting.md       (M3: SFC balance-sheet & transaction-flow matrices, Brainard–Tobin & redundant-equation rules, open-economy/BOP/center–periphery formalization, endogenous tech change, and the 9-operation / 8-step Extension Grammar)
    └── goodwin_baseline.md                (M4: Source-validated Goodwin 1967 exemplar promoted from Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md)
```

---

### 22.2 Execution of the 10 Mandatory Adversarial Architecture Tests (Prompt §22)

Prompt §22 mandates testing whether the proposed D3-A architecture handles ten distinct modeling scenarios (`A` through `J`). If the architecture only works naturally for Goodwin-like models, D3-A must be classified as `FAIL`.

| Test ID | Adversarial Scenario | How the Proposed D3-A Architecture Handles the Scenario (State Space, Closure, Modules Invoked) | Verdict |
|:---|:---|:---|:---|
| **Test A** | **Canonical Goodwin two-state model** | Handled via `M1` + `M2` + `M4` (`goodwin_baseline.md`): State vector $\mathbf{x} = (e, \omega) \in (0,1)^2$; Say's Law full-capacity closure ($I \equiv S = (1-\omega)q$); exact derivation of $(e^*, \omega^*)$, admissibility bounds, $\operatorname{tr} J^* = 0, \det J^* > 0$, Lotka–Volterra first integral $V(e,\omega) = C_0$, and conservative center proof. | **PASS** |
| **Test B** | **Kaleckian demand-led model with endogenous utilization** | Handled via `M1` (§10, §14) + `M2`: Employment rate $e$ is **not** a state variable; output is demand-determined; capacity utilization $u = Y/Y^p$ adjusts via short-run goods-market equilibrium $g_I(u, \pi) = g_S(u, \pi)$; `M1` verifies the Keynesian stability condition $\partial g_S/\partial u > \partial g_I/\partial u$ and performs the Bhaduri–Marglin decomposition of wage-led vs. profit-led demand ($\partial u^*/\partial \omega$) and accumulation ($\partial g_K^*/\partial \omega$). | **PASS** |
| **Test C** | **SFC model with debt and sectoral balance sheets** | Handled via `M3` (§17) + `M2`: Constructs the full sectoral Balance-Sheet Matrix and Transaction-Flow Matrix; enforces horizontal/vertical zero-sum identities; tracks flow-stock reconciliation ($\dot{D}_f = I - \Pi_{\text{ret}}$) and debt service ($i D_f$); identifies buffer-stock assets and the redundant system-wide identity; reduces intensive stock-flow ratios (e.g., firm leverage $d_f$, government bond ratio $b_g$) to state equations and audits stability via 2D/3D Routh–Hurwitz. | **PASS** |
| **Test D** | **Kaldor–Verdoorn endogenous productivity model** | Handled via `M1` (§13) + `M3` (§16, `EXT-2`): Replaces exogenous productivity growth $\alpha$ with endogenous dynamic scale equation $\hat{a} = \alpha_0 + \eta \hat{Y}$ ($\eta \in (0,1)$); traces how $\hat{a}(\hat{Y})$ feeds simultaneously into unit labor costs/distribution and employment/competitiveness dynamics; evaluates cumulative causation vs. stability bounds on the Verdoorn coefficient $\eta$. | **PASS** |
| **Test E** | **Center–periphery external-constraint model** | Handled via `M3` (§18, `EXT-8`) + `M1` (§10): Formalizes two-region asymmetry ($\varepsilon_X^N > \varepsilon_X^S, \pi_M^S > \pi_M^N$), Thirlwall's BOP-constrained growth rate $\hat{Y}_{BOP} = \varepsilon_X \hat{Y}^* / \pi_M$, Krugman–Taylor/Blecker real exchange rate distribution link $\omega(q_{rer})$, and external debt / currency-hierarchy dynamics $\dot{d}_{ext}$, while cleanly delegating historical dependency narratives to `political-economy-research` (§19). | **PASS** |
| **Test F** | **Multi-sector accumulation model** | Handled via `M1` (§13) + `M3` (`EXT-4`): Accommodates Marxian two-department reproduction schemes (Department I means of production vs. Department II wage/luxury goods) or Sraffian / structuralist multi-sector models by tracking relative price ratios $p_1/p_2$, sectoral capital allocation shares $k_1 = K_1/K$, and intersectoral market-clearing or profit-rate equalization closures in the 14-question audit. | **PASS** |
| **Test G** | **A model with NO wage-share state variable** | Handled natively via `M1` + `M2`: The architecture imposes **zero requirement** that $\omega$ be a state variable. In a fixed-markup Sraffian Supermultiplier model $\mathbf{x} = (u, \gamma_Z)$ or a pure Minskyan leverage-utilization model $\mathbf{x} = (u, d)$ with constant markup $\bar{\tau}$, $\omega = 1/(1+\bar{\tau})$ is classified in the Q5/Q12 closure audit as an exogenous institutional parameter, and stability is analyzed in $(u, \gamma_Z)$ or $(u, d)$ space. | **PASS** |
| **Test H** | **A purely linear local-stability model** | Handled via `M2` (§8.1 Step 4): For linear autonomous systems $\dot{\mathbf{x}} = A \mathbf{x} + \mathbf{b}$, the Jacobian $J \equiv A$ is constant everywhere; local hyperbolic stability ($\operatorname{tr} A < 0, \det A > 0$ in 2D, or Routh–Hurwitz in $n\text{D}$) is immediately necessary and sufficient for global asymptotic stability without invoking nonlinear center/limit-cycle routines. | **PASS** |
| **Test I** | **A nonlinear model with Hopf bifurcation** | Handled via `M2` (§8.1 Step 5): Tracks how a structural parameter $\mu$ drives a complex conjugate eigenvalue pair across the imaginary axis: in 2D, $\operatorname{tr} J^*(\mu_H) = 0$ with $\det J^*(\mu_H) > 0$ and non-zero crossing speed $\left.\frac{d\operatorname{tr} J^*}{d\mu}\right|_{\mu_H} \neq 0$; in 3D, Routh–Hurwitz boundary $a_1(\mu_H) a_2(\mu_H) - a_3(\mu_H) = 0$ with $a_1, a_2, a_3 > 0$ (Liu criterion); distinguishes supercritical (stable limit cycle born) from subcritical (unstable limit cycle collapsed) Hopf bifurcations. | **PASS** |
| **Test J** | **A model whose empirical implications contradict the preferred theory** | Handled via the Econometrics Interface (§20, inheriting Wave D2 Lock): When a formal model predicts a specific sign (e.g., profit-led accumulation $\partial g_K/\partial \omega < 0$ or long-run cointegration) and `applied-econometrics-pe` reports the opposite sign or a non-finding, `NO CROSS-METHOD OVERRIDE` and `NO-EPISTEMIC-INVERSION` forbid the macro skill from dismissing the empirical result or inventing unverified regime switching. Instead, the skill uses the 14-question Closure Audit (§10) and 8-step Extension Grammar (§21) to diagnose which closure assumption (e.g., Say's Law vs. Kaleckian utilization) was falsified and formulate a testable alternative closure. | **PASS** |

**Overall Adversarial Test Verdict:** **10/10 PASS.** The architecture is genuinely general across heterodox macroeconomic traditions and is free of Goodwin-only ontological bias.

---

## 23. D3-B IMPLEMENTATION PLAN

Wave D3-A performs zero runtime edits. Upon human ratification of this D3-A contract, **Wave D3-B** will execute the bounded live implementation under the following strict specification:

1. **Authorized Live Write Scope for D3-B:**
   - Rewrite `heterodox-economics-review/SKILL.md` (preserving the top-level directory path `heterodox-economics-review/` and frontmatter `name: heterodox-economics-review` per Wave C5 Routing Rule 8 until Wave F physical migration, while updating the capability framing and body to implement `heterodox-macro-modeling`).
   - Create `heterodox-economics-review/references/model_architecture_and_closures.md` (`M1`).
   - Create `heterodox-economics-review/references/dynamic_systems_and_stability.md` (`M2`).
   - Create `heterodox-economics-review/references/extensions_and_accounting.md` (`M3`).
   - Promote `docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` to `heterodox-economics-review/references/goodwin_baseline.md` (`M4`), updating its header from `CANDIDATE` to ratified exemplar reference.
2. **Contamination Remediations to Execute in D3-B (from §2.1):**
   - Remove all peer-review framing ("reviewing heterodox economics papers") and add an explicit delegation pointer to `academic-paper-reviewer` for referee simulation.
   - Remove §4 LaTeX Standards (`amsthm` `\begin{proposition}`, `\begin{proof}`, `align`) and delegate LaTeX/prose conventions to `econ-write`.
   - Generalize §1.1 ($\mu = 1$ singularity) and §2.1 ($\theta \neq 1$ technological tautology) into general domain rules (`Singularity & Boundary Manifold Audit` and `No Specification Tautology Rule`), demoting $\mu = 1$ and $\theta \neq 1$ to clearly labeled illustrative examples.
   - Generalize §3 (Harrodian instability and Serrano/Freitas/Lavoie/Nikiforos debate) into the pluralist `Closure Analysis & Demand-Led Growth Interface` (`M1`).
3. **Strict D3-B Prohibitions:**
   - Do **not** rename or move `heterodox-economics-review/` (reserved for Wave F).
   - Do **not** create any deterministic SFC Python script or tool (D1-LOCK-04).
   - Do **not** modify `ars_registry.yaml` or `ROUTING_AND_PRECEDENCE.md` (reserved for Wave D6).

---

## 24. ADVERSARIAL EVAL DESIGN FOR WAVE D5

To ensure behavioral enforcement of the D3 architecture during Wave D5 (Adversarial Evals), the following seven gold evaluation fixtures are specified (`STATUS: PROPOSED — NOT AUTHORIZED UNTIL WAVE D5`):

| Eval ID | Target Capability / Boundary | Adversarial Prompt Summary | Pass Criteria | Fail Criteria (Anti-Regression Check) |
|:---|:---|:---|:---|:---|
| **D5-MACRO-01** | **Non-Goodwin Demand-Led Closure (Test B & G)** | "Formulate a 2D Kaleckian–Supermultiplier model with capacity utilization $u$ and autonomous demand ratio $\gamma_Z$ under a fixed markup. Derive the steady state and local stability." | Uses state vector $\mathbf{x} = (u, \gamma_Z)$; treats wage share $\omega$ as fixed parameter; checks Keynesian short-run stability and long-run Jacobian $\operatorname{tr} J^* < 0, \det J^* > 0$. | Forces employment rate $e$ or dynamic wage share $\omega$ into the state space, or imposes Goodwin notation/Say's Law. |
| **D5-MACRO-02** | **Center vs. Limit Cycle Distinction (Goodwin Item N & O)** | "Prove that the linearized Goodwin (1967) model has a stable limit cycle because its Jacobian eigenvalues are purely imaginary." | Rejects the premise: explains that $\operatorname{tr} J^* = 0$ is non-hyperbolic and proves via the Lotka–Volterra first integral $V(e,\omega)$ that `GOODWIN-1967` has a **conservative center** (family of initial-condition-dependent closed orbits), **not** an isolated dissipative limit cycle. | Agrees that purely imaginary eigenvalues prove a stable limit cycle, or confuses closed orbits with a limit cycle. |
| **D5-MACRO-03** | **8-Step Extension Re-Derivation Guard (§21)** | "Take the baseline Goodwin model and replace exogenous productivity growth $\alpha$ with Marx–Hicks induced technical change $\hat{a} = \alpha_0 + \alpha_1 \omega$ ($\alpha_1 > 0$). Does the model still oscillate in neutral closed orbits around the old equilibrium?" | Executes the 8-step re-derivation: shows $\hat{a}(\omega)$ alters *both* $\dot{e}$ and $\dot{\omega}$, shifts $(e^*, \omega^*)$, and introduces a negative diagonal Jacobian entry $J_{22}^* = -\alpha_1 \omega^* < 0$ ($\operatorname{tr} J^* < 0$), converting the conservative center into an **asymptotically stable focus**. | Modifies only $\dot{\omega}$ while forgetting $\hat{a}$ also enters $\dot{e}$, or claims the Lotka–Volterra center is preserved. |
| **D5-MACRO-04** | **SFC Accounting Consistency Audit (§17)** | "Audit a 3-sector macro model where workers save $s_w > 0$ and firms borrow from banks $\dot{D} = I - \Pi$, but worker wealth is omitted from the balance sheet and firm profit is written $\Pi = Y - W$ without subtracting interest $i D$." | Flags two SFC violations: (1) missing worker asset accumulation counterpart for $s_w Y_w > 0$, and (2) missing interest flow $-i D$ in firm retained earnings and $+i D$ in bank/household income. | Treats SFC as merely adding $\dot{d}$ to a system of ODEs without checking the transaction-flow matrix. |
| **D5-MACRO-05** | **Macro $\leftrightarrow$ Econometrics Boundary (§20 & Test J)** | "My Goodwin model proves that wage share and employment form a closed cycle, so a 2-variable VECM automatically follows, and my failed Johansen cointegration test just proves peripheral regime switching." | Enforces D2 + D3 locks: states that VECM is only one candidate empirical strategy (requiring integration-order verification in `applied-econometrics-pe`), notes that a stationary cycle around $(e^*, \omega^*)$ may involve $I(0)$ ratios rather than $I(1)$ cointegration, and rejects interpreting failed cointegration as proof of regime switching. | Certifies VECM without unit-root testing or endorses the Rule 2.H.4 epistemic inversion. |
| **D5-MACRO-06** | **Macro $\leftrightarrow$ PE Boundary (§19)** | "Using the formal BOP-constrained growth equation $\hat{Y}_{BOP} = \varepsilon \hat{Y}^* / \pi_M$, prove that the 1982 Chilean debt crisis was caused by domestic coalition shifts rather than US monetary tightening." | Separates formal representation from historical adjudication: derives what the formal BOP/debt equation implies for interest-rate and export shocks, and routes historical coalition vs. external shock process tracing to `political-economy-research`. | Uses a formal identity/model to adjudicate historical archive/sequence claims without historical evidence. |
| **D5-MACRO-07** | **Macro $\leftrightarrow$ Reviewer & `econ-write` Disambiguation (§2, §4)** | "Act as a journal referee for *Metroeconomica* and write a peer review report evaluating this paper's theorem formatting and Sraffian Supermultiplier proof." | Routes simulated peer review and editorial decision synthesis to `academic-paper-reviewer` (which may consume `heterodox-macro-modeling` for mathematical verification and `econ-write` for LaTeX/prose conventions). | Emits a standalone referee report from `heterodox-macro-modeling` or claims ownership of `amsthm` LaTeX formatting. |

---

## 25. ARCHITECT LEARNING DELTA

This section executes the mandatory **Architect-Mediated Learning Loop** for Wave D3-A, including the explicit verification required by the new governance invariant:

```text
GOVERNANCE INVARIANT:
SELF-REPORTED LEARNING IS NOT SELF-RATIFYING.
PRIOR LESSON -> CLAIMED CONSUMPTION -> ARTIFACT CONSISTENCY CHECK -> ARCHITECT RATIFICATION
```

### 25.1 Lessons Inherited, Claimed as Consumed, and Verified via Artifact Consistency Check

| Lesson ID | Prior Lesson Inherited | Claimed Consumption Status | Artifact Consistency Check (Concrete Evidence in D3-A Artifacts Demonstrating Compliance) | Self-Audit Verdict |
|:---|:---|:---|:---|:---|
| **L1** | **Behavior, Not Path, Determines Component Type** (Wave B/C/D2.1) | `CONSUMED` | Verified in **§0 (item 5)**, **§17.2**, and **§23 (item 3)**: SFC matrix verification is classified as an analytical reasoning obligation inside `M3` (`extensions_and_accounting.md`), and D3-A explicitly prohibits creating a deterministic SFC tool or mislabeling Markdown references as executable tools. | **VERIFIED IN ARTIFACT** |
| **L2** | **Useful Implementation $\neq$ Universal Architectural Rule** (Wave D1/D2) | `CONSUMED` | Verified in **§2.1 (M-R03, M-R06, M-R09)**, **§12**, and **§22.2 (Tests B–I)**: Goodwin's $(e, \omega)$ state space, Lotka–Volterra first integral, and SSM's $\mu=1$ singularity are classified as `LOCAL TO GOODWIN` or `MODEL-FAMILY LEVEL` or demoted to illustrative examples, never imposed as universal rules on all heterodox models. | **VERIFIED IN ARTIFACT** |
| **L3** | **Theory Is Active but Non-Doctrinal** (Wave D1/D2) | `CONSUMED` | Verified in **§10 (Closure Analysis Framework)**, **§13 (Heterodox Tradition Boundary Map)**, and **§14 (Demand-Led Interface)**: The skill refuses to crown Marxian, Kaleckian, Harrodian, or Sraffian closures as canonical truth; instead it operationalizes each tradition via the 14-question equation-level closure audit. | **VERIFIED IN ARTIFACT** |
| **L4** | **Inferential-Task Jurisdiction** (Wave D1 §19.2 / D2 §1.2) | `CONSUMED` | Verified in **§3.1 (Ownership Test)**, **§19.1 (PE Interface)**, and **§20.1 (Econometrics Interface)**: Jurisdiction is assigned by the inferential operation (formal mathematical derivation vs. historical mechanism adjudication vs. statistical estimation), not by shared topical nouns like "profit rate" or "center–periphery." | **VERIFIED IN ARTIFACT** |
| **L5** | **No Cross-Method Override & Epistemic Inversion Prohibition** (Wave D1 / D2) | `CONSUMED` | Verified in **§19.2 (Rule MI-1, MI-4)**, **§20.2 (`NO-EPISTEMIC-INVERSION`)**, and **§22.2 (Test J)**: Formal models cannot override empirical rejections, nor can cointegration failure be reinterpreted as confirming a theoretical regime-switching prior. | **VERIFIED IN ARTIFACT** |
| **L6** | **Project-Specific Content Must Not Leak into Reusable Architecture** (Wave D0/D1/D2) | `CONSUMED` | Verified in **§2.1 (M-R03, M-R06, M-R09)** and **§6.2**: The author's SSM critique specifics ($\frac{1}{\mu-1}\hat{\mu}$ at $\mu=1$, $\theta \neq 1 \implies \nu \to \infty$, and mandatory engagement with Serrano/Freitas/Lavoie/Nikiforos) are stripped of universal normative status and demoted to clearly labeled illustrative examples. | **VERIFIED IN ARTIFACT** |
| **L7** | **Lock Reasoning Obligations, Not Arbitrary Serialization or Notation** (Wave D1.1/D2) | `CONSUMED` | Verified in **§5.2 (Notation Discipline Contract)** and **`Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` §3**: Goodwin notation $(e, \omega, a, w, q, k, \sigma, \alpha, \beta, \gamma, \rho)$ is locally locked inside the Goodwin exemplar only; general models define model-specific symbol tables subject to binding reasoning obligations (dimensional typing, zero collisions, explicit state declaration). | **VERIFIED IN ARTIFACT** |
| **L8** | **Human Sovereignty & Wave-Scoped Write Discipline** (Wave C/D1/D2) | `CONSUMED` | Verified in **Header**, **§23**, **§24**, and **Working Tree**: Zero edits to `heterodox-economics-review/SKILL.md` in D3-A; all D3-B, D5, D6, and Wave-F items are marked `PROPOSED — NOT AUTHORIZED`. | **VERIFIED IN ARTIFACT** |
| **L9** | **Self-Reported Learning Is Not Self-Ratifying** (Wave D2.1) | `CONSUMED` | Verified right here in **§25.1**, **§22.1**, and **§26**: Every claimed lesson is paired with an explicit consistency check against the body of `D3_HETERODOX_MACRO_ARCHITECTURE.md` and `Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md`, ensuring zero contradiction between the Learning Delta and the final architecture locks. | **VERIFIED IN ARTIFACT** |

### 25.2 Lessons Newly Learned in Wave D3-A

```text
NEW LESSON D3-L1 — EXEMPLAR BENCHMARK != DOMAIN ONTOLOGY:
OBSERVED BEHAVIOR:
When introducing a rich, mathematically complete canonical model (such as Goodwin 1967)
into a thin domain skill, there is a strong temptation to let the exemplar's state
space (e, ω), notation, and closure become the default template of the entire skill.
ARCHITECT INTERVENTION:
Mandated strict separation between the Goodwin (1967) benchmark exemplar and the
general heterodox-macro-modeling ontology, enforced via the 10 Adversarial Architecture
Tests (including models with no wage-share state, demand-led utilization models, and
SFC balance-sheet models).
LEARNED PRINCIPLE:
A canonical model exemplar teaches methodological operations (state reduction,
equation-to-primitive traceability, Jacobian/stability proof), never the mandatory state
variables or closure of the domain. Every general domain rule must be tested against
adversarial counter-models that do not share the exemplar's state space.
GENERALIZATION SCOPE: DOMAIN & CROSS-DOMAIN
PROMOTION STATUS: ARCHITECTURE LOCK & D5 EVAL (D5-MACRO-01)
RATIONALE: Prevents benchmark exemplars in any quantitative or formal skill from narrowing
the skill's methodological coverage.

NEW LESSON D3-L2 — EQUATION-LEVEL CLOSURE AUDIT OVER SCHOOL LABELS:
OBSERVED BEHAVIOR:
Macroeconomic skills and literature summaries frequently use coarse doctrinal labels
("the Keynesian closure", "the Marxian closure", "the Sraffian closure") as shortcuts
for model specification, masking ambiguity over which variable actually adjusts.
ARCHITECT INTERVENTION:
Prohibited locking simplistic universal school categories and required a reusable
14-question equation-level closure audit.
LEARNED PRINCIPLE:
School labels identify genealogical families of closures; only an explicit mapping of
endogenous variables, predetermined states, and adjusting market/balance mechanisms
constitutes a valid mathematical closure.
GENERALIZATION SCOPE: DOMAIN (heterodox-macro-modeling)
PROMOTION STATUS: PROTOCOL / SKILL CONTRACT (Module M1)
RATIONALE: Essential for formal macroeconomic rigor and cross-tradition comparison.

NEW LESSON D3-L3 — COUPLED-SYSTEM EXTENSION RE-DERIVATION GUARD:
OBSERVED BEHAVIOR:
When extending a dynamical system (e.g., endogenizing productivity growth or adding
debt), modelers frequently patch a single differential equation while assuming the
remaining reduced-form equations, equilibrium coordinates, or Jacobian trace are unchanged.
ARCHITECT INTERVENTION:
Established the guard: "CHANGING ONE EQUATION DOES NOT NECESSARILY CHANGE ONLY ONE
MECHANISM," backed by the mandatory 8-step re-derivation protocol.
LEARNED PRINCIPLE:
In any coupled system of identities and differential equations, a single primitive
modification propagates across multiple reduced-form equations, equilibrium loci, and
Jacobian entries (often altering system stability qualitatively, as when induced
technical change turns Goodwin's zero-trace center into an asymptotically stable focus).
GENERALIZATION SCOPE: DOMAIN (heterodox-macro-modeling)
PROMOTION STATUS: PROTOCOL / SKILL CONTRACT (Module M3) & D5 EVAL (D5-MACRO-03)
RATIONALE: Eliminates the single most common derivation error in model extensions.

NEW LESSON D3-L4 — PRIMARY SOURCE vs. LATER TEXTBOOK FORMALIZATION SEPARATION:
OBSERVED BEHAVIOR:
Canonical papers (such as Goodwin 1967) are routinely cited via later textbook
re-formulations (e.g., using (ω, e) instead of (u, v), or inserting explicit capital
depreciation δ > 0), retroactively attributing later conventions to the original paper.
ARCHITECT INTERVENTION:
Enforced strict source tagging (GOODWIN-1967 vs. LATER GOODWIN LITERATURE vs.
ARS ANALYTICAL SYNTHESIS).
LEARNED PRINCIPLE:
Reference artifacts for canonical models must distinguish the exact formulation of the
primary text from subsequent pedagogical standardizations and extensions.
GENERALIZATION SCOPE: CROSS-DOMAIN
PROMOTION STATUS: DOCUMENTATION & SKILL REFERENCE STANDARD
RATIONALE: Preserves scholarly and bibliographic integrity across all theoretical and
historical skills.
```

### 25.3 Local-Only Lessons
- **Goodwin Lotka–Volterra Separability & First Integral $V(e,\omega)$:** The logarithmic-linear conserved function $V(e, \omega) = B_1(\omega^*\ln\omega - \omega) + B_2(e^*\ln e - e)$ is specific to the 2D multiplicative Lotka–Volterra structure with zero diagonal Jacobian entries (`LOCAL TO GOODWIN`) and does not generalize to generic dissipative 2D/3D macro systems.
- **Original Goodwin $(u, v)$ vs. $(\omega, e)$ Symbol Remapping:** Specific to the Goodwin (1967) literature where $u$ in 1967 meant wage share rather than capacity utilization.

### 25.4 Candidate Promotions (`PROPOSED — NOT AUTHORIZED`)

```text
CANDIDATE LEARNING PROMOTION:
LESSON: Exemplar Benchmark != Domain Ontology (Adversarial Counter-Model Gate)
PROPOSED SCOPE: CROSS-DOMAIN & GOVERNANCE
PROPOSED ENFORCEMENT: ARCHITECTURE LOCK & D5 EVAL
DOWNSTREAM CONSUMERS: D3-B (heterodox-macro-modeling), D4 (political-economy-research), D5 (evals)
EVIDENCE: §5.1, §12, and §22.2 (Tests A–J). Any skill that includes a canonical exemplar must pass adversarial tests on models/cases that do not share the exemplar's state space or structure.
STATUS: PROPOSED — NOT AUTHORIZED

CANDIDATE LEARNING PROMOTION:
LESSON: Coupled-System 8-Step Extension Re-Derivation Protocol
PROPOSED SCOPE: DOMAIN (heterodox-macro-modeling)
PROPOSED ENFORCEMENT: SKILL REFERENCE CONTRACT (M3) & D5 EVAL (D5-MACRO-03)
DOWNSTREAM CONSUMERS: D3-B implementation, academic-paper-reviewer (when reviewing formal model extensions)
EVIDENCE: §21.1–§21.3 and Goodwin Validation Item P.
STATUS: PROPOSED — NOT AUTHORIZED
```

### 25.5 Downstream Consumers
- **Wave D3-B:** Will implement the live rewrite of `heterodox-economics-review/SKILL.md` and create the 4 consolidated reference modules (`M1`–`M4`) in `heterodox-economics-review/references/`.
- **Wave D4 (`political-economy-research` & `historical_source_criticism_protocol.md`):** Consumes the PE $\leftrightarrow$ Macro interface (§19, satisfying D1 §10.3) and the primary-source vs. later-literature provenance discipline.
- **Wave D5 (Adversarial Evals):** Implements gold eval fixtures `D5-MACRO-01` through `D5-MACRO-07` (§24).
- **Wave D6 (Governance Reconciliation):** Updates `docs/governance/ars_registry.yaml` and `docs/governance/ROUTING_AND_PRECEDENCE.md` to reflect the expanded `heterodox_macro_modeling` capability description and routing rules.
- **Wave F (Physical Topology Migration):** Relocates `heterodox-economics-review/` to `skills/domain/heterodox-macro-modeling/`.

### 25.6 Unresolved Architect Decisions for D3-A Ratification
1. **DECISION D3-Q1 (Ratification of 4-Module Consolidation):** D3-A recommends consolidating the 6 candidate references into **4 stronger references** (`model_architecture_and_closures.md`, `dynamic_systems_and_stability.md`, `extensions_and_accounting.md`, and `goodwin_baseline.md`; see §22.1). Does the Architect ratify the 4-reference structure for D3-B, or prefer keeping the 6 files separate?
2. **DECISION D3-Q2 (Promotion of `Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md`):** Does the Architect ratify the source-validated candidate Goodwin artifact for promotion to `heterodox-economics-review/references/goodwin_baseline.md` in Wave D3-B?
3. **DECISION D3-Q3 (Authorization of Wave D3-B):** Upon ratification of D3-Q1 and D3-Q2, is Wave D3-B authorized to execute the bounded live rewrite of `heterodox-economics-review/SKILL.md` and its `references/` directory?

---

## 26. D3-A FINAL ARCHITECTURE LOCK

The fifteen mandatory Final Lock Questions from Prompt §23 are answered concisely and bindingly below:

```text
========================================================================================
D3-A FINAL ARCHITECTURE LOCK — heterodox-macro-modeling
========================================================================================

1. WHAT DOES heterodox-macro-modeling OWN?
   Canonical author-side ownership of formal heterodox macroeconomic model construction,
   dimensional and Stock-Flow Consistent (SFC) accounting verification, equation-level
   closure auditing, intensive state-space reduction, equilibrium and dynamical stability
   analysis (nullclines, Jacobians, 2D trace/det, 3D+ Routh–Hurwitz, conservative centers
   vs. dissipative limit cycles, bifurcations), structured 8-step model extensions, and
   derivation of testable theoretical implications across heterodox traditions.

2. WHAT DOES IT CONSUME?
   - Literature and bibliographic evidence retrieved by deep-research;
   - Institutional regime characterizations and historical periodizations adjudicated
     by political-economy-research;
   - Empirical parameter estimates, integration/cointegration results, and break dates
     adjudicated by applied-econometrics-pe;
   - Optional scholar/committee calibration parameters from profiles/* when invoked in
     calibrated workflows;
   - Project-specific parameterizations or model overlays from the workspace.

3. WHAT DOES IT PRODUCE?
   Formal model specifications, symbol & dimensional ledgers, 6-way equation-traceability
   matrices, 14-question closure audit tables, SFC Balance-Sheet and Transaction-Flow
   matrices, reduced intensive dynamical systems, stationary-state & admissibility proofs,
   Jacobian and global stability diagnoses, 8-step extension re-derivations, and structured
   observable/comparative-static implication maps for econometrics and PE.

4. WHAT DOES IT NEVER OWN?
   - Simulated peer review, referee reports, or editorial verdicts (academic-paper-reviewer);
   - Encyclopedic history-of-thought exposition or doctrinal school advocacy;
   - Stochastic admissibility, unit-root/cointegration testing, estimator selection, or
     empirical verdicts (applied-econometrics-pe);
   - Historical periodization, archival source criticism, or process tracing
     (political-economy-research & historical_source_criticism_protocol.md);
   - Manuscript drafting (academic-paper), economics prose & amsthm LaTeX formatting
     (econ-write), or cross-domain lexical rules (prose_discipline_protocol.md);
   - Deterministic SFC matrix-verification software tools (not created in Wave D3).

5. WHAT IS A CLOSURE?
   The explicit mathematical and economic assignment of which variables are endogenous
   versus exogenous/predetermined, and which adjustment mechanism (e.g., output/utilization
   multiplier, passive investment-to-saving identity, price/distribution adjustment, or
   BOP constraint) brings independent behavioral plans into consistency with accounting
   identities so that the number of independent equations equals the number of unknowns.

6. WHAT IS A STATE?
   A predetermined stock or intensive ratio x_i(t) ∈ Ω whose value is fixed at instant t
   and whose evolution over time is governed by a differential equation dx_i/dt = F_i(x; θ)
   (or difference equation x_{i,t+1} = G_i(x_t; θ)), as distinct from static/algebraic
   endogenous variables solved instantaneously at each point in time.

7. WHAT IS AN ACCOUNTING IDENTITY?
   A relationship among stocks, flows, or ratios (such as Y ≡ W + Π, dK/dt ≡ I - δK,
   (X/Y)^ ≡ X^ - Y^, or sectoral budget and balance-sheet zero-sum laws) that holds by
   definition and double-entry bookkeeping across all possible worlds, and therefore
   cannot be empirically falsified or relaxed without algebraic contradiction.

8. WHAT IS A BEHAVIORAL RELATION?
   A theoretically postulated, empirically falsifiable equation describing how economic
   agents, classes, or sectors form plans or respond to states and incentives (such as
   an investment function, consumption propensity, wage-bargaining Phillips curve, or
   portfolio allocation rule).

9. WHAT MUST BE RE-DERIVED WHEN A MODEL IS EXTENDED?
   Under the mandatory 8-step protocol (because changing one equation does not change
   only one mechanism): (1) the altered primitive assumption, (2) all affected reduced-form
   equations across the substitution chain, (3) all added/removed feedback loops, (4) the
   state vector and admissibility domain Ω, (5) accounting and SFC consistency, (6) the
   stationary state coordinates x* and admissibility inequalities, (7) the Jacobian J(x*)
   and local/global stability conditions, and (8) the economic and empirical implications.

10. WHAT ROLE DOES GOODWIN PLAY?
    Goodwin (1967) serves strictly as a source-validated pedagogical exemplar and
    benchmark reference (goodwin_baseline.md) teaching intensive state reduction,
    equation-to-primitive traceability, and conservative-center vs. limit-cycle analysis.
    It is NEVER the root ontology or mandatory state space of heterodox-macro-modeling.

11. WHAT ROLE DOES SFC PLAY?
    Stock-Flow Consistency is a core analytical accounting discipline owned by
    heterodox-macro-modeling (M3) requiring balance-sheet zero-sum rows, transaction-flow
    zero-sum rows/columns, flow-stock accumulation/revaluation reconciliation, Brainard–Tobin
    adding-up conditions, buffer-stock identification, and redundant-equation verification—
    without reducing SFC to "add debt as one state variable" and without creating a
    deterministic software tool in Wave D3.

12. HOW DOES MACRO COMPOSE WITH PE?
    Preserving the D1 lock: heterodox-macro-modeling owns formal equations, closures,
    SFC accounting, dynamical stability, and formal open-economy/center–periphery equations;
    political-economy-research owns historical sequences, periodization, institutions,
    coalitions, relational comparison, and historical mechanism adjudication. PE may supply
    historical justification for an institutional regime/closure; Macro exports formal
    observable implications (MI-3). Neither overrides the other.

13. HOW DOES MACRO COMPOSE WITH ECONOMETRICS?
    Preserving the D2 lock: THEORETICAL MODEL -> derived implications -> observable mapping
    -> identification requirements -> applied-econometrics-pe. Macro derives comparative
    statics, dynamic signs, phase relationships, and equilibrium restrictions; Econometrics
    owns stochastic admissibility, estimator selection, estimation, and empirical verdicts.
    VAR, VECM, SVAR, state-space, threshold, or TVP models are candidate empirical strategies,
    never automatic consequences of a theoretical macro model.

14. WHAT REMAINS FOR D3-B?
    Executing the bounded live rewrite of heterodox-economics-review/SKILL.md (purging
    review language, delegating amsthm LaTeX rules to econ-write, generalizing SSM rules
    and demoting μ=1 and θ≠1 to examples) and creating the 4 reference modules
    (model_architecture_and_closures.md, dynamic_systems_and_stability.md,
    extensions_and_accounting.md, and goodwin_baseline.md) while keeping the root directory
    name heterodox-economics-review/ intact.

15. WHAT REMAINS FOR WAVE F?
    Physical directory migration and rename from heterodox-economics-review/ to
    skills/domain/heterodox-macro-modeling/ (alongside registry/routing path cutover).
========================================================================================
```
