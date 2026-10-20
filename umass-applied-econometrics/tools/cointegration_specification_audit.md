# Cointegration Specification Audit Protocol
## Methodological Reasoning Protocol for `/umass-applied-econometrics`

This document serves as a methodological reasoning protocol embedded within the `/umass-applied-econometrics` skill suite. It operationalizes Rule G (*Integration Order Governance*), Rule H (*Interpretation of Econometric Parameters*), and Rule I (*Small-Sample Bootstrap Protocol*).

---

## 1. Audit Sequence & Execution Flow

When auditing a cointegration or VECM specification, execute this 7-step diagnostic sequence:

```text
[Candidate Enumeration] 
       │
       ▼
[Gate 1: Conceptual Admissibility & Mode Check] ── (Confirmatory mapping vs. exploratory inspection)
       │
       ▼
[Gate 2: Integration Order Screen] ── (ADF + KPSS on levels & first differences)
       │
       ▼
[Gate 3: Collinearity & I(2) Risk Filter] ── (VIF, CN > 30 check, products/ratios)
       │
       ▼
[Gate 4: Interaction & Orthogonalization] ── (Conditional FWL residual centering if collinear)
       │
       ▼
[Descriptive & Deterministic Checks] ── (Observed quantities, optional inflections, drift vs. trend)
       │
       ▼
[Consolidated Verdict Table] ── (Promoted / Held / Blocked / Rejected)
```

---

## 2. Gate Protocols

### Gate 1: Conceptual Admissibility & Construct Operationalization
- **Objective:** Map each candidate variable to its theoretical foundation (e.g., choice-of-technique conditions, capacity constraints, structural balance-of-payments envelopes).
- **Check:** Differentiate between theoretical *decision mechanisms* (latent constructs) and *observable empirical proxies* (measured time series). *(Illustrative example: distinguishing firm-level optimal capital intensity $q^*$ from the observable proxy $K^{\text{ME}}/L$).*
- **Mode Demarcation:**
  - **Confirmatory / Structural Mode:** Variables entering a theory-linked structural or causal cointegration specification must possess an explicit conceptual role / construct mapping and clear integration order.
  - **Exploratory / Descriptive Mode:** Data patterns and empirical associations may be inspected before a fully developed theoretical mechanism is established (for pattern discovery, anomaly detection, and hypothesis generation). However, causal mechanism attribution or structural interpretation by post-hoc storytelling without independent support is strictly prohibited.
- **Rule:** Sound theoretical motivation is strictly necessary for confirmatory inclusion, but conceptual relevance alone does not establish stochastic admissibility.

### Gate 2: Integration Order Screen ($I(d)$ Status)
- **Objective:** Verify integration orders of all candidate regressors to ensure stochastic compatibility with the selected estimator.
- **Check:** Run complementary unit root tests: ADF (null of unit root) and KPSS (null of stationarity) on both levels and first differences.
- **Requirement:** In standard cointegration frameworks (Johansen VECM, Engle-Granger), all regressors in the cointegrating vector must be $I(1)$ in levels and $I(0)$ in first differences. For estimators accommodating mixed integration orders (such as ARDL bounds testing), verify that no variable exceeds $I(1)$ (absence of $I(2)$).

### Gate 3: Collinearity & $I(2)$ Risk Filter
- **Objective:** Eliminate unstable or explosive regressor combinations before estimation.
- **Check 1 (Collinearity Heuristics):** Screen pairwise correlations and design matrix conditioning. Pairwise correlations $r > 0.99$ or Condition Numbers (CN) $> 30$ serve as recommended screening thresholds blocking regressor combinations unless collinearity remediation is implemented. *(Illustrative example: testing whether separate equipment and structures capital series exhibit collinearity).*
- **Check 2 ($I(2)$ Risk):** Test products, ratios, and accumulated sums directly. Ratios of two $I(1)$ series or cumulated integration series frequently inherit $I(2)$ properties, rendering them non-admissible in standard $I(1)$ cointegration frameworks.

### Gate 4: Interaction Terms & Auxiliary Orthogonalization (Conditional Remediation)
- **Objective:** Ensure non-linear interaction terms $(\tilde{x}_t \cdot \tilde{d}_t)$ do not induce severe multicollinearity with constituent base terms.
- **Procedure:** When interaction terms introduce severe collinearity ($\text{VIF} > 10$), apply Frisch-Waugh-Lovell (FWL) auxiliary regression as a conditional remediation:
  $$\tilde{x}_t \cdot \tilde{d}_t = \alpha_0 + \alpha_1 \tilde{x}_t + \alpha_2 \tilde{d}_t + \hat{u}_t$$
  Extract the orthogonal residual $\hat{u}_t$ and substitute $\hat{u}_t$ for the raw interaction product.
- **Interpretive Caution:** Note that substituting orthogonalized residuals alters the economic interpretation of base linear coefficients; base terms then represent effects evaluated at the sample mean of the interacting variable rather than when the interacting variable equals zero (Balli & Sørensen 2013). Re-verify that $\text{VIF} < 10$.

---

## 3. Descriptive Diagnostics & Deterministic Combinatorics

1. **Direct Descriptive Grounding:** Inspect and report directly observed quantities materially relevant to the empirical question before or alongside estimation. Non-parametric plots (such as LOESS or binscatter) serve as illustrative diagnostic aids, not mandatory visualization forms.
2. **Inflection Diagnostics (Optional):** Where structural shifts are suspected, compute second-derivative zero-crossings ($\frac{d^2 \tau_t}{dt^2} = 0$) of smoothed series as diagnostic inflection markers, providing data-driven evidence of trend acceleration or deceleration without imposing arbitrary step dummies.
3. **VECM Deterministic Combinatorics:** Estimate Johansen VECMs across alternative deterministic term specifications:
   - **Drift Controls (`ecdet = "const"`):** Unrestricted constant outside the cointegration space or restricted constant inside; tests long-run proportional growth.
   - **Trend Controls (`ecdet = "trend"`):** Linear trend in cointegration space; tests for deterministic drift in the equilibrium relation.
4. **Small-Sample Residual Bootstrap:** For historical samples with short time dimensions ($N \le 30$ or $T \le 50$), execute residual bootstrap resampling (minimum 300 replications; 1,000 preferred) under the null of no cointegration.
   - **Decision Rule:** When a validated bootstrap procedure is part of the declared inferential design, bootstrap-adjusted inference may govern according to that procedure's justified decision rule. Otherwise, report asymptotic and bootstrap inference separately, report disagreement transparently, explain which inferential procedure is privileged and why, and avoid applying a rigid repository-wide override threshold (e.g., bootstrap $p > 0.10$ is an illustrative screening heuristic, not a universal law).

---

## 4. Standardized Verdict Ledger Format

Every cointegration audit report must conclude with a consolidated verdict table adhering to this structure:

| Candidate Variable | Theoretical Motivation | Integration & Collinearity Evidence | Research Disposition | Methodological Rationale |
|---|---|---|---|---|
| *Variable Name* | *Construct / Model Anchor* | *ADF/KPSS, $r$, CN, $I(2)$ test* | **Promoted / Held / Blocked / Rejected** | *Specific gate reference & diagnostic evidence* |

### Research Disposition Definitions:
- **Promoted:** Clears all integration, collinearity, and construct gates; advances to active estimator specification.
- **Held:** Admissible at initial screen but held due to secondary collinearity, diagnostic ambiguity, or alternative proxy preference.
- **Blocked:** Exhibits structural non-admissibility (e.g., confirmed $I(2)$ risk, integration order incompatible with chosen estimator).
- **Rejected:** Fatal near-perfect collinearity ($r > 0.999$, $\text{CN} \gg 30$) or severe diagnostic instability that cannot be remediated.

*(Illustrative Application Example: In a capital accumulation study, an equipment capital series $K^{\text{ME}}$ is Promoted upon confirming $I(1)$ status; an unrestricted structures series $K^{\text{NRC}}$ is Held due to high collinearity with $K^{\text{ME}}$; a compound capital ratio $K^{\text{ME}}/L$ is Blocked due to confirmed $I(2)$ unit root properties; and an explosive polynomial term is Rejected).*
