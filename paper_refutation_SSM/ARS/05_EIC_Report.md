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
