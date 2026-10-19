# Wave D3-B / D3.1 Implementation Report: Heterodox Macro Modeling Live Capability Refactor

- **Pass Identity:** WAVE D3-B — HETERODOX MACRO MODELING LIVE IMPLEMENTATION (WITH WAVE D3.1 SOURCE FIDELITY + CONDITIONALITY FREEZE)
- **Status:** `HUMAN-RATIFIED BINDING MACRO MODELING ARCHITECTURE — WAVE D3 CLOSED`
- **Governing Checkpoint:** `917ee2f2332cef92015937bddd7337a52ef4b12d`
- **Execution Date:** 2026-10-17
- **Current Runtime Component:** `heterodox-economics-review/`
- **Future Semantic Capability Target:** `skills/domain/heterodox-macro-modeling/` (Wave F physical move)
- **Primary Upstream Ratified Contract Consumed:** `docs/design/wave-d/D3_HETERODOX_MACRO_ARCHITECTURE.md`

---

## 0. Executive Verdict

Wave D3-B and the Wave D3.1 freeze execute the authorized live implementation and final ratification of the D3-A architecture within the runtime component `heterodox-economics-review/`.

1. **Successful Modular Implementation:** The 29-line project-specific fragment in `heterodox-economics-review/SKILL.md` has been rewritten into a compact, authoritative capability router and contract. The 4 ratified logical reference modules (`M1`–`M4`) have been implemented in `heterodox-economics-review/references/`.
2. **Purge of Legacy Contaminations:** All simulated peer-review language, generic LaTeX formatting rules (`amsthm` environments), project-specific Sraffian Supermultiplier (SSM) disputes, and narrow sub-school requirements have been completely purged from the canonical capability contract.
3. **Pluralist Modeling Foundation:** The component natively supports models across Marxian, Classical/Sraffian, Kaleckian/Post-Keynesian, Harrodian, Kaldorian, Minskyan, Structuralist/Center–Periphery, Ecological, and SFC traditions.
4. **Goodwin Exemplar Demarcation & Source Fidelity:** Goodwin (1967) is promoted as an exemplar benchmark reference (`M4: goodwin_baseline.md`) demonstrating state reduction, primitive equation classification, and conservative center analysis. It is explicitly prevented from becoming the mandatory ontology or universal notation of the skill, and strictly distinguishes `GOODWIN-1967` (real, net terms where depreciation does not appear as a separate term) from `LATER / ALTERNATIVE GROSS REPRESENTATION` (where an explicit depreciation rate $\delta$ may be introduced).
5. **Capability Support $\neq$ Universal Application Requirement:** Universal SFC accounting laws and matrix-specific rules (Transactions-Flow vs. Balance-Sheet matrices) are separated from conditional portfolio and buffer-stock closures (`Brainard–Tobin`, buffer-stock identification), and higher-order/nonlinear dynamical theorems (`Routh–Hurwitz`, `Poincaré–Bendixson`, `Hopf`) are explicitly conditioned on system dimensionality and structure.
6. **Preservation of Cross-Domain Boundaries:** Unbreachable boundaries between Macro Modeling, Political-Economy Research (D1), and Applied Econometrics (D2) are enforced.
7. **Zero Repository Topology Drift:** The root folder `heterodox-economics-review/` remains in place; no registry, routing, profile, test, or earlier Wave-D files were modified.

---

## 1. Governing D3-A Locks Consumed

The implementation adheres strictly to the ratified decisions from Wave D3-A and Wave D3.1:
- **D3-Q1 (4-Module Architecture):** Consolidated into `model_architecture_and_closures.md` (M1), `dynamic_systems_and_stability.md` (M2), `extensions_and_accounting.md` (M3), and `goodwin_baseline.md` (M4).
- **D3-Q2 (Goodwin Promotion):** Promoted source-validated content from `Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` to `goodwin_baseline.md` with strict provenance tagging and local notation locks.
- **D3-Q3 (Live Implementation Authorization):** Executed exclusively within authorized files.
- **D1-LOCK-04 & Lesson L1 (SFC Tool Restraint):** Analytical SFC reasoning is owned in `M3`; no deterministic Python matrix-verification tool was created.
- **Governance Invariant:** `SELF-REPORTED LEARNING IS NOT SELF-RATIFYING` is enforced via an explicit artifact-level verification in §17.

---

## 2. Files Created / Modified

| File Path | Operation | Description |
|:---|:---|:---|
| `heterodox-economics-review/SKILL.md` | **REWRITE** | Rewritten from 29-line legacy fragment into compact capability router, equation classifier, closure auditor, and cross-domain contract. |
| `heterodox-economics-review/references/model_architecture_and_closures.md` | **CREATE (M1)** | Canonical 7-part modeling grammar, 6-way equation taxonomy, notation contract, 14-question closure audit, tradition boundary map, and demand-led utilization dynamics. |
| `heterodox-economics-review/references/dynamic_systems_and_stability.md` | **CREATE (M2)** | Intensive state reduction, domain $\Omega$ and singularity checks, equilibrium concepts, nullclines, Jacobians, local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants), conservative centers vs. limit cycles, and conditional Poincaré–Bendixson / Hopf bifurcations. |
| `heterodox-economics-review/references/extensions_and_accounting.md` | **CREATE (M3)** | Universal SFC Core (Balance-Sheet & Transactions-Flow matrices with matrix-specific zero-sum/net-worth laws, sectoral balances, stock-flow reconciliation, redundant-equation awareness) + Conditional SFC Portfolio/Closure mechanisms (Brainard–Tobin adding-up, buffer-stock identification), open-economy/BOP/center–periphery extensions, 9 extension operations, and the mandatory 8-step re-derivation protocol. |
| `heterodox-economics-review/references/goodwin_baseline.md` | **CREATE (M4)** | Promoted source-validated Goodwin (1967) benchmark exemplar, Items A–P validation ledger, local notation lock, real net terms vs. later gross $\delta$ distinction, conservative center proof, and 3-tier terminology guardrail. |
| `docs/design/wave-d/D3B_HETERODOX_MACRO_IMPLEMENTATION.md` | **CREATE / FREEZE** | Authoritative Wave D3-B / D3.1 implementation and verification report. |

---

## 3. Legacy Contamination Disposition

Every defect identified in the D3-A audit (`heterodox-economics-review/SKILL.md` lines 1–29) has been resolved:

| Item | Original Wording Summary | Classification | Final Disposition in Live Runtime | Target Location / Delegated Owner |
|:---|:---|:---|:---|:---|
| **M-R01, M-R02** | "Guidelines and checklists for writing, formatting, and reviewing heterodox economics papers..." | `REVIEW-LANGUAGE LEAKAGE` | **PURGED & REWRITTEN**. Skill reframed strictly as author-side formal macroeconomic modeling. Peer-review simulation explicitly delegated to `academic-paper-reviewer`. | `SKILL.md` §1 |
| **M-R03** | Singularity check at $\mu = 1$ in $\frac{1}{\mu-1}\hat{\mu}$. | `PROJECT-SPECIFIC SSM CONTENT` + `GENERIC PRINCIPLE` | **GENERALIZED & DEMOTED TO EXAMPLE**. General singularity audit codified in `M2` §2.3; specific $\mu=1$ in $\frac{1}{\mu-1}\hat{\mu}$ retained solely as an illustrative example. | `SKILL.md` §4.3 & `M2` §2.3 |
| **M-R04** | Boundary conditions near $\mu \to 0$ or $\mu \to \infty$. | `GENERIC DYNAMIC-SYSTEM PRINCIPLE` | **PRESERVED & GENERALIZED**. General boundary invariance checks codified in `M2` §2.3 across state bounds $\partial\Omega$. | `M2` §2.3 |
| **M-R05** | Double-check logarithmic time derivatives of ratios (e.g., $\phi = I/Y, \nu = K/Y^p$). | `GENERIC MODELING PRINCIPLE` | **PRESERVED & GENERALIZED**. Identity-Consistent Ratio Differentiation Rule (`ID-DIFF`) codified in `SKILL.md` §4.3 and `M1` §2. | `SKILL.md` §4.3 & `M1` §2 |
| **M-R06** | Fixing capacity-to-capital elasticity $\theta \neq 1$ forcing $\nu \to \infty$. | `PROJECT-SPECIFIC SSM CONTENT` + `GENERIC PRINCIPLE` | **GENERALIZED & DEMOTED TO EXAMPLE**. Codified as universal `NO-TAUTOLOGY` rule; the $\theta \neq 1 \implies \nu \to \infty$ case demoted to an illustrative example. | `SKILL.md` §4.3 & `M1` §2 |
| **M-R07** | Induced technical change vs. constant $\theta$. | `UNSUPPORTED UNIVERSAL RULE` (if read as banning exogenous tech change) | **GENERALIZED**. Pluralist Technical-Change Interface implemented in `M1` §3 and `M3` §2.1 (`EXT-2`, `EXT-9`). | `M1` §3 & `M3` §2.1 |
| **M-R08, M-R09** | Harrodian instability and mandatory Serrano/Freitas/Lavoie/Nikiforos debate engagement. | `UNSUPPORTED UNIVERSAL RULE` + `PROJECT-SPECIFIC SSM CONTENT` | **GENERALIZED & DEMOTED TO EXAMPLE**. Replaced by pluralist 14-question closure audit and demand-led utilization framework in `M1`. Sub-school debate retained as an illustrative example of normal utilization closures. | `M1` §3, §5.3 |
| **M-R10** | LaTeX standards: `amsthm` `\begin{proposition}`, `\begin{proof}`, `align`. | `PROSE / LATEX DUPLICATION` | **PURGED & DELEGATED**. Completely removed from macro skill; explicitly delegated to `econ-write` (`SKILL.md` lines 160–178). | `SKILL.md` §1.2 & `econ-write` |

---

## 4. Live Capability Contract

The live capability contract in `heterodox-economics-review/SKILL.md`:
- Defines the canonical author-side ownership of `heterodox_macro_modeling`.
- Explicitly delegates external peer review to `academic-paper-reviewer`, economics writing/LaTeX to `econ-write`, prose discipline to `prose_discipline_protocol.md`, econometric testing to `applied-econometrics-pe`, and historical process tracing to `political-economy-research`.
- Mandates the 6-stage modeling workflow:
  1. Construct & Notation $\to$ 2. Primitive Equation Classification $\to$ 3. Closure & Accounting Audit $\to$ 4. Dynamical System Reduction $\to$ 5. Equilibrium & Stability Analysis $\to$ 6. Theoretical Implication Mapping.
- Enforces the 14-Question Closure Audit, anti-tautology and singularity rules, the 8-step extension re-derivation protocol, and unbreachable cross-domain boundaries.

---

## 5. Module Architecture

The four implemented reference modules in `heterodox-economics-review/references/` provide cohesive, non-overlapping coverage:
- **`model_architecture_and_closures.md` (M1):** 7-part grammar, 6-way equation taxonomy, notation contract, 14-question closure audit, tradition boundary map (Marxian, Classical, Kaleckian, Harrodian, Kaldorian, Minskyan, Structuralist), and demand-led utilization dynamics (Keynesian stability, Bhaduri–Marglin, normal capacity).
- **`dynamic_systems_and_stability.md` (M2):** Intensive state reduction, admissible domain $\Omega$ and singularity checks, equilibrium concepts, nullclines, Jacobians, local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants), conservative centers vs. limit cycles, and conditional Poincaré–Bendixson (planar) and Hopf bifurcations.
- **`extensions_and_accounting.md` (M3):** Partitioned into Part I (Section 1.A Universal SFC Core: Balance-Sheet Matrix vs. Transactions-Flow Matrix accounting rules, Godley sectoral balances, stock-flow reconciliation/revaluation, redundant-equation awareness; Section 1.B Conditional SFC Closure & Portfolio Mechanisms: Brainard–Tobin adding-up restrictions and buffer-stock identification), Part II (9 extension operations, 8-step re-derivation protocol), and Part III (open-economy BOP constraints, Thirlwall's Law, center–periphery dynamics, contractionary devaluation, currency hierarchy).
- **`goodwin_baseline.md` (M4):** Canonical benchmark exemplar for state reduction and conservative center analysis.

---

## 6. Closure Framework Implementation

Implemented in `M1` §3:
- Enforces that no school label ("Keynesian", "Marxian", "Sraffian") may substitute for mathematical specification.
- Mandates the 14-question closure audit (`Q1`–`Q14`) examining output, utilization, investment, saving, distribution, wages/prices, employment, technical change, adjustment mechanisms, predetermined variables, clearing variables, exogenous/endogenous variables, and equation counting ($M = n + m$).

---

## 7. Dynamic-System Framework Implementation & D3.1 Applicability Verification

Implemented in `M2` (`dynamic_systems_and_stability.md`) and verified in Wave D3.1 (`NO EDIT REQUIRED`):
- Enforces the demarcation principle: $\text{ECONOMIC MECHANISM} \neq \text{MATHEMATICAL REPRESENTATION} \neq \text{PARAMETERIZATION}$.
- Mandates explicit declaration of state vector $\mathbf{x} \in \Omega$, checking boundary behavior $\partial\Omega$ and rational-function zero denominators $\mathcal{S}$.
- **Method-Applicability Scoping (`NO EDIT REQUIRED` in `M2`):**
  - `M2` line 22 explicitly prohibits invoking high-dimensional machinery (`Routh–Hurwitz` or `Hopf` bifurcations) when the dimensionality or mathematical structure does not warrant them;
  - `trace / determinant` (§5.1) applies to 2D local linearization;
  - `Routh–Hurwitz` (§5.2–5.3) applies where characteristic polynomial/dimensionality ($n \ge 3$) warrants;
  - `Poincaré–Bendixson` (§6.2) applies to applicable planar continuous systems ($n = 2$);
  - `Hopf` (§6.2) applies where relevant bifurcation conditions hold;
  - None is treated as a mandatory checklist item for every macro model.
- Prohibits calling every closed trajectory a limit cycle by proving the mathematical distinction between conservative centers (first integral $V(\mathbf{x}) = \text{const}$) and isolated dissipative limit cycles.

---

## 8. Accounting / SFC Framework Implementation

Implemented in `M3` (Part I):
- **Universal SFC Core (§1.A):**
  1. **Balance-Sheet Matrix Consistency (§1.1):** Distinguishes **Financial Asset / Liability Rows** (every financial asset held by one sector has an exact counterpart financial liability in another sector, $\sum_j A_{ij}^{\text{fin}} \equiv 0$) from **Real / Tangible Asset Rows** (physical capital $p_K K$, inventories $p_{INV} INV$, etc. appear as positive holdings without an offsetting liability entry, $\sum_j A_{ij}^{\text{real}} = K_{\text{tot}} > 0$) and **Sectoral Net-Worth Columns** ($\sum_i A_{ij} - NW_j = 0$, aggregating to $\sum_j NW_j \equiv K_{\text{tot}}$). Never states a generic zero-sum rule treating every row of both matrices identically.
  2. **Transactions-Flow Matrix Consistency (§1.2):** Every transaction row sums to zero across sectors ($\sum_j F_{ij} \equiv 0$), and every fully specified sectoral budget constraint column sums to zero ($\sum_i F_{ij} \equiv 0$) under the model's accounting convention.
  3. **Sectoral Budget Constraints & Financial Balances (§1.3):** Godley identity $(S - I) \equiv (G - T) + CAB$.
  4. **Stock-Flow Reconciliation & Accumulation/Revaluation (§1.4):** $\dot{S}_{ij} = F_{ij} - \delta_{ij} S_{ij} + \dot{p}_i Q_{ij}$.
  5. **Redundant-Equation Awareness (§1.5):** By Walras's Law / accounting identity, $N-1$ independent equations imply the $N$-th redundant equation $\mathcal{R}_N$.
- **Conditional SFC Closure & Portfolio Mechanisms (§1.B — `CAPABILITY SUPPORT ≠ UNIVERSAL REQUIREMENT`):**
  6. **Brainard–Tobin Portfolio Adding-Up Restrictions (§1.6 — `CONDITIONAL METHOD`):** Applies *only* when the model contains multiple assets ($m \ge 2$) and endogenous portfolio allocation ($\sum_{i=1}^m \lambda_{i0} = 1$, $\sum_{i=1}^m \lambda_{ik} = 0$). Single-asset or non-portfolio SFC models do not require Brainard–Tobin matrices.
  7. **Buffer-Stock Identification (§1.7 — `CONDITIONAL METHOD`):** Applies *only* when a buffer-stock mechanism is part of the model's stated closure.
- Confirms zero premature deterministic software tool creation in Wave D3.

---

## 9. Extension Grammar Implementation

Implemented in `M3` (Part II):
- Enforces the fundamental extension invariant: *Changing one equation does not necessarily change only one mechanism.*
- Catalogs the 9 canonical extension operations (`EXT-1` through `EXT-9`).
- Enforces the mandatory 8-step re-derivation checklist:
  1. Identify altered assumption $\to$ 2. Identify all affected equations $\to$ 3. Identify added/removed feedbacks $\to$ 4. Update state vector $\mathbf{x} \in \Omega$ $\to$ 5. Re-check accounting/SFC consistency $\to$ 6. Re-derive stationary states $\mathbf{x}^*$ and admissibility bounds $\to$ 7. Re-analyze local and global stability $\to$ 8. Reassess economic interpretation and observable implications.

---

## 10. Goodwin Import-Fidelity Audit

The promotion from `Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` to `goodwin_baseline.md` was audited and refined in Wave D3.1:
- **Provenance Discipline:** 100% of propositions remain classified under `GOODWIN-1967`, `LATER GOODWIN LITERATURE`, `BROADER HETERODOX TRADITION`, or `ARS ANALYTICAL SYNTHESIS`.
- **Purge of Unlabeled Localisms:** All unverified local workspace conventions were removed or explicitly labeled as illustrative examples.
- **Depreciation Fidelity (`GOODWIN-1967` vs. `LATER / ALTERNATIVE GROSS REPRESENTATION`):**
  - `GOODWIN-1967`: All quantities are formulated in real, net terms; depreciation therefore does not appear as a separate term in the canonical accumulation equation ($\dot{k} = q(1-\omega)$).
  - `LATER / ALTERNATIVE GROSS REPRESENTATION`: An explicit depreciation rate $\delta$ may be introduced ($\dot{k} = q(1-\omega) - \delta k$, where setting $\delta = 0$ is an equivalent later bookkeeping representation, never attributed literally to Goodwin 1967).
- **Lotka–Volterra Center Proof:** The first integral $V(e, \omega) = \text{const}$ proof of a conservative center is preserved in full.
- **Terminology Guardrail:** `GOODWIN BASELINE`, `GOODWIN-FAMILY MODEL`, and `GOODWIN-INSPIRED MODEL` are locked as an ARS analytical taxonomy.

---

## 11. Goodwin Non-Dominance Check

`heterodox-economics-review/SKILL.md` and `references/` were inspected to verify that Goodwin does not dominate routing or ontology:
- **State Spaces Supported Without Goodwin:** Natively supports models with no wage-share state (e.g., fixed-markup Kaleckian or Supermultiplier models $\mathbf{x} = (u, \gamma_Z)$), models with no employment state, pure capacity-utilization models, Minskyan debt models $\mathbf{x} = (u, d)$, and Thirlwall open-economy models.
- **Notation Scoping:** Goodwin notation $(e, \omega, a, w, q, k, \sigma, \alpha, \beta, \gamma, \rho)$ is strictly locked inside `M4` (`goodwin_baseline.md`) and is not required in `M1`, `M2`, or `M3`.

---

## 12. Political-Economy Boundary Check

Preserves Wave D1 Lock (`D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md` §10):
- Macro owns formal equations, closures, SFC matrices, dynamical stability, and formal open-economy models.
- `political-economy-research` owns comparative-historical sequences, periodization, institutions, and process tracing.
- Enforces Rules `MI-1` (formal model $\neq$ historical evidence), `MI-2` (closure justification flow), `MI-3` (exporting structured implications for PE's `A3`), and `MI-4` (`NO CROSS-METHOD OVERRIDE`).

---

## 13. Econometrics Boundary Check

Preserves Wave D2 Lock (`D2_APPLIED_ECONOMETRICS_BOUNDARY_REFACTOR.md` §0, §11, §18):
- Enforces $\text{THEORETICAL MODEL} \longrightarrow \text{derived implications} \longrightarrow \text{observable mapping} \longrightarrow \text{identification requirements} \longrightarrow \text{applied-econometrics-pe}$.
- Macro derives comparative statics, dynamic signs, phase relations, and equilibrium restrictions; it never owns stochastic admissibility, integration order, estimator selection, or empirical verdicts.
- Enforces `NO-AUTO-ESTIMATOR` (VAR, VECM, SVAR, state-space, threshold/TVP models are candidate empirical strategies, never automatic theoretical consequences).
- Enforces `NO-EPISTEMIC-INVERSION` (empirical non-findings or cointegration rejections cannot be inverted into confirmations of theoretical regime switching).

---

## 14. Adversarial Self-Audit

The live runtime files were tested against all 10 adversarial scenarios:

| Test ID | Scenario | Verification in Live Runtime Files | Verdict |
|:---|:---|:---|:---|
| **A** | Canonical Goodwin 2D model | Handled via `M4` (`goodwin_baseline.md`): Say's Law closure, real net quantities, exact ODEs, $(e^*, \omega^*)$, $V(e,\omega) = \text{const}$, conservative center. | **PASS** |
| **B** | Kaleckian demand-led model with endogenous utilization | Handled via `M1` §5: No $e$ state; endogenous $u^*$; Keynesian stability check; Bhaduri–Marglin wage-led vs. profit-led decomposition. | **PASS** |
| **C** | SFC model with balance sheets and debt | Handled via `M3` Part I: Universal SFC Core (Balance-Sheet & Transactions-Flow matrices, Godley identity, stock-flow reconciliation, redundant equation check) + conditional Brainard–Tobin / buffer-stock mechanisms where applicable. | **PASS** |
| **D** | Kaldor–Verdoorn endogenous productivity model | Handled via `M1` §4 and `M3` §2.1 (`EXT-2`): Dynamic scale economies $\hat{a}(\hat{Y})$; cumulative causation vs. stability bounds. | **PASS** |
| **E** | Center–periphery external-constraint model | Handled via `M3` Part III: Two-region structuralist asymmetry, Thirlwall's Law $\hat{Y}_{BOP} = \varepsilon_X \hat{Y}^* / \pi_M$, external debt ODEs. | **PASS** |
| **F** | Multi-sector accumulation model | Handled via `M1` §4 and `M3` §2.1 (`EXT-4`): Marxian Department I & II, relative price dynamics $p_1/p_2$, intersectoral allocation shares. | **PASS** |
| **G** | Macro model with NO wage-share state | Handled via `M1` §3 (Q5) and `M2` §2.1: Fixed-markup SSM $\mathbf{x} = (u, \gamma_Z)$ or debt-utilization $\mathbf{x} = (u, d)$; $\omega$ treated as exogenous parameter. | **PASS** |
| **H** | Linear 2D local-stability problem | Handled via `M2` §5.1: Constant Jacobian $J \equiv A$; necessary and sufficient trace/determinant conditions without invoking nonlinear cycles. | **PASS** |
| **I** | Nonlinear system with potential Hopf bifurcation | Handled via `M2` §6.2: Crossing speed $\left.\frac{d\operatorname{tr} J^*}{d\mu}\right|_{\mu_H} \neq 0$ and first Lyapunov coefficient separating supercritical from subcritical Hopf. | **PASS** |
| **J** | Theoretical implication contradicted by empirical evidence | Handled via `SKILL.md` §5.2 and `M1` §3: `NO CROSS-METHOD OVERRIDE` and `NO-EPISTEMIC-INVERSION` require transparent reporting and re-evaluating closures. | **PASS** |

**Adversarial Self-Audit Result:** **10/10 PASS.**

---

## 15. Candidate D5 Behavioral Evals (`PROPOSED — NOT AUTHORIZED`)

The seven behavioral eval fixtures specified in D3-A §24 (`D5-MACRO-01` through `D5-MACRO-07`) remain designated for implementation during Wave D5.

---

## 16. Candidate D6 Governance Updates (`PROPOSED — NOT AUTHORIZED`)

The registry update (`ars_registry.yaml` line 328 updating `heterodox_macro_modeling` description) and routing doc updates (`ROUTING_AND_PRECEDENCE.md`) remain designated for Wave D6 reconciliation.

---

## 17. Architect Learning Delta

In accordance with the ratified governance invariant `SELF-REPORTED LEARNING IS NOT SELF-RATIFYING`, every inherited lesson and new Wave D3 lesson was verified against concrete evidence in the generated runtime files:

| Lesson ID | Inherited / D3 Lesson | Concrete Artifact Evidence in Live Files Demonstrating Compliance | Verdict |
|:---|:---|:---|:---|
| **L1** | Behavior, Not Path, Determines Component Type | `SKILL.md` §1.2, `M3` Part I: Analytical SFC is an author-side reasoning obligation; zero deterministic tools created. | **VERIFIED IN ARTIFACT** |
| **L2** | Useful Implementation $\neq$ Universal Rule | `M1` §2, `M2` §2.3: SSM $\mu=1$ singularity and $\theta \neq 1$ critique demoted to illustrative examples; general anti-tautology and singularity rules codified. | **VERIFIED IN ARTIFACT** |
| **L3** | Theory Is Active but Non-Doctrinal | `SKILL.md` §4.2, `M1` §3–§4: 14-question closure audit applied neutrally across all traditions without crowning a single school. | **VERIFIED IN ARTIFACT** |
| **L4** | Inferential-Task Jurisdiction | `SKILL.md` §1.1, §5.1, §5.2: Mathematical derivations owned by Macro; process tracing owned by PE; estimation owned by Econometrics. | **VERIFIED IN ARTIFACT** |
| **L5** | No Cross-Method Override & Epistemic Inversion Prohibition | `SKILL.md` §5.2: Theoretical models cannot override econometric non-findings or declare that failed tests prove regime switching. | **VERIFIED IN ARTIFACT** |
| **L6** | Project-Specific Content Must Not Leak | `SKILL.md`, `M1`–`M4`: Zero un-demoted dissertation parameter thresholds, private variable tags, or thesis-specific claims. | **VERIFIED IN ARTIFACT** |
| **L7** | Lock Reasoning Obligations, Not Arbitrary Notation | `SKILL.md` §4.1, `M1` §1, `M4` §3: Goodwin notation locally locked in `M4`; general models define their own symbol tables. | **VERIFIED IN ARTIFACT** |
| **L8** | Human Sovereignty & Wave Scope | Working tree: Zero edits outside authorized live surface; all D5/D6/Wave-F items marked `PROPOSED — NOT AUTHORIZED`. | **VERIFIED IN ARTIFACT** |
| **L9** | Self-Reported Learning Is Not Self-Ratifying | Verified right here in §17 & §20: Every claimed lesson is paired with concrete line/section evidence in the live files. | **VERIFIED IN ARTIFACT** |
| **D3-L1** | Exemplar Benchmark $\neq$ Domain Ontology | `SKILL.md` §6, `M4`: Goodwin validated as benchmark exemplar; 10/10 adversarial self-audit confirms skill handles non-Goodwin models natively. | **VERIFIED IN ARTIFACT** |
| **D3-L2** | Equation-Level Closure Audit Over School Labels | `M1` §3: 14-question equation-level audit codified as mandatory gate. | **VERIFIED IN ARTIFACT** |
| **D3-L3** | Coupled-System Extension Re-Derivation Guard | `M3` §2.2: Mandatory 8-step re-derivation protocol codified. | **VERIFIED IN ARTIFACT** |
| **D3-L4** | Primary Source vs. Later Textbook Separation | `M4` §1, §3, §4: `GOODWIN-1967` real net variables (where depreciation does not appear as a separate term) cleanly separated from `LATER / ALTERNATIVE GROSS REPRESENTATION` explicit depreciation $\delta$. | **VERIFIED IN ARTIFACT** |
| **D3-L5** | Capability Support $\neq$ Universal Application Requirement | `SKILL.md` §1.1, §2, §3; `M2` §1, §5, §6; `M3` §1.A vs. §1.B: Universal SFC Core separated from conditional `Brainard–Tobin` / `buffer-stock` closures; `Routh–Hurwitz`, `Poincaré–Bendixson`, and `Hopf` scoped strictly to applicable dimensionality and structure. | **VERIFIED IN ARTIFACT** |

### Wave D3.1 Learning Delta Record (`D3-L5`)

```text
OBSERVED BEHAVIOR:
Earlier D3-B formulations grouped Brainard–Tobin portfolio adding-up restrictions and
buffer-stock identification alongside universal SFC accounting laws, and summarized
higher-order/nonlinear dynamical methods (Routh–Hurwitz, Poincaré–Bendixson, Hopf)
in module routing tables without consistently repeating their dimensionality and
structural preconditions. Additionally, Goodwin (1967)'s net formulation was summarized
using the shorthand "δ = 0", and balance-sheet / transactions-flow zero-sum rules risked
being read as an undifferentiated row rule across both matrices.

ARCHITECT INTERVENTION:
1. Distinguished GOODWIN-1967 (all quantities formulated in real, net terms so
   depreciation does not appear as a separate term) from LATER / ALTERNATIVE GROSS
   REPRESENTATION (explicit depreciation rate δ introduced, where δ = 0 is a later
   bookkeeping equivalence).
2. Separated the universal SFC core (balance-sheet consistency, transactions-flow
   consistency, sectoral budget constraints, stock-flow reconciliation, stock
   accumulation/revaluation, redundant-equation awareness) from conditional portfolio
   and closure mechanisms (Brainard–Tobin portfolio adding-up when multiple assets and
   endogenous portfolio choice exist; buffer-stock identification when a buffer-stock
   closure is stated).
3. Distinguished TRANSACTIONS-FLOW MATRIX (rows and columns sum to zero under the
   model's accounting convention) from BALANCE-SHEET MATRIX (financial asset/liability
   positions offset across sectors; sectoral columns balance with net worth; real/tangible
   assets need not have an offsetting liability entry).
4. Enforced the principle: CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT.

LEARNED PRINCIPLE:
A method can belong to a capability without being universally mandatory
(CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT). Domain capabilities must
explicitly separate universal structural invariants from conditional analytical methods
whose invocation depends on the model's dimensionality, asset structure, or closure
(e.g., Routh–Hurwitz, Poincaré–Bendixson, Hopf bifurcations, Brainard–Tobin portfolio
restrictions, and buffer-stock mechanisms).

GENERALIZATION SCOPE:
DOMAIN

PROMOTION STATUS:
LOCK

RATIONALE:
In formal macroeconomic and quantitative domain skills, including advanced methods in a
capability reference can easily mislead an agent into treating them as mandatory checklist
items for every model. Explicitly tagging conditional methods with their structural
activation conditions prevents false methodological critiques of simpler models while
preserving full analytical support when those structures are present.
```

---

## 18. D3-B / D3.1 Final Lock

```text
========================================================================================
FINAL ARCHITECTURAL & OPERATIONAL LOCK — heterodox-macro-modeling
STATUS: HUMAN-RATIFIED BINDING MACRO MODELING ARCHITECTURE — WAVE D3 CLOSED
========================================================================================

1. WHAT DOES heterodox-macro-modeling OWN?
   Author-side domain ownership of formal macroeconomic model construction, dimensional
   consistency, equation classification, equation-level closure auditing, analytical SFC
   accounting matrices, intensive state reduction, dynamical stability analysis (2D trace/det;
   3D+ Routh–Hurwitz where dimensionality warrants; conservative centers vs. limit cycles;
   conditional Poincaré–Bendixson and Hopf bifurcations where structure warrants), structured
   8-step model extensions, and theoretical implication mapping across heterodox traditions.

2. WHAT DOES IT CONSUME?
   Literature from deep-research; institutional regime evidence from political-economy-research;
   econometric estimates and break dates from applied-econometrics-pe; scholar/committee
   calibration parameters from profiles/*; and project overlays from workspaces.

3. WHAT DOES IT PRODUCE?
   Formal model specifications, symbol tables, 6-way equation ledgers, 14-question closure
   audit tables, SFC Balance-Sheet and Transaction-Flow matrices, reduced dynamical systems,
   stationary-state & admissibility proofs, Jacobian/stability evaluations, 8-step extension
   re-derivations, and structured theoretical implication maps.

4. WHAT DOES IT NEVER OWN?
   Simulated peer review or referee reports (academic-paper-reviewer); history-of-thought
   encyclopedias or doctrinal advocacy; econometric admissibility or statistical verdicts
   (applied-econometrics-pe); historical periodization or process tracing
   (political-economy-research); manuscript drafting (academic-paper); economics prose and
   amsthm LaTeX formatting (econ-write); or deterministic SFC software tools.

5. WHAT IS THE REQUIRED MODEL-CONSTRUCTION WORKFLOW?
   The 6-stage sequence: 1. Construct & Notation -> 2. Primitive Equation Classification ->
   3. Closure & Accounting Audit -> 4. Dynamical System Reduction -> 5. Equilibrium &
   Stability Analysis -> 6. Theoretical Implication Mapping.

6. WHAT IS THE REQUIRED CLOSURE AUDIT?
   The mandatory 14-question audit (M1 §3) determining what explains output, utilization,
   investment, saving, distribution, wages/prices, employment, and technical change; what
   adjusts when plans conflict; which variables are predetermined vs. clearing; and verifying
   mathematical closure (M = n + m).

7. WHAT MUST BE RE-DERIVED AFTER EXTENSION?
   Under the 8-step protocol (M3 §2.2): (1) altered assumption, (2) affected equations,
   (3) altered feedbacks, (4) state vector and domain Ω, (5) accounting/SFC consistency,
   (6) stationary states and admissibility bounds, (7) Jacobian and local/global stability,
   and (8) economic and observable implications.

8. WHAT ROLE DOES GOODWIN PLAY?
   Goodwin (1967) is an exemplar benchmark reference (goodwin_baseline.md) demonstrating
   state reduction, equation traceability, and conservative-center analysis (with all
   quantities in GOODWIN-1967 formulated in real, net terms, distinct from later gross
   representations introducing an explicit depreciation rate δ). It is NEVER the root
   ontology, default state space, or mandatory notation of the skill.

9. WHAT ROLE DOES SFC PLAY?
   Stock-Flow Consistency is an analytical accounting discipline owned in M3 separated into:
   (a) Universal SFC Core: Balance-Sheet Matrix consistency (financial asset/liability row
       offsetting, real/tangible asset rows without offsetting liabilities, sectoral net-worth
       column balance), Transactions-Flow Matrix consistency (row and column zero-sums under
       the model's accounting convention), sectoral budget constraints, stock-flow
       reconciliation, stock accumulation/revaluation, and redundant-equation awareness;
   (b) Conditional SFC Mechanisms: Brainard–Tobin portfolio adding-up restrictions (conditional
       on multiple assets and endogenous portfolio allocation) and buffer-stock identification
       (conditional on a buffer-stock mechanism being part of the stated closure)—without
       creating a deterministic tool in Wave D3.

10. HOW DOES MACRO COMPOSE WITH PE?
    Preserving Wave D1: Macro owns formal equations, closures, SFC, and dynamic systems; PE
    owns historical sequences, periodization, institutions, and process tracing. Macro exports
    observable implications (MI-3) and consumes institutional regime evidence (MI-2).
    NO CROSS-METHOD OVERRIDE.

11. HOW DOES MACRO COMPOSE WITH ECONOMETRICS?
    Preserving Wave D2: THEORETICAL MODEL -> derived implications -> observable mapping ->
    identification requirements -> applied-econometrics-pe. Macro derives theoretical
    restrictions; Econometrics owns stochastic admissibility, estimation, and empirical
    verdicts. NO-AUTO-ESTIMATOR and NO-EPISTEMIC-INVERSION govern.

12. WHAT REMAINS PROPOSED / NOT AUTHORIZED?
    - Deterministic SFC matrix-verification tool script (pending demonstrated need);
    - Gold behavioral eval fixtures for macro modeling (slated for Wave D5);
    - Registry and routing metadata updates to v1.2.0 (slated for Wave D6);
    - Physical directory rename to skills/domain/heterodox-macro-modeling/ (locked for Wave F).

13. WHAT REMAINS FOR D5?
    Implementing behavioral evaluation fixtures D5-MACRO-01 through D5-MACRO-07 in evals/gold/.

14. WHAT REMAINS FOR D6?
    Reconciling docs/governance/ars_registry.yaml and ROUTING_AND_PRECEDENCE.md.

15. WHAT REMAINS FOR WAVE F?
    Physical directory rename: heterodox-economics-review/ -> skills/domain/heterodox-macro-modeling/.
========================================================================================
```

---

## 19. Regression & Working-Tree Status

- **Automated Regression Test Suite:** All 6 repository test scripts executed; **100% PASS**:
  - `scripts/test_wave_c_reconciliation.py`: **11/11 PASS**
  - `scripts/validate_ars_registry.py`: **18 components, 20 capabilities PASS**
  - `scripts/test_routing_contract.py`: **17/17 cases PASS**
  - `scripts/test_prose_discipline.py`: **11/11 gold fixtures PASS**
  - `scripts/test_profile_contract.py`: **19/19 assertions PASS**
  - `scripts/test_revision_guard.py`: **12/12 cases PASS**
- **Git Hygiene:** `git diff --check` reported **0 errors**.
- **Working-Tree Integrity:**
  - Zero edits to `D0`, `D1`, or `D2` artifacts;
  - Zero edits to `umass-applied-econometrics/`;
  - Zero edits to `profiles/`, `shared/protocols/`, `docs/governance/`, or test suites;
  - Edits strictly confined to authorized live files in `heterodox-economics-review/` and `docs/design/wave-d/`;
  - Zero git commits, zero git pushes.

---

## 20. Wave D3.1 Source-Fidelity & Conditionality Freeze Audit

All D3 runtime files (`heterodox-economics-review/SKILL.md` and `heterodox-economics-review/references/*.md`) were searched for occurrences of `δ = 0` (`\delta = 0`), `Brainard`, `Tobin`, `buffer stock` (`buffer-stock`), `Routh–Hurwitz`, `Poincaré`, and `Hopf`. Every occurrence is classified below:

| File & Line | Matched Term(s) | Exact Context Summary | Classification |
|:---|:---|:---|:---|
| `SKILL.md:24` | `Routh–Hurwitz` | Local stability (`2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants`) and bifurcations where conditions warrant. | `CONDITIONAL METHOD` |
| `SKILL.md:62` | `Routh–Hurwitz` | Stage 5 workflow: `Evaluate local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants).` | `CONDITIONAL METHOD` |
| `SKILL.md:80` | `Routh–Hurwitz`, `Poincaré–Bendixson`, `Hopf` | M2 routing description: `local stability (2D trace/det; 3D+ Routh–Hurwitz where dimensionality warrants)... conditional Poincaré–Bendixson (planar) and Hopf bifurcation analysis.` | `CONDITIONAL METHOD` |
| `SKILL.md:81` | `Brainard–Tobin`, `buffer-stock` | M3 routing description: `Universal SFC core (...) + conditional Brainard–Tobin portfolio adding-up and buffer-stock closures`. | `CONDITIONAL METHOD` |
| `references/dynamic_systems_and_stability.md:22` | `Routh–Hurwitz`, `Hopf` | Core invariant 3: `Do not invoke high-dimensional machinery (e.g., Routh–Hurwitz or Hopf bifurcations) when the dimensionality or mathematical structure does not warrant them.` | `CONDITIONAL METHOD` |
| `references/dynamic_systems_and_stability.md:101` | `Routh–Hurwitz` | Section 5.2 heading: `Routh–Hurwitz Stability Theorem for n = 3` (explicitly scoped to 3D systems in §5.2 and $n \ge 4$ in §5.3). | `CONDITIONAL METHOD` |
| `references/dynamic_systems_and_stability.md:115` | `Poincaré–Bendixson`, `Hopf` | Table contrasting `Conservative Center (e.g., Goodwin 1967 Baseline)` vs. `Dissipative Limit Cycle (e.g., Poincaré–Bendixson / Hopf)`. | `ILLUSTRATIVE EXAMPLE` |
| `references/dynamic_systems_and_stability.md:124` | `Poincaré–Bendixson` | Section 6.2 item 1: `Poincaré–Bendixson Theorem (Planar Systems n = 2): If a compact trapping region...` | `CONDITIONAL METHOD` |
| `references/dynamic_systems_and_stability.md:125, 128` | `Hopf` | Section 6.2 item 2: `Hopf Bifurcation Theorem: When a parameter μ crosses a critical value μ_H...` (distinguishing supercritical vs. subcritical Hopf). | `CONDITIONAL METHOD` |
| `references/extensions_and_accounting.md:64` | `Brainard–Tobin` | Section 1.6 heading & rule under §1.B (`CAPABILITY SUPPORT ≠ UNIVERSAL REQUIREMENT`): `Brainard–Tobin Portfolio Adding-Up Restrictions (CONDITIONAL METHOD)` — applies only when multiple assets ($m \ge 2$) and endogenous portfolio allocation exist. | `CONDITIONAL METHOD` |
| `references/extensions_and_accounting.md:68–70` | `Buffer-Stock`, `buffer-stock` | Section 1.7 heading & rule under §1.B: `Buffer-Stock Identification (CONDITIONAL METHOD)` — applies only when a buffer-stock mechanism is part of the model's stated closure. | `CONDITIONAL METHOD` |
| `references/extensions_and_accounting.md:82` | `Routh–Hurwitz` | `EXT-3` (`ADD A STATE VARIABLE`): `when n >= 3, stability analysis upgrades to Routh–Hurwitz where dimensionality warrants.` | `CONDITIONAL METHOD` |
| `references/extensions_and_accounting.md:85` | `Poincaré–Bendixson`, `Hopf` | `EXT-6` (`ADD AN INSTITUTIONAL NONLINEARITY`): `may generate limit cycles (analyzed via Poincaré–Bendixson in planar systems or Hopf bifurcation where conditions warrant).` | `CONDITIONAL METHOD` |
| `references/extensions_and_accounting.md:120` | `Routh–Hurwitz` | Step 7 of 8-step re-derivation checklist: `evaluate 2D trace/determinant or 3D+ Routh-Hurwitz conditions where dimensionality warrants`. | `CONDITIONAL METHOD` |
| `references/goodwin_baseline.md:94` | `\delta = 0` | Section 4.C (`LATER / ALTERNATIVE GROSS REPRESENTATION`): `an explicit depreciation rate δ > 0 may be introduced (where setting δ = 0 is an equivalent later bookkeeping representation that recovers the net algebraic form, not a literal assumption stated by Goodwin 1967)`. | `SOURCE-FAITHFUL BASELINE` |

- **Total Occurrences Audited Across Live Runtime (`heterodox-economics-review/`):** 15 line locations (22 term matches)
- **`SOURCE-FAITHFUL BASELINE`:** 1
- **`CONDITIONAL METHOD`:** 13
- **`ILLUSTRATIVE EXAMPLE`:** 1
- **`RESIDUAL DEFECT`:** **0**
