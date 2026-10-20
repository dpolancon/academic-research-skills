# Toda–Yamamoto Macroeconomic Causality & Specification Mapping Protocol
## Methodological Reasoning Protocol for `/umass-applied-econometrics` (Amiri & Ventelou 2012 Benchmark)

This document serves as a methodological reasoning protocol embedded within the `/umass-applied-econometrics` skill suite. It operationalizes Rule J (*Toda–Yamamoto Causality & Specification Mapping*), Rule A (*Forensic Transparency*), and Rule D (*Specification-Space Mapping*).

---

## 1. Methodological Foundation: Toda & Yamamoto (1995) / Dolado & Lütkepohl (1996)

When testing temporal precedence and directional causality in macroeconomic time series that exhibit unit roots ($I(1)$ or mixed $I(0)/I(1)$ processes), standard Granger causality tests in first differences suffer from:
1. **Severe power loss** due to overdifferencing.
2. **Omission of cointegrating relationships** (long-run levels information).
3. **Non-standard asymptotic distributions** if estimated in unaugmented levels VARs.

The **Toda–Yamamoto (1995)** and **Dolado–Lütkepohl (1996)** procedure overcomes these defects through intentional **levels lag-augmentation**:
$$\mathbf{Y}_t = \mathbf{\alpha}_0 + \sum_{i=1}^k \mathbf{\Phi}_i \mathbf{Y}_{t-i} + \sum_{j=k+1}^{k + d_{\max}} \mathbf{\Phi}_j \mathbf{Y}_{t-j} + \mathbf{\varepsilon}_t$$
where:
- $k$ is the true/optimal structural lag order of the VAR system.
- $d_{\max}$ is the maximal order of integration observed empirically across the candidate variable vector.
- Linear hypothesis restrictions ($H_0: \mathbf{R} \operatorname{vec}(\mathbf{\Phi}_1, \dots, \mathbf{\Phi}_k) = \mathbf{0}$) are tested **strictly on the first $k$ coefficient matrices**, leaving the extra $d_{\max}$ lag matrices unconstrained.

### Asymptotic Invariance Theorem
Under $(k + d_{\max})$ augmentation, the Modified Wald (MWALD) test statistic converges asymptotically to a standard $\chi^2(m)$ distribution with $m = \operatorname{rank}(\mathbf{R})$ degrees of freedom, regardless of cointegration status or whether series are $I(0)$ or $I(1)$, provided $k \ge d_{\max}$.

---

## 2. Benchmark Architecture: Core Procedure vs. Optional Reporting Layers

To prevent ad-hoc specification selection and ensure complete forensic transparency, applied econometric studies executing Toda–Yamamoto testing should distinguish between the core estimation procedure and recommended reporting layers benchmarked on **Amiri & Ventelou (2012, *Economics Letters* 116: 541–544)**:

```text
========================================================================================
METHODOLOGICAL CORE PROCEDURE (ESTIMATION & TESTING)
========================================================================================
[Phase 1: Integration Order Screen] ── Confirm d_max across all series via ADF/KPSS/DF-GLS
       │
       ▼
[Phase 2: Lag Order Selection] ── Evaluate VAR(k) information criteria (SBIC, AIC, HQ, FPE)
       │
       ▼
[Phase 3: Levels Lag-Augmented VAR] ── Estimate unrestricted (k + d_max) levels VAR
       │
       ▼
[Phase 4: MWALD Testing on k Lags] ── Test linear restrictions strictly on first k lag matrices
       │
       ▼
[Phase 5: Residual Diagnostics Gate] ── Verify white-noise residuals at optimal k* (BG, ARCH, JB)
========================================================================================
RECOMMENDED / OPTIONAL REPORTING & INTERPRETIVE LAYERS
========================================================================================
- Specification Mapping Across Lag Grid: Report test statistics for k in {1, ..., p_max} (marker ^a)
- Dynamic Direction & Sign Tracking: Report structural sum of coefficients sum \hat{\beta}_i
- Four-Way Directional Decision Rule: Report X -> Y, Y -> X, X <-> Y, or X _|_ Y
- Theoretical Comparison Table: Contrast competing theoretical predictions against empirical signs
========================================================================================
```

### Core Methodological Invariants:
1. **Empirical Determination of $d_{\max}$:** Establish $d_{\max}$ via unit root testing; do not assume $d_{\max}=1$ as a constant.
2. **Ex-Ante Openness:** Estimate unrestricted $(k + d_{\max})$ levels systems without constraining foreign or institutional blocks to zero ex-ante. Exogeneity is identified strictly *ex-post* via MWALD joint tests.
3. **Linear Restriction Testing:** Test restrictions exclusively on the first $k$ structural lags.
4. **Diagnostic Integrity:** Verify white-noise residual properties (Breusch-Godfrey LM, ARCH LM, Jarque-Bera, White) at the selected lag order.

### Recommended / Optional Reporting Enhancements:
1. **Lag Robustness & Transparency (The Specification Map):**
   - Reporting statistics across a grid of candidate lag lengths $k \in \{1, \dots, p_{\max}\}$ (with $k \in \{1, 2, 3, 4\}$ serving as an illustrative default grid for quarterly/annual macro series) exposes lag sensitivity. Optimal lag order $k^*$ selected by SBIC and AIC is marked with note marker $^a$.
2. **Dynamic Direction & Sign ($\sum \hat{\beta}_i$):**
   - Reporting the sum of structural lagged coefficients $\sum_{i=1}^k \hat{\beta}_i$ alongside the Wald statistic captures cumulative dynamic sign stability where economically meaningful.
3. **Four-Way Directional Decision Rule:**
   - $X \to Y$: Unidirectional rejection of $H_0: X \not\to Y$ at declared $\alpha$ (e.g., $p < 0.05$), failure to reject $H_0: Y \not\to X$.
   - $Y \to X$: Unidirectional rejection of $H_0: Y \not\to X$ at declared $\alpha$, failure to reject $H_0: X \not\to Y$.
   - $\text{Bilateral } (X \leftrightarrow Y)$: Symmetrical rejection of both null hypotheses.
   - $\text{No Precedence } (X \perp Y)$: Failure to reject both null hypotheses.

---

## 3. Table Architecture Standard (Amiri-Ventelou Format)

### Table 1: Unit Root & Integration Order Battery
Must report ADF/KPSS statistics on levels ($z_t$) and first differences ($\Delta z_t$), identifying the maximal order of integration $d_{\max}$ empirically across candidate series.

### Table 2: Modular Specification Mapping Table (Optional Reporting Format)

The specification map may report all evaluated lag lengths, identifying optimal lag $k^*$ with note marker $^a$:

```latex
\begin{tabular}{llcccccc}
\toprule
\textbf{Dependent Variable} & \textbf{Regressor} & \textbf{Lag ($k$)} & \textbf{$F$-Stat} & \textbf{$\chi^2$ (MWALD)} & \textbf{$p$-value} & \textbf{$\sum \hat{\beta}_i$} & \textbf{Direction} \\
\midrule
Base Money ($g_{H,t}$) & Inflation ($\pi_t$) & 1$^a$ & 28.324$^{***}$ & 28.324 & $<0.0001$ & +0.298 & $\pi \to g_H$ \\
Base Money ($g_{H,t}$) & Inflation ($\pi_t$) & 2   & 14.892$^{***}$ & 29.784 & $<0.0001$ & +0.452 & $\pi \to g_H$ \\
Base Money ($g_{H,t}$) & Inflation ($\pi_t$) & 3   & 11.450$^{***}$ & 34.350 & $<0.0001$ & +0.581 & $\pi \to g_H$ \\
Base Money ($g_{H,t}$) & Inflation ($\pi_t$) & 4   & 15.004$^{***}$ & 60.015 & $<0.0001$ & +0.680 & $\pi \to g_H$ \\
\bottomrule
\end{tabular}
```
*Notes marker:* $^a$ Denotes the selected optimum lag length of the $(k+d_{\max})$ augmented VAR based on SBIC/AIC. *(Data in table above provided as an illustrative macro application).*

---

## 4. Theoretical Sign & Precedence Comparison Table Protocol (Optional Interpretive Layer)

To synthesize empirical causality results into substantive economic contributions, researchers may construct a **Theoretical Sign & Precedence Comparison Table**.

This protocol requires:
1. Formulating explicit theoretical hypotheses for competing models or paradigms (e.g., Theory A vs. Theory B vs. Null Hypothesis).
2. Explicitly stating the predicted directional precedence and expected dynamic sign ($\sum \hat{\beta}_i$) for each hypothesis *prior* to reporting empirical outcomes.
3. Contrasting the empirical Toda–Yamamoto MWALD results and cumulative signs against the theoretical predictions without dogmatic favoritism.

### Illustrative Application Example (Monetary & Credit Transmission Channels):

| Transmission Belt | Variable Pair | Theoretical Hypothesis A | Theoretical Hypothesis B | Toda–Yamamoto Empirical Result | Empirical Verdict |
|---|---|---|---|---|---|
| Nominal Core | $\pi_t \leftrightarrow g_{H,t}$ | $g_H \to \pi$ (+) Exogenous money growth causes inflation | $\pi \to g_H$ (+) Reverse accommodation of price shocks | Bilateral: $\pi \to g_H$ ($F=28.32^{***}$), $g_H \to \pi$ ($F=14.56^{***}$) | Bilateral Accommodation |
| Banking Credit | $M1_t \leftrightarrow H_t$ | $H \to M1$ (+) Multiplier causality from base to credit | $M1 \to H$ (+) Credit demand drives reserve creation | Bilateral with credit lead ($M1 \to H$, $F=21.45^{***}$) | Credit-Led Precedence |
| Money Velocity | $m_t \leftrightarrow \pi_t$ | $m \to \pi$ (+) Autonomous velocity shock | $\pi \to m$ ($-$) Defensive flight / demonetization | $\pi \to m$ ($F=5.13^{***}$, $\sum\hat{\beta}=-0.19$), $m \not\to \pi$ | Flight Effect Supported; Multiplier Refuted |
| Output Response | $g_{H,t} \leftrightarrow Q_t$ | $g_H \to Q$ (+) Stimulative or neutral transmission | $g_H \to Q$ ($-$) Defensive distress accommodation | $g_H \to Q$ ($F=7.15^{***}$, $\sum\hat{\beta}=-0.17$) | Negative Distress Correlation |
| Solvency Gate | $\text{Res}_t \leftrightarrow g_{H,t}$ | $g_H \to \text{Res}$ ($-$) Voluntary reserve depletion | $\text{Res} \to g_H$ ($-$) Reserve bottleneck forces emission | $\text{Res} \to g_H$ ($F=11.15^{***}$, $\sum\hat{\beta}=-0.31$) | Reserve Constraint Supported |

*(Note: The channels and predictions above represent an illustrative macroeconomic application. Applied researchers must define variable pairs and competing theoretical hypotheses specific to their research question).*
