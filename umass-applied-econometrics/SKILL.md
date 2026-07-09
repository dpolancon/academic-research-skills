---
name: umass-applied-econometrics
description: "Applied econometrics guidelines in political economy, synthesizing Plamen Nikolov's IZA guidelines with the UMass Amherst school of thought (forensic replication, visual-first data, endogenous class struggle, and Marglin-style descriptive macro grounding)."
---

# UMass Amherst Applied Econometrics & Political Economy Writing Guidelines

This skill defines the distinctive UMass Amherst approach to applied econometrics and political economy writing. It functions as a layer modifying standard economics writing tips (such as Plamen Nikolov’s *IZA Writing Tips*) to ensure that quantitative work remains conceptually rich, institutionally grounded, and forensic in its rigor.

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

---

## 3. Diagnostic Checklist for Writing & Reviewing Agents

Agents auditing a manuscript must evaluate it against this 10-point checklist:

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
