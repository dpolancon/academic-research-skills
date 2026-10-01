# Cointegration Specification Audit Protocol (Tool for `/umass-applied-econometrics`)

This document serves as an operational tool embedded within the `/umass-applied-econometrics` skill suite. It operationalizes Rule G (*Integration Order Governance*), Rule H (*Political Economy Interpretation*), and Rule I (*Small-Sample Bootstrap Protocol*).

---

## 1. Audit Sequence & Execution Flow

When auditing a cointegration or VECM specification, execute this 7-step sequence:

```
[Candidate Enumeration] 
       │
       ▼
[Gate 1: Theoretical Admissibility] ── (Identify theoretical mechanism & latent variables)
       │
       ▼
[Gate 2: Integration Order Screen] ── (ADF + KPSS on levels & first differences)
       │
       ▼
[Gate 3: Collinearity & I(2) Risk Filter] ── (VIF, CN > 30 check, products/ratios)
       │
       ▼
[Gate 4: Interaction & Orthogonalization] ── (FWL residual centering if I(2) risk present)
       │
       ▼
[LOESS Pre-Filter & Window Combinatorics] ── (2nd derivative zero-crossings; drift vs. trend)
       │
       ▼
[Consolidated Verdict Table] ── (Promoted / Held / Blocked / Rejected)
```

---

## 2. Gate Protocols

### Gate 1: Theoretical Admissibility
- **Objective:** Map each candidate variable to its theoretical foundation (e.g., FOC choice of technique, capacity identity, structural envelope, foreign-exchange bottleneck).
- **Check:** Differentiate between theoretical *decision mechanisms* (e.g., firm-level optimal $q^*$) and *observable macroeconomic proxies* (e.g., $K^{\text{ME}}/L$).
- **Rule:** Sound theoretical motivation is necessary for entry, but does not grant automatic promotion.

### Gate 2: Integration Order Screen ($I(d)$ Status)
- **Objective:** Verify integration orders of all candidate regressors.
- **Check:** Run both ADF (null: unit root) and KPSS (null: stationarity) on levels and first differences.
- **Requirement:** Regressors in standard cointegration must be $I(1)$ in levels and $I(0)$ in first differences.

### Gate 3: Collinearity & $I(2)$ Risk Filter
- **Objective:** Eliminate unstable or explosive regressor combinations.
- **Check 1 (Collinearity):** Pairwise correlation $r > 0.99$ or design matrix Condition Number (CN) $> 30$ blocks regressor pairs (e.g., unrestricted $k^{\text{ME}}$ and $k^{\text{NRC}}$, accumulated path $Q_t^\omega$ alongside $k^{\text{cap}}$).
- **Check 2 ($I(2)$ Risk):** Test products, ratios, and accumulated sums directly. Ratios of two $I(1)$ series (such as $q_t = K^{\text{ME}}/L$) or cumulated terms often inherit $I(2)$ risk, rendering them non-admissible in standard $I(1)$ cointegration frameworks.

### Gate 4: Interaction Term & Auxiliary Orthogonalization
- **Objective:** Ensure interaction terms $(\tilde{x}_t \cdot \tilde{d}_t)$ do not induce spurious $I(2)$ behavior or collinearity with base terms.
- **Check:** Apply Frisch-Waugh-Lovell (FWL) auxiliary regression:
  $$\tilde{x}_t \cdot \tilde{d}_t = \alpha_0 + \alpha_1 \tilde{x}_t + \alpha_2 \tilde{d}_t + \hat{u}_t$$
  Extract residual $\hat{u}_t$ and substitute $\hat{u}_t$ for the raw interaction product (e.g., Specification $D_7$, $D_9$). Re-verify VIF $< 10$.

---

## 3. LOESS Pre-Filter & Deterministic Combinatorics

1. **Non-parametric LOESS Inspection:** Fit LOESS curves to key structural ratios ($\tau_t = \ln K^{\text{ME}} - \ln K^{\text{NRC}}$) prior to parametric estimation.
2. **2nd Derivative Inflections:** Calculate $\frac{d^2 \tau_t}{dt^2} = 0$ zero-crossings. Use these dates as diagnostic inflection markers (reading technical acceleration/deceleration) rather than parametric step-dummies.
3. **VECM Deterministic Combinatories:** Estimate Johansen VECMs across both:
   - **Drift Controls (`ecdet = "const"`):** Constant in cointegration space; suitable for long-run proportional growth.
   - **Trend Controls (`ecdet = "trend"`):** Linear trend in cointegration space; tests for deterministic drift in equilibrium ratio.
4. **Small-Sample Residual Bootstrap:** For historical sub-samples with $N \le 30$, execute residual bootstrap resampling (minimum 300 replications) under the null of no cointegration. Overrule asymptotic trace rejections if bootstrap $p > 0.10$ (size distortion).

---

## 4. Standardized Verdict Ledger Format

Every audit report generated using this tool must conclude with a consolidated verdict table adhering to this structure:

| Candidate Variable | Theoretical Basis | Integration & Collinearity Evidence | Status | Governing Lock / Rationale |
|---|---|---|---|---|
| *Name* | *Formal Model Anchor* | *ADF/KPSS, $r$, CN, $I(2)$ test* | **Promoted / Held / Blocked / Rejected** | *Vault note or gate reference* |

- **Promoted:** Clears all gates; advances to active estimator preparation (e.g., $D_7$, $D_9$).
- **Held:** Admissible at initial screen but held due to secondary collinearity or diagnostic status (e.g., $Q_t^{\text{ME share}}$).
- **Blocked:** Carries fatal $I(2)$ risk or structural non-admissibility (e.g., $q_t$, $Q_t^q$).
- **Rejected:** Fatal collinearity ($r > 0.999$) or unstable level design (e.g., unrestricted $k^{\text{ME}}$ and $k^{\text{NRC}}$, $Q_t^\omega$).
