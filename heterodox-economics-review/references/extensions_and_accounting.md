# Reference Module M3: Extensions, Stock-Flow Consistency, and Accounting

- **Module Role:** Canonical Reference for Model Extensions, Analytical SFC, and Open-Economy Formalization
- **Location:** `heterodox-economics-review/references/extensions_and_accounting.md`
- **Authority:** Authoritative reference module implementing Ratified Wave D3-A Architecture (`§16`, `§17`, `§18`, `§21`)

---

## 1. Internal Module Structure

To preserve rigorous modular organization without creating shallow micro-files, this reference is internally partitioned into three coordinated sections:

```text
========================================================================================
PART I:   ACCOUNTING & STOCK-FLOW CONSISTENT (SFC) SUBSTRATE
PART II:  MODEL EXTENSION OPERATIONS & 8-STEP RE-DERIVATION PROTOCOL
PART III: OPEN-ECONOMY & EXTERNAL-CONSTRAINT EXTENSIONS
========================================================================================
```

---

# PART I: ACCOUNTING & STOCK-FLOW CONSISTENT (SFC) SUBSTRATE

Stock-Flow Consistency is an analytical double-entry accounting discipline ensuring that every financial transaction has a counterpart and every flow accumulates into a stock. SFC is **never** reduced to "adding debt as one state variable."

## 1.A Universal SFC Core

Whenever a model includes sectoral balance sheets, financial assets/liabilities, or multi-sector flows, the **Universal SFC Core** consists of the following six accounting invariants:

### 1.1 Balance-Sheet Matrix Consistency (Stocks at Instant $t$)
Columns represent institutional sectors (e.g., Households $h$, Production Firms $f$, Commercial Banks $b$, Central Bank $cb$, Government $g$, Rest of World $row$). Rows distinguish **financial assets/liabilities** from **real/tangible assets**.
- **Financial Asset/Liability Row Offsetting:** Every financial instrument row $i$ (money deposits $+M$, loans $-L$, bills $+B_h / -B_g$, equities) has both an asset holder ($+$) and a liability issuer ($-$) and must offset identically to zero across sectors:
  $$\sum_{j} A_{ij}^{\text{fin}} \equiv 0 \qquad \text{for every financial instrument row } i$$
- **Real / Tangible Asset Rows:** Real/tangible assets (such as physical capital $+K$, inventories, or land) have **no offsetting liability entry**; their horizontal sum equals total tangible wealth in the economy ($\sum_j K_j \equiv K$).
- **Sectoral Column Balance with Net Worth:** Each sector's column balances tangible plus net financial assets against sectoral net worth ($NW_j \equiv K_j + \sum_i A_{ij}^{\text{fin}}$, or written with $-NW_j$ so the column sums to zero), implying that aggregate net worth equals aggregate tangible capital ($\sum_j NW_j \equiv K$).
- *Accounting Guardrail:* Never apply a generic row-and-column zero-sum rule that treats every row of the Balance-Sheet Matrix identically to the Transactions-Flow Matrix.

### 1.2 Transactions-Flow Matrix Consistency (Flows over Period $t$)
- **Row Zero-Sum Law:** Under the model's sign convention (inflows $+$, outflows $-$), every transaction row (consumption, investment, wages, profits, taxes, interest payments $i_{t-1} D_{t-1}$, and flow-of-funds changes $\Delta M, \Delta L, \Delta B$) must sum identically to zero across sectors:
  $$\sum_j F_{kj} \equiv 0 \qquad \text{for every transaction row } k$$
- **Column Zero-Sum Law (Sectoral Budget Constraints):** Every sector's column must sum identically to zero under the model's accounting convention:
  $$\text{Current Receipts}_j - \text{Current Outlays}_j - \text{Physical Investment}_j \equiv \text{Net Financial Lending}_j \equiv \sum_i \Delta \text{Assets}_{ij} - \sum_i \Delta \text{Liabilities}_{ij}$$

### 1.3 Sectoral Financial Balances Identity
In an open economy with government, summing sectoral budget constraints across the private domestic, government, and external sectors yields the accounting identity:
$$(S - I) + (T - G) - CAB \equiv 0 \iff (S - I) \equiv (G - T) + CAB$$
No model may postulate simultaneous private net saving, fiscal deficit, and current-account paths that violate this identity.

### 1.4 Stock-Flow Reconciliation & Stock Accumulation/Revaluation
Every balance-sheet stock $S_{ij}(t)$ must be reconciled with transactions-flow and revaluation entries via exact continuous or discrete accumulation laws:
$$\dot{S}_{ij} = F_{ij} - \delta_{ij} S_{ij} + \dot{p}_i Q_{ij} \quad \text{(Net Transaction Flow } - \text{Depreciation/Default } + \text{Capital Gains Revaluation)}$$

### 1.5 Redundant-Equation Awareness (Walras's Law Analogue)
Because all rows and columns of the Transactions-Flow Matrix sum to zero, **one system-wide accounting identity is mathematically implied by all the others**. An $M$-variable SFC system contains only $M - 1$ independent market-clearing/accounting identities; dropping one redundant equation avoids overdetermination, and verifying `LHS - RHS == 0` on the omitted identity confirms global accounting consistency.
- *Tool Governance Notice:* In accordance with D1-LOCK-04 and Lesson L1, deterministic software matrix verification remains `PROPOSED — NOT AUTHORIZED` and is **not** created in Wave D3.

---

## 1.B Conditional SFC Closure & Portfolio Mechanisms (`CAPABILITY SUPPORT ≠ UNIVERSAL REQUIREMENT`)

The following two mechanisms belong to `heterodox-macro-modeling` capability support, but are **strictly conditional** on the model's specification and closure—never mandatory for every SFC model:

### 1.6 Brainard–Tobin Portfolio Adding-Up Restrictions (`CONDITIONAL METHOD`)
- **Applicability Condition:** Applies **only** when a model specifies multiple financial assets and endogenous portfolio allocation across those assets. (Not required in single-asset or fixed-financing SFC models.)
- **Conditional Rule:** When a sector allocates wealth $V_h$ across $K \ge 2$ assets via portfolio shares $\lambda_k = A_k/V_h$, parameters must satisfy vertical adding-up ($\sum_k \lambda_k \equiv 1$) and horizontal zero-sum sensitivities across asset returns and income ratios ($\sum_k \frac{\partial \lambda_k}{\partial r_j} \equiv 0 \; \forall j$, $\sum_k \frac{\partial \lambda_k}{\partial (Y/V)} \equiv 0$).

### 1.7 Buffer-Stock Identification (`CONDITIONAL METHOD`)
- **Applicability Condition:** Applies **only** when a buffer-stock asset or liability mechanism (such as residual money deposit accumulation $M_h$, inventory buffering, or endogenous overdraft loan accommodation $L_f$) is part of the model's stated closure.
- **Conditional Rule:** When a buffer-stock closure is used, the model must identify which specific asset or liability absorbs ex-post budget or expectation discrepancies in each sector rather than assigning it a conflicting independent behavioral equation.

---

# PART II: MODEL EXTENSION OPERATIONS & 8-STEP PROTOCOL

### 2.1 The Nine Canonical Extension Operations

| Op ID | Operation Name | Description | Classic Application | Typical Impact on Dynamics |
|:---|:---|:---|:---|:---|
| **EXT-1** | `REPLACE A CLOSURE` | Swap which variable adjusts to clear an accounting balance. | Replace Goodwin's Say's Law ($I \equiv S$) with a Kaleckian multiplier ($I(u) = S(u)$). | Changes reduced-form accumulation $g_K(\omega)$; can flip regime from profit-led to wage-led. |
| **EXT-2** | `ENDOGENIZE AN EXOGENOUS PROCESS` | Convert a constant parameter into a behavioral/technological function of states. | Replace $\hat{a} = \alpha$ with induced technical change $\hat{a} = \phi(\omega)$ or Kaldor–Verdoorn $\hat{a} = \alpha_0 + \eta \hat{Y}$. | Adds diagonal Jacobian entry $J_{ii}^* \neq 0$; can convert a neutral center into a stable focus. |
| **EXT-3** | `ADD A STATE VARIABLE` | Turn a constant ratio into a dynamic state with its own law of motion. | Allow capital-output ratio $\sigma$ to vary ($\dot{\sigma} = \sigma(\hat{k}-\hat{q})$) or investment share $h$ to adjust ($\dot{h} = h\gamma(u-u_n)$). | Increases dimension $n \to n+1$; when $n \ge 3$, stability analysis upgrades to Routh–Hurwitz where dimensionality warrants. |
| **EXT-4** | `ADD A SECTOR` | Disaggregate into multiple production or social sectors. | Disaggregate into Marxian Department I & II, or tradables vs. non-tradables. | Introduces relative price dynamics $p_1/p_2$ and intersectoral allocation shares. |
| **EXT-5** | `ADD A BALANCE SHEET` | Introduce debt, deposits, and financial interest flows. | Extend Goodwin $(e, \omega)$ to Keen (1995) Goodwin–Minsky $(e, \omega, d)$ with firm bank loans. | Subtracts interest $i d$ from profits; adds debt state $d$; introduces debt-deflation crisis boundary. |
| **EXT-6** | `ADD AN INSTITUTIONAL NONLINEARITY` | Replace linear behavioral equations with bounded or asymptotic functions. | Nonlinear real-wage Phillips curve $\phi(e) \to \infty$ as $e \to 1$, or nonlinear investment functions. | Enforces state-space invariance ($e < 1$); may generate limit cycles (analyzed via Poincaré–Bendixson in planar systems or Hopf bifurcation where conditions warrant). |
| **EXT-7** | `ADD REGIME DEPENDENCE` | Parameters or closures switch across state thresholds (piecewise-smooth/Filippov). | Central bank policy rate switching above an inflation target, or downward wage rigidity floors. | Partitions phase space into sub-regions $\Omega_1, \Omega_2$; requires checking sliding on switching manifolds. |
| **EXT-8** | `ADD AN EXTERNAL CONSTRAINT` | Open a closed economy to international trade, exchange rates, and capital flows. | Couple accumulation to Thirlwall's Law or foreign debt-to-GDP dynamics. | Constrains growth to $\hat{Y}_{BOP}$ or adds external debt state $d_{ext}$; links $\omega$ to real exchange rates. |
| **EXT-9** | `ADD TECHNICAL CHANGE FEEDBACK` | Couple factor productivities dynamically to profitability or ecological stocks. | Foley–Michl / Duménil–Lévy endogenous technical change paths. | Determines whether the maximum profit rate $r_{\max} = 1/\sigma$ stabilizes or trends downward. |

### 2.2 Mandatory 8-Step Extension Re-Derivation Protocol

```text
========================================================================================
MANDATORY 8-STEP EXTENSION RE-DERIVATION PROTOCOL
Invariant: Changing one equation does not necessarily change only one mechanism.
========================================================================================
STEP 1: IDENTIFY ALTERED ASSUMPTION
        Explicitly state which baseline assumption (ID, TECH, BEH, INST, CLOS, EXOG)
        is modified and write the new primitive equation.

STEP 2: IDENTIFY ALL EQUATIONS AFFECTED
        Trace the substitution chain through all equations; never assume a single
        reduced-form ODE changes in isolation.

STEP 3: IDENTIFY ADDED OR REMOVED FEEDBACKS
        Identify all newly created or eliminated partial derivatives ∂(dx_i/dt)/∂x_j,
        especially diagonal self-feedbacks J_ii.

STEP 4: UPDATE STATE VECTOR & ADMISSIBILITY DOMAIN
        Declare the new state vector x_new ∈ Ω_new (dimension n_new) and intensive definitions.

STEP 5: RE-CHECK ACCOUNTING & SFC CONSISTENCY
        Verify that new flows have counterpart stocks and satisfy sectoral budget identities.

STEP 6: RE-DERIVE STATIONARY STATES & ADMISSIBILITY BOUNDS
        Solve F_new(x*) = 0 from scratch and prove interior admissibility x* ∈ int(Ω_new).

STEP 7: RE-ANALYZE LOCAL & GLOBAL STABILITY
        Recompute Jacobian J_new(x*), applying 2D trace/determinant or higher-dimensional
        Routh-Hurwitz conditions where dimensionality warrants, and determine whether
        stability, oscillations, or bifurcations change.

STEP 8: REASSESS ECONOMIC INTERPRETATION & OBSERVABLE IMPLICATIONS
        State how the extension alters comparative statics, demand/growth regimes,
        and testable predictions for econometrics and PE.
========================================================================================
```

---

# PART III: OPEN-ECONOMY & EXTERNAL-CONSTRAINT EXTENSIONS

### 3.1 Balance-of-Payments Constrained Growth (Thirlwall's Law)
Starting from trade equilibrium $P_d X = E P_f M$ and export/import demand functions $X = (E P_f / P_d)^{\eta_X} (Y^*)^{\varepsilon_X}$ and $M = (P_d / (E P_f))^{\eta_M} Y^{\pi_M}$:
- Under constant real exchange rates ($\hat{q}_{rer} = 0$), derive Thirlwall's baseline growth rate:
  $$\hat{Y}_{BOP} = \frac{\varepsilon_X \hat{Y}^*}{\pi_M} = \frac{\hat{X}}{\pi_M}$$
- When capital flows $F$ or external debt servicing $i^* D_{ext}$ are present, incorporate foreign debt sustainability conditions (Moreno-Brid 1998/2003; Barbosa-Filho 2001).

### 3.2 Structuralist Center–Periphery (North–South) Dynamics
In coupled two-region models:
- **Center (North):** Endogenous technical change with high income elasticity of exports ($\varepsilon_X^N > 1$).
- **Periphery (South):** Structural BOP constraint with high income elasticity of imports ($\pi_M^S > 1$) and primary-commodity terms-of-trade degradation (Prebisch–Singer effect).

### 3.3 Real Exchange Rate, Distribution, and Contractionary Devaluation
- Real exchange rate $q_{rer} \equiv E P^* / P$ links import costs to domestic price markups, establishing the distributional curve $\omega = \omega(q_{rer})$ with $\partial \omega / \partial q_{rer} < 0$.
- **Contractionary Devaluation Test:** Audits whether currency depreciation expands output (Marshall–Lerner trade substitution dominates) or contracts output (redistribution from high-propensity wages to profits and foreign debt service reduces domestic demand).

### 3.4 Currency Hierarchy & External Debt Dynamics
In an open economy subject to international currency hierarchy (liquidity premium $\rho_N > \rho_S$):
$$i_S = i_N + \hat{E}^e + \xi(d_{ext}, f_{res}) - (\rho_S - \rho_N)$$
External debt-to-GDP ratio $d_{ext} \equiv D_{ext}/(P Y)$ evolves via:
$$\dot{d}_{ext} = (i^* + \hat{q}_{rer} - \hat{Y}) d_{ext} - nx(q_{rer}, u, Y^*)$$
Auditing stability requires checking whether the interest-growth differential $(i^* + \hat{q}_{rer} - \hat{Y})$ generates an explosive debt spiral.
