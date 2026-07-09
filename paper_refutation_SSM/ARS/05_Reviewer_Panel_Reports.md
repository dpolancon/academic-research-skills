# Consolidated Peer Review Reports

## Editor-in-Chief (EIC) Report

# Peer Review Report

## Manuscript Information
- **Title**: Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation and Choice of Technique
- **Manuscript ID**: N/A (Discussion Note)
- **Review Date**: 2026-06-20
- **Review Round**: First Round

---

## Reviewer Information

### Reviewer Role *
EIC (Editor-in-Chief / Associate Editor)

### Reviewer Identity *
Co-Editor of *Metroeconomica*, a senior mathematical economist specializing in Sraffian growth theory and classical distribution, with extensive experience editing journals that host the SSM vs. Harrodian stability debate.

### Reviewer Focus *
Evaluating journal fit for *Metroeconomica*, assessing the conceptual originality and strategic contribution to the Sraffian Supermultiplier debate, ensuring balanced representation of opposing theoretical positions, and examining the logical structure and readability for our analytical economics readership.

---

## Overall Assessment *

### Recommendation *
- [ ] **Accept** — Can be published directly, only minor formatting changes needed
- [ ] **Minor Revision** — Minor revisions needed, no re-review after revision
- [x] **Major Revision** — Substantial revisions needed, re-review required after revision
- [ ] **Reject** — Not suitable for publication in this journal

### Confidence Score *
4

### Summary Assessment *
This discussion note evaluates the long-run stability of the Sraffian Supermultiplier (SSM) model when the capital-capacity ratio ($v$) is endogenized via classical cost-minimizing choice of technique. By introducing a mechanization function where capacity labor productivity growth is an increasing, concave function of mechanization growth, the note shows that a constant $v$ represents a knife-edge case requiring a specific profit share. Under unbalanced growth ($\theta \neq 1$), the note proves there is no interior steady state and that the system exhibits a singularity at normal capacity utilization, leading to Harrodian instability. 
From an editorial standpoint, this is a highly rigorous, relevant, and well-structured contribution that directly addresses a central debate in heterodox macroeconomics, making it an excellent fit for *Metroeconomica*. However, the paper is limited by a conceptual "specification tautology" where the capital-capacity ratio is allowed to drift indefinitely ($v \to 0$ or $v \to \infty$) without feedback, which is economically implausible in the long run. Additionally, the tone is overly definitive regarding the inevitability of Harrodian instability, neglecting behavioral and institutional stabilizers discussed by SSM proponents. A major revision is required to address this long-run drift, clarify the economic intuition of the capacity transformation parameter, and temper the paper's claims.

---

## Strengths *

### S1: Structural Integration of Choice of Technique and Macro-Dynamics *
The note bridges two traditionally isolated literatures: the Sraffian Supermultiplier stability debate (e.g., Lavoie 2016, Serrano and Freitas 2017) and the classical choice of technique literature (e.g., Kurz and Salvadori 1995). As noted in Section 5 (p. 6), previous stability debates have treated the capital-capacity ratio $v$ as a constant parameter. By formalizing $v$ as an endogenous outcome of cost-minimizing technique selection along the wage-profit schedule (Equations 79–84), the paper exposes a critical, previously unexamined assumption of the SSM model.

### S2: Rigorous Mathematical desingularization proof *
The paper provides a rigorous mathematical proof (Proposition 1, Section 3) showing the non-existence of an interior steady state under unbalanced growth. The desingularization analysis at $\mu = 1$ (Step 5, p. 5) using the time reparameterization $d\tau/dt = 1/(\mu - 1)$ is exceptionally well-executed. It clarifies the mathematical nature of the divergence by showing that the vector field does not vanish at normal capacity utilization ($\mu = 1$), meaning trajectories must flow through this region rather than settle.

### S3: Concise and Focused Metroeconomica-Style Exposition *
The paper is structured perfectly for a discussion note in *Metroeconomica*. It uses a formal Proposition-Proof formatting (amsthm style, Section 3), state variables $(\mu, \phi)$ in a 2D dynamical system, and a compact, rigorous presentation that gets straight to the analytical core without unnecessary padding.

---

## Weaknesses *

### W1: Long-Run Implausibility of Indefinite Capital-Capacity Drift (Specification Tautology) *
**Problem**: The paper assumes that under unbalanced growth ($\theta \neq 1$), the capital-capacity ratio $v$ grows or shrinks indefinitely ($v \to \infty$ or $v \to 0$). Specifically, Equation 103 indicates $\hat{v} = (1 - \theta)\gamma(\mu - 1)$, and Equation 107 links the investment share $\phi$ to $v$. If $v$ drifts indefinitely, the investment share must eventually either collapse to zero or exceed the total product, which is economically impossible in the long run.
**Why it matters**: This represents a "specification tautology": by fixing the capacity transformation elasticity $\theta$ as a structural constant that does not respond to the long-run trend of $v$, the model is mathematically forced to diverge. It is economically implausible that capitalists would allow the capital-capacity ratio to grow or shrink indefinitely without technical or distributive adjustments (e.g., induced technical change forcing $\theta \to 1$).
**Suggestion**: The author must add a dedicated discussion in Section 5 or 6 addressing this limitation. They should acknowledge that in the ultra-long run, feedback mechanisms (such as induced technical change or distributive adjustments) must endogenously drive the economy back toward balanced growth ($\theta \to 1$). The claim of generic Harrodian instability should be qualified as a medium-to-long-run structural tendency rather than an absolute long-run prediction.
**Severity**: Critical

### W2: Overly Definitive Tone and Unbalanced Representation of the SSM Debate *
**Problem**: The note asserts that "Harrodian instability is the generic outcome" (p. 2, p. 5) and that the convergence of the SSM "holds only at a distributive knife edge" (p. 7). This frames the SSM's stability as practically impossible. It does not sufficiently engage with the behavioral and expectational arguments made by SSM proponents (e.g., Serrano and Freitas 2017) regarding the "taming" of Harrodian instability through expected growth rate adjustments.
**Why it matters**: A discussion note in *Metroeconomica* must maintain a balanced, objective representation of opposing views. Presenting Harrodian instability as the "generic outcome" without discussing how SSM proponents might respond (e.g., via adjustments in the desired rate of utilization or long-run changes in the autonomous demand growth rate) weakens the academic neutrality of the note.
**Suggestion**: Rephrase the concluding remarks (Section 6) and the abstract to frame the results as a "structural challenge to the standard SSM closure under endogenous choice of technique," rather than a definitive refutation. Discuss how the introduction of expected demand growth rate adjustments (as in Lavoie 2016) might alter the stability dynamics.
**Severity**: Major

### W3: Direct Equating of Mechanization Growth to Capital Accumulation *
**Problem**: In Section 2, the paper assumes a constant labor force ($\hat{L} = 0$) to directly equate the rate of mechanization growth $q$ to the capital accumulation rate $g_K$ (i.e., $q = g_K = \gamma(\mu - 1)$ on p. 4).
**Why it matters**: Mechanization (capital-labor ratio growth) and capital accumulation are distinct physical and economic processes. In the short-to-medium run, labor force growth or changes in labor intensity mean $q \neq g_K$. Equating them directly simplifies the mathematics but obscures the behavioral mechanism: it implies that firms adjust their long-term technical choice (mechanization rate) purely in response to short-run capacity utilization gaps ($\mu - 1$).
**Suggestion**: The author should introduce a brief discussion (or a detailed footnote) justifying this assumption. Specifically, they should clarify how the model behaves if labor force growth is positive ($n > 0$, yielding $q = g_K - n$) and explain the economic rationale for why the pace of mechanization is coupled to the utilization-driven investment accelerator.
**Severity**: Minor

---

## Detailed Comments *

### Title & Abstract
- **Title**: The title is accurate, descriptive, and appropriate for *Metroeconomica*.
- **Abstract**: The abstract (144 words) is concise and summarizes the main steps of the proof well. However, it should clarify that the result assumes distribution is exogenous.

### Introduction
- The introduction provides good coverage of the SSM stability debate (citing Lavoie, Serrano, Allain, Skott) and choice of technique (Kurz, Pasinetti).
- The transition from the SSM stability debate to choice of technique could be improved. The author should explain *why* capitalists choose techniques in a way that affects the capital-capacity ratio, providing the economic intuition before introducing the math.

### Literature Review / Theoretical Framework
- The integration of Sraffian choice of technique with the supermultiplier model is highly original.
- The use of Foley and Michl's (1999) mechanization function (Equation 75) is appropriate.
- However, the paper should acknowledge that in Sraffian long-period analysis, the capital-capacity ratio is generally assumed to be constant at the normal level of utilization because the choice of technique is analyzed under static distribution. The dynamic transition between techniques when distribution changes is what causes the drift in $v$, and this distinction should be explicitly articulated.

### Methodology / Research Design
- The mathematical formulation is clean and elegant.
- The desingularization in Section 3, Step 5 is the mathematical highlight of the paper. Reparameterizing time to resolve the singularity at $\mu=1$ is a standard tool in dynamical systems but rare in Post-Keynesian macroeconomics. The author is commended for this.

### Results / Findings
- Proposition 1 is clearly stated and the proof is logically sound under the model's assumptions.
- The algebraic contradiction (0 > 0) is a direct consequence of the incompatible nullclines.

### Discussion
- Section 4 ("Distribution, Technique, and the Persistence of Unbalanced Growth") provides a clear explanation of how the capacity transformation parameter $\theta(\pi)$ is determined by the profit share.
- However, as noted in Weakness 1, the discussion lacks a critical self-evaluation of the long-run limits of the model. If $v$ drifts indefinitely, the model violates basic physical and economic accounting identities in the long run. The discussion must address this.

### Conclusion
- The concluding remarks (Section 6) should be expanded slightly to discuss the implications of endogenizing distribution or including feedback from the capital-capacity ratio back to the choice of technique.
- The suggestion to explore how distributive dynamics might be attracted to the knife-edge profit share $\pi^*$ is a good starting point for future research.

### References
- The references are highly relevant, recent, and cover the key contributors to the SSM debate (Serrano, Freitas, Lavoie, Allain, Skott, Nikiforos).
- The Sraffian choice of technique references (Kurz & Salvadori, Pasinetti, Foley & Michl) are also appropriate.
- One minor issue: the citation style is mostly correct but the author should verify that the format aligns with *Metroeconomica*'s author guidelines (e.g., author-year citations).

---

## Questions for Authors *

1. **Long-Run Feasibility of Capital-Capacity Drift**: If $\theta \neq 1$, the capital-capacity ratio $v$ drifts indefinitely over time. Economically, this means the ratio of capital to capacity output either goes to zero or to infinity. How do you justify this indefinite drift in a long-run macro model? What feedback mechanisms (e.g., induced technical change, endogenous distribution, or labor supply constraints) do you think would prevent this drift in the real world, and how would they affect your stability results?
2. **Robustness to Alternative Investment Specifications**: Sraffian Supermultiplier models often include an expected rate of accumulation in the investment function to stabilize the model (e.g., Lavoie 2016). If the accelerator function (Equation 98) was modified to include an expected growth rate that adjusts slowly over time, would the singularity at $\mu=1$ still prevent convergence to a steady state, or could it lead to a steady state with a drifting $v$ but stable utilization?
3. **Economic Rationale for Coupling Mechanization and Utilization**: Equation 100 sets the rate of mechanization growth $q$ equal to the capital accumulation rate $g_K$ (assuming $\hat{L}=0$). Why would capitalists' choice of the *rate of mechanization* (which is a long-run technological choice) be driven by the short-run capacity utilization gap ($\mu-1$)? Would it not be more realistic for $q$ to be driven by relative factor prices (wages and profits) and a secular trend, while $g_K$ is driven by utilization?

---

## Minor Issues

### Language / Grammar
- Page 4, Equation 100: "Since mechanization growth is $q = \hat{K} - \hat{L}$, and assuming a constant labor force for simplicity ($\hat{L} = 0$), we have $q = g_K = \gamma(\mu - 1)$." The statement "Assuming a constant labor force for simplicity... ($q = g_K$)" should be formulated more carefully, as in the long run a constant labor force with positive productivity growth ($a^p > 0$) implies employment $L$ must shrink if output doesn't grow fast enough. This should be noted.
- Page 5, Step 5 of the proof: "the desingularized vector field requires $\frac{d\mu}{d\tau} = 0$, but the investment share dynamics reduce to $\frac{d\phi}{d\tau} = \phi^* g_z \neq 0$". The term $\phi^*$ should be written as $\phi$ since we are analyzing the dynamics off-equilibrium.

### Citation Format
- The citations generally follow the author-year format, which is appropriate for *Metroeconomica*.

### Layout
- The spacing and section layout are clean and match the journal style.

---

## Recommendations to Peer Reviewers

- **Reviewer 1 (Methodology)**: Please pay close attention to the time reparameterization in Step 5 of the proof ($d\tau/dt = 1/(\mu - 1)$). Verify whether the vector field limit $d\phi/d\tau \neq 0$ holds and if the transition through $\mu=1$ is mathematically sound and free from edge-case violations.
- **Reviewer 2 (Domain)**: Please review the choice of technique formulation based on the mechanization function (Equations 79–84) and check whether the capacity transformation parameter $\theta(\pi)$ aligns with Sraffian standards (e.g., Pasinetti, Kurz & Salvadori) or if it inadvertently introduces neoclassical production function assumptions.
- **Reviewer 3 (Perspective)**: Please evaluate the economic realism of the long-run non-convergence and challenge the assumption of a constant $\theta$ when the capital-capacity ratio is drifting. Confirm if this constitutes a "specification tautology" that artificially forces Harrodian instability.

---

## Dimension Scores *

Score each dimension 0-100 using the rubrics in `references/quality_rubrics.md`. Report the range descriptor that best matches.

| Dimension | Score (0-100) | Descriptor | Notes |
|-----------|--------------|------------|-------|
| Originality (20%) | 85 | Strong | Novel theoretical framework integrating choice of technique and SSM, exposing the implicit assumption of a constant $v$. |
| Methodological Rigor (25%) | 75 | Strong | Very sound mathematical modeling and elegant desingularization proof. Gaps relate to the physical implausibility of the long-run drift. |
| Evidence Sufficiency (25%) | 72 | Adequate | 15 references. While appropriate for a short mathematical note, a slightly wider review of SSM stability extensions would strengthen it. |
| Argument Coherence (15%) | 70 | Adequate | Very clear logical flow from the choice of technique to the dynamic instability. Gaps relate to the assumption of indefinite drift of $v$ without feedback. |
| Writing Quality (15%) | 80 | Strong | High-quality, precise mathematical economic prose. Tone could be slightly more balanced. |
| **Weighted Average** | **76.3** | **Major Revision** | Weighted score is 76.3 (which falls in the Minor Revision numerical range), but due to the critical conceptual weakness (indefinite drift of the capital-capacity ratio), a Major Revision is recommended. |


---

## Peer Reviewer 1 (Methodology) Report

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


---

## Peer Reviewer 2 (Domain) Report

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


---

## Peer Reviewer 3 (Perspective) Report

# Peer Review Report

## Manuscript Information
- **Title**: Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation and Choice of Technique
- **Manuscript ID**: N/A (Pre-submission Draft)
- **Review Date**: June 20, 2026
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role *
Peer Reviewer 3 (Perspective)

### Reviewer Identity *
A Post-Keynesian macroeconomist specializing in induced technical change and evolutionary growth models, known for critiquing rigid theoretical assumptions using empirical growth accounting.

### Review Focus *
Evaluating the economic realism of the long-run path, the potential "specification tautology" of fixing the capacity transformation parameter $\theta$ to cause instability, the behavioral specification of the investment function, and the representation of Harrodian instability.

---

## Overall Assessment *

### Recommendation *
- [ ] **Accept** — Can be published directly, only minor formatting changes needed
- [ ] **Minor Revision** — Minor revisions needed, no re-review after revision
- [x] **Major Revision** — Substantial revisions needed, re-review required after revision
- [ ] **Reject** — Not suitable for publication in this journal

### Confidence Score *
4
| Score | Meaning |
|-------|---------|
| 5 | Completely within my area of expertise, I am very confident in my assessment |
| 4 | Mostly within my area of expertise, high confidence |
| 3 | Partially within my area of expertise, moderate confidence |
| 2 | Some aspects outside my expertise, somewhat uncertain about my assessment |
| 1 | Mostly outside my expertise, my opinion is for reference only |

### Summary Assessment *
This manuscript explores the stability of the Sraffian Supermultiplier (SSM) when the capital-capacity ratio is allowed to vary due to capitalists' choice of technique. By modeling capacity labor productivity growth as a concave function of mechanization growth and letting capitalists cost-minimize, the authors show that unless the capacity transformation parameter $\theta$ equals 1, the SSM fails to converge to an interior steady state, resulting in a mathematical singularity at normal utilization.

From a Post-Keynesian perspective, while the paper makes a commendable contribution by linking Sraffian choice of technique with macroeconomic growth dynamics, it suffers from two major limitations: it treats the capacity transformation parameter $\theta$ as permanently fixed, which creates a specification tautology of explosive capital-capacity ratios, and it utilizes a restrictive, non-standard investment accelerator that lacks a trend growth component. These assumptions artificially manufacture instability.

Consequently, I recommend a Major Revision. The authors need to address the long-run economic implausibility of their technological assumptions and reformulate their investment function to align with standard SSM specifications.

---

## Strengths *

### S1: Integration of Choice of Technique with Demand-Led Growth *
The paper successfully bridges Sraffian choice of technique along the wage-profit schedule with the macroeconomic dynamics of the Sraffian Supermultiplier (Section 4, pp. 6–7). This is a valuable contribution, as these two heterodox economic literatures have largely evolved in parallel. The paper highlights how supply-side technical choices and cost minimization can constrain demand-side growth models.

### S2: Rigorous Identification of the Role of Capacity Elasticity ($\theta$) *
The model highlights that the stability of the Sraffian Supermultiplier depends on a hidden technological assumption: that the elasticity of capacity labor productivity growth with respect to mechanization ($\theta$) must equal exactly unity (Section 2, pp. 3–4). Citing this structural link provides a clear mathematical condition for balanced growth that is usually neglected in heterodox growth models.

### S3: Formal Analysis of the Vector Field Singularity *
The use of desingularization techniques (reparameterizing time $\tau$ via $d\tau/dt = 1/(\mu - 1)$) to analyze the vector field at $\mu = 1$ (Section 3, pp. 5–6) provides a rigorous mathematical demonstration of why the system cannot rest at the normal rate of capacity utilization under unbalanced growth.

---

## Weaknesses *

### W1: The "Specification Tautology" of Fixed $\theta$ in the Long Run *
**Problem**: The authors assume that $\theta$ (the elasticity of capacity labor productivity growth with respect to mechanization) is fixed and exogenous to the long-run growth process once the profit share $\pi$ is determined (Equation 87, p. 4 and Section 4, pp. 6-7). However, if $\theta \neq 1$, the capital-capacity ratio $v$ must grow or shrink indefinitely ($\hat{v} = (1 - \theta)q \neq 0$). In the long run, $v \to \infty$ or $v \to 0$ is economically impossible, as it implies either that capital becomes infinitely unproductive or that infinite output can be produced with zero capital.
**Why it matters**: By fixing $\theta \neq 1$ as a constant structural parameter, the authors build a tautology where instability is mathematically forced. In reality, feedback mechanisms (such as induced technical change, endogenous labor supply, or shifts in income distribution) must drive the economy toward $\theta \to 1$ in the long run. The conclusion of generic instability is an artifact of this rigid parameterization.
**Suggestion**: The authors should relax the assumption of a strictly constant $\theta$ in the long run. They should discuss how induced technical progress or endogenous distributive dynamics (e.g., as in Palley 2019 or Foley & Michl 1999) might act as error-correction mechanisms that pull $\theta$ toward 1, thereby restoring long-run stability.
**Severity**: Critical

### W2: Misspecification of the Investment Accelerator *
**Problem**: The investment function is specified as a simple Okishio-Harrod accelerator: $g_K = \gamma(\mu - 1)$ (Equation 98, p. 4). Under this specification, if capacity utilization is at its normal level ($\mu = 1$), the capital growth rate is zero ($g_K = 0$).
**Why it matters**: In a growing economy where autonomous demand grows at $g_z > 0$, a steady state requires capital to grow at the same rate ($g_K^* = g_z$). If $g_K = \gamma(\mu - 1)$, then to achieve $g_K^* = g_z$, the steady state must have $\mu^* = 1 + g_z/\gamma > 1$ (Equation 181, p. 5). Thus, even under balanced growth ($\theta = 1$), the model cannot converge to normal capacity utilization ($\mu_n = 1$). The authors' claim that "the investment share requires normal utilization ($\mu^* = 1$) for stationarity" is a consequence of their specific, restrictive, and economically implausible formulation of the accelerator, which lacks a trend-growth component (like expected growth of demand $g^e$ or $g_z$).
**Suggestion**: The authors should reformulate the investment function using standard Sraffian Supermultiplier specifications (e.g., Serrano 1995 or Lavoie 2016), where $g_K = g^e + \gamma(\mu - 1)$ where $g^e$ is the expected growth rate of demand that adapts over time, or using the investment share dynamics $\dot{\phi} = \gamma(\mu - 1)\phi$. Both allow the system to grow at normal utilization ($\mu^* = 1$) under balanced growth.
**Severity**: Major

### W3: Reductive Definition of Harrodian Instability *
**Problem**: The authors frame Harrodian instability as a structural/technological mismatch ($\theta \neq 1$) that makes the utilization and investment nullclines incompatible (Introduction, p. 2, lines 53-55).
**Why it matters**: In heterodox macroeconomics, Harrodian instability is a behavioral and expectational phenomenon driven by "animal spirits" and the feedback between actual utilization and investment expectations (e.g., Skott 2017, Lavoie 2016). By defining instability as a technological discrepancy, the paper shifts the focus away from the behavioral interactions that define the Harrodian tradition and reduces it to a supply-side technical mismatch.
**Suggestion**: The introduction and discussion sections should clarify this distinction. The authors should explicitly acknowledge that they are analyzing a structural source of instability (unbalanced growth via technique choice) rather than behavioral Harrodian instability, and discuss how behavioral expectation adjustments interact with this structural constraint.
**Severity**: Major

---

## Detailed Comments *

### Title & Abstract
- The title is accurate and appealing.
- The abstract is structured and complete, but it should mention the specific investment function used (the Okishio-Harrod accelerator) as it is critical to the result.

### Introduction
- The research background on SSM stability and Choice of Technique is well-positioned.
- The research question is clear.
- The research motivation is persuasive, but it overstates the generality of the result by not mentioning the restrictive nature of the investment function.

### Literature Review / Theoretical Framework
- The literature review is generally good, but fails to cite key works on induced technical change in heterodox models (e.g., Foley and Michl 1999; Marquetti 2004; Zamparelli 2015) that directly discuss the long-run convergence of $\theta$ to 1.
- The Sraffian distributive bracket is accepted for the sake of the argument, but the exogeneity of $\theta$ in the long run is problematic.

### Methodology / Research Design
- The choice of techniques is formally modeled. However, the accelerator function $g_K = \gamma(\mu - 1)$ is highly restrictive for a growth model, as it lacks a trend-growth term.

### Results / Findings
- Proposition 1 and its proof show a clear mathematical contradiction under the model's assumptions.
- Step 5 (Singularity Analysis) is technically well-done, but the economic interpretation of why the vector field doesn't vanish at $\mu = 1$ is an artifact of the misspecified investment function.

### Discussion
- The discussion connects choice of technique with SSM, which is positive.
- However, it fails to discuss the long-run implausibility of $v \to \infty$ or $v \to 0$ when $\theta \neq 1$.
- It also fails to discuss how expected growth rates could tame the system.

### Conclusion
- The conclusion over-infers that Harrodian instability is the "generic outcome" of Choice of Technique, whereas it is actually the outcome of combining a fixed $\theta \neq 1$ with a trendless accelerator.
- The future research directions should include endogenizing technical change (induced technical change) and distribution.

### References
- The references are relevant and recent. They cover the main authors (Lavoie, Serrano, Freitas, Allain, Skott).

---

## Questions for Authors *

1. **Long-Run Plausibility of $v \to \infty$ or $v \to 0$**: In your model, when $\theta \neq 1$, the capital-capacity ratio $v$ grows or shrinks at a rate $(1 - \theta)q$ (Equation 92). In the long run, this implies that $v$ will either grow to infinity or shrink to zero. How do you justify the long-run economic realism of this outcome, given that empirical capital-output ratios are relatively stable? Shouldn't there be an endogenous feedback mechanism (such as induced technical change or distributive changes) that forces $\theta \to 1$ in the long run?
2. **Misspecification of the Accelerator**: The investment function is specified as $g_K = \gamma(\mu - 1)$ (Equation 98). Under this specification, at normal utilization ($\mu = 1$), capital accumulation is zero ($g_K = 0$). In a growing economy where autonomous demand grows at $g_z > 0$, this specification implies that the economy can never grow at a normal rate of utilization (since $g_K^* = g_z$ requires $\mu^* = 1 + g_z/\gamma > 1$). How would your results change if you adopted the standard SSM investment function, such as $g_K = g^e + \gamma(\mu - 1)$ where $g^e$ is the expected growth rate of demand that adapts to $g_z$, or the investment share dynamics $\dot{\phi} = \gamma(\mu - 1)\phi$, both of which allow for steady-state growth at normal utilization ($\mu^* = 1$)?
3. **Induced Technical Change vs. Sraffian Exogeneity**: You treat the capacity transformation parameter $\theta(\pi)$ as a constant determined solely by the profit share $\pi$ (Equation 220). In the literature on induced technical change (e.g., Foley & Michl 1999; Julius 2005), technical change is responsive to labor scarcity or wage growth, which can dynamically adjust the mechanization function. Could you discuss how endogenizing the choice of technique through induced technical progress might act as an error-correction mechanism that tames the instability identified in the paper?

---

## Minor Issues

### Language / Grammar
- Page 5, Line 178: The equation is written as `$$ 0 = g_z - \theta\gamma(\mu^* - 1) $$`. The use of double dollar signs `$$` inside a list item is inconsistent with the single-bracket LaTeX style `\[ ... \]` used elsewhere in the proofs (e.g., lines 149, 154, 186). It should be formatted consistently.

### Citation Format
- JEL Codes (Page 2, Line 42): While JEL code O41 (One-sector growth models) and E11 (Marxian; Sraffian; Institutional; Evolutionary) are appropriate, the authors should consider adding JEL code O33 (Technological Change: Choices and Consequences) due to the heavy focus on the choice of technique and mechanization function.

---

## Dimension Scores *

| Dimension | Score (0-100) | Descriptor | Notes |
|-----------|--------------|------------|-------|
| Originality (20%) | 75 | Strong | Novel connection of Choice of Technique with SSM stability, but the claims are over-generalized. |
| Methodological Rigor (25%) | 55 | Weak | Severe model specification flaws (trendless investment, fixed $\theta \neq 1$) that lead to artificial instability. |
| Evidence Sufficiency (25%) | 55 | Weak | Key conceptual claims are unsupported due to the rigid technology assumption, and references are on the minimum threshold (15). |
| Argument Coherence (15%) | 55 | Weak | Significant logical jumps, particularly framing Harrodian instability as technological mismatch rather than behavioral. |
| Writing Quality (15%) | 80 | Strong | Professional academic prose, clear structure, and precise terminology. |
| Literature Integration (optional) | 65 | Adequate | Good coverage of SSM, but misses key literature on induced technical change. |
| Significance & Impact (optional) | 60 | Adequate | Theoretical contribution is clear, but the impact is limited by the restrictive model assumptions. |
| **Weighted Average** | **62.75** | **Major Revision** | Weighted average score falls in the Major Revision range (50-64). |


---

## Devil's Advocate Report

## Devil's Advocate Review

### Strongest Counter-Argument
The manuscript makes an elegant and formally rigorous attempt to connect the classical Sraffian choice of technique with the macroeconomic dynamics of the Sraffian Supermultiplier (SSM), rightly pointing out that the stability of the capital-capacity ratio is a crucial, yet often unexamined, assumption in this literature. However, a defender of the SSM would argue that the paper’s proof of structural instability is an artifact of two highly restrictive and contradictory assumptions. First, the paper defines capital accumulation as $g_K = \gamma(\mu - 1)$ (Equation 97), omitting the expected rate of growth of demand ($g^e$, which converges to the autonomous growth rate $g_z$) that is central to the SSM investment function (Serrano 1995; Freitas and Serrano 2015). By omitting this term, the author's investment share $\phi$ is forced to zero at normal utilization ($\mu^* = 1$). This means the non-existence of a steady state is not a result of technical change, but a trivial consequence of a misspecified investment function. Second, the assumption of a constant capacity transformation elasticity $\theta \neq 1$ in the long run represents a "specification tautology." If $\theta \neq 1$, the capital-capacity ratio $v$ must drift indefinitely ($v \to \infty$ or $v \to 0$), which is economically impossible in the long run. In reality, capitalists would face rising capital costs that induce technical change to save capital, endogenously driving $\theta \to 1$. When the investment function is correctly specified and technical change is endogenously biased, the SSM's stability is fully restored.

### Issue List

#### CRITICAL
| # | Dimension | Issue Description | Location | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|----------|---------------------|-----------------------------|
| 1 | Logic Chain Validation | **Mathematical Error in Desingularization Proof (Step 5)**: The author's proof of the non-existence of a steady state and the flow of trajectories through $\mu = 1$ relies on a desingularization analysis. The author claims that at $\mu = 1$, the desingularized vector field has $d\phi/d\tau = \phi^* g_z \neq 0$ (line 211), meaning the vector field does not vanish. However, this is an algebraic error. In the original system, the investment share dynamics are given by $\dot{\phi} = \phi ( \frac{\dot{\mu}}{\mu(\mu - 1)} + (1 - \theta)\gamma(\mu - 1) )$ (line 202). When desingularized with $d\tau/dt = 1/(\mu - 1)$, the derivative $d\phi/d\tau = \dot{\phi}(\mu - 1)$ contains a factor of $(\mu - 1)$. Since $\dot{\phi}$ approaches a finite limit $(-(s+m-\phi)g_z)$ as $\mu \to 1$ (due to the feedback loop where $\hat{\phi}$ cancels with the investment term in the $\hat{\mu}$ equation), the desingularized derivative $d\phi/d\tau$ must vanish at $\mu = 1$. The desingularized system actually has a line of equilibria at $\mu = 1$ (where both $d\mu/d\tau = 0$ and $d\phi/d\tau = 0$), completely invalidating the claim that trajectories must flow through this region without settling. | Section 3, Proof of Proposition 1, Step 5 (Lines 199-212) | N/A | N/A |
| 2 | Logic Chain Validation | **Logical Contradiction Between Choice of Technique and the Investment Accelerator**: The model contains an overdetermination and a direct logical contradiction in the definition of the mechanization rate $q$. Section 2 defines $q$ as the solution to the cost-minimization problem: $f'(q^*) = \pi$ (Equation 84), which yields a constant $q^*(\pi)$ for a given profit share $\pi$. However, Equation (100) and (102) assume that $q = g_K = \gamma(\mu - 1)$ (under $\hat{L} = 0$). This implies that the mechanization rate $q$ varies dynamically with capacity utilization $\mu$. Capitalists cannot simultaneously choose a constant cost-minimizing mechanization rate $q^*$ based on distribution and a variable rate $q$ driven by the capacity utilization gap. If $q$ is determined by cost minimization, then $g_K$ is pinned to a constant $q^*$, which contradicts the Harrodian investment accelerator $g_K = \gamma(\mu - 1)$. If the accelerator holds, then $q$ is not cost-minimizing, and the relation $a^p = \theta q$ with constant $\theta$ is invalid. | Section 2 (Lines 78-103) & Section 4 (Lines 216-222) | N/A | N/A |

#### MAJOR
| # | Dimension | Issue Description | Location | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|----------|---------------------|-----------------------------|
| 1 | Overgeneralization Check | **Specification Tautology of Long-Run $\theta \neq 1$**: The author's instability result is a direct consequence of fixing the capacity transformation elasticity $\theta \neq 1$ in the long run. If $\theta \neq 1$, then $\hat{v} = (1-\theta)q \neq 0$ in any state with positive mechanization growth. This means the capital-capacity ratio $v$ must grow or shrink indefinitely ($v \to \infty$ or $v \to 0$), which is economically impossible. In heterodox growth theory, the long-run capital-capacity ratio must be stable due to endogenous technical change or distribution adjustments (induced technical change), which forces $\theta \to 1$. By assuming a constant $\theta \neq 1$ in the long run, the author builds instability into the model by design, making it a specification tautology. | Section 2 (Lines 86-94) & Section 4 (Lines 216-225) | In macroeconomic growth theory (both neoclassical and heterodox, e.g., Foley & Michl 1999; Kaldor 1957), a long-run steady-state growth model must satisfy the Kaldor fact of a stable capital-output (or capital-capacity) ratio ($v$). A model where $v \to \infty$ or $v \to 0$ in the long run violates basic physical and economic consistency constraints (as the capital share of output would exceed 1 or go to 0). | The manuscript violates this consistency boundary by assuming $\theta \neq 1$ is a persistent, long-run parameter. This forces the capital-capacity ratio $v$ to drift indefinitely at rate $(1-\theta)q$ without any feedback mechanism (such as induced technical change or endogenous distribution) to stabilize it, thereby generating artificial long-run instability. |
| 2 | Logic Chain Validation | **Incomplete Representation of the Sraffian Supermultiplier Investment Function**: The author represents the capital accumulation rate as $g_K = \gamma(\mu - 1)$ (Equation 97). This formulation lacks the expected rate of growth of demand ($g^e$ or $g_z$), which is a defining feature of the Sraffian Supermultiplier investment function (Serrano 1995; Freitas & Serrano 2015; Lavoie 2016). In a standard SSM model, investment adjusts to track autonomous demand, meaning $g_K = g^e + \gamma(\mu - 1)$ where $g^e$ is the expected growth rate. In the steady state, $g^e = g_z$ and $\mu^* = 1$, allowing the investment share to be positive ($\phi^* = g_z v > 0$). By omitting the expected growth term, the author's model forces $\phi^* = 0$ if $\mu^* = 1$, which algebraically prevents a steady state with positive growth from existing, regardless of technical change. The paper's non-existence proof is thus a trivial result of an incomplete investment function rather than choice of technique. | Section 2, Equation (97) (Line 96-103) | Standard representations of the Sraffian Supermultiplier in heterodox economics (Freitas & Serrano 2015; Lavoie 2016) require that the investment-to-capital ratio or the rate of capital accumulation adjusts dynamically, and incorporates a term representing the expected growth rate of demand ($g^e$) to ensure that a steady state with positive growth and normal capacity utilization can exist. | The manuscript claims to refute the Sraffian Supermultiplier, but it reviews a model that does not include the expected growth term in the investment function, which is the core mechanism of the SSM. This represents a straw-man critique of the SSM. |

#### MINOR
| # | Dimension | Issue Description | Location |
|---|-----------|-------------------|----------|
| 1 | Overgeneralization Check | **Treatment of the Labor Force Growth Rate**: The author assumes a constant labor force ($\hat{L} = 0$) for simplicity (line 100). While this is a standard simplifying assumption, in a model of mechanization and productivity growth, if $\hat{L} = 0$, then the growth rate of output $g_z$ must eventually equal the growth rate of labor productivity $a^p$ to maintain stable employment. If $a^p$ is determined by cost minimization, this places a strict constraint on autonomous growth $g_z$. If $g_z > a^p$, employment grows indefinitely, violating $\hat{L}=0$. If $g_z < a^p$, employment shrinks to zero. This should be discussed. | Section 2, Line 100 |
| 2 | Cherry-Picking Detection | **Omission of the Wage-Profit Frontier Context**: The author asserts that $\theta(\pi)$ is constant for a given distribution $\pi$ (line 222). In a classical Sraffian choice of technique framework, the relationship between distribution (the wage rate $w$ and profit rate $r$) and the chosen technique is non-linear and can exhibit phenomena like reswitching or capital reversing. A constant elasticity $\theta$ is a simplifying assumption that contradicts the complex, non-linear nature of Sraffian technique selection along the wage-profit schedule. | Section 4, Lines 214-222 |

### Ignored Alternative Explanations/Paths
1. **Endogenous Capacity Transformation ($\theta \to 1$) via Induced Technical Change**: If the capital-capacity ratio $v$ drifts, this changes the cost structure of firms. For instance, if $v$ rises, capital costs rise relative to labor, which induces capitalists to select techniques that save capital (i.e. increase $a^p$ relative to $q$), forcing $\theta$ toward 1. This feedback mechanism (induced technical change) is standard in classical-Marxian models (e.g., Foley 2003, Duménil & Lévy 2003) and would restore long-run balanced growth.
2. **Endogenous Distribution ($\pi \to \pi^*$)**: If the growth process is unbalanced and leads to Harrodian instability, the resulting changes in employment and utilization would affect the bargaining power of classes, causing the profit share $\pi$ to adjust. If there is a feedback loop from macroeconomic instability to distribution, the profit share may converge to the knife-edge value $\pi^*$ where $\theta(\pi^*) = 1$, stabilizing the system.

### Missing Stakeholder Perspectives
- **Bargaining Workers / Trade Unions**: The model treats the profit share $\pi$ as prior and constant, determined by "class conflict, institutional bargaining, or monetary policy," but it completely ignores how workers react to unbalanced growth, high capacity utilization, or persistent unemployment. Their bargaining behavior would change the path of $\pi$ and thus $\theta$.
- **Central Bank / Monetary Authority**: The central bank's interest rate policy influences the profit rate and thus the profit share $\pi$. The central bank would likely adjust monetary policy in response to Harrodian instability or persistent capacity utilization gaps, which would change the distribution and the choice of technique.

### Unexamined Premise
- **Continuous and Smooth Choice of Technique**: The paper assumes that technical change is a continuous, differentiable process where firms can choose any rate of mechanization $q$ along a smooth function $f(q)$ at every instant (Equation 75). In Sraffian theory, technology is typically represented by a discrete book of blueprints (a set of distinct production methods). Technical change occurs through discrete shifts from one technique to another, rather than continuous adjustments of a growth rate. Assuming a smooth, continuous mechanization function is a neoclassical-style framing that is inconsistent with the classical Sraffian concept of a discrete choice of technique.

### Observations (Non-Defects)
- **Conceptual Synthesis**: The paper successfully highlights an important gap in the SSM literature, which is that the stability of the model has rarely been analyzed under conditions of structural change or drifting capital-output ratios.
- **Metroeconomica Style**: The mathematical structure of the note is highly elegant and fits the formatting conventions of Metroeconomica, using a concise Proposition-Proof style.


---

