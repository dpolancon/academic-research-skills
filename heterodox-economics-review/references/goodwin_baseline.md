# Reference Module M4: Goodwin (1967) Growth-Cycle Benchmark Exemplar

- **Module Role:** Canonical Pedagogical and Benchmark Reference Exemplar for `heterodox-macro-modeling`
- **Location:** `heterodox-economics-review/references/goodwin_baseline.md`
- **Canonical Meaning:** CANONICAL EXEMPLAR / BENCHMARK REFERENCE — Demonstrates state reduction, equation-to-primitive traceability, and conservative-center analysis.
- **Architectural Negative Invariant:** This module is **NOT** the universal ontology, default state space, or mandatory notation of heterodox macroeconomics.
- **Authority:** Promoted from validated candidate artifact `docs/design/wave-d/Goodwin_Canonical_Heterodox_Macro_Model_CANDIDATE.md` following Human Ratification in Wave D3-A.

---

## 1. Provenance Ledger & Import-Fidelity Audit

Every proposition, equation, and structural assumption in this reference is tagged with its validated epistemic classification:

| Tag | Epistemic Definition |
|:---|:---|
| `GOODWIN-1967` | Directly attributable to R. M. Goodwin (1967), "A Growth Cycle," in C. H. Feinstein (ed.), *Socialism, Capitalism and Economic Growth: Essays Presented to Maurice Dobb*, Cambridge University Press, pp. 54–58. |
| `LATER GOODWIN LITERATURE` | Attributable to subsequent mathematical literature, textbook formalizations, and extensions (e.g., Desai 1973; Shah & Desai 1981; van der Ploeg 1985; Flaschel 2009; Grasselli & Costa Lima 2012). |
| `BROADER HETERODOX TRADITION` | Marxian, Classical/Sraffian, Kaleckian, Post-Keynesian, or Kaldorian concepts intersecting with or contrasting against Goodwin. |
| `ARS ANALYTICAL SYNTHESIS` | Methodological classifications, equation traceability tables, and terminology guardrails developed within ARS for rigorous model auditing. |

---

## 2. Goodwin Terminology Guardrail (`ARS ANALYTICAL SYNTHESIS`)

To prevent conceptual conflation, this artifact enforces a strict three-tier classification:

```text
GOODWIN BASELINE (GOODWIN-1967)
    The canonical two-state (e, ω) 1967 closure: Say's Law / full-capacity profit-driven
    accumulation (S = I = Π), fixed capital-output ratio (σ), Harrod-neutral technical
    progress (α), exogenous labor force growth (β), and real-wage Phillips curve in
    employment rate e, producing a conservative Lotka–Volterra predator-prey center.

GOODWIN-FAMILY MODEL (LATER GOODWIN LITERATURE / ARS ANALYTICAL SYNTHESIS)
    Retains the recognizable cyclic accumulation–employment–distribution feedback core
    while modifying specific behavioral closures or adding states (e.g., Desai 1973
    nominal wage-price dynamics; Shah & Desai 1981 induced technical change; Keen 1995 /
    Grasselli & Costa Lima 2012 Minskyan private-debt 3D extension).

GOODWIN-INSPIRED MODEL (BROADER HETERODOX TRADITION / ARS ANALYTICAL SYNTHESIS)
    Imports selected Goodwin state variables or concepts, but operates under a materially
    different causal architecture or closure (e.g., Kaleckian demand-led utilization
    models; Sraffian Supermultiplier models; structuralist BOP-constrained models).
```

---

## 3. Local Notation Lock (`ARS ANALYTICAL SYNTHESIS`)

> **Architectural Guardrail:** The notation below is **locally locked** inside this Goodwin benchmark module. It is **never** globally binding across the general `heterodox-macro-modeling` skill. Note that original `GOODWIN-1967` used $u$ for the wage share and $v$ for the employment ratio; modern literature standardizes on $(\omega, e)$ to prevent collision with capacity utilization $u$.

| Symbol | Mathematical Definition | Economic Meaning | Dimensional Type | Original `GOODWIN-1967` Symbol |
|:---|:---|:---|:---|:---|
| $q(t)$ | $q > 0$ | Real aggregate net output (income) | Flow (real units / time) | $q$ |
| $k(t)$ | $k > 0$ | Real net capital stock | Stock (real units) | $k$ |
| $L(t)$ | $L > 0$ | Employed labor | Stock / Flow of labor | $l$ |
| $N(t)$ | $N > 0$ | Available labor supply | Stock | $n$ |
| $a(t)$ | $a \equiv q / L$ | Average labor productivity | Ratio (output / worker) | $a$ |
| $w(t)$ | $w > 0$ | Real wage rate per worker | Rate (output / worker) | $w$ |
| $\sigma$ | $\sigma \equiv k / q$ | Capital-output ratio (constant) | Ratio (time, stock / flow) | $\sigma$ |
| $\omega(t)$ | $\omega \equiv (w L)/q = w/a$ | Wage share of national income | Dimensionless share $\in (0,1)$ | $u$ |
| $\pi(t)$ | $\pi \equiv 1 - \omega = \Pi / q$ | Profit share of national income | Dimensionless share $\in (0,1)$ | $1 - u$ |
| $e(t)$ | $e \equiv L / N = q / (a N)$ | Employment rate | Dimensionless ratio $\in (0,1)$ | $v$ |
| $r(t)$ | $r \equiv \Pi / k = (1-\omega)/\sigma$ | Rate of profit on capital | Rate ($1/\text{time}$) | $(1-u)/\sigma$ |
| $\alpha$ | $\hat{a} \equiv \dot{a}/a = \alpha > 0$ | Exogenous productivity growth rate | Growth rate ($1/\text{time}$) | $\alpha$ |
| $\beta$ | $\hat{N} \equiv \dot{N}/N = \beta > 0$ | Exogenous labor-force growth rate | Growth rate ($1/\text{time}$) | $\beta$ |
| $\delta$ | $\delta > 0$ (optional in gross formulations) | Explicit capital depreciation rate (`LATER / ALTERNATIVE GROSS REPRESENTATION` only; absent in `GOODWIN-1967`) | Rate ($1/\text{time}$) | Absent (all quantities in real, net terms) |
| $\gamma, \rho$ | $\hat{w} = -\gamma + \rho e$ ($\gamma, \rho > 0$) | Real-wage Phillips curve parameters | Parameters ($1/\text{time}$) | $-\gamma + \rho v$ |

---

## 4. Validated Baseline Derivations (Items A–P)

### A. Canonical Assumptions (`GOODWIN-1967`)
1. Steady disembodied Harrod-neutral technical progress: $\hat{a} = \alpha > 0$ (`TECH` / `EXOG`).
2. Steady labor supply growth: $\hat{N} = \beta > 0$ (`EXOG`).
3. Homogeneous output and factors: 1-sector economy, no relative price wedges (`TECH` / `ID`).
4. Real, net quantities: all quantities ($q$ and $k$) are formulated in real, net terms; depreciation therefore does not appear as a separate term in the canonical accumulation equation (`ID`).
5. Classical class savings: all wages consumed, all profits saved and invested ($S = \Pi = (1-\omega)q$) (`BEH` / `INST`).
6. Say's Law / full-capacity closure: $I \equiv \dot{k} = S$, with utilization fixed at full capacity ($u = 1$) (`CLOS`).
7. Fixed capital-output ratio: $\sigma = k/q = \text{const} \implies \hat{q} = \hat{k}$ (`TECH` / `CLOS`).
8. Real-wage Phillips curve: $\hat{w} = -\gamma + \rho e$ ($\gamma > 0, \rho > 0$) (`BEH` / `INST`).

### B. Definitions & Logarithmic Time Derivatives (`GOODWIN-1967` + `ARS ANALYTICAL SYNTHESIS`)
- Wage share: $\omega \equiv w/a \implies \hat{\omega} = \hat{w} - \hat{a}$.
- Employment rate: $e \equiv L/N = q/(a N) \implies \hat{e} = \hat{q} - \hat{a} - \hat{N}$.

### C. Accumulation Equation & G. Depreciation (`GOODWIN-1967` vs. `LATER GOODWIN LITERATURE`)
- **`GOODWIN-1967` (Real, Net Terms):**
  All quantities are formulated in real, net terms; depreciation therefore does not appear as a separate term in the canonical accumulation equation:
  $$\hat{k} = \frac{\dot{k}}{k} = \frac{(1-\omega)q}{k} = \frac{1-\omega}{\sigma} = r$$
- **`LATER / ALTERNATIVE GROSS REPRESENTATION` (`LATER GOODWIN LITERATURE`):**
  In later textbook or gross-output representations, an explicit depreciation rate $\delta > 0$ may be introduced (where setting $\delta = 0$ is an equivalent later bookkeeping representation that recovers the net algebraic form, not a literal assumption stated by Goodwin 1967):
  $$\hat{k} = \frac{1-\omega}{\sigma} - \delta$$

### D. Wage-Share Law of Motion & E. Role of Productivity Growth $\alpha$
Substituting $\hat{w} = -\gamma + \rho e$ and $\hat{a} = \alpha$ into $\hat{\omega} = \hat{w} - \hat{a}$:
$$\dot{\omega} = \omega \left[ -(\alpha + \gamma) + \rho e \right]$$
*Role of $\alpha$:* Technical progress reduces unit labor requirements and exerts continuous downward pressure on $\omega$, enabling real wages to grow at rate $\alpha$ in the steady state without exhausting profits.

### F. Employment Law of Motion, H. Constant $\sigma$, and Natural Rate $\beta$
Substituting the canonical net accumulation rate $\hat{q} = \hat{k} = \frac{1-\omega}{\sigma}$, $\hat{a} = \alpha$, and $\hat{N} = \beta$ into $\hat{e} = \hat{q} - \alpha - \beta$ (`GOODWIN-1967`):
$$\dot{e} = e \left[ \frac{1-\omega}{\sigma} - (\alpha + \beta) \right]$$
*(In the `LATER / ALTERNATIVE GROSS REPRESENTATION` with explicit depreciation rate $\delta$, the natural-plus-replacement threshold becomes $\alpha + \beta + \delta$.)*

### J. Reduced Two-Dimensional Autonomous System (`GOODWIN-1967`)
$$\begin{aligned}
\dot{e} &= e \left[ \frac{1 - \omega}{\sigma} - (\alpha + \beta) \right] \equiv F_1(e, \omega) \\[6pt]
\dot{\omega} &= \omega \left[ -(\alpha + \gamma) + \rho e \right] \equiv F_2(e, \omega)
\end{aligned}$$
*(In the `LATER / ALTERNATIVE GROSS REPRESENTATION`, an explicit depreciation rate $\delta$ enters $F_1$ via $-(\alpha + \beta + \delta)$.)*

### K. Interior Stationary State & Nullclines (`GOODWIN-1967`)
- **Nullclines:** $\dot{e} = 0 \implies \omega^* = 1 - \sigma(\alpha + \beta)$ (horizontal line); $\dot{\omega} = 0 \implies e^* = \frac{\alpha + \gamma}{\rho}$ (vertical line).
- **Interior Equilibrium (`GOODWIN-1967`):**
  $$(e^*, \omega^*) = \left( \frac{\alpha + \gamma}{\rho}, \;\; 1 - \sigma(\alpha + \beta) \right)$$
  *(In the `LATER / ALTERNATIVE GROSS REPRESENTATION`, $\omega^* = 1 - \sigma(\alpha + \beta + \delta)$.)*

### L. Economic Admissibility Conditions
Interior admissibility $(e^*, \omega^*) \in (0, 1)^2$ in the canonical net formulation requires:
$$0 < \alpha + \gamma < \rho \qquad \text{and} \qquad 0 < \alpha + \beta < \frac{1}{\sigma}$$
*(or $0 < \alpha + \beta + \delta < \frac{1}{\sigma}$ when an explicit gross depreciation rate $\delta$ is introduced).*

### M. Lotka–Volterra Structure & Exact First Integral (`GOODWIN-1967`)
Letting $A_1 = \frac{1}{\sigma} - (\alpha+\beta)$ (or $\frac{1}{\sigma} - (\alpha+\beta+\delta)$ in the gross representation), $B_1 = \frac{1}{\sigma}$, $A_2 = \alpha+\gamma$, $B_2 = \rho$:
$$\dot{e} = e(A_1 - B_1 \omega), \qquad \dot{\omega} = \omega(-A_2 + B_2 e)$$
Dividing ODEs separates variables, yielding the exact conserved Lyapunov-type first integral:
$$V(e, \omega) = \frac{1}{\sigma} (\omega^* \ln \omega - \omega) + \rho (e^* \ln e - e) = C_0$$
Along any trajectory, $\dot{V}(e, \omega) \equiv 0$. Level sets of $V$ form closed concentric orbits surrounding $(e^*, \omega^*)$.

### N. Local Stability: Jacobian, Purely Imaginary Eigenvalues, and Non-Hyperbolic Center
Evaluating the Jacobian at $(e^*, \omega^*)$:
$$J^* = \begin{bmatrix} 0 & -\dfrac{e^*}{\sigma} \\[8pt] \rho \omega^* & 0 \end{bmatrix}$$
- **Trace:** $\operatorname{tr}(J^*) = 0$.
- **Determinant:** $\det(J^*) = \frac{\rho}{\sigma} e^* \omega^* > 0$.
- **Eigenvalues:** $\lambda_{1,2} = \pm i \sqrt{\frac{\rho}{\sigma} e^* \omega^*}$ (purely imaginary).
- *Nonlinear Proof:* Because $\operatorname{tr}(J^*) = 0$ is non-hyperbolic, linearization alone is inconclusive. The existence of the strictly convex first integral $V(e, \omega)$ proves that $(e^*, \omega^*)$ is a **conservative nonlinear center**. Trajectories circulate counterclockwise in the $(e, \omega)$ plane.

### O. Closed Orbits (Conservative Center) vs. Dissipative Limit Cycles
- The baseline Goodwin cycle consists of a **one-parameter continuum of closed orbits** whose amplitude depends permanently on initial conditions $\mathbf{x}(0)$.
- It is **structurally unstable** (any perturbation to the diagonal of $J^*$ destroys the closed orbits).
- It is **not** an isolated dissipative limit cycle.

### P. Relaxing Goodwin Assumptions: Why Changing One Equation Changes Dynamics
- **Endogenous Utilization (Kaleckian synthesis):** Breaks $I \equiv S$ and $u=1$; introduces diagonal terms $J_{ii}^* \neq 0$; enables wage-led or profit-led regimes.
- **Private Debt (Keen 1995 / Minsky synthesis):** Expands state vector to 3D $\mathbf{x} = (e, \omega, d)$; adds debt service $i d$; introduces debt-deflation crisis dynamics.
- **Induced Technical Change ($\hat{a} = \phi(\omega), \phi' > 0$):** Adds negative diagonal entry $J_{22}^* = -\omega^* \phi'(\omega^*) < 0$, making $\operatorname{tr}(J^*) < 0$ and converting the conservative center into an **asymptotically stable focus**.
