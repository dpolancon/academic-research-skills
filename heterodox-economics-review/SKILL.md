---
name: heterodox-economics-review
description: Author-side formal macroeconomic modeling, closure analysis, dynamic systems, stability, and stock-flow consistency across heterodox traditions.
---

# Heterodox Macroeconomic Modeling (`heterodox-macro-modeling`)

> **Runtime Identity & Governance Status:**
> - **Current Runtime Path:** `heterodox-economics-review/` (Directory move to `skills/domain/heterodox-macro-modeling/` deferred to Wave F).
> - **Frontmatter Name Key:** `heterodox-economics-review` preserved for Wave C compatibility until Wave D6 / Wave F reconciliation.
> - **Capability Ownership:** Sole canonical author-side owner of `heterodox_macro_modeling`.
> - **Authoritative Contract:** `docs/design/wave-d/D3_HETERODOX_MACRO_ARCHITECTURE.md`.

---

## 1. Domain Ownership & Non-Ownership

### 1.1 What This Skill Owns
`heterodox-macro-modeling` is an author-side domain reasoning capability governing the formal specification, mathematical reduction, stability analysis, and theoretical implications of macroeconomic models across heterodox traditions:
- **Model Architecture & Dimensional Consistency:** Definition of stocks, flows, ratios, rates, and intensive state variables with dimensional homogeneity.
- **Primitive Equation Classification:** Explicit separation of identities, technological assumptions, behavioral equations, institutional assumptions, closure rules, and exogenous processes.
- **Equation-Level Closure Auditing:** Determining how markets, balances, and distributional claims reconcile mathematically without doctrinal favoritism.
- **Analytical Stock-Flow Consistency (SFC):** Sectoral balance-sheet matrices, transaction-flow matrices, flow-stock reconciliation, and redundant-equation auditing.
- **Dynamical Systems & Stability:** Intensive state-space reduction, nullclines, stationary states, Jacobians, local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants), nonlinear dynamics (conservative centers vs. dissipative limit cycles), and bifurcations where conditions warrant.
- **Structured Model Extensions:** 8-step re-derivation protocol ensuring that modifying one equation re-evaluates all affected feedbacks and stability properties.
- **Theoretical Implications:** Comparative statics, dynamic signs, phase relationships, and testable observable restrictions.

### 1.2 Explicit Non-Ownership & Delegations
- **Simulated External Peer Review:** Referees, accept/reject decisions, scores, and editorial critique are strictly owned by [`academic-paper-reviewer`](file:///c:/ReposGitHub/academic-research-skills/academic-paper-reviewer/SKILL.md).
- **Economics Prose & LaTeX Formatting:** Section architecture, narrative flow, BLUF, results rhetoric, and `amsthm` theorem/proof environments (`\begin{proposition}`, `\begin{proof}`) are strictly owned by [`econ-write`](file:///c:/ReposGitHub/academic-research-skills/econ-write/SKILL.md) (lines 160–178).
- **Prose Discipline & Lexical Bans:** Sentence syntax, active voice, and lexical audit are governed by [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md).
- **Econometric Testing & Admissibility:** Stochastic admissibility, integration order ($I(d)$), cointegration testing, estimator selection, and empirical verdicts are strictly owned by [`applied-econometrics-pe`](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/SKILL.md).
- **Historical Process Tracing & Periodization:** Qualitative historical causality, institutional emergence, archives, and comparative-historical case studies are strictly owned by `political-economy-research` (Wave D4).
- **Doctrinal Hegemony / Theory Encyclopedias:** The skill models formal mechanisms across traditions; it does not maintain theory encyclopedias or enforce school orthodoxy.

---

## 2. Canonical Modeling Workflow

Every macroeconomic modeling task executed by this skill follows an auditable 6-stage sequence:

```text
[1. CONSTRUCT & NOTATION]
    Declare intensive state vector x ∈ Ω, define all symbols with dimensional types,
    and prevent intra-model symbol collisions.
          ↓
[2. PRIMITIVE EQUATION CLASSIFICATION]
    Decompose equations into: Accounting Identity (ID), Technological Assumption (TECH),
    Behavioral Relation (BEH), Institutional Assumption (INST), Closure Rule (CLOS),
    and Exogenous Process (EXOG).
          ↓
[3. CLOSURE & ACCOUNTING AUDIT]
    Execute the 14-Question Closure Audit. If financial assets or sectoral balances
    are present, construct Balance-Sheet and Transaction-Flow matrices.
          ↓
[4. DYNAMICAL SYSTEM REDUCTION]
    Differentiate intensive ratios via logarithmic identities (X/Y)^ = X^ - Y^.
    Formulate the autonomous system dx/dt = F(x; θ) and define admissible domain Ω.
          ↓
[5. EQUILIBRIUM & STABILITY ANALYSIS]
    Derive stationary states x* ∈ Ω and nullclines. Construct Jacobian J(x*).
    Evaluate local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants).
    Distinguish conservative centers from dissipative limit cycles where oscillations arise.
    Check boundary behavior and singularities.
          ↓
[6. THEORETICAL IMPLICATION MAPPING]
    Derive comparative statics ∂x*/∂θ, dynamic signs, and phase lead/lag relations
    for downstream empirical testing or historical contextualization.
```

---

## 3. Reference Module Routing

Detailed mathematical reasoning, matrices, proofs, and taxonomies are modularized into four canonical reference documents:

| Module ID | Reference Path | Core Reasoning Load Owned | When to Route |
|:---|:---|:---|:---|
| **M1** | [`references/model_architecture_and_closures.md`](file:///c:/ReposGitHub/academic-research-skills/heterodox-economics-review/references/model_architecture_and_closures.md) | 7-part modeling grammar; 6-way equation taxonomy; notation contract; 14-question closure audit; pluralist tradition boundary map (Marxian, Classical/Sraffian, Kaleckian, Harrodian, Kaldorian, Structuralist); demand-led growth regimes (wage-led vs. profit-led). | Formulating new models, classifying equations, auditing closures, analyzing utilization dynamics, or comparing theoretical traditions. |
| **M2** | [`references/dynamic_systems_and_stability.md`](file:///c:/ReposGitHub/academic-research-skills/heterodox-economics-review/references/dynamic_systems_and_stability.md) | Intensive state reduction; domain $\Omega$ and singularity checks; equilibrium concepts; nullclines; Jacobians; local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants); conservative centers vs. limit cycles; conditional Poincaré–Bendixson (planar) and Hopf bifurcation analysis. | Reducing systems of ODEs, checking zero-denominators, calculating Jacobians, proving local/global stability, or analyzing oscillations. |
| **M3** | [`references/extensions_and_accounting.md`](file:///c:/ReposGitHub/academic-research-skills/heterodox-economics-review/references/extensions_and_accounting.md) | Universal SFC core (Balance-Sheet & Transactions-Flow matrices, sectoral balances, stock-flow reconciliation, redundant equation check) + conditional Brainard–Tobin portfolio adding-up and buffer-stock closures; open-economy BOP constraints; endogenous technical change; 9 extension operations; 8-step re-derivation protocol. | Building SFC balance sheets, introducing financial debt/assets, opening the economy to trade/capital flows, endogenizing productivity, or modifying baseline models. |
| **M4** | [`references/goodwin_baseline.md`](file:///c:/ReposGitHub/academic-research-skills/heterodox-economics-review/references/goodwin_baseline.md) | Source-validated Goodwin (1967) growth cycle benchmark exemplar; local notation lock; Items A–P validation ledger; conservative center proof via first integral $V(e,\omega) = \text{const}$; 3-tier terminology guardrail. | Studying Goodwin benchmark dynamics, teaching state reduction and Lotka–Volterra mechanics, or evaluating reserve-army feedback. |

---

## 4. Fundamental Modeling Disciplines

### 4.1 Notation Discipline
- **No Global Notation Lock:** Goodwin notation $(e, \omega, a, w, q, k, \sigma, \alpha, \beta, \gamma, \rho)$ is locally scoped to `M4`. Other traditions define their own symbol tables.
- **Mandatory Symbol Table:** Every model derivation must declare symbol definitions, dimensional units (stock, flow, ratio, rate, share), and state variables prior to derivation.
- **Zero Intra-Model Collisions:** Never use the same symbol for multiple constructs (e.g., $\pi$ for inflation and profit share, or $\mu$ for markup and utilization) within one model.

### 4.2 Closure Audit Discipline
- **Equation-Level Specification Over School Labels:** Doctrinal labels ("Keynesian closure", "Marxian closure", "Sraffian closure") identify candidate closure families, never mathematical specifications.
- **The 14-Question Gate:** Every model must specify what determines output, utilization, investment, saving, distribution, wages, employment, and technical change; which variables are predetermined vs. adjusting; and verify that independent equations equal endogenous variables ($M = n + m$).

### 4.3 Anti-Tautology & Singularity Discipline
- **Logarithmic Differentiation (`ID-DIFF`):** Ratios $z \equiv X/Y$ must be differentiated as $\hat{z} = \hat{X} - \hat{Y}$. Setting $\dot{z} = 0$ requires an explicit closure or technological condition $\hat{X} = \hat{Y}$.
- **No Specification Tautologies (`NO-TAUTOLOGY`):** Dynamic instability or convergence must arise from behavioral feedbacks, never from hardcoding non-homogeneous technological elasticities (e.g., fixing capacity-to-capital elasticity $\theta \neq 1$ so that $K/Y^p \to \infty$ by definition).
- **Singularity Audits:** Rational ODE terms $\frac{N_i(\mathbf{x})}{D_i(\mathbf{x})}$ must be audited for zero-denominators within the admissible domain $\Omega$ (e.g., evaluating whether term coefficients diverge as utilization approaches normal values, using L'Hôpital limits or phase-plane methods).

### 4.4 Model Extension Discipline
- **Fundamental Invariant:** *Changing one equation does not necessarily change only one mechanism.*
- **Mandatory 8-Step Re-Derivation Protocol:** Whenever an assumption is relaxed, an exogenous parameter endogenized, or a state/sector/balance sheet added, the modeler must execute the 8-step protocol in `M3`:
  1. Identify altered assumption; 2. Trace affected equations; 3. Identify altered feedbacks; 4. Update state vector $\mathbf{x} \in \Omega$; 5. Check accounting/SFC consistency; 6. Re-derive stationary states $\mathbf{x}^*$; 7. Re-analyze Jacobian and stability; 8. Reassess economic interpretation.

---

## 5. Cross-Domain Composition Contracts

### 5.1 Political Economy Interface (`heterodox-macro-modeling` $\leftrightarrow$ `political-economy-research`)
- **Preserve Wave D1 Lock (D1 §10):** Macro owns formal equations, closures, accounting consistency, dynamic stability, and formal open-economy/center–periphery models. PE owns comparative-historical sequences, periodization, institutions, coalitions, and historical mechanism adjudication.
- **Model $\neq$ Historical Evidence (Rule MI-1):** A formal model demonstrates theoretical plausibility or institutional compatibility; it cannot serve as historical evidence that a mechanism operated in a concrete case.
- **Closure Justification Flow (Rule MI-2):** Historical evidence that an institutional regime matches a model's closure assumptions (e.g., wage-setting institutions or capital controls) is supplied by PE and consumed by Macro.
- **Observable Implication Export (Rule MI-3):** Macro exports structured comparative statics and dynamic phase relations that PE's Mechanism Specification can reference.
- **No Cross-Method Override (Rule MI-4):** Neither domain may override the analytical jurisdiction of the other.

### 5.2 Econometrics Interface (`heterodox-macro-modeling` $\leftrightarrow$ `applied-econometrics-pe`)
- **Preserve Wave D2 Lock (D2 §0, §11, §18):**
  $$\text{THEORETICAL MODEL} \longrightarrow \text{derived implications} \longrightarrow \text{observable mapping} \longrightarrow \text{identification requirements} \longrightarrow \text{applied-econometrics-pe}$$
- **Candidate Empirical Strategies Only (`NO-AUTO-ESTIMATOR`):** Theoretical dynamical systems do not automatically dictate VAR, VECM, SVAR, state-space, or threshold/TVP estimators. Estimator selection and stochastic admissibility belong strictly to `applied-econometrics-pe`.
- **Epistemic Inversion Prohibition (`NO-EPISTEMIC-INVERSION`):** If empirical testing finds no cointegration or opposite-signed effects, the theoretical model may not override the empirical finding or declare that rejection confirms "structural regime switching." Divergences must be reported transparently.

---

## 6. Pedagogical Role of Goodwin (Exemplar, Not Root Ontology)

- **Exemplar Status:** Goodwin (1967) is referenced via [`references/goodwin_baseline.md`](file:///c:/ReposGitHub/academic-research-skills/heterodox-economics-review/references/goodwin_baseline.md) to demonstrate state reduction, equation-to-primitive traceability, and the distinction between conservative centers and limit cycles.
- **Non-Dominance Invariant:** The skill natively handles models with:
  - no wage-share state variable (e.g., fixed-markup Kaleckian or Supermultiplier models);
  - no employment-rate state variable (e.g., pure capacity-utilization models);
  - endogenous capacity utilization ($u \neq 1$);
  - autonomous non-capacity-creating demand ($Z$);
  - private and public debt states ($d_f, b_g$);
  - endogenous Kaldor–Verdoorn productivity;
  - external balance-of-payments constraints (Thirlwall's Law);
  - multi-sector reproduction schemes; and
  - full SFC balance sheets.
- Routing to Goodwin is restricted to inquiries specifically concerning Goodwin-family models, reserve-army cycles, or Classical-Marxian full-capacity accumulation.
