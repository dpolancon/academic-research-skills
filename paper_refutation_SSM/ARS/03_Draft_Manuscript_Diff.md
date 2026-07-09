# Change Control & Diff Report: Manuscript Revision (Choice of Technique Edition)

This report tracks the changes made between the original LaTeX draft and the revised draft, incorporating the choice-of-technique micro-foundation of $\theta$ and correcting the mathematical proof to address the peer review comments.

## 1. Summary of Changes

| Section / Element | Status | Description |
| :--- | :--- | :--- |
| **Title** | Modified | Changed to *"Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation and Choice of Technique"* |
| **Abstract** | Modified | Updated to include the classical choice-of-technique micro-foundation of $\theta$ and the desingularization result. |
| **Introduction** | Modified | Framed $\theta$ as the joint growth elasticity of productivity and mechanization rather than neoclassical elasticity, and referenced the Sraffian choice-of-technique. |
| **Formal Setup (Section 2)** | Modified | Rigorously derived Equations (1) and (2) from accounting identities, defining $A^p$, $Q$, and $v$ from first principles, and showing that $q = g_K$. |
| **Propositions & Proofs (Section 3)** | Corrected | Removed the fabricated nullcline. Proved the steady-state contradiction using the correct $\hat{\mu} = 0$ nullcline ($\mu^* - 1 = g_z/(\theta\gamma)$) and the $\hat{\phi} = 0$ stationarity requirement ($\mu^* = 1$). Added a desingularization proof for the singularity at $\mu=1$. |
| **Distributive Bracket (Section 4)**| New | Added a dedicated section deriving $\theta(\pi)$ from cost minimization under a Sraffian distributive share $\pi$, explaining why unbalanced growth is persistent. |
| **Concluding Remarks** | Modified | Updated to discuss the implications of endogenous choice of technique and the Sraffian distribution. |
| **References** | Preserved | Preserved standard references (Serrano, Freitas, Lavoie, Nikiforos). |

## 2. Detailed Diff Log of Core Mathematical Sections

```diff
- \title{Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation}
+ \title{Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation and Choice of Technique}

- We introduce a capacity transformation parameter, \theta, which captures the long-run presence of technical change and structural bottlenecks.
+ Technical change is governed by a mechanization function where capacity labor productivity growth is an elastic function of the rate of mechanization, parameterized by \theta. Cost-minimizing capitalists optimize the technique under a Sraffian distributive schedule.

- \section{The Baseline Sraffian Supermultiplier with Capacity Transformation}
+ \section{The Model with Choice of Technique and Capacity Transformation}

- In the standard SSM framework, induced investment is governed by the need to adjust capacity to expected demand...
+ The capital-capacity ratio v is defined as v = K/Y^p. Let Q = K/L represent mechanization and A^p = Y^p/L capacity labor productivity.
+ \hat{v} = q - a^p.
+ Capacity labor productivity growth is a^p = f(q) where f'(q) > 0, f''(q) < 0.
+ Cost-minimizing capitalists maximize f(q) - q\pi, giving FOC f'(q^*) = \pi.
+ a^p = \theta q yields \hat{v} = (1 - \theta)q.
+ With Okishio-Harrod accelerator g_K = \gamma(\mu - 1) and q = g_K, we get \hat{v} = (1 - \theta)\gamma(\mu - 1).
+ Taking logs and differentiating \phi = g_K v / \mu yields:
+ \hat{\phi} = \frac{1}{\mu - 1}\hat{\mu} + (1 - \theta)\gamma(\mu - 1)

- \hat{\mu} = g_z + \frac{\phi}{s + m - \phi}\hat{\phi} - \gamma(\mu - 1) + \xi
+ \hat{\mu} = g_z + \frac{\phi}{s + m - \phi}\hat{\phi} - \theta\gamma(\mu - 1)

- \textit{Step 3: Evaluation of the \hat{\mu} nullcline.}
- The author asserts that the \hat{\mu} nullcline requires the condition \mu - 1 = z / (\theta\gamma). This equation is entirely unjustified.
+ \textbf{Step 3: Evaluation of the \hat{\mu} = 0 Nullcline.}
+ Set \hat{\mu} = 0 and \hat{\phi} = 0 in Equation (2) to obtain:
+ 0 = g_z - \theta\gamma(\mu^* - 1) \implies \mu^* - 1 = \frac{g_z}{\theta\gamma}
+ Since g_z > 0, \theta > 0, and \gamma > 0, we must have \mu^* - 1 = \frac{g_z}{\theta\gamma} > 0.
+ However, Step 2 requires \mu^* - 1 = 0. This yields the contradiction 0 = \frac{g_z}{\theta\gamma} > 0.

+ \textbf{Step 5: Singularity Analysis.}
+ Reparameterizing time by d\tau/dt = 1/(\mu - 1) yields the desingularized system.
+ At \mu = 1, d\mu/d\tau = 0, but d\phi/d\tau = \phi^* g_z \neq 0.
+ The vector field does not vanish at \mu = 1, proving divergence.
```
