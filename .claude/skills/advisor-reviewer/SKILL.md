---
name: advisor-reviewer
description: "Academic paper reviewer customized for Michael (advisor) feedback, economic working paper standards (IZA Guidelines), and the UMass Amherst applied econometrics political economy style."
---

# Advisor Reviewer Custom Skill (Dissertation Rewrite Guide)

This skill calibrates the `academic-paper-reviewer` and `academic-paper` tools for the Critical Replication of Shaikh's capacity utilization chapter. It codifies the specific theoretical, empirical, and stylistic expectations of the advisor (Michael Ash), the committee, and the candidate (Diego Polanco).

---

## 1. Advisor (Michael Ash) Core Directives & Concerns

When reviewing or rewriting the manuscript, address these issues as high-priority constraints:

### A. Econometric Simplification & Cointegration Basics
* **Admissibility Definition:** Demystify the concept of "admissibility" in Section 4. Define it explicitly and explain what is at stake. Frame it in terms of counterfactuals (e.g., *What specifications are not admissible, and why?*).
* **Basics of Cointegration:** Focus on the core economic meaning of cointegration rather than drowning the reader in criteria and specification counts. 
* **Stationarity of Residuals:** If the series are not cointegrated (i.e., if the residuals are nonstationary after applying the cointegrating relationship), the write-up must explicitly reflect that. Do not hide nonstationarity under model selection criteria.
* **Model Selection:** Reduce the detailed discussion of criteria. Explain clearly what criteria were used (e.g., AIC, BIC, PSS bounds), present the best-performing models, and provide a brief sense of which alternatives failed and why.

### B. Theoretical Definitions & Math Clarification
* **Overaccumulation vs. Underaccumulation:** Retain the candidate's existing overaccumulation and stagnation tendency regime classification (Table 1). Frame and defend this classification by explicitly presenting its single-sector macro bounding as a limitation of the approach in the text.
* **Capital-Capacity Elasticity ($\theta$):** Review whether estimates of $\theta$ are biased downward by right-hand-side measurement error. Discuss this econometric limitation openly.
* **Acceleration Term ($d\hat{k}/dt$):** The advisor is confused by this second derivative of capital. Clarify that this is an acceleration term. Address whether it can systematically deviate from zero for long periods, or if there are temporary or rate-limiting institutional factors keeping it bounded.

### C. Descriptive & Institutional Transmission Mechanisms
* **The "Black Box" Mechanism:** Break down the high-level macroeconomic abstraction. Describe the concrete, institutional, and workplace-level mechanisms:
  * How does capital actually get converted into potential output (capacity) at the workplace level?
  * What changes this conversion rate over time (e.g., technical change, intensity of labor)?
  * How does actual output get produced from potential output (capacity utilization)?
  * How does class struggle (distributional conflict between labor and capital) moderate or mediate these workplace and market conversions?
* **Descriptive Grounding (The Marglin Emulation):** Following Stephen Marglin's approach in *"What Difference Does It Make?"*, supplement the co-integration econometrics with casual, descriptive, non-econometric observations of GDP, employment, and capital stock growth. **This grounding must focus strictly on the US economy (1947–2011) to align with Shaikh's original replication database. It must be integrated directly throughout Section 3 (Conceptual Framework) and Section 4 (Critical Replication) as a core pedagogical tool, and must not be demoted to an appendix.**

---

## 2. Bringing the Literature Section Down to Earth

* **Structure Preservation:** Keep the existing structure and subheadings of the literature review (Section 2 & 2.3) intact. Do not demolish the structure or remove subheadings.
* **Tone and Clarity:** "Bring it down to earth" by rewriting the prose to be highly accessible, clear, and less snobbish or paternalistic. Remove academic posturing, overly defensive heterodox framing, and unnecessary jargon. Make it reader-friendly while sustaining the core pillars of the theoretical argument (expectational adjustments, profitability regulation, and output-gap discipline).

---

## 3. Down-to-Earth Numerical Examples & Pedagogical Counterfactuals

For all sections **excluding** the literature review (especially Section 3: Conceptual Framework and Section 4: Critical Replication):

* **Stylized Baseline Parameters:** Reconstruct abstract concepts of "disproportionality," "unbalanced growth," or "instability" using concrete, intuitive numerical paths. Use stylized, simplified round numbers (e.g., a baseline capital growth rate $g_k = 3\%$, capacity growth rate $g_{yp} = 2\%$, and capital-capacity elasticity $\theta = 0.8$) to make the math clean and pedagogical.
* **The Punchline Principle:** Ensure each subsection has a clear mathematical/economic punchline that shows what is at stake. For example, explain how a small parameter change shifts the long-run trajectory:
  * *"A 1% increase in capital accumulation rate relative to capacity formation entails a X% increase in chronic excess capacity, inducing a path-dependent disequilibrium of Y% over time."*
* **Pedagogical Counterfactual Examples:** Introduce two specific counterfactual examples strictly to bring the econometrics down to earth (not as a central de facto counterfactual study):
  1. **In Section 4.3 (Stage S1):** Illustrate the "restriction counterfactual" ($\theta=1$ constraint) to show that imposing balanced growth causes the estimated capacity utilization path to drift to economically absurd levels.
  2. **In Section 4.6 (Stage S2):** Illustrate the "no-dummy counterfactual" to show that omitting the institutional dummy variables results in nonstationary residuals (spurious cointegration), demonstrating what is at stake in the admissibility gates.

---

## 4. Applied Econometrics in Political Economy (UMass Benchmark)

Load and enforce the comprehensive guidelines in the `umass-applied-econometrics` skill. Emulate the style of the papers in folder `09` (including `AshBasuDube2017.pdf` and `HAP2014.pdf`) as the benchmark for empirical political economy:

* **Forensic Transparency:** Detail data exclusions, weights, and sample boundary sensitivities.
* **Data-First Visualization:** Use non-parametric or semi-parametric plots of raw trends before VECM parametric regressions.
* **Balanced Critique:** Critique Shaikh's single-equation ARDL respectfully but rigorously using system-level VECM check restrictions.

---

## 5. Writing Structure & Clarity (IZA-UMass Synthesis)

Adhere to the unified prose standards of the `umass-applied-econometrics` skill, which synthesizes Plamen Nikolov's *Writing Tips for Crafting Effective Economics Research Papers (IZA)* with UMass PE DNA:

* **Active Voice & Simplicity:** Avoid passive, wordy AI-generated phrasing (e.g., "Furthermore," "Moreover").
* **BLUF Principle:** State the core thesis and contribution by the second paragraph of the Introduction.
* **Technical Definition:** Define variables (e.g., capital-capacity elasticity $\theta$) immediately upon introduction.

---

## 6. Preserving the Candidate's Marxist-Heterodox Style

Maintain the analytical strengths of Diego Polanco's writing voice (`profit_rate_chile.pdf`):

* **Surplus Approach:** Ground the work firmly within the Marxian surplus approach, focusing on profitability dynamics and distribution conflict as the drivers of accumulation.
* **Critique of Mainstream Output-Gap Governance:** Keep the historical and institutional critique of mainstream output-gap routines (e.g., survey indicators, Federal Reserve methods) as a political-economic mechanism of price-level and wage discipline.

---

## 7. Diagnostic Review Protocol

When executing a diagnostic check on the manuscript:
1. **Contrast the draft** (`CH1_CriticalReplication.pdf`) directly against the 68 items in the `Feedback_Matrix.xlsx` (specifically looking at items where `AI did ok?` was marked "no", such as the correction of "labor capacity" to "latent capacity" on Page 17, and the Page 7 comments on VECM/Specification space).
2. **Assess the mathematical and dynamic consistency** of the theoretical equations (applying the `heterodox-economics-review` skill guidelines on supermultipliers, singularities at $\mu=1$, and boundary conditions).
3. **Audit against the 10-Point Checklist** defined in the `umass-applied-econometrics` skill to enforce the visual-first, forensic transparency, active prose, and descriptive grounding constraints.
4. **Audit for prose tone and numerical grounding:**
   - Flag "snobbish" or paternalistic over-elaborations in the literature review, checking if it is brought "down to earth" without demolishing its structure.
   - Flag abstract mathematical assertions that lack a concrete "down-to-earth" numerical punchline in the framework and results sections.
   - Ensure that US historical/descriptive GDP, employment, and capital growth grounding comparisons are integrated directly within Sections 3 and 4, and not demoted to the appendix.
   - Ensure that the pedagogical counterfactuals ($\theta=1$ constraint and no-dummy cointegration) are presented as illustrative grounding examples rather than de facto counterfactual analyses.
   - **Verify that the single-sector bounding of the overaccumulation and stagnation tendency regime classification (Table 1) is explicitly discussed as an analytical limitation of the approach.**
5. **Generate a prioritized revision matrix** categorized by these themes.
