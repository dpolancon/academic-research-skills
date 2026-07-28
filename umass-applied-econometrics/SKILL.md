---
name: umass-applied-econometrics
description: "Applied econometrics guidelines in political economy, synthesizing Plamen Nikolov's IZA guidelines with the UMass Amherst school of thought (forensic replication, visual-first data, endogenous class struggle, and Marglin-style descriptive macro grounding)."
---

# UMass Amherst Applied Econometrics & Political Economy Writing Guidelines

This skill defines the distinctive UMass Amherst approach to applied econometrics and political economy writing. It functions as a layer modifying standard economics writing tips (such as Plamen Nikolov’s *IZA Writing Tips*) to ensure that quantitative work remains conceptually rich, institutionally grounded, and forensic in its rigor.

> **Embedded Tools:**
> - [Cointegration Specification Audit Protocol](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/tools/cointegration_specification_audit.md): A step-by-step diagnostic tool for evaluating theoretical vs. stochastic admissibility of candidate regressors, collinearity filtering, FWL residual centering, LOESS pre-filtering, and bootstrap VECM combinatorics.

---

## 1. The Prose & Tone Layer (IZA-UMass Synthesis)

When drafting or editing economic papers, balance mainstream standards of clarity with the critical perspective of heterodox political economy:

*   **The BLUF Principle (Bottom Line Up Front):** State the main thesis, empirical strategy, and key results early. By the end of the second paragraph of the Introduction, the reader must see the phrase *"This paper examines..."* and immediately understand the paper's contribution.
*   **Simplicity Over Complexity:** Cut mathematical clutter and pretentious jargon. Avoid passive verb structures (e.g., *"it is observed that"* or *"estimation was performed"*). Use active voice (e.g., *"we estimate,"* *"the data show"*). Position subjects and verbs early in sentences.
*   **Banish AI-isms & Snobbish Posturing:** Eliminate mechanical transition words (e.g., *Furthermore, Moreover, It is important to note that, Indeed*). Restructure paragraphs so that connections are driven by the logical weight of the argument. Avoid defensive, paternalistic, or patronizing heterodox framing; let empirical rigor and clear theory carry the critique.
*   **Variable Definition:** Define mathematical symbols and variables immediately when they are first introduced (e.g., clearly define capital-capacity elasticity $\theta$ or utilization $u_t$ in the same sentence or paragraph where they appear).

---

## 2. The Empirical Forensic Protocol (The Econometrics Layer)

Standard econometrics treats models as neutral estimation routines. The UMass approach, informed by the work of department faculty and researchers, treats econometrics as a site of critical forensic investigation. Apply these six rules from the `09_papers_PDF` corpus:

### A. Forensic Transparency (Herndon, Ash, & Pollin 2014)
*   **The Rule:** Avoid "black-box" models. Make all coding, data exclusions, and weighting methodologies transparent.
*   **Implementation:** In the text, explicitly justify why specific years, countries, or outliers were excluded. Provide sensitivity checks demonstrating how estimation coefficients change under alternative data-cleaning choices.

### B. Data-First (Non-parametric) Visualization (Ash, Basu, & Dube 2017)
*   **The Rule:** Let the raw historical trends and discontinuities speak for themselves before imposing parametric model constraints.
*   **Implementation:** Incorporate non-parametric or semi-parametric plots of the raw data (e.g., locally weighted regressions, binscatter plots) in the conceptual or descriptive sections. Parametric regressions should justify or test the patterns observed in these raw plots, not contradict them.

### C. Endogenous Class Struggle & Distribution (Basu, Chen, & Oh; Rotta & Kumar 2024)
*   **The Rule:** Treat class struggle and distributional variables (profit rate, wage share) as endogenous drivers of accumulation, rather than exogenous dummy controls.
*   **Implementation:** When estimating long-run relationships, supplement single-equation models (like ARDL) with system-level models (like VECM/VAR) to check for bidirectional feedback. Discuss how structural variables (e.g., labor market tightness, reserve army of labor) mediate accumulation and utilization.

### D. Specification-Space Mapping (Maziarz 2017)
*   **The Rule:** Transparently display the boundaries of your specification search rather than presenting a single "preferred" model in isolation.
*   **Implementation:** Map the specification space. Explain which lag-lengths, deterministic specifications (e.g., PSS bounds testing cases), or dummy structures were tested. Report which specifications failed cointegration or stability tests, and explain the economic significance of these failures.

### E. Descriptive Macro Grounding (Marglin)
*   **The Rule:** Complement complex econometric estimations with simple, intuitive, descriptive historical growth indicators.
*   **Implementation:** Direct historical observations of GDP, employment, and capital stock growth rates must be integrated directly into the main text (e.g., Section 3 or 4). Cointegration residuals and derived utilization series must align with these descriptive trends; do not relegate basic macro-grounding to an appendix.

### F. Institutional Deconstruction of Indicators (Pollin 1998)
*   **The Rule:** Critique mainstream statistical indicators by revealing their underlying institutional and political-economic transmission mechanisms.
*   **Implementation:** When using variables like "capacity utilization" or "output gaps," explain how these measures are shaped at the firm and workplace level (e.g., intensity of labor, capital conversion rates, and class conflict over work schedules) rather than treating them as neutral physical indexes.

### G. Integration Order Governance as Specification Gate
*   **The Rule:** No variable enters a long-run cointegration specification solely on theoretical grounds. Theoretical motivation is necessary but not sufficient. Integration order evidence provides the binding constraint. Execute using the embedded [Cointegration Specification Audit Protocol](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/tools/cointegration_specification_audit.md).
*   **Implementation:** For each candidate regressor:
    1. Confirm $I(1)$ status using at least two complementary tests (e.g., ADF + KPSS) on both levels and first differences.
    2. Check pairwise collinearity: correlations above 0.99 or condition numbers above 30 block the candidate regardless of theoretical motivation.
    3. Check $I(2)$ risk: products, ratios, or accumulated paths of $I(1)$ variables may inherit $I(2)$. Test the candidate directly; do not assume integration order from its components.
    4. Present a consolidated verdict table mapping each candidate to its theoretical basis, integration evidence, and final disposition (promoted / held / blocked / rejected).
    5. Explain *why* blocked candidates fail in economic terms—the theory describes the decision mechanism; the stochastic evidence determines whether the observable proxy for that mechanism is admissible in a long-run regression.

### H. Political Economy Interpretation of Econometric Parameters
*   **The Rule:** Econometric parameters (cointegrating coefficients, error-correction speeds, interaction elasticities) are not neutral technical objects. Read them through the surplus approach, class struggle, and institutional periodization.
*   **Implementation:**
    1. State what the coefficient *means* in the analytical model—not just its statistical magnitude. E.g., "The cointegrating coefficient $\hat{\gamma}$ between log-machinery and log-structures recovers the long-run relative elasticity of the intensive to the extensive margin of accumulation."
    2. Interpret sign and magnitude changes across historical sub-windows as regime signatures: $\hat{\gamma} \approx 1$ = balanced Fordist mechanization; $\hat{\gamma} \gg 1$ = decoupled post-Fordist machinery acceleration; $\hat{\gamma} < 0$ = institutional incoherence.
    3. Connect distributional conditioning ($\omega_t$, $\pi_t$) to the induced innovation mechanism: rising wages drive mechanization through the FOC, not through exogenous technology shocks.
    4. For peripheral economies, interpret failures to cointegrate as evidence of structural regime-switching (e.g., FX-constrained accumulation) rather than data deficiency.

### I. Small-Sample Bootstrap for Short Macro Panels
*   **The Rule:** Asymptotic critical values for Johansen trace statistics, Engle-Granger residual tests, and related cointegration tests are calibrated for $T \to \infty$. In macro panels with $N \le 30$, use residual bootstrap resampling to guard against over-rejection.
*   **Implementation:**
    1. For sub-sample VECMs with $N \le 30$, report both asymptotic and bootstrap $p$-values.
    2. Use residual resampling (reshuffle estimated VAR/VECM residuals under the null of no cointegration) with at least 300 replications; 1,000 preferred.
    3. If asymptotic trace rejects but bootstrap $p > 0.10$, flag the result as "size distortion" and do not treat it as genuine cointegration evidence.
    4. Report bootstrap results in a dedicated table, not buried in footnotes.

---

## 3. Diagnostic Checklist for Writing & Reviewing Agents

Agents auditing a manuscript must evaluate it against this 14-point checklist:

1.  **BLUF Check:** Is the core contribution stated by the second paragraph of the introduction?
2.  **Variable Audit:** Are all mathematical parameters defined in-text immediately upon appearance?
3.  **Active Voice Check:** Are passive constructions and generic AI transition words (e.g., *Furthermore, Moreover*) removed?
4.  **Visual-First Test:** Is there a raw, non-parametric visualization of the main variables before parametric regressions are presented?
5.  **Forensic Transparency Check:** Are data exclusions, outliers, and weighting decisions explicitly justified in the text?
6.  **Endogeneity Audit:** Does the analysis discuss structural feedback between distribution and accumulation? If single-equation methods are used, is their system-level validity (VECM) checked?
7.  **Specification Map:** Does the text summarize which alternative models failed cointegration or stationarity gates, and why?
8.  **Descriptive Grounding Check:** Are raw growth rates of GDP, capital, and labor integrated into the narrative to contextualize the econometrics?
9.  **Institutional Critique:** Are mainstream indicators deconstructed to show their class/political-economic transmission mechanisms?
10. **Tone Balance:** Is the tone authoritative and critical, yet measured and free of defensive heterodox posturing?
11. **Integration Order Gate:** Are all candidate regressors tested for $I(d)$ order on both levels and first differences? Are blocked candidates reported with economic rationale?
12. **Coefficient PE Interpretation:** Are estimated coefficients interpreted through the political economy framework (surplus approach, class struggle, institutional periodization), not just as statistical magnitudes?
13. **Bootstrap Sensitivity:** For sub-samples with $N \le 30$, are bootstrap $p$-values reported alongside asymptotic critical values?
14. **Consolidated Verdict Table:** Is there a summary table mapping each candidate variable to its theoretical basis, integration order evidence, and final research disposition?
