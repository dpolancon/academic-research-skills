# Toda–Yamamoto Macroeconomic Causality & Specification Mapping Protocol (Amiri & Ventelou 2012 Benchmark)

This document serves as an operational tool embedded within the `/umass-applied-econometrics` skill suite. It operationalizes Rule J (*Toda–Yamamoto Causality & Specification Mapping*), Rule A (*Forensic Transparency*), and Rule D (*Specification-Space Mapping*).

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
- $d_{\max}$ is the maximal order of integration observed across the candidate variable vector.
- Linear hypothesis restrictions ($H_0: \mathbf{R} \operatorname{vec}(\mathbf{\Phi}_1, \dots, \mathbf{\Phi}_k) = \mathbf{0}$) are tested **strictly on the first $k$ coefficient matrices**, leaving the extra $d_{\max}$ lag matrices unconstrained.

### Asymptotic Invariance Theorem
Under $(k + d_{\max})$ augmentation, the Modified Wald (MWALD) test statistic converges asymptotically to a standard $\chi^2(m)$ distribution with $m = \operatorname{rank}(\mathbf{R})$ degrees of freedom, regardless of cointegration status.

---

## 2. The Amiri & Ventelou (2012) Benchmark Standards

To prevent ad-hoc specification selection and ensure complete forensic transparency, applied econometric papers must adhere to the publication standard established by **Amiri & Ventelou (2012, *Economics Letters* 116: 541–544)**:

```
[Phase 1: Integration Order Screen] ── Confirm d_max across all series via ADF/KPSS/DF-GLS
       │
       ▼
[Phase 2: Lag Selection Grid] ── Evaluate VAR(k) information criteria (SBIC, AIC, HQ, FPE) for k = 1..p_max
       │
       ▼
[Phase 3: Systematic Lag Battery] ── Estimate Toda-Yamamoto MWALD across full lag grid k in {1, 2, 3, 4}
       │
       ▼
[Phase 4: Specification Map Table] ── Report p-values, sum of coefficients, mark optimal k* with ^a
       │
       ▼
[Phase 5: Lakatosian Sign Tournament] ── Contrast competing theoretical predictions against empirical signs
       │
       ▼
[Phase 6: Residual Diagnostics Gate] ── Verify white-noise residuals at optimal k* (BG LM, ARCH, JB, White)
```

### Key Principles of the Benchmark:

1. **Ex-Ante Openness**:
   - Zero exogeneity restrictions are imposed *ex-ante*. All variables enter all equations unrestricted. Block-exogeneity is an *ex-post* empirical outcome.
2. **Lag Robustness & Transparency (The Specification Map)**:
   - Rather than reporting only the preferred model, report test statistics and $p$-values across a grid of candidate lag lengths $k \in \{1, 2, 3, 4\}$.
   - Identify the optimal lag order $k^*$ using Schwarz Bayesian Information Criterion (SBIC/SC) and Akaike (AIC). Mark $k^*$ explicitly with superscript $^a$ in all tables.
3. **Dynamic Direction & Sign ($\sum \hat{\beta}_i$)**:
   - Always report the sum of structural lagged coefficients $\sum_{i=1}^k \hat{\beta}_i$ alongside the Wald statistic to capture the economic sign and cumulative dynamic impact.
4. **Four-Way Directional Decision Rule**:
   - $X \to Y$: Unidirectional rejection of $H_0: X \not\to Y$ at $p < 0.05$, failure to reject $H_0: Y \not\to X$.
   - $Y \to X$: Unidirectional rejection of $H_0: Y \not\to X$ at $p < 0.05$, failure to reject $H_0: X \not\to Y$.
   - $\text{Bilateral } (X \leftrightarrow Y)$: Symmetrical rejection of both null hypotheses at $p < 0.05$.
   - $\text{No } (X \perp Y)$: Failure to reject both null hypotheses ($p \ge 0.10$).

---

## 3. Table Architecture Standard (Amiri-Ventelou Format)

### Table 1: Unit Root & Integration Order Battery
Must report ADF/KPSS statistics on levels ($z_t$) and first differences ($\Delta z_t$), identifying maximal integration order $d_{\max} = 1$.

### Table 2: Modular Specification Mapping Table
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
*Notes marker:* $^a$ Denotes the selected optimum lag length of the $(k+d_{\max})$ augmented VAR based on SBIC.

---

## 4. The Lakatosian Five-Sign Tournament Table (Punchline Protocol)

To synthesize empirical results into a direct political-economy contribution, construct a consolidated **Sign-Discrimination Tournament Table**:

| Transmission Belt | Pair | Orthodox Prediction (Monetarism/FRT) | Heterodox Prediction (PK/Structuralism) | Toda–Yamamoto Empirical Result | Theoretical Verdict |
|---|---|---|---|---|---|
| Nominal Core | $\pi_t \leftrightarrow g_{H,t}$ | $g_H \to \pi$ (+) unidirectional | $\pi \to g_H$ (+) reverse accommodation | Bilateral: $\pi \to g_H$ ($F=28.32^{***}$), $g_H \to \pi$ ($F=14.56^{***}$) | Heterodox Accommodating |
| Banking Credit | $M1_t \leftrightarrow H_t$ | $H \to M1$ (+) vertical multiplier | $M1 \to H$ (+) credit-led horizontalism | Bilateral with credit lead ($M1 \to H$, $F=21.45^{***}$) | Post-Keynesian Horizontalist |
| Multiplier | $m_t \leftrightarrow \pi_t$ | $m \to \pi$ (+) autonomous shock | $\pi \to m$ ($-$) disintermediation / flight | $\pi \to m$ ($F=5.13^{***}$, $\sum\hat{\beta}=-0.19$), $m \not\to \pi$ | Monetarism Refuted |
| Real Sector | $g_{H,t} \leftrightarrow Q_{\text{manuf}}$ | $g_H \to Q$ (+) stimulus / neutral | $g_H \to Q$ ($-$) defensive distress emission | $g_H \to Q_{\text{manuf}}$ ($F=7.15^{***}$, $\sum\hat{\beta}=-0.17$) | Defensive Accommodation |
| Reserve Gate | $\text{SolvR}_t^H \leftrightarrow g_{H,t}$ | $g_H \to \text{SolvR}$ ($-$) voluntary depletion | $\text{SolvR} \to g_H$ ($-$) reserve-gate constraint | $\text{SolvR}^H \to g_H$ ($F=11.15^{***}$, $\sum\hat{\beta}=-0.31$) | Balance-Sheet Solvency Gate |
