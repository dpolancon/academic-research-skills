# Rigorous Mathematical Proof of Steady-State Non-Convergence under Unbalanced Growth

This document provides a formal mathematical proof showing that the Sraffian Supermultiplier (SSM) model admits no interior steady state when capacity transformation is unbalanced ($\theta \neq 1$), resulting in persistent divergence (Harrodian instability).

## 1. The 2D Dynamical System

The dynamical system is defined on the state space $(\mu, \phi) \in \mathbb{R}_{>0} \times (0, s+m)$, where $\mu$ represents capacity utilization and $\phi$ represents the investment share. The equations governing the dynamics are:

\begin{equation} \label{eq:phi_dyn}
    \hat{\phi} = \frac{1}{\mu - 1}\hat{\mu} + (1 - \theta)\gamma(\mu - 1)
\end{equation}

\begin{equation} \label{eq:mu_dyn}
    \hat{\mu} = g_z + \frac{\phi}{s + m - \phi}\hat{\phi} - \theta\gamma(\mu - 1)
\end{equation}

where $\gamma > 0$ is the investment sensitivity, $g_z > 0$ is the exogenous growth rate of autonomous demand, $s > 0$ is the saving rate, $m > 0$ is the leakage rate, and $\theta > 0$ is the capacity transformation elasticity ($\theta \neq 1$ under unbalanced growth).

---

## 2. Derivation of the Stationarity Loci (Nullclines)

An interior steady state $(\mu^*, \phi^*)$ is defined by the simultaneous stationarity of both state variables:
$$ \hat{\phi} = 0 \quad \text{and} \quad \hat{\mu} = 0 $$

### Step 1: The $\hat{\phi} = 0$ Nullcline Locus
Set the growth rate of the investment share to zero ($\hat{\phi} = 0$) in Equation \eqref{eq:phi_dyn}:
$$ 0 = \frac{1}{\mu - 1}\hat{\mu} + (1 - \theta)\gamma(\mu - 1) $$

Multiplying both sides by $(\mu - 1)$ to clear the denominator yields:
$$ 0 = \hat{\mu} + (1 - \theta)\gamma(\mu - 1)^2 $$

Isolating the growth rate of capacity utilization $\hat{\mu}$ along this stationarity locus:
\begin{equation} \label{eq:phi_null}
    \hat{\mu} = (\theta - 1)\gamma(\mu - 1)^2
\end{equation}

### Step 2: The Steady-State Capacity Utilization Locus
By definition, a steady state requires the growth rate of capacity utilization to be zero ($\hat{\mu} = 0$). Substituting $\hat{\mu} = 0$ into Equation \eqref{eq:phi_null} gives:
$$ 0 = (\theta - 1)\gamma(\mu^* - 1)^2 $$

Since the system is subject to unbalanced growth, we have $\theta \neq 1$. Furthermore, the behavioral sensitivity is positive ($\gamma > 0$). Thus, we must have:
$$ (\mu^* - 1)^2 = 0 \implies \mu^* = 1 $$
This shows that along the $\hat{\phi} = 0$ locus, the only possible steady-state capacity utilization rate is normal utilization ($\mu^* = 1$).

### Step 3: The $\hat{\mu} = 0$ Nullcline Locus
Now, we evaluate the stationarity of capacity utilization ($\hat{\mu} = 0$) in the second dynamic equation \eqref{eq:mu_dyn}. Impose both steady-state conditions $\hat{\mu} = 0$ and $\hat{\phi} = 0$:
$$ 0 = g_z + \frac{\phi^*}{s + m - \phi^*}(0) - \theta\gamma(\mu^* - 1) $$
$$ 0 = g_z - \theta\gamma(\mu^* - 1) $$

Isolating the utilization gap $(\mu^* - 1)$ yields:
\begin{equation} \label{eq:mu_null}
    \mu^* - 1 = \frac{g_z}{\theta\gamma}
\end{equation}
This condition represents the capacity utilization rate required to keep capacity utilization stationary in the presence of growing autonomous demand and capacity transformation drag.

---

## 3. The Algebraic Contradiction

To find the steady state, we must solve Equations \eqref{eq:phi_null} and \eqref{eq:mu_null} simultaneously. 

1. From Step 2, stationarity of the investment share requires:
   $$ \mu^* - 1 = 0 \implies \mu^* = 1 $$
2. Substituting $\mu^* = 1$ into the capacity utilization nullcline condition \eqref{eq:mu_null} yields:
   $$ 1 - 1 = \frac{g_z}{\theta\gamma} \implies 0 = \frac{g_z}{\theta\gamma} $$
3. Since $g_z > 0$, $\theta > 0$, and $\gamma > 0$, the right-hand side is strictly positive:
   $$ \frac{g_z}{\theta\gamma} > 0 $$
   This results in the contradiction:
   $$ 0 > 0 $$

Thus, no real-valued pair $(\mu^*, \phi^*)$ can simultaneously satisfy both stationarity conditions. The nullclines do not intersect in the state space.

---

## 4. Singular Vector Field Analysis

We now formally analyze the singularity at $\mu = 1$. The dynamic equation for $\phi$ in levels is:
$$ \dot{\phi} = \phi \hat{\phi} = \phi \left( \frac{\dot{\mu}}{\mu(\mu - 1)} + (1 - \theta)\gamma(\mu - 1) \right) $$

As $\mu \to 1$, the coefficient $\frac{1}{\mu - 1}$ diverges. To analyze the vector field in the neighborhood of $\mu = 1$, we define a desingularized system by scaling time by a factor of $(\mu - 1)$:
$$ \frac{d\tau}{dt} = \frac{1}{\mu - 1} $$

For $\mu > 1$ (the standard region of utilization), this time reparameterization is orientation-preserving. The desingularized system is:
$$ \frac{d\phi}{d\tau} = \phi \left[ \frac{\dot{\mu}}{\mu} + (1 - \theta)\gamma(\mu - 1)^2 \right] $$
$$ \frac{d\mu}{d\tau} = \mu(\mu - 1) \left[ g_z + \frac{\phi}{s + m - \phi}\hat{\phi} - \theta\gamma(\mu - 1) \right] $$

At $\mu = 1$, the desingularized capacity equation yields:
$$ \frac{d\mu}{d\tau} = 0 $$
However, the desingularized investment share equation yields:
$$ \frac{d\phi}{d\tau} = \phi \left[ \frac{d\mu/dt}{\mu} \right] $$
Substituting the actual capacity utilization growth rate at $\mu = 1$ (where the utilization gap is zero) and setting $\hat{\phi} = 0$:
$$ \frac{d\mu}{dt} = \mu \left( g_z \right) = g_z > 0 $$
This gives:
$$ \frac{d\phi}{d\tau} = \phi^* g_z \neq 0 \quad (\text{since } \phi^* > 0 \text{ and } g_z > 0) $$

Thus, even in the desingularized system, the vector field does not vanish at $\mu = 1$. The trajectories must flow through $\mu = 1$, preventing the existence of a stationary equilibrium point.

---

## 5. Conclusion

Under unbalanced growth ($\theta \neq 1$), the behavioral requirement of the Okishio-Harrod accelerator ($\mu^* = 1$) and the macroeconomic requirement of capacity utilization stationarity ($\mu^* = 1 + g_z/(\theta\gamma)$) are mutually exclusive. The system is structurally incapable of achieving a steady state. The capacity utilization rate and the investment share must continuously drift, resulting in persistent Harrodian instability and divergence. The stable Sraffian Supermultiplier steady state exists if and only if capacity growth is perfectly balanced ($\theta = 1$).