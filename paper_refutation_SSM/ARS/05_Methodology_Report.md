# Peer Review Report

## Manuscript Information
- **Title**: Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation and Choice of Technique
- **Manuscript ID**: N/A (Discussion Note)
- **Review Date**: June 20, 2026
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role *
Peer Reviewer 1 (Methodology)

### Reviewer Identity *
A mathematical macroeconomist specializing in dynamical systems theory, phase-plane analysis, bifurcation theory, and the desingularization of singular differential equations in economic dynamics.

### Review Focus *
Rigor of research design and mathematical/algebraic consistency. Specifically verifying step-by-step mathematical derivations (such as logarithmic differentiation), checking singularity resolution at capacity utilization $\mu = 1$, and confirming algebraic consistency of proofs and theorems.

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
| 4 | Mostly within my area of expertise, high confidence |
| 3 | Partially within my area of expertise, moderate confidence |
| 2 | Some aspects outside my expertise, somewhat uncertain about my assessment |
| 1 | Mostly outside my expertise, my opinion is for reference only |

### Summary Assessment *
This discussion note investigates the Sraffian Supermultiplier (SSM) stability debate by introducing Sraffian choice of technique and capacity transformation. The author models the elasticity of capacity labor productivity growth with respect to mechanization ($\theta$) as an endogenous outcome of cost-minimization along a Sraffian wage-profit schedule, showing that under unbalanced growth ($\theta \neq 1$) the SSM fails to converge to an interior steady state. From a methodological perspective, the paper's integration of Sraffian choice of technique with demand-led growth dynamics is highly original and mathematically structured. However, the mathematical proof contains a critical error in the handling of the vector field singularity at capacity utilization $\mu = 1$, where a regular, removable singularity is incorrectly treated as a divergent singularity, leading to a flawed desingularization analysis. Additionally, the model suffers from a "specification tautology" by fixing $\theta \neq 1$ in the long run, forcing the capital-capacity ratio to grow or shrink indefinitely. I recommend a Major Revision to address these mathematical and conceptual issues before the paper can be considered for publication in *Metroeconomica*.

---

## Strengths *

### S1: Integration of Choice of Technique with SSM Growth Dynamics *
The paper makes a valuable theoretical contribution by connecting the classical Sraffian literature on choice of technique (e.g., Kurz & Salvadori 1995, Foley & Michl 1999) with the macroeconomic stability debate of the Sraffian Supermultiplier (e.g., Allain 2015, Lavoie 2016, Serrano & Freitas 2017). Specifically, Section 4 (pp. 5-6) models the elasticity $\theta$ of labor productivity growth with respect to mechanization as an endogenous outcome of cost-minimizing technique selection along the wage-profit schedule, demonstrating that $\theta$ depends on the profit share $\pi$ and is not a free parameter.

### S2: Rigorous Derivation of Explicit 2D Dynamical System *
The step-by-step derivation of the dynamical system in capacity utilization $\mu$ and investment share $\phi$ (Section 2, pp. 3-4) is logically structured and mathematically consistent up to the formulation of Equations \eqref{eq:phi_dynamic} and \eqref{eq:mu_dynamic}. The use of logarithmic differentiation of the investment share identity $\phi = g_K v / \mu$ is executed correctly.

### S3: Structured Mathematical Exposition *
The paper uses clear and standard Metroeconomica-style presentation, utilizing formal propositions and proofs to structure its arguments (e.g., Proposition 1 and its proof on pp. 4-5) using the standard `amsthm` package environments (`\begin{proposition}` and `\begin{proof}`).

---

## Weaknesses *

### W1: Removable Singularity and Flawed Desingularization Analysis *
**Problem**: In Step 5 of the proof of Proposition 1 (p. 5), the author claims that the term $\frac{1}{\mu-1}\hat{\mu}$ in the investment share dynamics diverges at $\mu=1$, presenting a singularity in the vector field, and attempts to desingularize it using a time reparameterization $d\tau/dt = 1/(\mu-1)$. However, when solving the coupled system of equations \eqref{eq:phi_dynamic} and \eqref{eq:mu_dynamic} explicitly for the state variables' derivatives, we find that $\hat{\mu}$ is proportional to $(\mu-1)$. Specifically, we have:
$$\hat{\mu} = (\mu - 1) \frac{g_z + \gamma(\mu - 1) \left[ M(1 - \theta) - \theta \right]}{\mu - 1 - M}$$
where $M = \phi/(s+m-\phi) > 0$. Therefore, the term $\frac{1}{\mu-1}\hat{\mu}$ has a well-defined and finite limit as $\mu \to 1$:
$$\lim_{\mu \to 1} \frac{\hat{\mu}}{\mu - 1} = \frac{g_z}{-M} = -g_z \frac{s + m - \phi}{\phi}$$
**Why it matters**: The vector field is actually smooth and non-singular at $\mu=1$. The author's time reparameterization is mathematically incorrect and unnecessary. Furthermore, the author's claim that $\frac{d\phi}{d\tau} = \phi^* g_z \neq 0$ at $\mu = 1$ is incorrect because $\dot{\mu}$ vanishes at $\mu=1$, making $\frac{d\phi}{d\tau} = 0$ in the desingularized system. The desingularization incorrectly freezes the flow on the invariant manifold $\mu=1$ rather than resolving a singularity.
**Suggestion**: The author must rewrite Step 5 of the proof. Instead of claiming a singularity and attempting a time reparameterization, the author should write the dynamical system in its explicit state-space form, show that it is smooth and regular at $\mu=1$, and analyze the flow on the invariant manifold $\mu=1$ where $\dot{\mu}=0$ and $\dot{\phi} = -g_z(s+m-\phi) < 0$. This still supports the non-existence of an interior steady state but does so with correct mathematical arguments.
**Severity**: Critical

### W2: Long-Run "Specification Tautology" of Fixed Capacity-to-Capital Elasticity ($\theta \neq 1$) *
**Problem**: The model assumes that the elasticity $\theta$ is fixed and determined by the cost-minimizing technique under a given profit share $\pi$ (Section 4, pp. 5-6). If $\theta \neq 1$ in the long run, the capital-capacity ratio $v$ must drift indefinitely, growing or shrinking at a constant exponential rate: $v(t) = v(0) \exp[g_z(1/\theta - 1)t]$.
**Why it matters**: A continuously growing ($v \to \infty$ if $\theta < 1$) or shrinking ($v \to 0$ if $\theta > 1$) capital-capacity ratio is economically nonsensical in the long run. Capitalists would not continue to operate under a regime where the capital requirements for a unit of capacity drift to infinity or zero. This assumption creates a "specification tautology" that forces instability by assuming technology and distribution remain rigidly decoupled from the macroeconomic consequences of their drift.
**Suggestion**: The author should acknowledge this limitation and discuss how induced technical change or factor substitution (e.g., endogenizing the mechanization function or distribution) would act to bring $\theta \to 1$ in the long run, thus restoring balanced growth. This will make the paper's critique of the SSM more robust by framing it as a medium-run instability that requires endogenous technical adjustment to resolve, rather than a permanent technological tautology.
**Severity**: Major

### W3: Inconsistent Definition and Framing of Harrodian Instability *
**Problem**: Throughout the paper (e.g., Section 1, p. 2, and Section 4, p. 6), the author frames the instability arising from $\theta \neq 1$ as "Harrodian instability."
**Why it matters**: In the heterodox macroeconomics tradition, Harrodian instability is defined as a behavioral or expectational phenomenon driven by investment responsiveness to deviations of capacity utilization from its normal rate (e.g., the feedback loop between utilization and investment growth). In this paper, however, the instability is driven by a technological discrepancy ($\theta \neq 1$) and the algebraic non-existence of a steady state. Conflating these two concepts confuses the theoretical contribution.
**Suggestion**: The author should clarify the terminology. The instability due to $\theta \neq 1$ should be framed as "structural instability due to unbalanced technical change" or "unbalanced growth," and contrasted with traditional behavioral Harrodian instability.
**Severity**: Major

---

## Detailed Comments *

### Title & Abstract
- The title is clear and accurate. The abstract is concise (124 words) and summarizes the paper's thesis well, but it should be modified to reflect the corrected mathematical analysis of the vector field at $\mu=1$ (i.e., replacing the claim that "the vector field exhibits a singularity at $\mu=1$" with a description of the invariant manifold flow).

### Introduction
- The introduction provides a very good overview of the SSM stability debate and sets up the choice-of-technique critique. However, the author should preview how the "specification tautology" of a fixed $\theta \neq 1$ is handled or at least acknowledge that it is a simplifying assumption.

### Literature Review / Theoretical Framework
- The framework linking choice of technique (Sraffian schedule) with the capital-capacity ratio $v$ is elegant. But the author must clarify the economic intuition of why capitalists would allow $v$ to drift indefinitely without induced technical feedback.

### Methodology / Research Design
- The dynamical system derivation is sound until the singularity analysis. The author must solve the coupled equations explicitly for $\dot{\mu}$ and $\dot{\phi}$ to verify that the singularity is removable. The LaTeX formatting should also be cleaned up: replace the display math delimiters `$$` on line 178 with `\begin{equation}` or `\begin{align}`.

### Results / Findings
- The proof of Proposition 1 is correct in Steps 1-4, but Step 5 contains the mathematical errors identified in Weakness #1.

### Conclusion
- The conclusion summarizes the paper well, but it should be tempered by the mathematical corrections and a brief discussion of how endogenizing distribution or technical change (as mentioned on p. 6) might restore convergence.

### References
- The reference list is highly appropriate for *Metroeconomica* and *Journal of Post Keynesian Economics*, referencing key contributions in the SSM debate. The citation format is consistent.

---

## Questions for Authors *

1. If the coupled dynamical system in $\dot{\mu}$ and $\dot{\phi}$ is solved explicitly, the term $\frac{1}{\mu-1}\hat{\mu}$ does not diverge as $\mu \to 1$, but rather converges to a finite value. Given that the vector field is smooth at $\mu=1$, how does this affect your interpretation of $\mu=1$ as a "singularity"? Can you show that the line $\mu=1$ is a regular invariant manifold of the system?
2. If $\theta \neq 1$ is maintained in the long run, the capital-capacity ratio $v$ must grow or shrink exponentially without bound. What is the economic justification for capitalists selecting a technique that leads to such explosive or vanishing capital requirements in the long run? How would the introduction of induced technical change (where the mechanization function shifts in response to changes in $v$) affect the stability of the system?
3. Why do you frame the instability driven by the technological discrepancy $\theta \neq 1$ as "Harrodian instability," given that the latter is traditionally understood as a behavioral phenomenon driven by expectations and the investment accelerator?

---

## Minor Issues

### LaTeX Math Delimiters
- On line 178, the author uses `$$ 0 = g_z - \theta\gamma(\mu^* - 1) $$`. This should be replaced with `\begin{equation}` or `\begin{align}` to ensure consistent LaTeX spacing and formatting.

---

## Dimension Scores *

Score each dimension 0-100 using the rubrics in `references/quality_rubrics.md`. Report the range descriptor that best matches.

| Dimension | Score (0-100) | Descriptor | Notes |
|-----------|--------------|------------|-------|
| Originality (20%) | 70 | Adequate | Novel connection between choice of technique and SSM stability, but compromised by mathematical/conceptual issues. |
| Methodological Rigor (25%) | 48 | Weak | Sound derivation of equations, but critical mathematical errors in singularity analysis and desingularization. |
| Evidence Sufficiency (25%) | 62 | Adequate | Good selection of 15 theoretical references in the field; sufficient for a discussion note. |
| Argument Coherence (15%) | 55 | Weak | Clear structure, but logical disconnect in desingularization proof and specification tautology. |
| Writing Quality (15%) | 82 | Strong | Clear academic prose, excellent paragraph structure, and appropriate mathematical styling. |
| **Weighted Average** | **62.05** | **Major Revision** | **Required revisions on desingularization proof and handling of the specification tautology.** |
