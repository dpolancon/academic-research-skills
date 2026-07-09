# Peer Review Report

## Manuscript Information
- **Title**: Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation and Choice of Technique
- **Manuscript ID**: N/A
- **Review Date**: June 20, 2026
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role *
Peer Reviewer 2 (Domain)

### Reviewer Identity *
A senior Sraffian theorist specializing in choice of technique, the wage-profit schedule, and Sraffian distributive growth models, with a research focus on the relation between mechanization, technical change, and capacity transformation.

### Review Focus *
Assessments of the Sraffian theoretical framework, choice of technique consistency, definition of the capacity transformation parameter $\theta$, and the methodological bracketing of distributive variables.

---

## Overall Assessment *

### Recommendation *
- [ ] **Accept** — Can be published directly, only minor formatting changes needed
- [ ] **Minor Revision** — Minor revisions needed, no re-review after revision
- [x] **Major Revision** — Substantial revisions needed, re-review required after revision
- [ ] **Reject** — Not suitable for publication in this journal

### Confidence Score *
5
| Score | Meaning |
|-------|---------|
| 5 | Completely within my area of expertise, I am very confident in my assessment |

### Summary Assessment *
This paper explores the long-run stability of the Sraffian Supermultiplier (SSM) model when the capital-capacity ratio is endogenized via classical choice of technique. Capitalists choose the rate of mechanization to maximize the profit rate at a given real wage along a Sraffian distributive schedule, causing the capital-capacity ratio to drift at a rate determined by distribution. Under unbalanced growth, the authors prove that the SSM model lacks an interior steady state, leading to generic Harrodian instability. 

From a Sraffian perspective, this note represents a valuable and long-overdue bridge between classical choice of technique literature and demand-led macro dynamics. However, the manuscript contains a significant mathematical inconsistency in its singularity analysis, where it evaluates the vector field at a state that violates the model's own definitional identities. Additionally, the definition of the capacity transformation parameter is conceptually ambiguous, and the foundational Sraffian references are omitted. Major revisions are required to resolve these issues before the paper can be published in a leading heterodox journal.

---

## Strengths *

### S1: Integration of Classical Choice of Technique with Macro Dynamics *
The note successfully bridges two research programs that have historically run in parallel: the Sraffian Supermultiplier convergence debate (e.g., Lavoie 2016, Serrano & Freitas 2017) and the classical theory of choice of technique (Kurz & Salvadori 1995). By showing that the constancy of the capital-capacity ratio $v$ (taken for granted in the SSM literature) is mediated by distribution-driven technique selection, the paper exposes an important unstated assumption in demand-led growth models.

### S2: Methodologically Consistent Bracketing of Distribution *
In Section 4, the author correctly treats the profit share $\pi$ as prior to the macroeconomic growth and adjustment dynamics. This aligns perfectly with Sraffa's (1960) core methodology, where distributive variables are determined by social, institutional, and historical factors outside the system of price and output determination, rather than being treated as endogenous parameters of a macroeconomic utility or production function.

### S3: Concise and Rigorous Proof of Non-Existence *
The algebraic proof in Steps 1-4 of Proposition 1 is elegant and compelling. By showing that the stationarity of the investment share requires $\mu^* = 1$ (Equation 168) while the capacity utilization nullcline requires $\mu^* - 1 = g_z/(\theta\gamma) > 0$ (Equation 181), the author establishes a clear, insurmountable algebraic contradiction that rules out an interior steady state under unbalanced growth ($\theta \neq 1$).

---

## Weaknesses *

### W1: Inconsistent Level-Growth Identity in Singularity Analysis *
**Problem**: In Step 5 of the proof of Proposition 1 (lines 199-212), the author performs a desingularization analysis at $\mu = 1$ and claims that at this boundary, the desingularized vector field requires $d\mu/d\tau = 0$ while the investment share dynamics reduce to $d\phi/d\tau = \phi^* g_z \neq 0$, assuming a steady-state investment share $\phi^* > 0$. However, by definition (Equation 107), the investment share is $\phi = \frac{\gamma(\mu-1)v}{\mu}$. If $\mu = 1$, the investment share $\phi$ MUST be identically zero. Assuming a state where $\mu = 1$ and $\phi^* > 0$ is a logical contradiction.
**Why it matters**: Evaluating the vector field at a state ($\mu=1, \phi^* > 0$) that violates the model's definitional identities makes the desingularization analysis mathematically invalid. In reality, the "singularity" at $\mu = 1$ is a coordinate artifact of formulating the system in growth rates ($\hat{g}_K = \dot{g}_K/g_K$, which divides by $g_K = 0$ at $\mu = 1$). In levels, the system is smooth, and the non-existence of a steady state at $\mu = 1$ follows directly from the fact that $\mu = 1 \implies \phi = 0 \implies \hat{\mu} = g_z > 0$, preventing stationarity.
**Suggestion**: The author should remove the desingularization analysis in Step 5 and instead provide a direct, levels-based explanation of why the system cannot rest at $\mu = 1$, highlighting that $\mu = 1$ forces $\phi = 0$, which causes output growth to track autonomous demand ($g_z$) while capital growth is zero, driving $\mu$ away from 1.
**Severity**: Critical

### W2: Ambiguity and Mislabeling of the Parameter $\theta$ *
**Problem**: The capacity transformation parameter $\theta$ is defined in the abstract and Section 2 (lines 87-88) as the "elasticity of capacity labor productivity growth with respect to mechanization." However, in Equation 88 ($a^p = \theta q$), $\theta$ is the ratio of the growth rates ($a^p/q = \hat{A}^p/\hat{Q}$). This represents the elasticity of the *level* of capacity labor productivity ($A^p$) with respect to the *level* of mechanization ($Q$). The elasticity of the *growth rate* ($a^p$) with respect to the *growth rate* ($q$) would instead be $\epsilon = \frac{d\ln a^p}{d\ln q} = \frac{q f'(q)}{f(q)}$.
**Why it matters**: In heterodox macroeconomics, precise terminology is vital to avoid confusion with neoclassical concepts. Mislabeling the level-elasticity as a growth-rate elasticity is mathematically incorrect and obscures the connection to Sraffian cost minimization.
**Suggestion**: Clarify that $\theta = a^p/q$ is the elasticity of the *level* of capacity labor productivity with respect to the *level* of mechanization (or the ratio of their growth rates), and distinguish it from the growth-rate elasticity $\epsilon = q f'(q)/f(q)$.
**Severity**: Major

### W3: Lack of Micro-foundations for the Capitalist Objective Function *
**Problem**: Equation 79 states that capitalists maximize productivity growth net of mechanization costs: $\max_q [f(q) - q\pi]$, yielding $f'(q^*) = \pi$ (Equation 84). The author does not explain why the profit share $\pi$ enters as a linear weight on the mechanization growth rate $q$.
**Why it matters**: In Sraffian theory, capitalists minimize unit costs or maximize the profit rate at a given real wage. Without deriving Equation 79 from these classical micro-foundations, the optimization problem appears ad-hoc.
**Suggestion**: Derivation should be added. Under a given real wage $w$ and a circulating capital model, the profit rate is $r = (A^p - w)/Q$. Differentiating with respect to time shows that the growth rate of the profit rate is $\hat{r} = a^p/\pi - q$, where $\pi = 1 - w/A^p$ is the profit share. Maximizing $\hat{r}$ with respect to $q$ subject to $a^p = f(q)$ is equivalent to $\max_q [f(q)/\pi - q]$, which (since $\pi > 0$) is equivalent to $\max_q [f(q) - q\pi]$.
**Severity**: Major

### W4: Omission of Foundational Sraffian Literature *
**Problem**: The paper frequently references Sraffian choice of technique and distributive schedules but does not cite Piero Sraffa's foundational 1960 book, *Production of Commodities by Means of Commodities*.
**Why it matters**: A paper asserting Sraffian foundations must engage with the primary text that established the wage-profit schedule and choice of technique framework.
**Suggestion**: Add a citation to Sraffa (1960) in the introduction and Section 4.
**Severity**: Minor

---

## Detailed Comments

### Title & Abstract
- The title is appropriate and descriptive.
- In the abstract, the term "elasticity of capacity labor productivity growth with respect to mechanization" should be corrected to "elasticity of capacity labor productivity with respect to mechanization" to align with the math.
- The claim in the abstract that "trajectories flow without settling" through the singularity is mathematically imprecise and should be revised in light of W1.

### Introduction
- The introduction does an excellent job of positioning the note within the SSM stability debate (Lavoie, Allain, Serrano, Freitas) and the choice of technique literature.
- Sraffa (1960) must be cited here when introducing the Sraffian distributive schedule.

### Literature Review / Theoretical Framework
- The choice of technique model is theoretically sound once the micro-foundations are derived (see W3).
- The author should explicitly contrast the Sraffian definition of $\theta$ with the neoclassical elasticity of output with respect to capital. Because $f(q)$ is concave ($f'' < 0$), the first-order condition $f'(q^*) = \pi$ implies that $\pi = f'(q^*) < f(q^*)/q^* = \theta$. Thus, $\theta > \pi$. This contrasts sharply with neoclassical growth theory, where the capital elasticity is identical to the profit share ($\alpha = \pi$). Highlighting this is a major contribution to the heterodox nature of the paper.

### Methodology / Research Design
- The dynamical system $(\mu, \phi)$ in Equations 120 and 134 is logically consistent, except for the singularity interpretation.
- The assumption $\hat{L} = 0$ is a reasonable simplification for a note, and the author's parenthetical note on how $n > 0$ affects the model is appreciated.

### Results / Findings
- Step 5 of the proof of Proposition 1 is mathematically inconsistent and must be revised (see W1). The levels-based representation is much cleaner and avoids the spurious singularity.

### Discussion
- The bracketing of distribution in Section 4 is well-reasoned. The author should expand on the discussion of endogenous distribution (Section 5) by noting that if distribution were endogenous to capacity utilization deviations, it could potentially stabilize the system by driving $\pi \to \pi^*$, representing a "distributive taming" of Harrodian instability.

### Conclusion
- The concluding remarks are clear and summarize the contribution well.

### References
- The references are highly relevant and recent (e.g., Palley 2019, Hein 2018).
- Piero Sraffa's (1960) *Production of Commodities by Means of Commodities* is missing and must be added.

---

## Questions for Authors

1. **Definitional Consistency**: How do you reconcile the assumption that the steady-state investment share $\phi^* > 0$ at $\mu = 1$ with the definition $\phi = \frac{\gamma(\mu-1)v}{\mu}$, which mathematically requires $\phi = 0$ when $\mu = 1$?
2. **Derivation of Objective Function**: Can you show the explicit steps deriving the capitalist objective function $\max_q [f(q) - q\pi]$ from the maximization of the profit rate or cost minimization under a Sraffian distributive schedule?
3. **Levels vs. Growth Elasticity**: Why is $\theta$ referred to as the elasticity of capacity labor productivity *growth* when Equation 88 ($a^p = \theta q$) defines it as the ratio of growth rates, which corresponds to the elasticity of the *level* variables ($d\ln A^p/d\ln Q$)?
4. **Endogenous Distribution Feedback**: If the profit share $\pi$ is made endogenous to capacity utilization (e.g., a wage-squeeze during high utilization), would this feedback loop stabilize the system toward the balanced growth path $\theta(\pi^*) = 1$?

---

## Minor Issues

### Language / Grammar
- Page 3, Equation 100: "Since mechanization growth is $q = \hat{K} - \hat{L}$..." — Note that $Q = K/L$ implies $\hat{Q} = \hat{K} - \hat{L}$, which is correct. However, using lowercase $q$ for the growth rate of capital-labor ratio $Q$ and capital letters elsewhere could be made more consistent.

### Citation Format
- In line 242, the publisher location for Harvard University Press is Cambridge, MA, which is correct. The bibliography formatting is clean and consistent.

---

## Dimension Scores

Score each dimension 0-100 using the rubrics in `references/quality_rubrics.md`.

| Dimension | Score (0-100) | Descriptor | Notes |
|-----------|--------------|------------|-------|
| Originality (20%) | 85 | Strong | The integration of choice of technique with the SSM is highly original. |
| Methodological Rigor (25%) | 60 | Adequate | The algebraic proof is correct, but the singularity/desingularization analysis is flawed (W1). |
| Evidence Sufficiency (25%) | 80 | Strong | Model setup and equations are fully specified, and proofs are detailed. |
| Argument Coherence (15%) | 75 | Adequate | Mostly coherent, but contains terminology ambiguity regarding $\theta$ (W2). |
| Writing Quality (15%) | 85 | Strong | The paper is well-written, clear, and follows Metroeconomica style conventions. |
| Literature Integration (optional) | 88 | Strong | Excellent engagement with SSM debates, but misses Sraffa (1960). |
| **Weighted Average** | **76.2** | **Major Revision** | **Required revisions on the mathematical proofs and terminology.** |
