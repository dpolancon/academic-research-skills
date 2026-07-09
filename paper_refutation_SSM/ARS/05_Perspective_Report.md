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
