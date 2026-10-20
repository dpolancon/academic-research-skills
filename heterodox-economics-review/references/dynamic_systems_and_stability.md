# Reference Module M2: Dynamic Systems, State Reduction, and Stability Analysis

- **Module Role:** Canonical Mathematical Systems and Stability Reference for `heterodox-macro-modeling`
- **Location:** `heterodox-economics-review/references/dynamic_systems_and_stability.md`
- **Authority:** Authoritative reference module implementing Ratified Wave D3-A Architecture (`§7`, `§8`, `§9`, `§11`, `§12`)

---

## 1. Mathematical Discipline & Demarcation Principle

This module enforces a strict separation among three distinct epistemic layers:

$$\text{ECONOMIC MECHANISM} \neq \text{MATHEMATICAL REPRESENTATION} \neq \text{PARAMETERIZATION}$$

- **Economic Mechanism:** The substantive theory of behavior, institutions, and conflict (e.g., reserve-army wage discipline or animal spirits).
- **Mathematical Representation:** The formal dynamical system (ODEs, difference equations, state space $\Omega$, Jacobians, vector fields).
- **Parameterization:** Specific numerical values or functional forms chosen for simulation or empirical illustration.

**Binding Negative Invariants:**
1. Do **not** infer economic coherence merely because a computer simulation exhibits oscillations.
2. Do **not** label every closed trajectory a "limit cycle"; distinguish conservative centers from dissipative limit cycles.
3. Do **not** invoke high-dimensional machinery (e.g., Routh–Hurwitz or Hopf bifurcations) when the dimensionality or mathematical structure does not warrant them.

---

## 2. Intensive State Reduction & Admissible Domain $\Omega$

### 2.1 State Vector Declaration
To analyze steady states, cycles, and growth paths in growing economies, trending extensive variables ($Y, K, L, N, D, Z$) must be transformed into **intensive state variables** (shares, rates, ratios). The model must declare:
- Dimension $n$ of the state vector: $\mathbf{x}(t) = (x_1(t), \dots, x_n(t))^T \in \Omega \subseteq \mathbb{R}^n$.
- Autonomous system of differential equations:
  $$\dot{x}_i = F_i(\mathbf{x}; \boldsymbol{\theta}), \qquad i = 1, \dots, n$$
  *(where $\boldsymbol{\theta}$ is the vector of time-invariant structural parameters).*
- Separation between **predetermined dynamic states** $\mathbf{x}(t)$ (governed by differential equations) and **algebraic endogenous variables** $\mathbf{y}(t)$ (solved instantaneously via static equilibrium conditions $\mathbf{0} = \mathbf{G}(\mathbf{y}, \mathbf{x}; \boldsymbol{\theta})$).

### 2.2 Economic Admissibility Domain $\Omega$
Before conducting stability analysis, the model must declare the economically admissible state space $\Omega$:
- Dimensionless shares: wage share $\omega \in (0, 1)$, profit share $\pi \in (0, 1)$.
- Dimensionless rates: employment rate $e \in (0, 1)$, capacity utilization $u \in (0, u_{\max})$ or $\mathbb{R}_{++}$.
- Capital-output ratio $\sigma \in \mathbb{R}_{++}$, net debt ratio $d \in \mathbb{R}$.

### 2.3 Boundary Invariance and Singularity Checks
- **Boundary Behavior ($\partial \Omega$):** Audit vector fields near boundaries (e.g., $e \to 0, 1$, $\omega \to 0, 1$, $u \to 0$):
  - Multiplicative boundaries $\dot{x}_i = x_i f_i(\mathbf{x})$ ensure $x_i = 0$ is an invariant manifold (positivity is preserved).
  - Check whether functional forms enforce upper bounds globally (e.g., nonlinear real wage bargaining $\lim_{e \to 1^-} f(e) = +\infty$) or only locally near equilibrium.
- **Singularity Audits:** For rational ODE terms $\dot{x}_i = \frac{N_i(\mathbf{x})}{D_i(\mathbf{x})}$, identify the zero locus $\mathcal{S} = \{ \mathbf{x} \in \Omega : D_i(\mathbf{x}) = 0 \}$:
  - Determine whether $\mathcal{S}$ intersects the interior admissible domain $\Omega$ or normal equilibrium values.
  - Evaluate limits using L'Hôpital's rule or phase-plane limits.
  - *Illustrative Example:* If a specification contains $\frac{1}{\mu - 1}\hat{\mu}$, verify whether $\hat{\mu} \to 0$ as utilization approaches normal capacity ($\mu \to 1$) or whether a non-removable singularity exists.

---

## 3. Equilibrium and Stationary-State Concepts

Macroeconomic analysis requires specifying which equilibrium concept is invoked:

| Equilibrium Concept | Time Horizon & Clearing Mechanism | Formal Representation |
|:---|:---|:---|
| **Short-Run Temporary Equilibrium** | Fast quantity/price adjustments with capital stock $K$, technology $a$, debt $D$, and distribution $\omega$ fixed. | Algebraic subsystem $\mathbf{0} = \mathbf{G}(\mathbf{y}, \mathbf{x}; \boldsymbol{\theta})$ solved for $\mathbf{y} = \mathbf{H}(\mathbf{x}; \boldsymbol{\theta})$. |
| **Medium-Run Stationary State** | Intensive state ratios cease to change ($\dot{\mathbf{x}} = \mathbf{0}$); extensive stocks grow at constant or balanced rates. | Fixed point $\mathbf{x}^* \in \Omega$ of $\mathbf{F}(\mathbf{x}^*; \boldsymbol{\theta}) = \mathbf{0}$. |
| **Long-Run Balanced Growth Path (BGP) / Normal Position** | Stocks and flows expand at a common rate $g^*$; capacity utilization equals normal/desired utilization ($u^* = u_n$). | $\hat{Y} = \hat{K} = g^*$, with $\dot{u} = 0, u^* = u_n$, and intersectoral profit rates equalized. |
| **Center of Gravitation** | Actual market paths fluctuate persistently around a long-run position without coming to rest at it. | Time-average property $\lim_{T\to\infty} \frac{1}{T}\int_0^T \mathbf{x}(t)\,dt = \mathbf{x}^*$ (e.g., Goodwin closed orbits). |
| **Hysteretic Moving Equilibrium** | The stationary state depends on the historical traverse path or initial conditions (zero eigenvalue / continuum of states). | Non-isolated fixed-point manifold or path-dependent parameter evolution. |

---

## 4. Stability Analysis Protocol

### 4.1 Nullclines and Phase-Space Partitioning
1. Derive nullclines by setting $\dot{x}_i = F_i(\mathbf{x}; \boldsymbol{\theta}) = 0$ for each $i = 1, \dots, n$.
2. Separate trivial boundary nullclines (e.g., $e = 0$, $\omega = 0$) from non-trivial interior nullclines.
3. Compute the directional signs of $\dot{x}_i$ across phase regions to establish vector-field orientation.

### 4.2 Stationary State & Interior Admissibility Gate
1. Solve $\mathbf{F}(\mathbf{x}^*; \boldsymbol{\theta}) = \mathbf{0}$ simultaneously for interior stationary state $\mathbf{x}^*$.
2. **Mandatory Admissibility Test:** State the exact parameter restrictions ensuring $\mathbf{x}^* \in \operatorname{int}(\Omega)$. Any equilibrium outside $\Omega$ (e.g., $\omega^* < 0$ or $e^* > 1$) is economically inadmissible.

### 4.3 General Jacobian Matrix Construction
Derive the symbolic Jacobian matrix $J(\mathbf{x}) = \left[ \frac{\partial F_i}{\partial x_j}(\mathbf{x}) \right]_{i,j=1}^n$ and evaluate $J^* \equiv J(\mathbf{x}^*)$ at the interior equilibrium.

---

## 5. Local Stability Classification by System Dimension

### 5.1 Planar Systems ($n = 2$)
Characteristic polynomial: $\lambda^2 - \operatorname{tr}(J^*)\lambda + \det(J^*) = 0$, with discriminant $\Delta = (\operatorname{tr} J^*)^2 - 4 \det J^*$.

| Conditions on $\operatorname{tr}(J^*)$ and $\det(J^*)$ | Eigenvalue Properties ($\lambda_1, \lambda_2$) | Dynamic Classification |
|:---|:---|:---|
| $\det(J^*) < 0$ | Real eigenvalues of opposite sign ($\lambda_1 < 0 < \lambda_2$) | **Hyperbolic Saddle Point** (1D stable manifold, 1D unstable manifold). |
| $\det(J^*) > 0$ and $\operatorname{tr}(J^*) < 0$, with $\Delta \ge 0$ | Real negative eigenvalues ($\lambda_1, \lambda_2 < 0$) | **Locally Asymptotically Stable Node**. |
| $\det(J^*) > 0$ and $\operatorname{tr}(J^*) < 0$, with $\Delta < 0$ | Complex conjugate with negative real parts ($\operatorname{Re}(\lambda) < 0$) | **Locally Asymptotically Stable Focus** (damped oscillations). |
| $\det(J^*) > 0$ and $\operatorname{tr}(J^*) > 0$, with $\Delta \ge 0$ | Real positive eigenvalues ($\lambda_1, \lambda_2 > 0$) | **Locally Unstable Node**. |
| $\det(J^*) > 0$ and $\operatorname{tr}(J^*) > 0$, with $\Delta < 0$ | Complex conjugate with positive real parts ($\operatorname{Re}(\lambda) > 0$) | **Locally Unstable Focus** (explosive oscillations). |
| $\det(J^*) > 0$ and $\operatorname{tr}(J^*) = 0$ | Purely imaginary eigenvalues ($\lambda_{1,2} = \pm i \sqrt{\det J^*}$) | **Non-Hyperbolic Point** (Hartman–Grobman fails; linearization inconclusive; requires nonlinear center vs. limit cycle analysis). |

### 5.2 Three-Dimensional Systems ($n = 3$)
Characteristic polynomial: $\lambda^3 + a_1 \lambda^2 + a_2 \lambda + a_3 = 0$, where:
$$a_1 = -\operatorname{tr}(J^*), \qquad a_2 = M_{11} + M_{22} + M_{33} \text{ (sum of principal } 2\times 2 \text{ minors)}, \qquad a_3 = -\det(J^*)$$

**Routh–Hurwitz Stability Theorem for $n = 3$:**
All three eigenvalues have strictly negative real parts ($\operatorname{Re}(\lambda_i) < 0$) if and only if all four conditions hold:
$$a_1 > 0, \qquad a_2 > 0, \qquad a_3 > 0, \qquad \text{and} \qquad a_1 a_2 - a_3 > 0$$

### 5.3 Higher Dimensions ($n \ge 4$)
Construct the Hurwitz matrix and verify that all principal leading minors $\Delta_k > 0$ ($k = 1, \dots, n$), or establish block-recursive triangular decomposition.

---

## 6. Nonlinear Dynamics: Centers, Limit Cycles, and Bifurcations

### 6.1 Conservative Centers vs. Dissipative Limit Cycles
A critical error in macroeconomic writing is conflating a conservative center with an isolated limit cycle:

| Attribute | Conservative Center (e.g., Goodwin 1967 Baseline) | Dissipative Limit Cycle (e.g., Poincaré–Bendixson / Hopf) |
|:---|:---|:---|
| **Mathematical Definition** | Continuum of nested closed orbits surrounding $\mathbf{x}^*$. | Isolated closed periodic orbit $\Gamma$ in phase space. |
| **First Integral / Conserved Quantity** | Admits a smooth constant of motion $V(\mathbf{x}) = \text{const}$ with $\dot{V} \equiv 0$. | No constant of motion; energy/wealth dissipates or pumps cyclically. |
| **Initial Condition Dependence** | **Permanent memory:** Cycle amplitude is permanently fixed by initial conditions $\mathbf{x}(0)$. | **Asymptotic independence:** Trajectories inside the basin of attraction converge onto $\Gamma$. |
| **Response to Transient Shocks** | One-time shocks permanently displace the economy onto a new closed orbit. | Economy returns asymptotically to the unique limit cycle $\Gamma$ after a shock. |
| **Structural Stability (Andronov–Pontryagin)** | **Structurally unstable:** Any perturbation adding $\operatorname{tr}(J^*) \neq 0$ destroys the center. | **Structurally stable:** Hyperbolic limit cycles persist under small vector-field perturbations. |

### 6.2 Proving Limit Cycles
1. **Poincaré–Bendixson Theorem (Planar Systems $n = 2$):** If a compact trapping region $\mathcal{D} \subset \Omega$ contains no stationary states other than a unique locally unstable focus/node, then $\mathcal{D}$ contains at least one stable limit cycle.
2. **Hopf Bifurcation Theorem:** When a parameter $\mu$ crosses a critical value $\mu_H$:
   - In 2D: $\operatorname{tr}(J^*(\mu_H)) = 0$ with $\det(J^*(\mu_H)) > 0$ and non-zero eigenvalue velocity $\left.\frac{d\operatorname{tr} J^*}{d\mu}\right|_{\mu_H} \neq 0$.
   - In 3D: $a_1(\mu_H) a_2(\mu_H) - a_3(\mu_H) = 0$ with $a_1, a_2, a_3 > 0$.
   - Distinguish **supercritical Hopf** (stable limit cycle emerges as equilibrium loses stability) from **subcritical Hopf** (unstable limit cycle collapses onto equilibrium, creating catastrophic jump/hysteresis).
