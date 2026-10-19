STATUS:
CANDIDATE KNOWLEDGE ARTIFACT — NOT YET CANONICAL

# Goodwin (1967) Growth-Cycle Benchmark & Analytical Reference Architecture

- **Document Role:** Candidate Knowledge Artifact for Wave D3-A Validation (Exemplar Reference Candidate `goodwin_baseline.md` for future `heterodox-macro-modeling` skill)
- **Authority:** CANDIDATE KNOWLEDGE INPUT — Validated for mathematical and historical-source accuracy in Wave D3-A; subject to Architect ratification before promotion to runtime skill reference in Wave D3-B.
- **Architectural Constraint:** Goodwin (1967) serves as a **canonical benchmark and pedagogical exemplar** for state-space reduction, accounting-to-dynamics derivation, and growth-distribution feedback. It is **NOT** the master template or root ontology of `heterodox-macro-modeling`.
- **Governing Checkpoint:** `917ee2f2332cef92015937bddd7337a52ef4b12d`

---

## 1. SOURCE DISCIPLINE & PROVENANCE LEDGER

Every proposition, assumption, equation, and analytical taxonomy in this artifact is explicitly tagged with one of the following six epistemic provenance labels:

| Tag | Definition |
|:---|:---|
| `GOODWIN-1967` | Directly attributable to R. M. Goodwin (1967), "A Growth Cycle," in C. H. Feinstein (ed.), *Socialism, Capitalism and Economic Growth: Essays Presented to Maurice Dobb*, Cambridge: Cambridge University Press, pp. 54–58. |
| `LATER GOODWIN LITERATURE` | Attributable to subsequent mathematical formalizations, textbook syntheses, or extensions of the Goodwin growth cycle (e.g., Desai 1973; Shah & Desai 1981; van der Ploeg 1985; Barbosa-Filho & Taylor 2006; Veneziani & Mohun 2006; Flaschel 2009; Grasselli & Costa Lima 2012). |
| `BROADER HETERODOX TRADITION` | Concepts drawn from Marxian, Classical/Sraffian, Kaleckian, Post-Keynesian, Harrodian, Kaldorian, Minskyan, structuralist, institutionalist, or ecological macroeconomics that intersect with or critique Goodwin (1967). |
| `PROJECT-SPECIFIC CONVENTION` | Notation, parameterizations, or framing conventions originating in local research workspaces rather than canonical literature. |
| `ARS ANALYTICAL SYNTHESIS` | Methodological classifications, equation-traceability ledgers, and structural comparison taxonomies synthesized by ARS for modeling rigor. |
| `SOURCE VALIDATION REQUIRED` | Marker applied wherever a historical or literature attribution cannot be verified from established primary sources without external bibliographic lookup. |

---

## 2. GOODWIN TERMINOLOGY GUARDRAIL (`ARS ANALYTICAL SYNTHESIS`)

To prevent conceptual slippage where every model containing a wage share or employment rate is loosely labeled "a Goodwin model," this artifact enforces a strict three-tier classification. This taxonomy is an **`ARS ANALYTICAL SYNTHESIS`** for model-architecture auditing; it is not claimed as universal terminology across the published literature:

```text
GOODWIN BASELINE (GOODWIN-1967)
    The canonical two-state (e, omega) 1967 closure: Say's Law / full-capacity
    profit-led accumulation (S = I = Pi), fixed capital-output ratio (sigma),
    harrod-neutral disembodied technical progress (alpha), exogenous labor force
    growth (beta), and real-wage Phillips curve in employment rate e, yielding a
    conservative Lotka–Volterra predator-prey center with closed orbits.

GOODWIN-FAMILY MODEL (LATER GOODWIN LITERATURE / ARS ANALYTICAL SYNTHESIS)
    Retains the recognizable cyclic accumulation–employment–distribution feedback
    core (profit-squeezing wage dynamics coupled with profitability-driven accumulation)
    while modifying specific behavioral closures, functional forms, or adding states
    (e.g., Desai 1973 nominal wage-price dynamics; Shah & Desai 1981 induced technical
    change; Keen 1995 / Grasselli & Costa Lima 2012 Minskyan private-debt 3D extension).

GOODWIN-INSPIRED MODEL (BROADER HETERODOX TRADITION / ARS ANALYTICAL SYNTHESIS)
    Imports selected Goodwin state variables (such as e or omega) or distributional
    terminology, but operates under a materially different causal architecture or closure
    (e.g., Kaleckian demand-led utilization closures where output is demand-determined
    and wage-led growth is possible; Sraffian Supermultiplier models with autonomous
    demand driving long-run growth; structuralist BOP-constrained models).
```

---

## 3. LOCAL NOTATION LOCK (`ARS ANALYTICAL SYNTHESIS` / `PROJECT-SPECIFIC CONVENTION`)

> **Architectural Rule:** The notation table below is **locally locked** inside this Goodwin benchmark artifact to ensure internal mathematical consistency. The general `heterodox-macro-modeling` skill **must not** universalize this notation across non-Goodwin models (where $\sigma$, $q$, $\omega$, or $u$ may carry distinct tradition-specific meanings). Note also that original `GOODWIN-1967` used $u$ for the workers' share of product and $v$ for the employment ratio; using $(\omega, e)$ is a standard convention from `LATER GOODWIN LITERATURE` adopted here to avoid colliding with capacity utilization $u$ in broader heterodox models.

| Symbol | Mathematical Definition | Economic Meaning | Dimensional Type | Original `GOODWIN-1967` Symbol |
|:---|:---|:---|:---|:---|
| $q(t)$ | $q > 0$ | Real aggregate net output (income) | Flow (real units / time) | $q$ |
| $k(t)$ | $k > 0$ | Real net capital stock | Stock (real units) | $k$ |
| $L(t)$ | $L > 0$ | Employed labor | Stock / Flow of labor services | $l$ |
| $N(t)$ | $N > 0$ | Available labor supply | Stock | $n$ |
| $a(t)$ | $a \equiv q / L$ | Average labor productivity | Ratio (output / worker) | $a$ |
| $w(t)$ | $w > 0$ | Real wage rate per unit of labor | Rate (output / worker) | $w$ |
| $\sigma$ | $\sigma \equiv k / q$ | Capital-output ratio (assumed constant) | Ratio (time, stock / flow) | $\sigma$ |
| $\omega(t)$ | $\omega \equiv (w L) / q = w / a$ | Wage share of national income | Dimensionless share $\in (0,1)$ | $u$ |
| $\pi(t)$ | $\pi \equiv 1 - \omega = \Pi / q$ | Profit share of national income | Dimensionless share $\in (0,1)$ | $1 - u$ |
| $e(t)$ | $e \equiv L / N = q / (a N)$ | Employment rate | Dimensionless ratio $\in (0,1)$ | $v$ |
| $r(t)$ | $r \equiv \Pi / k = (1 - \omega) / \sigma$ | Rate of profit on capital | Rate ($1/\text{time}$) | $(1-u)/\sigma$ |
| $\alpha$ | $\hat{a} \equiv \dot{a}/a = \alpha > 0$ | Exogenous Harrod-neutral productivity growth rate | Growth rate ($1/\text{time}$) | $\alpha$ |
| $\beta$ | $\hat{N} \equiv \dot{N}/N = \beta > 0$ | Exogenous labor-force growth rate | Growth rate ($1/\text{time}$) | $\beta$ |
| $\delta$ | $\delta \ge 0$ | Capital depreciation rate ($\delta=0$ in `GOODWIN-1967`) | Rate ($1/\text{time}$) | Absent (net output/capital used) |
| $\gamma, \rho$ | $\hat{w} = -\gamma + \rho e$ ($\gamma > 0, \rho > 0$) | Linearized real-wage Phillips curve parameters | Parameters ($1/\text{time}$) | $-\gamma + \rho v$ |

*Notation convention:* For any differentiable variable $x(t) > 0$, a dot denotes the time derivative $\dot{x} \equiv dx/dt$, and a hat denotes the proportional growth rate $\hat{x} \equiv \dot{x}/x = d(\ln x)/dt$.

---

## 4. COMPLETE VALIDATION LEDGER: ITEMS A–P

### A. Canonical Assumptions (`GOODWIN-1967`)

Every structural assumption of the canonical 1967 model is classified below by its role in the modeling grammar (`ARS ANALYTICAL SYNTHESIS`):

| ID | Assumption Statement | Provenance Tag | Grammar Classification | Role in Generating the 2D Closure |
|:---|:---|:---|:---|:---|
| **A1** | **Steady Disembodied Harrod-Neutral Technical Progress:** Labor productivity $a = q/L$ grows at a constant exogenous rate $\hat{a} = \alpha > 0$. | `GOODWIN-1967` | `Exogenous process` + `Technological assumption` | Decouples productivity growth from accumulation and distribution; provides the downward drift $-\alpha$ on the wage share $\omega$. |
| **A2** | **Steady Exogenous Labor Supply Growth:** Labor force $N$ grows at a constant exogenous rate $\hat{N} = \beta > 0$. | `GOODWIN-1967` | `Exogenous process` | Fixes the natural growth rate benchmark $g_n = \alpha + \beta$ against which output growth $\hat{q}$ determines $\hat{e}$. |
| **A3** | **Two Homogenous Factors (Labor and Capital), Single Good:** Homogeneous output $q$ is usable either for consumption or capital accumulation; no price-of-production relative price shifts. | `GOODWIN-1967` | `Technological assumption` / `Accounting structure` | Eliminates relative price dynamics between wage goods and capital goods (contra Sraffian multi-sector models). |
| **A4** | **All Quantities Real and Net:** Income $q$ and capital $k$ are defined in real net terms (or capital is immortal, $\delta = 0$). | `GOODWIN-1967` | `Accounting structure` | Avoids price-level/inflation equations and gross-to-net depreciation wedges in the baseline. |
| **A5** | **Classical / Marxian Class Savings Assumption:** All wages are consumed ($C_w = wL$); all profits are saved and automatically invested ($S = \Pi = (1-\omega)q$). | `GOODWIN-1967` | `Behavioral relation` + `Institutional assumption` | Eliminates worker wealth/debt accumulation (no Pasinetti state variable) and links saving directly to the profit share $1-\omega$. |
| **A6** | **Say's Law / Full-Capacity Investment-Saving Identity:** Investment equals saving identically ($I \equiv \dot{k} = S = (1-\omega)q$), with no independent investment demand function and no variable capacity utilization. | `GOODWIN-1967` | `Closure rule` | Closes goods market by making accumulation purely profit-driven ($\hat{k} = (1-\omega)/\sigma$); suppresses Keynesian effective-demand and Harrodian utilization states. |
| **A7** | **Fixed Capital-Output Ratio (Leontief Technology at Full Capacity):** $\sigma = k/q$ is constant ($\hat{\sigma} = 0 \implies \hat{q} = \hat{k}$). | `GOODWIN-1967` | `Technological assumption` + `Closure rule` | Eliminates smooth neoclassical factor substitution ($K/L$ responds only through $\alpha$) and equates output growth $\hat{q}$ directly to capital growth $\hat{k}$. |
| **A8** | **Real-Wage Bargain Driven by Employment Rate (Reserve Army / Real Phillips Curve):** Real wage growth $\hat{w} = f(e)$ with $f'(e) > 0$, rises steeply near full employment ($e \to 1$), and is linearized around the operating range as $\hat{w} = -\gamma + \rho e$ ($\gamma > 0, \rho > 0$). | `GOODWIN-1967` | `Behavioral relation` + `Institutional assumption` | Supplies the distributive feedback from labor-market tightness $e$ to real wage growth $\hat{w}$, closing the predator-prey loop. |

---

### B. Definitions of $e$ and $\omega$ & Accounting Identities (`GOODWIN-1967` + `ARS ANALYTICAL SYNTHESIS`)

1. **Income Decomposition Identity (`Identity`):**
   $$q \equiv w L + \Pi$$
   Dividing through by $q > 0$ defines the **wage share** $\omega$ and **profit share** $\pi$:
   $$\omega \equiv \frac{w L}{q} = \frac{w}{q / L} = \frac{w}{a}, \qquad \pi \equiv \frac{\Pi}{q} = 1 - \omega$$
   - *Dimensional verification:* $w$ has units $[\text{output}/\text{worker}]$, $a$ has units $[\text{output}/\text{worker}]$, so $\omega = w/a$ is a dimensionless share. Economic admissibility requires $\omega \in (0, 1)$ so that both wages and profits are strictly positive.

2. **Labor-Market Ratio Definition (`Identity`):**
   $$e \equiv \frac{L}{N} = \frac{q / a}{N} = \frac{q}{a N}$$
   - *Dimensional verification:* $L$ and $N$ are both measured in workers, so $e$ is a dimensionless ratio. Because employed labor cannot exceed the total available labor force in a closed economy without overtime/participation elasticity, economic admissibility requires $e \in (0, 1)$.

---

### C. Accumulation Equation & G. Treatment of Depreciation (`GOODWIN-1967` vs. `LATER GOODWIN LITERATURE`)

It is essential to distinguish the exact `GOODWIN-1967` formulation from the textbook augmentation with explicit capital depreciation $\delta$:

1. **Original `GOODWIN-1967` Formulation (Net Output / $\delta = 0$):**
   - *Accounting Identity (`Identity`):* $\dot{k} = I$ (where $k$ and $q$ are already net of depreciation).
   - *Class Savings & Say's Law Closure (`Behavioral relation` + `Closure rule`):* $I = S = \Pi = (1 - \omega)q$.
   - *Fixed Capital-Output Ratio (`Technological assumption`):* $\sigma = k/q \implies q/k = 1/\sigma$.
   - *Resulting Capital Growth Rate:*
     $$\hat{k} \equiv \frac{\dot{k}}{k} = \frac{(1 - \omega)q}{k} = \frac{1 - \omega}{\sigma} = r$$
   Thus, under `GOODWIN-1967`, the rate of capital accumulation equals the rate of profit $r = (1-\omega)/\sigma$ (the Cambridge equation $g_K = s_c r$ with $s_c = 1$).

2. **Textbook Gross-Investment / Explicit Depreciation Formulation (`LATER GOODWIN LITERATURE`):**
   - Many later expositions define $q$ as gross output and introduce a constant proportional capital depreciation rate $\delta \ge 0$:
     $$\dot{k} = I_{\text{gross}} - \delta k = (1 - \omega)q - \delta k \implies \hat{k} = \frac{1 - \omega}{\sigma} - \delta$$
   - **Verification Note (`ARS ANALYTICAL SYNTHESIS`):** Setting $\delta = 0$ recovers `GOODWIN-1967` exactly. Including $\delta > 0$ does not alter the qualitative Lotka–Volterra dynamics or the Jacobian trace, because $\delta$ is a constant that simply shifts the required gross profit rate at the stationary state from $\alpha + \beta$ to $\alpha + \beta + \delta$. In the derivations below, we write $\delta \ge 0$ in brackets `[+ \delta]` so that both the strict `GOODWIN-1967` equation ($\delta = 0$) and the `LATER GOODWIN LITERATURE` textbook equation ($\delta > 0$) are transparently represented without conflation.

---

### D. Wage-Share Derivation & E. Role of Productivity Growth $\alpha$ (`GOODWIN-1967`)

Starting from the definitional identity $\omega \equiv w / a$:
1. Take logarithmic time derivatives (`Identity`):
   $$\hat{\omega} \equiv \frac{\dot{\omega}}{\omega} = \hat{w} - \hat{a}$$
2. Substitute the exogenous productivity growth process (`Exogenous process` A1: $\hat{a} = \alpha$) and the real-wage Phillips relation (`Behavioral relation` A8: $\hat{w} = -\gamma + \rho e$):
   $$\hat{\omega} = -\gamma + \rho e - \alpha = -(\alpha + \gamma) + \rho e$$
3. Multiply through by $\omega$ to obtain the state differential equation for the wage share:
   $$\dot{\omega} = \omega \left[ -(\alpha + \gamma) + \rho e \right]$$

- **Role of Productivity Growth $\alpha$ (`GOODWIN-1967`):** Technical progress $\alpha > 0$ continuously lowers unit labor requirements ($L/q = 1/a$). For a given real wage growth $\hat{w}$, productivity growth acts as a structural downward pressure on the wage share ($\partial \hat{\omega} / \partial \alpha = -1$), preventing rising real wages from immediately exhausting profits and allowing positive steady-state real wage growth ($\hat{w}^* = \alpha > 0$) alongside a constant steady-state wage share ($\dot{\omega} = 0$).

---

### F. Role of Labor-Force Growth $\beta$ & H. Fixed Capital-Output Ratio $\sigma$ (`GOODWIN-1967`)

Starting from the definitional identity $e \equiv L / N = q / (a N)$:
1. Take logarithmic time derivatives (`Identity`):
   $$\hat{e} \equiv \frac{\dot{e}}{e} = \hat{q} - \hat{a} - \hat{N}$$
2. Apply the fixed capital-output ratio (`Technological assumption` + `Closure rule` A7: $\sigma = k/q = \text{const} \implies \hat{q} = \hat{k}$):
   $$\hat{e} = \hat{k} - \hat{a} - \hat{N}$$
3. Substitute the accumulation equation ($\hat{k} = \frac{1-\omega}{\sigma} - \delta$), productivity growth ($\hat{a} = \alpha$), and labor-force growth ($\hat{N} = \beta$):
   $$\hat{e} = \frac{1 - \omega}{\sigma} - (\alpha + \beta + \delta)$$
   *(where $\delta = 0$ in `GOODWIN-1967` and $\delta > 0$ in `LATER GOODWIN LITERATURE`).*
4. Multiply through by $e$ to obtain the state differential equation for the employment rate:
   $$\dot{e} = e \left[ \frac{1 - \omega}{\sigma} - (\alpha + \beta + \delta) \right]$$

- **Role of $\beta$ (`GOODWIN-1967`):** Together with productivity growth $\alpha$, labor supply growth $\beta$ defines Harrod's natural rate of growth $g_n \equiv \alpha + \beta$. Employment rate $e$ rises ($\dot{e} > 0$) if and only if the warranted/actual profit-driven accumulation rate $\hat{k} = (1-\omega)/\sigma - \delta$ exceeds the natural growth rate $\alpha + \beta$.
- **Role of $\sigma$ (`GOODWIN-1967`):** $\sigma$ governs the sensitivity of output and employment growth to changes in the profit share ($\partial \hat{e} / \partial \omega = -1/\sigma$) and locks output growth to capital growth ($\hat{q} = \hat{k}$).

---

### I. Wage Phillips Relation (`GOODWIN-1967` vs. `LATER GOODWIN LITERATURE`)

1. **In `GOODWIN-1967`:** Goodwin posits a **real-wage** bargaining curve directly in terms of the employment rate:
   $$\frac{\dot{w}}{w} = f(e), \qquad f'(e) > 0, \qquad \lim_{e \to 1^-} f(e) = +\infty$$
   Goodwin then linearizes $f(e)$ for analytical tractability as:
   $$\frac{\dot{w}}{w} = -\gamma + \rho e, \qquad \gamma > 0, \quad \rho > 0$$
2. **Conceptual Distinction (`LATER GOODWIN LITERATURE` / `BROADER HETERODOX TRADITION`):**
   - Original Phillips (1958) formulated a *nominal* wage growth curve against unemployment. By writing $\dot{w}/w = f(e)$ in *real* terms, `GOODWIN-1967` implicitly assumes either a fixed price level, money-illusion-free real wage bargaining, or constant mark-up pricing where nominal wage increases translate one-for-one into real wage changes (`Institutional assumption`).
   - Subsequent extensions (`LATER GOODWIN LITERATURE`, e.g., Desai 1973; Flaschel 2009) separate nominal wage bargaining $\hat{W} = f(e) + \eta \hat{p}^e$ from price inflation $\hat{p}$ determined by conflict-inflation markups or capacity utilization.
   - Note also that the linearized approximation $\hat{w} = -\gamma + \rho e$ does **not** automatically enforce the upper ceiling $e < 1$, whereas a nonlinear asymptote $\lim_{e \to 1^-} f(e) = +\infty$ prevents $e$ from crossing $1$.

---

### J. Reduced Two-Dimensional Dynamical System & Equation Traceability (`GOODWIN-1967` + `ARS ANALYTICAL SYNTHESIS`)

Combining the derivations in C–I yields the closed 2D autonomous nonlinear system in the state vector $\mathbf{x} = (e, \omega)^T \in \mathbb{R}_+^2$:

$$\begin{aligned}
\dot{e} &= e \left[ \frac{1 - \omega}{\sigma} - (\alpha + \beta + \delta) \right] \equiv F_1(e, \omega) \\[6pt]
\dot{\omega} &= \omega \left[ -(\alpha + \gamma) + \rho e \right] \equiv F_2(e, \omega)
\end{aligned}$$
*(with $\delta = 0$ in `GOODWIN-1967`).*

#### Equation-to-Primitive Traceability Matrix (`ARS ANALYTICAL SYNTHESIS`)

| Reduced-Form Term | Primitive Equation / Assumption | Grammar Category |
|:---|:---|:---|
| $\dot{e}/e = \hat{q} - \hat{a} - \hat{N}$ | $e \equiv q / (a N)$ | `Identity` |
| $\hat{q} = \hat{k}$ | $\sigma \equiv k / q = \text{const}$ | `Technological assumption` + `Closure rule` |
| $\hat{k} = I_{\text{net}} / k$ | $\dot{k} \equiv I_{\text{gross}} - \delta k$ | `Identity` |
| $I_{\text{gross}} = S$ | Say's Law / full-capacity investment-saving closure | `Closure rule` |
| $S = \Pi = (1 - \omega) q$ | Classical class savings ($s_w = 0, s_\pi = 1$) | `Behavioral relation` + `Institutional assumption` |
| $-(\alpha + \beta)$ in $\dot{e}/e$ | $\hat{a} = \alpha$, $\hat{N} = \beta$ | `Exogenous process` |
| $\dot{\omega}/\omega = \hat{w} - \hat{a}$ | $\omega \equiv w / a$ | `Identity` |
| $\hat{w} = -\gamma + \rho e$ | Reserve-army real-wage bargaining curve (linearized) | `Behavioral relation` + `Institutional assumption` |
| $-\alpha$ in $\dot{\omega}/\omega$ | $\hat{a} = \alpha$ | `Exogenous process` |

---

### K. Equilibria, Nullclines, and Interior Stationary State (`GOODWIN-1967`)

Setting $\dot{e} = 0$ and $\dot{\omega} = 0$ yields:

1. **Nullclines (Zero-Motion Loci):**
   - **Employment Nullcline ($\dot{e} = 0$):** Either $e = 0$ (trivial boundary) or:
     $$\omega = \omega^* \equiv 1 - \sigma(\alpha + \beta + \delta)$$
     (Horizontal line in $(e, \omega)$ space; for $\omega < \omega^*$, $\dot{e} > 0$; for $\omega > \omega^*$, $\dot{e} < 0$.)
   - **Wage-Share Nullcline ($\dot{\omega} = 0$):** Either $\omega = 0$ (trivial boundary) or:
     $$e = e^* \equiv \frac{\alpha + \gamma}{\rho}$$
     (Vertical line in $(e, \omega)$ space; for $e > e^*$, $\dot{\omega} > 0$; for $e < e^*$, $\dot{\omega} < 0$.)

2. **Stationary States (Equilibria):**
   - **Trivial Boundary Equilibrium:** $(e_0, \omega_0) = (0, 0)$, which is a saddle point on the boundary of the nonnegative orthant.
   - **Unique Interior Stationary State (`GOODWIN-1967`):**
     $$(e^*, \omega^*) = \left( \frac{\alpha + \gamma}{\rho}, \;\; 1 - \sigma(\alpha + \beta + \delta) \right)$$
     *(with $\delta = 0$ in `GOODWIN-1967`, giving $\omega^* = 1 - \sigma(\alpha + \beta)$).*

3. **Steady-State Growth Characteristics at $(e^*, \omega^*)$ (`GOODWIN-1967`):**
   - Output and capital grow at Harrod's natural rate: $\hat{q}^* = \hat{k}^* = \alpha + \beta$.
   - Employment grows at the labor-force growth rate: $\hat{L}^* = \hat{q}^* - \alpha = \beta$ (so $e^*$ is stationary).
   - Real wages grow at the rate of labor productivity: $\hat{w}^* = \alpha$ (so $\omega^*$ is stationary).
   - Profit rate is stationary at $r^* = (1 - \omega^*)/\sigma = \alpha + \beta + \delta$.

---

### L. Admissibility Conditions (`ARS ANALYTICAL SYNTHESIS` / `LATER GOODWIN LITERATURE`)

A mathematically well-defined interior point $(e^*, \omega^*)$ is **economically admissible** only if both state variables lie strictly inside their unit intervals and trajectories remain within the economically meaningful domain $\Omega = (0, 1) \times (0, 1)$:

1. **Interior Stationary-State Parameter Restrictions:**
   - **Profitability / Positive Wage Share Condition ($0 < \omega^* < 1$):**
     $$\alpha + \beta + \delta > 0 \quad \text{and} \quad \sigma(\alpha + \beta + \delta) < 1 \iff \frac{1}{\sigma} > \alpha + \beta + \delta$$
     *Economic meaning:* The maximum technologically possible net rate of profit (when $\omega = 0$, $r_{\max} = \frac{1}{\sigma} - \delta$) must strictly exceed the natural growth rate $\alpha + \beta$.
   - **Interior Employment Rate Condition ($0 < e^* < 1$):**
     $$0 < \alpha + \gamma < \rho$$
     *Economic meaning:* At full employment ($e = 1$), real wage growth $\hat{w}(1) = -\gamma + \rho$ must strictly exceed productivity growth $\alpha$.

2. **Global Trajectory Admissibility Warning (`LATER GOODWIN LITERATURE`):**
   - Even when $(e^*, \omega^*) \in (0, 1)^2$, the **linearized** Phillips curve $\hat{w} = -\gamma + \rho e$ and linear profit rate $r = (1-\omega)/\sigma$ preserve positivity ($e(t) > 0, \omega(t) > 0$ for all $t$ given $e(0) > 0, \omega(0) > 0$, since $e=0$ and $\omega=0$ are invariant axes), but **do not** automatically prevent large-amplitude closed orbits from violating the upper bounds $e(t) \le 1$ or $\omega(t) \le 1$ for initial conditions far from $(e^*, \omega^*)$.
   - Enforcing global invariance of $(0, 1)^2$ requires either restricting initial conditions to level curves $V(e, \omega) = c$ contained entirely within $(0, 1)^2$ or specifying nonlinear boundary asymptotes (e.g., $\lim_{e \to 1^-} f(e) = +\infty$ as noted qualitatively in `GOODWIN-1967`).

---

### M. Lotka–Volterra Structure & First Integral (`GOODWIN-1967`)

Writing $A_1 \equiv \frac{1}{\sigma} - (\alpha + \beta + \delta) > 0$, $B_1 \equiv \frac{1}{\sigma} > 0$, $A_2 \equiv \alpha + \gamma > 0$, and $B_2 \equiv \rho > 0$, the system is isomorphic to the classic Lotka–Volterra predator-prey equations (`GOODWIN-1967`):
$$\dot{e} = e (A_1 - B_1 \omega), \qquad \dot{\omega} = \omega (-A_2 + B_2 e)$$
- **Ecological Analogy (`GOODWIN-1967`):** The employment rate $e$ plays the role of the **prey**, while the wage share $\omega$ plays the role of the **predator**. High employment empowers labor, driving up $\omega$ ($\dot{\omega} > 0$); a rising wage share squeezes profits and slows accumulation below the natural rate ($\dot{e} < 0$); falling employment disciplines wage demands ($\dot{\omega} < 0$), restoring profitability and restarting accumulation ($\dot{e} > 0$).
- **Separable ODE & Exact First Integral (Constant of Motion) (`GOODWIN-1967`):**
  Dividing $\dot{\omega}$ by $\dot{e}$ for $e, \omega > 0$ separates variables:
  $$\frac{d\omega}{de} = \frac{\omega (-A_2 + B_2 e)}{e (A_1 - B_1 \omega)} \implies \left( \frac{A_1}{\omega} - B_1 \right) d\omega + \left( \frac{A_2}{e} - B_2 \right) de = 0$$
  Integrating yields the conserved Lyapunov-type function (first integral) $V: \mathbb{R}_{++}^2 \to \mathbb{R}$:
  $$V(e, \omega) \equiv A_1 \ln \omega - B_1 \omega + A_2 \ln e - B_2 e = \text{const}$$
  Or, normalizing by the interior equilibrium values $e^* = A_2/B_2$ and $\omega^* = A_1/B_1$:
  $$V(e, \omega) = B_1 \left( \omega^* \ln \omega - \omega \right) + B_2 \left( e^* \ln e - e \right) = C_0$$
  Along any solution trajectory $(e(t), \omega(t)) \in \mathbb{R}_{++}^2$, the time derivative is identically zero:
  $$\dot{V}(e, \omega) = \frac{\partial V}{\partial e}\dot{e} + \frac{\partial V}{\partial \omega}\dot{\omega} = B_2 \left(\frac{e^* - e}{e}\right) e B_1 (\omega^* - \omega) + B_1 \left(\frac{\omega^* - \omega}{\omega}\right) \omega B_2 (e - e^*) \equiv 0$$

---

### N. Local Stability Analysis: Center vs. Asymptotically Stable Equilibrium (`GOODWIN-1967` + `ARS ANALYTICAL SYNTHESIS`)

1. **General Jacobian Matrix $J(e, \omega)$:**
   $$J(e, \omega) = \begin{bmatrix} \dfrac{\partial F_1}{\partial e} & \dfrac{\partial F_1}{\partial \omega} \\[8pt] \dfrac{\partial F_2}{\partial e} & \dfrac{\partial F_2}{\partial \omega} \end{bmatrix} = \begin{bmatrix} \dfrac{1 - \omega}{\sigma} - (\alpha + \beta + \delta) & -\dfrac{e}{\sigma} \\[8pt] \rho \omega & -(\alpha + \gamma) + \rho e \end{bmatrix}$$

2. **Jacobian Evaluated at Interior Equilibrium $(e^*, \omega^*)$:**
   Since the diagonal bracketed terms vanish at $(e^*, \omega^*)$:
   $$J(e^*, \omega^*) = \begin{bmatrix} 0 & -\dfrac{e^*}{\sigma} \\[8pt] \rho \omega^* & 0 \end{bmatrix}$$

3. **Trace, Determinant, and Eigenvalues:**
   - **Trace:** $\operatorname{tr} J(e^*, \omega^*) = 0 + 0 = 0$.
   - **Determinant:** $\det J(e^*, \omega^*) = (0)(0) - \left(-\frac{e^*}{\sigma}\right)(\rho \omega^*) = \frac{\rho}{\sigma} e^* \omega^* > 0$ (for all admissible $e^* > 0, \omega^* > 0$).
   - **Characteristic Polynomial:** $\lambda^2 - \operatorname{tr}(J)\lambda + \det(J) = \lambda^2 + \frac{\rho}{\sigma} e^* \omega^* = 0$.
   - **Eigenvalues:**
     $$\lambda_{1,2} = \pm i \theta_G, \qquad \theta_G \equiv \sqrt{\frac{\rho}{\sigma} e^* \omega^*} = \sqrt{\frac{(\alpha + \gamma)\left[1 - \sigma(\alpha + \beta + \delta)\right]}{\sigma}} > 0$$
   - **Period of Small Oscillations:** Near $(e^*, \omega^*)$, the cycle period is $T = \frac{2\pi}{\theta_G}$.
   - **Phase Orientation:** At $e = e^*$ and $\omega < \omega^*$, $\dot{e} > 0$ and $\dot{\omega} = 0$; as $e$ rises above $e^*$, $\dot{\omega} > 0$. Thus trajectories circulate **counterclockwise** in the $(e, \omega)$ plane (when $e$ is plotted on the horizontal axis and $\omega$ on the vertical axis).

4. **Nonlinear Center Proof (Why Linearization Alone Is Insufficient) (`ARS ANALYTICAL SYNTHESIS`):**
   - In general nonlinear planar systems, purely imaginary eigenvalues ($\operatorname{tr} J = 0, \det J > 0$) are **non-hyperbolic**; by the Hartman–Grobman theorem, linearization alone cannot distinguish a nonlinear center from a weak asymptotically stable focus (spiral sink) or weak unstable focus (spiral source).
   - In `GOODWIN-1967`, $(e^*, \omega^*)$ is proven to be a genuine **nonlinear center** (Lyapunov stable, **not** asymptotically stable) because the system possesses the strict first integral $V(e, \omega)$ established in Item M, whose Hessian at $(e^*, \omega^*)$ is definite ($\nabla^2 V(e^*, \omega^*) = \operatorname{diag}(-B_2/e^*, -B_1/\omega^*) \prec 0$), making level sets of $V$ closed curves surrounding $(e^*, \omega^*)$.

---

### O. Critical Distinction: Closed Orbits (Conservative Center) vs. Limit Cycles (Dissipative Attractor) (`ARS ANALYTICAL SYNTHESIS` / `LATER GOODWIN LITERATURE`)

A frequent error in informal macro discussions is calling the `GOODWIN-1967` cycle a "limit cycle." The architecture must enforce the exact mathematical distinction:

| Property | `GOODWIN-1967` Baseline (Conservative Center) | Limit Cycle in Extended Models (`LATER GOODWIN LITERATURE`) |
|:---|:---|:---|
| **Mathematical Object** | Continuum (one-parameter family) of closed orbits $V(e, \omega) = c$. | Isolated closed trajectory $\Gamma$ in state space. |
| **Dependence on Initial Conditions** | **Initial-condition dependent:** Every initial point $(e(0), \omega(0)) \neq (e^*, \omega^*)$ determines forever the amplitude of the cycle. | **Initial-condition independent (locally):** Nearby trajectories spiral onto (stable limit cycle) or away from (unstable limit cycle) $\Gamma$. |
| **Response to Transient Shocks** | **Permanent amplitude shift:** A one-time shock moves the economy onto a new level curve $V = c'$, permanently altering cycle amplitude. | **Self-correcting amplitude:** After a transient shock within the basin of attraction, the economy returns asymptotically to $\Gamma$. |
| **Structural Stability (Andronov–Pontryagin)** | **Structurally unstable:** Any arbitrarily small perturbation to the diagonal of $J(e^*, \omega^*)$ ($\operatorname{tr} J \neq 0$) destroys the family of closed orbits. | **Structurally stable (hyperbolic limit cycle):** Persists under small smooth perturbations of the vector field. |
| **Typical Generating Mechanism** | Zero diagonal Jacobian terms ($\partial \dot{e}/\partial e = 0, \partial \dot{\omega}/\partial \omega = 0$ at equilibrium) + separable Lotka–Volterra structure. | Dissipative state self-feedback ($\operatorname{tr} J \neq 0$) combined with nonlinear saturation (e.g., Poincaré–Bendixson theorem or supercritical Hopf bifurcation). |

---

### P. Which Assumptions Generate the Two-State Closure — and How Relaxing Them Changes the System (`ARS ANALYTICAL SYNTHESIS` + `LATER GOODWIN LITERATURE`)

The `GOODWIN-1967` model reduces to a 2D conservative system in $(e, \omega)$ **only** because of five knife-edge structural assumptions. Modifying any one of them changes either the Jacobian diagonal or the dimension of the state vector:

| Relaxed `GOODWIN-1967` Assumption | Modified Specification (`LATER GOODWIN LITERATURE` / `BROADER HETERODOX TRADITION`) | Effect on State Vector $\mathbf{x}$ | Effect on Jacobian / Dynamics |
|:---|:---|:---|:---|
| **1. Say's Law ($I \equiv S$) & Fixed Utilization** | Introduce independent investment function $g_K = g_K(u, \pi)$ and endogenous capacity utilization $u = Y/Y^p$ (Kaleckian / Post-Keynesian synthesis, e.g., Barbosa-Filho & Taylor 2006). | Either $u$ adjusts algebraically via short-run goods market equilibrium $u = u(\omega)$ (2D) or adjusts dynamically $\dot{u} = \phi(I - S)$ (3D). | Introduces diagonal feedback $\partial \dot{e}/\partial e \neq 0$ or $\partial \dot{u}/\partial u \neq 0$; breaks conservative Lotka–Volterra structure; allows damped/explosive spirals or Hopf limit cycles, and enables **demand-led** (wage-led or profit-led) regimes. |
| **2. Pure Internal Profit Financing ($I = \Pi$)** | Firms finance investment above retained profits via bank loans $\dot{D} = I - \Pi_{\text{retained}}$, with interest $i D$ (Minskyan synthesis, e.g., Keen 1995; Grasselli & Costa Lima 2012). | Adds private debt-to-output ratio $d \equiv D / Y$ as a **3rd state variable**: $\mathbf{x} = (e, \omega, d)^T$. | 3D system; admits a productive interior equilibrium and a debt-deflation crisis boundary ($d \to \infty, e \to 0$) depending on financial fragility and animal spirits. |
| **3. Worker Saving $s_w = 0$** | Workers save $s_w > 0$ and accumulate capital or claims $K_w$ alongside capitalists $K_c$ (Pasinetti 1962 / Samuelson–Modigliani). | Adds worker capital share $z \equiv K_w / K$ (or wealth ratio) as an additional state variable. | Alters long-run income distribution and steady-state profit rate ($r^* = g_n / s_c$ on the Pasinetti branch). |
| **4. Exogenous Productivity Growth $\hat{a} = \alpha$ and Constant $\sigma$** | Endogenous technical change via Kaldor–Verdoorn ($\hat{a} = a_0 + \eta \hat{q}$) or Marx–Hicks induced bias ($\hat{a} = \phi(\omega), \hat{\sigma} = \psi(\omega)$, e.g., Shah & Desai 1981; Foley 2003). | If $\hat{a} = \phi(\omega)$, stays 2D; if $\sigma$ becomes a dynamic state variable ($\hat{\sigma} \neq 0$), expands to **3D**: $\mathbf{x} = (e, \omega, \sigma)^T$. | If $\hat{a} = \phi(\omega)$ with $\phi'(\omega) > 0$, adds negative diagonal term $\partial \dot{\omega}/\partial \omega = -\omega \phi'(\omega) < 0$, making $\operatorname{tr} J < 0$ and converting the conservative center into an **asymptotically stable focus**! |
| **5. Real-Wage Bargain Without Price Dynamics** | Separate nominal wage Phillips curve $\hat{W} = f(e) + \eta \hat{p}^e$ and adaptive inflation expectations or partial price adjustment (Desai 1973). | Can remain 2D (if $\hat{p}$ is algebraic) or become 3D (with expected inflation $\pi^e$ as a state). | Introduces nonzero diagonal entries in $J(e^*, \omega^*)$, replacing neutral closed orbits with damped or explosive oscillations. |

---

## 5. PEDAGOGICAL & ARCHITECTURAL ROLE IN `heterodox-macro-modeling` (`ARS ANALYTICAL SYNTHESIS`)

When promoted in Wave D3-B to `references/goodwin_baseline.md`, this artifact will serve exclusively as a **worked reference exemplar** demonstrating:
1. How to reduce a macroeconomic system of stocks, flows, and growth rates to an intensive dimensionless state vector.
2. How to audit every reduced-form differential equation back to its underlying identities, technological assumptions, behavioral equations, and closure rules.
3. How to derive nullclines, stationary states, parameter admissibility bounds, and the Jacobian matrix.
4. Why a non-hyperbolic linearization ($\operatorname{tr} J = 0$) requires nonlinear global analysis (first integral vs. limit cycle) rather than naive reliance on local eigenvalues.
5. How modifying a single assumption (e.g., making $\hat{a} = \phi(\omega)$ or introducing endogenous utilization $u$) alters multiple equations, feedback loops, and stability properties simultaneously.
