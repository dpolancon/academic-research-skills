# Reference Module M1: Model Architecture, Equation Classification, and Closures

- **Module Role:** Canonical Architecture and Closure Reference for `heterodox-macro-modeling`
- **Location:** `heterodox-economics-review/references/model_architecture_and_closures.md`
- **Authority:** Authoritative reference module implementing Ratified Wave D3-A Architecture (`§5`, `§6`, `§10`, `§13`, `§14`, `§15`, `§16`)

---

## 1. Canonical Modeling Grammar

Heterodox macroeconomic models across all traditions share a common structural grammar:

$$\text{MODEL} = \text{State Space} + \text{Accounting Structure} + \text{Technology \& Exogenous Processes} + \text{Behavioral Relations} + \text{Closure} + \text{Feedback Architecture} + \text{Institutional Regime}$$

1. **State Space ($\mathbf{x} \in \Omega \subseteq \mathbb{R}^n$):** The minimal set of intensive stock or ratio variables whose continuous laws of motion $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x}; \boldsymbol{\theta})$ or discrete transitions $\mathbf{x}_{t+1} = \mathbf{G}(\mathbf{x}_t; \boldsymbol{\theta})$ govern the dynamic trajectory of the economy.
2. **Accounting Structure:** The foundational identities (national income, cost decomposition, stock-flow accumulation, financial asset-liability offsetting, and transactions-flow consistency) that hold true by definition in all states of the world.
3. **Technology & Exogenous Processes:** Physical production constraints (potential capacity $Y^p = K/\sigma_{\text{cap}}$, labor productivity $a = Y/L$) and autonomous environmental/policy trajectories (labor-force growth $\beta$, autonomous demand growth $g_Z$).
4. **Behavioral Relations:** Functional descriptions of how classes, firms, households, and financial institutions formulate plans and react to states (investment functions, consumption propensities, conflict curves, portfolio demands).
5. **Closure:** The system-level choice of which variables adjust to reconcile independent behavioral plans with accounting identities, ensuring mathematical determinacy ($M = n + m$).
6. **Feedback Architecture:** The signed network of direct self-reinforcing ($J_{ii} > 0$), self-damping ($J_{ii} < 0$), and cross-coupling ($J_{ij} J_{ji}$) loops governing stability and cyclicality.
7. **Institutional Regime:** The historical parameter constraints, wage-setting structures, central bank reaction functions, and international rules that fix parameter values $\boldsymbol{\theta}$ and select the operative closure.

---

## 2. Six-Way Primitive Equation Taxonomy

Every equation in a model must be classified into exactly one primitive category:

| Category | Definition | Epistemic Status & Falsifiability | Mathematical Examples |
|:---|:---|:---|:---|
| **Accounting Identity (`ID`)** | Mathematical relation that holds true by definition or double-entry bookkeeping across all possible states. | Unfalsifiable by definition; violation is an algebraic or accounting error. | $Y \equiv W + \Pi$; $\dot{K} \equiv I - \delta K$; $\widehat{(X/Y)} \equiv \hat{X} - \hat{Y}$; $\sum_j \text{Net Lending}_j \equiv 0$. |
| **Technological Assumption (`TECH`)** | Engineering/physical relation linking inputs to outputs, capacity, or productivity. | Structural approximation; can be relaxed through induced technical change or variable factor proportions. | $Y^p = K / \sigma_{\text{cap}}$ (constant $\sigma_{\text{cap}}$); $a \equiv Y/L$ growing at exogenous rate $\alpha$. |
| **Behavioral Relation (`BEH`)** | Equation specifying how economic agents or classes form plans or respond to economic stimuli. | Empirically falsifiable; theoretical locus of macroeconomic debate. | Investment: $g_K = \gamma_0 + \gamma_u u + \gamma_\pi \pi$; Real-wage bargaining: $\hat{w} = -\gamma + \rho e$; Consumption: $C = (1-s_w)W + (1-s_\pi)\Pi$. |
| **Institutional Assumption (`INST`)** | Constraint reflecting legal, political, or institutional rules governing markets, classes, or policies. | Institutionally contingent; valid within a declared historical regime. | Class saving differential: $s_w = 0, s_\pi > 0$; Taylor rule policy rate: $i = i_0 + \phi_\pi (\pi - \bar{\pi})$; Fixed exchange rate peg. |
| **Closure Rule (`CLOS`)** | Specification of which variable clears an accounting balance or equates planned magnitudes across agents. | System-level modeling choice determining causal ordering. | Say's Law ($I \equiv S, u = 1$); Keynesian goods-market clearing ($S(u, \omega) = I(u, \omega)$ solved for $u$); Kaldor–Pasinetti income distribution clearing ($S(\omega) = I$). |
| **Exogenous Process (`EXOG`)** | Specification of variables whose values or trajectories are determined outside the model's feedback loops. | Boundary condition; potential target for model endogenization. | Autonomous demand growth $\hat{Z} = g_Z$; Labor force growth $\hat{N} = \beta$; World income growth $\hat{Y}^*$. |

### Anti-Tautology & Ratio Differentiation Disciplines
- **Logarithmic Differentiation Rule (`ID-DIFF`):** For any ratio $z \equiv X/Y$, its time derivative must be derived strictly as:
  $$\hat{z} \equiv \frac{\dot{z}}{z} = \hat{X} - \hat{Y} \implies \dot{z} = z(\hat{X} - \hat{Y})$$
  Setting $\dot{z} = 0$ is permitted only by explicitly imposing a closure or technology condition that equates $\hat{X}$ to $\hat{Y}$.
- **No Specification Tautology Rule (`NO-TAUTOLOGY`):** Dynamic instability, stationarity, or oscillations must emerge from behavioral feedbacks (`BEH`) and closures (`CLOS`), never from an unexamined technological or accounting exponent.
  - *Illustrative Example:* In capacity utilization models, assuming $Y^p = A K^\theta$ with constant $\theta \neq 1$ mechanically forces the capital-capacity ratio $\nu = K/Y^p = A^{-1} K^{1-\theta}$ to drift to $0$ or $\infty$ whenever capital accumulates ($\hat{K} > 0$), manufacturing secular instability by technological definition rather than behavioral dynamics.

---

## 3. Mandatory 14-Question Closure Audit

Simplistic school labels ("the Keynesian closure", "the Marxian closure", "the Sraffian closure") are prohibited as stand-ins for mathematical specification. Every model must execute the 14-question audit:

```text
========================================================================================
THE 14-QUESTION EQUATION-LEVEL CLOSURE AUDIT
========================================================================================
Q1.  WHAT DETERMINES OUTPUT (Y)?
     (Effective demand Y = C+I+G+NX, productive capacity Y = K/σ, labor supply Y = aL,
     or BOP constraint Y = Y_BOP?)

Q2.  WHAT DETERMINES CAPACITY UTILIZATION (u = Y/Y^p)?
     (Fixed at full capacity u = 1, fixed at normal capacity u = u_n, an endogenous
     short-run adjusting variable u = u*, or a dynamic state adjusting to excess demand?)

Q3.  WHAT DETERMINES INVESTMENT (I or g_K)?
     (Passively determined by saving I ≡ S, or an independent behavioral function
     g_K(u, π, r, i, γ_Z)?)

Q4.  WHAT DETERMINES SAVING (S)?
     (Worker/capitalist saving propensities s_w, s_π, firm retained earnings s_f,
     fiscal deficits, or foreign capital inflows?)

Q5.  WHAT DETERMINES INCOME DISTRIBUTION (ω, π, r)?
     (Exogenous markup, classical subsistence wage, Kaldor-Pasinetti endogenous
     adjusting variable, or dynamic bargaining state dw/dt = F_2(e, ω)?)

Q6.  WHAT DETERMINES WAGES AND PRICES (W, P, w)?
     (Bargained directly in real terms w, or determined by separate nominal wage setting
     and price markup inflation with conflict dynamics?)

Q7.  WHAT DETERMINES EMPLOYMENT (L, e = L/N)?
     (Market clearing at full employment, or derived residually from output L = Y/a,
     making employment rate e endogenous?)

Q8.  WHAT DETERMINES TECHNICAL CHANGE (a, σ)?
     (Exogenous rates α and σ_cap, or endogenous Kaldor-Verdoorn scale effects a^(Y)
     and Marx-Hicks induced technical bias a^(ω), σ^(ω)?)

Q9.  WHAT ADJUSTS WHEN PLANNED MAGNITUDES CONFLICT?
     (When planned I ≠ S or wage claims conflict with target markups, does adjustment
     occur through output/utilization, price inflation, inventories, or rationed credit?)

Q10. WHICH VARIABLES ARE PREDETERMINED AT INSTANT t?
     (Which stocks K, D, N and intensive ratios are dynamic state variables fixed at
     time t, evolving only via continuous differential equations?)

Q11. WHICH VARIABLES CLEAR MARKETS OR BALANCES INSTANTANEOUSLY?
     (Explicit mapping of each algebraic endogenous variable to the specific identity
     or market equilibrium condition that determines it?)

Q12. WHAT IS EXOGENOUS?
     (Complete ledger of exogenous parameters θ and autonomous forcing paths?)

Q13. WHAT IS ENDOGENOUS?
     (Complete ledger of n dynamic states x plus m algebraic endogenous variables y?)

Q14. WHAT CLOSES THE SYSTEM MATHEMATICALLY?
     (Verification that total independent equations equal M = n + m, the algebraic
     Jacobian is non-singular, and no redundant identity is double-counted?)
========================================================================================
```

---

## 4. Pluralist Heterodox Tradition Boundary Map

Heterodox macroeconomics comprises distinct research traditions with differing ontologies and closure choices. The taxonomy below classifies inter-tradition relationships into five analytical categories:
- `GENEALOGICAL CONNECTION`
- `FORMAL SIMILARITY`
- `CLOSURE DIFFERENCE`
- `LATER SYNTHESIS`
- `DISTINCT MODEL ONTOLOGY`

| Tradition | Distinct Model Ontology & Focal Variables | Closure Difference | Formal Similarity & Genealogy | Major Later Syntheses |
|:---|:---|:---|:---|:---|
| **Marxian** | Surplus value; class struggle over wage share $\omega$; reserve army of labor $e$; organic composition $\sigma$; profit rate $r = (1-\omega)/\sigma$ driving accumulation. | Accumulation is profit-driven ($g_K = f(r)$); long-run output is capacity-constrained ($u=1$); technical change is Marx-biased (labor-saving, capital-using). | Shared classical surplus approach with Sraffa; Lotka–Volterra ODE formalization of *Capital* Vol. I Ch. 25. | Marxian–Kaleckian models (Marglin & Bhaduri 1990; Barbosa-Filho & Taylor 2006); Foley–Michl induced technical change. |
| **Classical / Sraffian** | Physical reproduction; social surplus; prices of production equalizing profit rates across sectors; distribution exogenous to prices. | One distributive variable ($w$ or $r$) fixed from outside the price system; capacity utilization must gravitate to normal capacity in the long run ($u^* = u_n$). | Classical surplus foundation; multi-sector input-output matrices $\mathbf{p} = (1+r)\mathbf{p}\mathbf{A} + w\mathbf{l}$. | Sraffian Supermultiplier (Serrano 1995; Freitas & Serrano 2015) coupling normal utilization with autonomous demand $Z$. |
| **Kaleckian / Post-Keynesian** | Effective demand in short and long run; oligopolistic markup pricing ($\omega = 1/(1+\tau)$); persistent excess capacity ($u < 1$) as the normal state. | Investment is independent of saving; utilization $u$ is an endogenous adjusting variable in both short and long run ($u^* \neq u_n$); growth can be wage-led or profit-led. | Rooted in Kalecki (1954), Steindl (1952), Robinson (1956); differential class saving ($s_w < s_\pi$). | Kaleckian–Goodwin models (endogenous $\dot{\omega}$ and $\dot{u}$); Post-Keynesian SFC models (Godley & Lavoie 2007). |
| **Harrodian** | Dual nature of investment (capacity creation vs. demand generation); knife-edge instability of warranted growth ($g_w = s/\sigma$). | Normal utilization $u_n$ is a structural target; utilization gaps $u - u_n$ cause cumulative investment acceleration ($\dot{g}_K = \phi(u - u_n)$). | Harrod (1939); shares effective demand with Keynes but rejects permanent passive deviation of $u^*$ from $u_n$. | Shaikh (2009) classical-Harrodian models; Skott (1989) Kaldor–Harrod cycles; SSM taming via autonomous demand $Z$. |
| **Kaldorian / Verdoorn** | Cumulative causation; dynamic increasing returns; endogenous productivity driven by output growth (**Kaldor–Verdoorn Law**: $\hat{a} = \alpha_0 + \eta \hat{Y}$). | Technical progress $\hat{a}$ is endogenous to demand growth; early Kaldor–Pasinetti models adjust distribution $\omega$ to clear $I=S$ at full employment. | Growth-rate feedback loops; connects productivity to trade competitiveness. | Kaldor–Goodwin models; Thirlwall–Kaldor export-led cumulative causation (Dixon & Thirlwall 1975). |
| **Minskyan** | Financial instability hypothesis; hedge, speculative, and Ponzi financial structures; endogenous liquidity and debt-deflation crises. | Investment exceeds retained profits via debt creation ($\dot{D} = I - \Pi_{\text{ret}}$); private debt-to-capital ratio $d = D/K$ is a central dynamic state variable. | Rooted in Keynes Ch. 12/17 and Kalecki's increasing risk; expressed via coupled nonlinear ODEs (3D+). | Keen (1995) and Grasselli & Costa Lima (2012) 3D Goodwin–Minsky $(e, \omega, d)$ models; SFC Minsky models. |
| **Structuralist / Center–Periphery** | Asymmetric global division of labor; productive heterogeneity; structural foreign-exchange bottlenecks; currency hierarchy. | Domestic growth and utilization are constrained by external payments ($\hat{Y} \le \hat{Y}_{BOP}$); currency devaluation redistributes income away from wages. | ECLAC / CEPAL tradition (Prebisch, Furtado); Taylor (1983, 1991) structuralist macro matrices. | North–South uneven development models (Dutt 1990; Cimoli & Porcile 2014); BOP-constrained Kaleckian models. |

---

## 5. Demand-Led Modeling & Utilization Dynamics

When modeling demand-led systems, the skill enforces the following analytical standards:

### 5.1 Short-Run Multiplier & Keynesian Stability
In models where capacity utilization $u \equiv Y/Y^p$ adjusts to clear the goods market $g_I(u, \pi) = g_S(u, \pi)$:
- The model must verify the **Keynesian stability condition**:
  $$\frac{\partial g_S}{\partial u} - \frac{\partial g_I}{\partial u} > 0$$
  *(Saving is more responsive to utilization than investment in the short run).*
- If $\partial g_I/\partial u > \partial g_S/\partial u$, short-run multiplier adjustment is unstable, and the system requires nonlinear bounding or dynamic inventory/accelerator states.

### 5.2 Bhaduri–Marglin Wage-Led vs. Profit-Led Decomposition
The impact of distribution on economic activity must be decomposed into demand and accumulation regimes:
- **Demand Regime ($\partial u^* / \partial \omega$):**
  $$\frac{\partial u^*}{\partial \omega} = \frac{(s_\pi - s_w) u - \frac{\partial g_I}{\partial \pi}}{\frac{\partial g_S}{\partial u} - \frac{\partial g_I}{\partial u}}$$
  - **Wage-Led Demand:** Differential consumption $(s_\pi - s_w)u$ exceeds the profit sensitivity of investment $\partial g_I/\partial \pi \implies \partial u^*/\partial \omega > 0$.
  - **Profit-Led Demand:** Profit sensitivity of investment outweighs consumption stimulus $\implies \partial u^*/\partial \omega < 0$.
- **Accumulation Regime ($\partial g_K^* / \partial \omega$):**
  $$\frac{\partial g_K^*}{\partial \omega} = \frac{\partial g_I}{\partial u} \frac{\partial u^*}{\partial \omega} - \frac{\partial g_I}{\partial \pi}$$
  Even when demand is wage-led ($\partial u^*/\partial \omega > 0$), capital accumulation can be **profit-led** if the direct profit squeeze on investment dominates the indirect capacity utilization effect.

### 5.3 Pluralist Treatment of Normal Utilization ($u_n$)
When analyzing Harrodian instability and normal utilization, the skill evaluates the author's declared closure neutrally:
1. *Kaleckian Closure:* $u^*$ remains an endogenous adjusting variable across medium/long horizons, or $u_n$ adapts endogenously toward actual utilization ($\dot{u}_n = \xi(u - u_n)$).
2. *Classical-Harrodian Closure (Shaikh/Skott):* Actual utilization gravitates toward or cycles around normal capacity $u_n$ via profit retention, credit rationing, or labor-market feedback.
3. *Sraffian Supermultiplier Closure (Serrano/Freitas):* Autonomous non-capacity demand $Z$ grows at $\hat{Z} = g_Z$; investment share $h \equiv I/Y$ adjusts dynamically $\dot{h} = h \gamma (u - u_n)$; stability holds if and only if accelerator responsiveness $\gamma$ is bounded by the marginal propensity to save.
