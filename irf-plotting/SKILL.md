---
name: irf-plotting
description: >-
  Publication-grade standard and code pipelines for extracting, wrangling, plotting, and documenting
  Impulse Response Functions (IRFs) and Generalized Impulse Response Functions (GIRFs) in linear VAR/SVAR
  and non-linear TVAR models. Calibrated to Cambridge Journal of Economics (CJE), Journal of Post Keynesian
  Economics (JPKE), and Review of Political Economy (ROPE) standards. Triggers on: plot IRF, IRF visualization,
  GIRF, impulse response plot, SVAR IRF, TVAR GIRF, publication plots, IRF formatting.
---

# Publication-Grade Impulse Response Function (IRF & GIRF) Plotting & Reporting Engine

## 1. Description & Scope

This skill establishes a publication-grade standard for extracting, transforming, plotting, and documenting **Impulse Response Functions (IRFs)** and **Generalized Impulse Response Functions (GIRFs)** in empirical macroeconomics. It bridges the econometrics of linear systems (via `vars::irf`) and non-linear regime-switching threshold models (via `tsDyn::GIRF`).

The standard formalizes the visual aesthetics, scaling discipline, and reporting practices found in applied macroeconomic journals (*Cambridge Journal of Economics*, *Journal of Applied Econometrics*, *Review of Political Economy*, *Journal of Post Keynesian Economics*), referencing the benchmarks of **Bachurewicz (2019)** and **Fry-McKibbin & Zheng (2016)**.

---

## 2. Invariant Visual Grammar (Mandatory Across All Figures)

Every generated IRF or GIRF plot must strictly adhere to six universal invariants:

### 2.1 No Redundant Internal Plot Titles
- **Never** inject `plot_annotation(title = ...)` or `labs(title = ...)` inside the figure canvas when the figure is wrapped in a LaTeX `\caption{...}`.
- Top-level narratives belong strictly in the LaTeX caption. The plot canvas should rely solely on clean facet labels or minimalist column headers (e.g., *Hedge*, *Speculative*, *Forced Ponzi*).

### 2.2 Clean Corner Panel Tags
- Subplots or multi-row panels must feature uppercase tags `(A)`, `(B)`, `(C)` in the top-left corner (via `geom_text(x = -Inf, y = Inf, ...)` or patchwork `tag_levels = 'A'`) for direct cross-referencing in manuscript prose.

### 2.3 Strict Grayscale Compatibility (Line Styles + Colors)
- **Never rely on color alone.** Trajectories must pair distinct color palettes with unique line styles to ensure dynamics remain identifiable in monochrome print:
  * **Baseline / Expansion / Hedge / Regime 1:** Solid Navy (`#1D3557` or `#2B5C8F`), `linetype = "solid"`, `linewidth = 0.85`
  * **Pre-Lockout / Transition:** Dot-Dash Teal (`#2A9D8F`), `linetype = "dotdash"`, `linewidth = 0.80`
  * **Crisis / High Stress:** Dashed Terracotta (`#E76F51`), `linetype = "dashed"`, `linewidth = 0.80`
  * **Deregulation / Forced Ponzi / Regime 3:** Long-Dash Crimson (`#9E2A2B` or `#B00020`), `linetype = "longdash"`, `linewidth = 0.80`

### 2.4 Standardized Neutral Zero Line
- A single horizontal benchmark at $y = 0$: `geom_hline(yintercept = 0, color = "#4A4E69", linewidth = 0.40, linetype = "solid")`.

### 2.5 Borderless Semi-Transparent Ribbons
- Shaded confidence bands must use `alpha = 0.20` to `0.25` and `linetype = "blank"` to avoid gridline occlusion and edge clutter.

### 2.6 Unclipped Scales & Explicit Physical Units
- **Horizontal Axis:** Forecast horizon $h \in [0, H]$ in discrete integer steps, labeled in units (*Months* or *Quarters*).
- **Vertical Axis:** Explicitly labeled (*Percentage points*, *Log deviations $\times 100$*, *Basis points*). If accumulated responses are plotted, state *Accumulated Response*. Ensure $y$-limits fully accommodate bootstrap intervals without clipping.

---

## 3. Theoretical & Methodological Foundations

### 3.1 Linear IRFs vs. Non-Linear GIRFs

| Dimension | Linear VAR IRFs (`vars`) | Non-Linear GIRFs (`tsDyn`) |
| :--- | :--- | :--- |
| **Theoretical Model** | Wold Moving Average representation | Generalized IRF (Koop, Pesaran, & Potter, 1996) |
| **Mathematical Definition** | $\Psi_s = \Phi_s P$ | $\mathbb{E}[Y_{t+h} \mid \delta, \Omega_{t-1}] - \mathbb{E}[Y_{t+h} \mid \Omega_{t-1}]$ |
| **Invariance Properties** | Time-invariant, sign-symmetric, scale-linear | History-dependent, sign-asymmetric, non-linear |
| **Reference Baseline** | Zero disturbance vector | Conditional expectation averaged over simulated random innovations ($R$) |
| **Visual Encoding** | Single point estimate + shaded CI ribbon | Multi-curve overlay across regimes or shock magnitudes |
| **Scale Testing Standard** | Not applicable ($2\sigma = 2 \times 1\sigma$) | Normalization mandatory: plot $\text{GIRF}(2\sigma)/2$ |
| **Projection Horizon** | 8–20 quarters / months | 30–60 quarters / months |

### 3.2 Invariant Methodological Requirements

1. **Orthogonalization & Identification Disclosure:**
   - Recursive systems must state the contemporaneous Cholesky ordering vector in figure notes.
   - Non-recursive SVAR ($A Y_t = B \varepsilon_t$) or sign-restricted models must reference the structural restriction matrix.
2. **Dynamic GIRF vs. Static Regime IRFs:**
   - Computing linear IRFs within static regimes (`irf.TVAR(..., regime = "L")`) assumes the system never crosses the threshold $\hat{\gamma}$ across the horizon.
   - Static regime IRFs are strictly preliminary diagnostics; research manuscripts must report dynamic GIRFs that integrate out future shocks via Monte Carlo simulation ($R \ge 500$).
3. **Shock Normalization for Scale Asymmetry:**
   - When evaluating shock-size asymmetries ($1\sigma$ vs. $2\sigma$), the response to $2\sigma$ must be scaled down by a factor of 2 ($\text{GIRF}/2$) to allow visual evaluation of non-proportionality.
4. **Mandatory Companion Parameter Reporting:**
   - IRF figures must be accompanied by full regression tables (lag coefficients, standard errors, $t$-statistics, $R^2$, equation $F$-tests, and residual covariance determinants $\vert{}\hat{\Sigma}\vert{}$).

---

## 4. Tidy R Extraction & Wrangling Pipelines

### 4.1 Extracting from `vars::irf` (Linear VAR / SVAR)

```r
#' Convert vars::irf object to a tidy tibble
#' @param irf_obj Object of class 'varirf'
#' @return A tidy tibble with columns: horizon, impulse, response, irf, lower, upper
tidy_varirf <- function(irf_obj) {
  library(dplyr)
  library(tidyr)
  library(purrr)

  impulses <- irf_obj$impulse
  responses <- irf_obj$response
  n_ahead <- nrow(irf_obj$irf[[1]]) - 1

  map_dfr(impulses, function(imp) {
    map_dfr(responses, function(resp) {
      tibble(
        horizon  = 0:n_ahead,
        impulse  = imp,
        response = resp,
        irf      = as.numeric(irf_obj$irf[[imp]][, resp]),
        lower    = if (!is.null(irf_obj$Lower)) as.numeric(irf_obj$Lower[[imp]][, resp]) else NA_real_,
        upper    = if (!is.null(irf_obj$Upper)) as.numeric(irf_obj$Upper[[imp]][, resp]) else NA_real_
      )
    })
  })
}
```

### 4.2 Extracting and Conditioning `tsDyn::GIRF` (Threshold VAR)

```r
#' Aggregate and condition tsDyn::GIRF output by historical regime
#' @param girf_df Data frame returned by tsDyn::GIRF()
#' @param tvar_model Fitted TVAR object from tsDyn
#' @param threshold_vals Numeric vector of threshold values (e.g., c(gamma1, gamma2))
#' @param regime_names Character vector of regime labels (e.g., c("Hedge", "Speculative", "Forced Ponzi"))
#' @return A tidy tibble of regime-averaged GIRF paths
tidy_girf_by_regime <- function(girf_df, tvar_model, threshold_vals, regime_names) {
  library(dplyr)

  th_var_series <- tvar_model$model.specific$thVar
  regime_factor <- cut(th_var_series, breaks = c(-Inf, threshold_vals, Inf), labels = regime_names)
  
  girf_df %>%
    mutate(regime = regime_factor[hist]) %>%
    filter(!is.na(regime)) %>%
    group_by(regime, var, n.ahead) %>%
    summarise(
      girf_mean  = mean(girf, na.rm = TRUE),
      girf_lower = quantile(girf, probs = 0.05, na.rm = TRUE),
      girf_upper = quantile(girf, probs = 0.95, na.rm = TRUE),
      .groups = "drop"
    )
}
```

---

## 5. Complete Production-Ready Plotting Functions

### 5.1 Template 1: Linear VAR Multi-Panel IRF (Bachurewicz 2019 Style)

```r
#' Plot Publication-Grade Linear IRFs (vars)
#' @param irf_tidy Tidy data frame from tidy_varirf()
#' @param target_impulse Character vector of the impulse shock to plot
#' @param var_labels Named vector for clean variable facet labels
#' @param h_label Label for horizontal axis (e.g., "Quarters", "Months")
#' @param ci_level Text label for confidence interval (e.g., "90%")
plot_linear_irf_grid <- function(irf_tidy, 
                                 target_impulse, 
                                 var_labels = NULL,
                                 h_label = "Months",
                                 ci_level = "90%") {
  library(ggplot2)
  library(dplyr)

  df_sub <- irf_tidy %>% filter(impulse == target_impulse)
  
  if (!is.null(var_labels)) {
    df_sub <- df_sub %>% mutate(response = recode(response, !!!var_labels))
  }

  ggplot(df_sub, aes(x = horizon, y = irf)) +
    geom_hline(yintercept = 0, color = "#4A4E69", linewidth = 0.40) +
    geom_ribbon(aes(ymin = lower, ymax = upper), 
                fill = "#2B5C8F", alpha = 0.22, linetype = "blank") +
    geom_line(color = "#1D3557", linewidth = 0.85, linetype = "solid") +
    facet_wrap(~ response, scales = "free_y", ncol = 2) +
    scale_x_continuous(expand = c(0.01, 0.01), breaks = scales::pretty_breaks()) +
    scale_y_continuous(breaks = scales::pretty_breaks(n = 5)) +
    labs(
      x = paste0("Forecast Horizon (", h_label, ")"),
      y = "Percentage Deviations / Basis Points"
    ) +
    theme_minimal(base_size = 11, base_family = "sans") +
    theme(
      strip.text = element_text(face = "bold", size = 11, hjust = 0.5, color = "grey15"),
      strip.background = element_rect(fill = "grey96", color = NA),
      panel.grid.major = element_line(color = "grey90", linewidth = 0.35),
      panel.grid.minor = element_blank(),
      panel.spacing = unit(1.1, "lines"),
      axis.title = element_text(face = "bold", size = 10, color = "grey20"),
      axis.text = element_text(size = 9, color = "grey25")
    )
}
```

### 5.2 Template 2: Threshold VAR Comparative Regime GIRF (Fry-McKibbin & Zheng Style)

```r
#' Plot Publication-Grade Comparative Regime GIRFs (tsDyn / TVAR)
#' @param girf_tidy Tidy data frame containing columns: regime, var, n.ahead, girf_mean
#' @param var_labels Named vector for facet labels
#' @param h_label Horizon unit (default: "Months")
plot_tvar_regime_girf <- function(girf_tidy, 
                                  var_labels = NULL,
                                  h_label = "Months") {
  library(ggplot2)
  library(dplyr)

  if (!is.null(var_labels)) {
    girf_tidy <- girf_tidy %>% mutate(var = recode(var, !!!var_labels))
  }

  ggplot(girf_tidy, aes(x = n.ahead, y = girf_mean, color = regime, linetype = regime)) +
    geom_hline(yintercept = 0, color = "#4A4E69", linewidth = 0.40) +
    geom_line(linewidth = 0.85) +
    facet_wrap(~ var, scales = "free_y", ncol = 3) +
    scale_color_manual(
      name = "Regime:",
      values = c("Hedge" = "#1D3557", "Speculative" = "#2A9D8F", "Forced Ponzi" = "#B00020")
    ) +
    scale_linetype_manual(
      name = "Regime:",
      values = c("Hedge" = "solid", "Speculative" = "dotdash", "Forced Ponzi" = "dashed")
    ) +
    scale_x_continuous(expand = c(0.01, 0.01), breaks = scales::pretty_breaks()) +
    scale_y_continuous(breaks = scales::pretty_breaks(n = 5)) +
    labs(
      x = paste0("Horizon (", h_label, ")"),
      y = "Percentage Deviations / Basis Points"
    ) +
    theme_minimal(base_size = 11, base_family = "sans") +
    theme(
      legend.position = "top",
      legend.justification = "left",
      legend.title = element_text(face = "bold", size = 10, color = "grey20"),
      legend.text = element_text(size = 9.5),
      strip.text = element_text(face = "bold", size = 10.5, color = "grey15"),
      strip.background = element_rect(fill = "grey95", color = NA),
      panel.grid.major = element_line(color = "grey92", linewidth = 0.35),
      panel.grid.minor = element_blank(),
      panel.spacing = unit(1.1, "lines"),
      axis.title = element_text(face = "bold", size = 10, color = "grey20"),
      axis.text = element_text(size = 9, color = "grey25")
    )
}
```

---

## 6. Endogenous Regime Switching & Non-Linear Identification

In the GIRF algorithm (Koop, Pesaran, & Potter, 1996), regime switching is dynamic and evaluated at every step:

1. **Baseline Path (Unperturbed):** At $t = 0$, the system occupies Regime 1. The algorithm simulates $R$ stochastic shock paths ($V_{t+1}, \dots, V_{t+n}$). At each horizon step $t + k$, the threshold variable $S_{t+k-1}$ is evaluated. If $S_{t+k-1} < \gamma$, Regime 1 coefficients generate $Y_{t+k}$.
2. **Perturbed Path (Shocked):** At $t = 0$, shock $\delta$ is applied.
3. **Endogenous Crossing:** If shock $\delta$ is large or future shocks accumulate, $S_{t+k-1}$ can cross $\gamma$. When $S_{t+k-1} > \gamma$, the system dynamically switches to Regime 2 coefficients for that simulation draw.
4. **Resulting GIRF:** The GIRF is the difference between the perturbed and baseline expectations:

$$\text{GIRF}_h(\delta, \Omega_{t-1}) = \mathbb{E}[Y_{t+h} \mid \delta, \Omega_{t-1}] - \mathbb{E}[Y_{t+h} \mid \Omega_{t-1}]$$

Crossing into Regime 2 alters subsequent multipliers and persistence, producing distinct kinks, inflection points, or sustained persistence unavailable in linear models.

### 6.1 Strategy 1: The Threshold Crossing Plot (The "Smoking Gun")

Plot the GIRF of the **threshold variable itself** ($S_{t+h}$) and overlay the estimated threshold $\hat{\gamma}$. If the trajectory or its confidence band crosses $\hat{\gamma}$, it demonstrates that the shock drives the system into the alternate regime.

```r
#' Plot Threshold Variable GIRF with Estimated Threshold Line
#' @param girf_tidy Tidy data frame for the threshold variable's GIRF
#' @param threshold_value Numeric value of estimated threshold (gamma)
#' @param h_label Horizon unit (default: "Quarters")
plot_threshold_crossing <- function(girf_tidy, threshold_value, h_label = "Quarters") {
  library(ggplot2)
  
  ggplot(girf_tidy, aes(x = horizon, y = girf_mean, color = regime, linetype = regime)) +
    geom_hline(yintercept = 0, color = "#4A4E69", linewidth = 0.40) +
    geom_hline(yintercept = threshold_value, color = "#2A9D8F", linewidth = 0.80, 
               linetype = "dotdash", alpha = 0.8) +
    annotate("text", x = Inf, y = threshold_value, 
             label = paste0("Threshold \u03B3 = ", round(threshold_value, 3)), 
             hjust = 1.1, vjust = -0.5, size = 3.5, color = "#2A9D8F", fontface = "bold") +
    geom_ribbon(aes(ymin = girf_lower, ymax = girf_upper, fill = regime, color = NULL), 
                alpha = 0.20, linetype = "blank") +
    geom_line(linewidth = 0.85) +
    scale_color_manual(values = c("Low Stress" = "#1D3557", "High Stress" = "#E76F51")) +
    scale_fill_manual(values = c("Low Stress" = "#1D3557", "High Stress" = "#E76F51")) +
    scale_linetype_manual(values = c("Low Stress" = "solid", "High Stress" = "dashed")) +
    labs(
      x = paste0("Forecast Horizon (", h_label, ")"),
      y = "Threshold Variable Index"
    ) +
    theme_minimal(base_size = 11) +
    theme(legend.position = "top", panel.grid.minor = element_blank())
}
```

### 6.2 Strategy 2: Normalized Shock Asymmetry ($1\sigma$ vs. $2\sigma/2$)

To isolate whether shock *magnitude* induces regime transition, plot the normalized response paths. Divide the $2\sigma$ response by 2. In a linear model, the normalized trajectories coincide ($1\sigma = 2\sigma/2$). Any divergence in trajectory profile confirms non-linear endogenous switching.

```r
#' Plot Normalized Shock Asymmetry to Prove Regime Switching
#' @param df_1sd Tidy data frame for 1 SD shock
#' @param df_2sd Tidy data frame for 2 SD shock
#' @param h_label Horizon unit (default: "Quarters")
plot_shock_asymmetry <- function(df_1sd, df_2sd, h_label = "Quarters") {
  library(ggplot2)
  library(dplyr)
  
  df_norm <- bind_rows(
    df_1sd %>% mutate(shock_scale = "1 Standard Deviation"),
    df_2sd %>% mutate(
      girf_mean  = girf_mean / 2,
      girf_lower = girf_lower / 2,
      girf_upper = girf_upper / 2,
      shock_scale = "2 s.d. (Normalized / 2)"
    )
  )
  
  ggplot(df_norm, aes(x = horizon, y = girf_mean, color = shock_scale, linetype = shock_scale)) +
    geom_hline(yintercept = 0, color = "#4A4E69", linewidth = 0.40) +
    geom_ribbon(aes(ymin = girf_lower, ymax = girf_upper, fill = shock_scale, color = NULL), 
                alpha = 0.15, linetype = "blank") +
    geom_line(linewidth = 0.85) +
    scale_color_manual(values = c("1 Standard Deviation" = "#1D3557", "2 s.d. (Normalized / 2)" = "#9E2A2B")) +
    scale_fill_manual(values = c("1 Standard Deviation" = "#1D3557", "2 s.d. (Normalized / 2)" = "#9E2A2B")) +
    scale_linetype_manual(values = c("1 Standard Deviation" = "solid", "2 s.d. (Normalized / 2)" = "longdash")) +
    labs(
      x = paste0("Horizon (", h_label, ")"),
      y = "Normalized Response (Percentage Points)"
    ) +
    theme_minimal(base_size = 11) +
    theme(legend.position = "top", panel.grid.minor = element_blank())
}
```

---

## 7. Self-Contained LaTeX Captions & Note Standards

Every figure must remain fully self-contained: identification, shock calibration, coverage intervals, and data sources must be discernible directly from the caption and notes.

### 7.1 LaTeX Wrapper Template

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{figures/fig_name.pdf}
    \caption{Descriptive Title Stating Focal Mechanism and Regimes}
    \label{fig:label_name}
    \begin{minipage}{\textwidth}
        \vspace{0.25cm}
        \footnotesize
        \textbf{Note:} (A) Response of [Variable 1] to a [Size and Unit, e.g., $+1\sigma$ orthogonalized innovation in $X$]; (B) Response of [Variable 2] to... Solid navy lines denote [Regime 1 / Baseline]; dashed terracotta lines denote [Regime 2]. Shaded envelopes depict [Coverage, e.g., 90\%] bootstrapped confidence intervals derived from [$B = 500$] iterations. Identification is achieved via [Cholesky decomposition with contemporaneous causal ordering $[X_1, X_2, X_3]'$ / structural SVAR AB restrictions]. Horizon $h = [H]$ months.
        
        \textbf{Source:} Author's estimations based on data from [Institutional Sources, Sample Range].
    \end{minipage}
\end{figure}
```

### 7.2 Explicit Caption Note for Endogenous Switching Figures

```latex
\textbf{Note:} \textbf{Panel A} displays the Generalized Impulse Response of the threshold variable (Financial Stress Index) to a $+1\sigma$ shock. The horizontal dot-dashed teal line indicates the estimated threshold ($\hat{\gamma} = 1.086$). Crossing of this threshold along the trajectory visually confirms an endogenous regime switch. \textbf{Panel B} tests for shock-induced non-linearity: the response to a $+2\sigma$ shock is normalized (divided by 2) and overlaid against the $+1\sigma$ baseline. Divergence in trajectory profile confirms that the larger shock pushes the system across the threshold, activating regime-specific propagation dynamics (Koop, Pesaran, & Potter, 1996).
```

### 7.3 Mandatory Checklist for Figure Notes

| Element | Requirement | Example Syntax |
| --- | --- | --- |
| **Impulse Shock** | Exact size, sign, and unit of the shock | $+1\sigma$ orthogonalized innovation in inflation ($\Delta \pi_t$) |
| **Model Type** | Estimator, lag length, and regime structure | 3-regime TVAR(1) conditioned on lagged Central Bank Solvency ($\text{SolvR}_{t-1}$) |
| **Identification Scheme** | Ordering vector or structural restriction matrix | Recursive Cholesky ordering: $[g_{P,\text{gold},t}, \Delta \ln \Theta_t, \Delta \pi_t, \Delta g_{H,t}]'$ |
| **Horizon & Frequency** | Total projection steps and time unit | Horizon $h = 24$ months |
| **Simulation Method** | Monte Carlo or bootstrap replication count ($R, B$) | $R = 500$ Monte Carlo histories; 90% percentile bands |
| **Response Metric** | Level, growth rate, or accumulated log deviations | Responses are accumulated percentage deviations |
| **Data Source** | Institutional data provider and sample interval | Central Bank of Chile and ODEPLAN (1958M01–1977M12) |

---

## 8. Reviewer & Auditor Rubric: IRF Graphics

| Defect | Methodological Violation | Reviewer Action |
| --- | --- | --- |
| **Redundant Title Banner** | In-plot title duplicating LaTeX caption or cluttering canvas. | **Minor Revision** |
| **Color-Only Encoding** | Lines differentiated solely by color, failing black-and-white printing. | **Minor Revision** |
| **Missing Zero Baseline** | Omitting horizontal zero reference line, obscuring statistical significance. | **Minor Revision** |
| **Missing Threshold Plot** | Omitting the threshold variable IRF with the estimated $\hat{\gamma}$ line overlaid. | **Major Revision** |
| **Unscaled Comparison** | Comparing $1\sigma$ and $2\sigma$ non-linear shocks without dividing $2\sigma$ by 2. | **Major Revision** |
| **Static Coefficients in TVAR** | Using `irf.TVAR(..., regime="L")` which fixes coefficients and artificially prevents crossing. | **Fatal Flaw (Reject)** |
| **Ambiguous Intervals** | Shaded ribbons displayed without defining coverage level or bootstrap iteration count. | **Minor Revision** |
| **Unspecified Ordering** | Reporting Cholesky IRFs without declaring the contemporaneous causal ordering vector. | **Major Revision** |
| **Floating Displays** | Figure lacking self-contained notes defining units, horizons, and data sources. | **Minor Revision** |

---

## 9. Paper Prose Interpretation Template

When reporting empirical results based on these visualizations, adapt this paragraph structure:

> *"Figure X (Panel A) illustrates the endogenous switching mechanism. Following a $+1\sigma$ financial stress shock, the index rises sharply, crossing the estimated threshold $\hat{\gamma}$ within two quarters. This crossing transitions the system from the low-stress to the high-stress regime, shifting shock propagation to the high-stress regime coefficients and generating a more persistent contraction in real activity. This mechanism is corroborated by Panel B, where the normalized $2\sigma$ shock exhibits a distinct trajectory profile relative to the $1\sigma$ shock, confirming that shock magnitude activates non-linear regime switching (Koop, Pesaran, & Potter, 1996)."*
