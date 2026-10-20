---
name: umass-applied-econometrics
description: "Applied econometrics guidelines in political economy: forensic replication, visual-first data inspection, integration order governance, small-sample bootstrapping, dynamic specification mapping (Toda-Yamamoto), and non-doctrinal empirical-theoretical demarcation."
---

# Applied Econometrics in Political Economy: Epistemic Standards & Forensic Methodology

This skill defines canonical methodological standards for applied econometrics within political economy (`applied-econometrics-pe`, maintained at runtime as `umass-applied-econometrics`). Drawing on the critical forensic tradition of the University of Massachusetts Amherst and contemporary empirical macroeconomics, it establishes rigorous protocols to ensure that quantitative research remains conceptually grounded, transparent, and epistemically open.

### The Governing Epistemic Boundary:

```text
THEORY
    proposes mechanisms, variables, hypotheses,
    restrictions, contrasts, and rival expectations
        ↓
EMPIRICAL METHOD
    determines stochastic admissibility, estimation,
    uncertainty, robustness, specification disposition,
    and empirical findings
        ↓
INTERPRETATION
    is conditioned on what the empirical evidence supports
```

- **A theoretical prior may motivate an empirical test; it may never dictate the empirical result.**
- **An empirical rejection may motivate a new hypothesis; it may never be converted into positive evidence for the rejected theory.**

### Implemented Domain & Scope Boundaries:
*   **Current Implemented Domain:** Political-economy time-series econometrics, specifically:
    - Integration-order analysis and unit root testing (ADF, KPSS, DF-GLS);
    - Cointegration testing and VECM / VAR system dynamics;
    - Toda–Yamamoto levels-augmented VAR causality testing;
    - Specification-space diagnostics and lag-order mapping;
    - Small-sample bootstrap sensitivity analysis;
    - Time-series empirical interpretation and descriptive macro grounding.
*   **Not Automatically Claimed by this Skill:** Cross-sectional causal inference, panel causal inference, Instrumental Variables (IV), Regression Discontinuity (RDD), Difference-in-Differences (DID) / event studies, synthetic control, matching, microeconometric treatment-effect methods, or other empirical fields not presently implemented. Expansion to these domains requires independent methodological justification.

> **Methodological Reasoning Protocols:**
> - [Cointegration Specification Audit Protocol](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/tools/cointegration_specification_audit.md): A diagnostic reasoning protocol for evaluating theoretical vs. stochastic admissibility of candidate regressors, collinearity filtering, conditional FWL residual orthogonalization, non-parametric inflection diagnostics, and small-sample bootstrap VECM combinatorics.
> - [Toda–Yamamoto Causality & Specification Mapping Protocol](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md): A standardized protocol benchmarked on Amiri & Ventelou (2012, *Economics Letters*) for level-augmented $(k + d_{\max})$ VAR estimation, lag-selection grid mapping, dynamic sign tracking ($\sum \hat{\beta}_i$), and open rival-hypothesis comparison tables.

---

## 1. Econometric Reporting Disciplines

Generic prose composition, paragraph architecture, and writing style are owned canonically by `econ-write` and `shared/protocols/prose_discipline_protocol.md`. This capability enforces the distinct reporting disciplines required for rigorous empirical econometrics:

*   **Forensic Accounting of Exclusions:** Every sample restriction, country removal, date truncation, or outlier trimming must be explicitly justified in the main text and accompanied by sensitivity checks.
*   **Operationalization Transparency:** Clearly define how unobservable theoretical constructs (e.g., capital capacity, technical change, bargaining power) are operationalized into observable statistical time series before presenting estimations.
*   **Specification-Space Exposure:** Do not present a single "preferred" specification in isolation. Report the boundaries of the specification search, including alternative lag structures, deterministic specifications, and specifications that failed diagnostic gates.
*   **Dispassionate Reporting of Non-Findings:** Treat empirical rejections, insignificant coefficients, and failed cointegration tests as substantive empirical findings rather than technical defects or opportunities for defensive rhetoric.

---

## 2. The Empirical Forensic Protocol (The Econometrics Layer)

Standard econometric practice too often treats models as mechanical estimation routines. Applied political economy treats econometrics as a site of critical forensic investigation, governed by strict empirical transparency:

### A. Forensic Transparency (Herndon, Ash, & Pollin 2014)
*   **The Rule:** Avoid "black-box" models. Make all coding, data exclusions, and weighting methodologies transparent.
*   **Implementation:** In the text, explicitly justify why specific years, countries, or outliers were excluded. Provide sensitivity checks demonstrating how estimation coefficients change under alternative data-cleaning and weighting choices.

### B. Direct Descriptive Grounding & Non-parametric Visualization (Ash, Basu, & Dube 2017)
*   **The Rule:** Before or alongside complex parametric estimation, inspect and report directly observed quantities materially relevant to the empirical question where this improves interpretability and model diagnosis.
*   **Implementation:** Incorporate descriptive plots of raw historical trends and discontinuities (e.g., non-parametric LOESS curves, binscatters) in introductory or data sections. Parametric regressions serve to evaluate, test, and conditionally qualify patterns observed in raw data, rather than superseding them without explanation. LOESS and binscatter plots represent useful diagnostic aids, not mandatory visualization forms for every study.

### C. Evaluating Endogenous Distribution & Structural Feedback
*   **The Rule:** When theoretical frameworks postulate bidirectional feedback between distribution and accumulation, test for feedback rather than assuming exogeneity mechanically.
*   **Implementation:** Evaluate whether distributional variables (profit rate, wage share) exhibit structural feedback with accumulation. Where bidirectional feedback is hypothesized, evaluate system-level models (such as VECM or VAR) alongside single-equation specifications. The choice between single-equation and system estimators must be justified based on identification assumptions, sample size, and diagnostic performance.

### D. Specification-Space Mapping (Maziarz 2017)
*   **The Rule:** Transparently display the boundaries of your specification search rather than presenting a single "preferred" model in isolation.
*   **Implementation:** Map the specification space. Explain which lag-lengths, deterministic specifications (e.g., PSS bounds testing cases), or dummy structures were evaluated. Report specifications that failed cointegration or stability tests, and explain the economic significance of these empirical non-findings.

### E. Descriptive Macro Grounding (Marglin)
*   **The Rule:** Ground complex econometric estimations in intuitive, descriptive historical macroeconomic aggregates.
*   **Implementation:** Integrate directly observed historical quantities materially relevant to the research question (such as growth rates of output, employment, investment, or sectoral aggregates) into the narrative. Cointegration residuals and derived utilization series must be evaluated alongside these descriptive series; any divergence between econometric estimates and observed aggregates must be transparently discussed and reconciled.

### F. Measurement Validity Assessment (Pollin 1998)
*   **The Rule:** Critique and assess statistical indicators by examining their underlying institutional construction and potential measurement biases.
*   **Implementation:** When utilizing composite or proxy variables (e.g., "capacity utilization," "output gaps," or "core inflation"), assess how these measures are constructed. Examine whether institutional shifts, changing statistical definitions, labor intensity variations, or aggregation procedures introduce systematic biases into the empirical series.

### G. Integration Order Governance & Mode Demarcation
*   **The Rule:** No variable enters an empirical specification solely on theoretical grounds. Theoretical motivation is necessary for conceptual relevance, but stochastic properties determine econometric admissibility. Execute using the embedded [Cointegration Specification Audit Protocol](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/tools/cointegration_specification_audit.md).
*   **Mode Demarcation:**
    - **Confirmatory / Structural Mode:** Variables entering a theory-linked structural or causal cointegration specification must possess an explicit conceptual role / construct mapping and clear integration order.
    - **Exploratory / Descriptive Mode:** Data patterns and empirical associations may be inspected before a fully developed theoretical mechanism is established (for pattern discovery, anomaly detection, and hypothesis generation). However, causal mechanism attribution or structural interpretation by post-hoc storytelling without independent support is strictly prohibited.
*   **Implementation:** For each candidate regressor in confirmatory models:
    1. **Integration Order Screen:** Confirm integration order using at least two complementary tests (e.g., ADF with null of unit root; KPSS with null of stationarity) on both levels and first differences. In standard cointegration (Johansen, Engle-Granger), regressors must be $I(1)$ in levels and $I(0)$ in first differences. Frameworks accommodating mixed orders (e.g., ARDL bounds testing, Toda–Yamamoto) must explicitly verify their required order constraints (e.g., absence of $I(2)$ series).
    2. **Collinearity Filter (Screening Heuristics):** Screen pairwise correlations and design matrix conditioning. Pairwise correlations above $0.99$ or condition numbers above $30$ serve as recommended diagnostic screening thresholds blocking candidate inclusion unless formal collinearity remediation is implemented.
    3. **$I(2)$ Risk Check:** Directly test products, ratios, or accumulated sums of $I(1)$ variables. Compound variables often inherit $I(2)$ properties; do not assume the integration order of compound series from their constituent parts.
    4. **Consolidated Verdict Table:** Present a summary table mapping each candidate variable to its theoretical motivation, integration and collinearity evidence, and final research disposition (**Promoted / Held / Blocked / Rejected**).
    5. **Demarcation Rationale:** Explain blocked candidates transparently: theoretical relevance defines the latent decision mechanism, while stochastic diagnostics determine whether the observable proxy is admissible in the chosen estimator.

### H. Interpretation of Econometric Parameters in Political Economy
*   **The Rule:** Econometric parameters (cointegrating vectors, error-correction speeds, interaction elasticities) must be interpreted through explicit analytical and institutional frameworks, rather than reported solely as statistical coefficients.
*   **Implementation:**
    1. **Analytical Meaning:** Explicitly link estimated coefficients to the structural parameters or first-order conditions of the underlying theoretical model. *(Example: interpreting the cointegrating elasticity between equipment capital and structures as the long-run elasticity of substitution between intensive and extensive accumulation margins).*
    2. **Subsample Stability & Anti-Cherry-Picking Discipline:**
       - Evaluate parameter stability across historically motivated subsamples or structural break dates. Interpret shifts in coefficient signs or magnitudes against stated historical hypotheses, rather than assigning hardcoded universal labels to numeric values. *(Example: evaluating whether mechanization elasticities shifted across pre- and post-structural-reform periods).*
       - **Anti-Cherry-Picking Rule:** Historically motivated subsample windows and structural breakpoints should, where feasible, be justified using historical or institutional evidence independent of the focal econometric result (`EX-ANTE / INDEPENDENTLY MOTIVATED PERIODIZATION`). If a window or breakpoint is selected after inspecting the focal regression result (`EX-POST RESULT-RESPONSIVE WINDOW SELECTION`), its status must be explicitly disclosed as exploratory/post-hoc, and sensitivity to alternative plausible windows must be transparently reported.
    3. **Distributional Mechanisms as Empirical Hypotheses:** Formulate hypotheses regarding distributional variables (e.g., wage share, profit share) as testable propositions. Evaluate whether estimated parameters support induced technological change or alternative mechanisms, reporting the empirical finding neutrally regardless of theoretical expectations.
    4. **Handling Empirical Non-Findings and Cointegration Failures:** A failure to find cointegration is strictly an empirical non-finding for the proposed long-run relationship in that sample and specification. It may **NOT** be interpreted as positive confirmation of structural regime-switching, foreign-exchange constraints, or institutional instability by fiat. Non-findings may motivate investigating alternative dynamic specifications, structural breaks, measurement errors, or regime changes, but each candidate explanation requires independent empirical verification.

### I. Small-Sample Bootstrap for Short Macro Panels
*   **The Rule:** Asymptotic critical values for Johansen trace statistics, Engle-Granger residual tests, and related cointegration tests are calibrated for $T \to \infty$. In macro panels with short samples ($N \le 30$ or $T \le 50$), use residual bootstrap resampling to guard against over-rejection (size distortion).
*   **Implementation:**
    1. **Dual Reporting:** For small-sample models, report both asymptotic and bootstrap $p$-values.
    2. **Resampling Protocol:** Execute residual bootstrap resampling under the null hypothesis of no cointegration using recommended computational defaults (minimum 300 replications; 1,000 preferred for publication tables).
    3. **Bootstrap Decision Rule:** When a validated bootstrap procedure is part of the declared inferential design, bootstrap-adjusted inference may govern the empirical decision according to that procedure's justified decision rule. Otherwise:
       - Report asymptotic and bootstrap inference separately;
       - Report disagreement transparently;
       - Explain which inferential procedure is privileged and why;
       - Do not apply a rigid repository-wide override threshold (e.g., bootstrap $p > 0.10$ is an illustrative screening heuristic, not a universal law).
    4. **Transparent Table Reporting:** Present bootstrap results in dedicated summary tables, not buried in footnotes.

### J. Toda–Yamamoto Causality & Specification Mapping (Amiri & Ventelou 2012 Benchmark)
*   **The Rule:** When evaluating directional precedence and temporal exogeneity in integrated or mixed time series, execute the levels-augmented Toda & Yamamoto (1995) $(k + d_{\max})$ VAR protocol following the publication standards of Amiri & Ventelou (2012, *Economics Letters*). Execute using the embedded [Toda–Yamamoto Causality & Specification Mapping Protocol](file:///c:/ReposGitHub/academic-research-skills/umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md).
*   **Methodological Core:**
    1. **Empirical $d_{\max}$ Determination:** Determine the maximal order of integration $d_{\max}$ empirically across all candidate series via unit root batteries (ADF/KPSS/DF-GLS). Do not assume $d_{\max}=1$ by default.
    2. **Ex-Ante Openness:** Maintain strict ex-ante openness. Estimate unrestricted $(k + d_{\max})$ levels systems without constraining foreign or institutional blocks to zero ex-ante. Exogeneity is identified strictly ex-post via Modified Wald (MWALD) joint tests on the first $k$ lags.
    3. **Modified Wald Testing:** Perform linear hypothesis testing strictly on the first $k$ structural coefficient matrices, leaving the extra $d_{\max}$ lag matrices unconstrained.
    4. **Diagnostic Integrity:** Verify lag selection stability and residual white-noise diagnostic gates (Breusch-Godfrey LM, ARCH LM, Jarque-Bera, White) at the optimal lag $k^*$ to ensure asymptotic validity.
*   **Recommended / Optional Reporting Layers:**
    - **Lag Robustness Grid:** Report test statistics across a grid of candidate lag lengths $k \in \{1, \dots, p_{\max}\}$ (with $k \in \{1, \dots, 4\}$ serving as an illustrative default grid for quarterly/annual macro data), identifying optimal lag $k^*$ selected by information criteria (SBIC and AIC) with note marker ($^a$).
    - **Dynamic Sign Tracking:** Report the structural coefficient sum $\sum_{i=1}^k \hat{\beta}_i$ alongside the Wald statistic to capture cumulative dynamic direction where economically meaningful.
    - **Theoretical Sign & Precedence Comparison Table:** Construct an open comparison table contrasting project-declared competing theoretical hypotheses (e.g., Theory A vs. Theory B vs. Null) against empirical MWALD outcomes and dynamic signs.

---

## 3. Diagnostic Checklist for Reviewing & Auditing Econometric Manuscripts

Agents auditing an applied econometrics manuscript must evaluate it against this 15-point checklist:

1.  **Forensic Transparency Check:** Are all sample exclusions, country selections, date trimmings, and weighting choices explicitly justified in the text and tested with sensitivity checks?
2.  **Operationalization Audit:** Are unobservable theoretical constructs explicitly mapped to observable empirical series and parameters before estimation?
3.  **Descriptive Grounding Inspection:** Are directly observed quantities relevant to the question reported alongside descriptive plots to establish basic empirical facts prior to parametric modeling?
4.  **Feedback & Endogeneity Evaluation:** Where bidirectional feedback between distribution and accumulation is theoretically plausible, is feedback empirically tested rather than assumed?
5.  **Specification-Space Exposure:** Does the text transparently display the boundaries of the specification search, including alternative lag lengths, deterministic options, and failed models?
6.  **Descriptive Macro Reconciliation:** Are observed macroeconomic aggregates integrated into the narrative, and is any divergence between econometric estimates and raw aggregates reconciled?
7.  **Measurement Validity Assessment:** Are statistical indicators assessed for institutional construction, aggregation issues, and potential measurement biases?
8.  **Dispassionate Reporting:** Is the empirical narrative free of defensive or patronizing rhetoric, allowing evidence and robust theory to carry the findings?
9.  **Integration Order Gate & Mode Check:** Are confirmatory variables tested with complementary unit root tests (ADF + KPSS)? If exploratory patterns are presented, are they explicitly disclosed as non-causal?
10. **Collinearity & $I(2)$ Risk Screen:** Are candidate variables screened for high collinearity ($r > 0.99, \text{CN} > 30$) and compound $I(2)$ risk?
11. **Epistemic Demarcation & Non-Finding Check:** Are empirical non-findings (e.g., cointegration rejections) reported transparently as non-findings, without converting rejections into positive theoretical confirmations by fiat?
12. **Parameter Analytical Interpretation:** Are estimated coefficients interpreted through explicit theoretical models or behavioral equations rather than reported as bare numbers?
13. **Subsample Selection Safeguard:** Are subsample windows justified by ex-ante independent evidence, or explicitly disclosed as exploratory/post-hoc with window sensitivity reported?
14. **Small-Sample Bootstrap Sensitivity:** For small samples ($N \le 30$ or $T \le 50$), are bootstrap $p$-values reported alongside asymptotic values, with inferential disagreements transparently explained?
15. **Toda–Yamamoto Protocol Check:** Are Granger causality tests executed with empirical $(k + d_{\max})$ levels augmentation, ex-ante openness, and proper separation of core MWALD testing from optional sign-tracking and tournament tables?
