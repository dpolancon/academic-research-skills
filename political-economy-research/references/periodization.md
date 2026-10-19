# Module M2: Historical Periodization & Boundary Typing

- **Reference ID:** `political-economy-research/references/periodization.md`
- **Owned Capability:** `O2` (Historical Periodization)
- **Interfaces:** [`shared/protocols/historical_source_criticism_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/historical_source_criticism_protocol.md) (boundary evidence); `applied-econometrics-pe` (statistical break reconciliation)

---

## 1. Scope & Core Periodization Principles (`P-1`–`P-8`)

`M2` governs how historical time is partitioned into analytically meaningful periods and how historical institutional boundaries compose with statistical structural breaks.

### 1.1 Mandatory Periodization Rules
1. **`P-1` Explicit Period Criterion First:** Before dating any boundary, declare the **period criterion**—the specific institutional, structural, or relational dimension whose qualitative transformation defines a new regime (e.g., wage-bargaining framework, central bank mandate and monetary target rule, capital-account convertibility regime, trade/tariff constitution, agrarian property-rights regime).
2. **`P-2` Mandatory Boundary Typing:** Every temporal division used in an analysis must be classified using the 5-type Boundary Typology (§2).
3. **`P-3` Evidentiary Justification of Institutional Boundaries:** Every `HISTORICAL_INSTITUTIONAL` boundary must be substantiated by documentary, statutory, or institutional evidence assessed under [`historical_source_criticism_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/historical_source_criticism_protocol.md) demonstrating that the stated period criterion actually changed.
4. **`P-4` Transition Intervals Over Forced Point Dates:** Institutional transformations frequently unfold across multi-year legislative, political, or organizational struggles. Where change is processual, represent the boundary as a **transition interval** `[t_start, t_end]` rather than forcing an arbitrary single point date.
5. **`P-5` Alternative Periodizations & Sensitivity:** Whenever boundary dates or criteria are historiographically contested, record at least one **alternative periodization** and state which substantive conclusions are sensitive to choosing one boundary over another.
6. **`P-6` Pre- vs. Post-Estimation Provenance (`set_before_estimation`):** Record whether each historical boundary was defined ex ante (prior to viewing econometric estimates) or revised after observing statistical results (`EI-6`).
7. **`P-7` Cyclical Fluctuation Demarcation:** Short-term business cycles, inventory swings, or commodity price oscillations within an unchanged institutional rule set must be typed `CYCLICAL_FLUCTUATION` and never promoted to regime boundaries unless accompanied by documented change in the period criterion.
8. **`P-8` Convenience Partition Restriction:** Arbitrary chronological cuts (decades, half-centuries, or start/end dates dictated solely by dataset availability) must be typed `CONVENIENCE` and are **strictly barred from bearing causal or regime-interpretive weight**.

### 1.2 Separation from Material Passport `timeline.schema.json`
The Material Passport `timeline.yaml` (`shared/contracts/passport/timeline.schema.json`, managed by `deep-research`) stores **verified dated facts** (e.g., *"Statute X enacted on Date D"*). Periodization boundaries are **interpretive analytical constructs** owned by `political-economy-research` and must never be written into the passport timeline as raw factual events.

---

## 2. Canonical Boundary Typology

Every temporal boundary in a political-economy study must be assigned one of the following five canonical types:

| Boundary Type | Definition | Admissible Analytical Use |
|:---|:---|:---|
| `HISTORICAL_INSTITUTIONAL` | A documented transformation in the stated period criterion supported by protocol-assessed historical/institutional evidence. | Full causal, comparative, and regime-interpretive analysis; may be exported to `applied-econometrics-pe` as an ex-ante structural break hypothesis. |
| `STATISTICAL_BREAK` | A shift in a time series' stochastic parameters (mean, trend, variance, or cointegrating vector) detected or tested by `applied-econometrics-pe`. | Statistical specification and parameter stability modeling. **Cannot** be interpreted as an institutional regime transition unless independently corroborated by historical evidence (`EI-2`). |
| `CYCLICAL_FLUCTUATION` | A recurrent or transitory expansion/contraction within an existing institutional regime without transformation of the period criterion. | Analyzing within-regime dynamics, business-cycle phases, or capacity utilization swings; never a regime boundary. |
| `CONVENIENCE` | A researcher-imposed partition (e.g., decadal tables, pre-/post-census cutoffs, or sample truncation due to missing data). | Descriptive summary and exposition only; **prohibited** as evidence of institutional or structural change. |
| `CONTESTED` | Historical records or historiography conflict on whether the period criterion changed or on which date/interval marks the transition. | Requires explicit comparative sensitivity analysis across the competing boundary dates. |

---

## 3. PE ↔ Econometrics Periodization Interface (`NO CROSS-METHOD OVERRIDE`)

```text
political-economy-research (M2)
    OWNS: Historical periodization, period criteria, and institutional boundary typing.
          │                                         ▲
          │ Exports ex-ante boundary hypotheses     │ Exports detected break dates, CIs,
          ▼                                         │ and test provenance
applied-econometrics-pe
    OWNS: Statistical break detection, structural break tests (Chow, Bai–Perron,
          Zivot–Andrews, Lee–Strazicich), and stochastic admissibility.
```

### 3.1 Binding Interface Rules (`EI-2`, `EI-3`, `EI-4`, `EI-6`)
- **`EI-2` (Statistical Break $\neq$ Historical Boundary):** An endogenous break date estimated by `applied-econometrics-pe` enters `M2` strictly as `STATISTICAL_BREAK`. It may prompt historical investigation (`prompted_by_statistical_break: true`), and is promoted to `HISTORICAL_INSTITUTIONAL` **only** if independent documentary/institutional evidence establishes that the period criterion changed.
- **`EI-3` (Historical Boundary $\neq$ Statistical Break):** A documented `HISTORICAL_INSTITUTIONAL` reform (e.g., dismantling a statutory wage-indexation board) that does not produce a statistically significant break in an aggregate time series remains a valid historical boundary. Both the institutional reform and the econometric non-finding are reported truthfully; neither overwrites the other.
- **`EI-4` (Anti-Reverse-Engineering / No Narrative Rescue):** Periodization must **never** be reverse-engineered to rescue a failed econometric specification or explain away non-cointegration without independent historical evidence.
- **`EI-6` (Post-Estimation Revision Downgrade):** If a period boundary is adjusted after viewing econometric break tests or parameter estimates, record `set_before_estimation: false` in the Periodization Ledger and trigger the `DATA_INFORMED_PERIODIZATION` causal-strength downgrade in `M4`.

### 3.2 Break Alignment & Reconciliation: No Universal $\pm N$-Year/Month Tolerances

> **HARD PROHIBITION:** Do **not** introduce or apply universal numeric alignment windows (such as hard-coded `±1 year`, `±2 years`, or `±4 quarters` rules) to judge whether a `STATISTICAL_BREAK` corresponds to a `HISTORICAL_INSTITUTIONAL` boundary.

Whether an institutional reform at time $t_{\text{hist}}$ and a statistical break at time $\hat{t}_{\text{stat}}$ corroborate one another is a **domain composition problem** evaluated across four structural factors:
1. **Temporal Granularity:** Decadal, annual, quarterly, and monthly analyses operate on fundamentally different scales of precision.
2. **Dating Uncertainty & Transition Intervals:** When institutional transformation spans an interval $[t_0, t_1]$ (e.g., legislation enacted in $t_0$, regulatory agency operational in $t_1$), a statistical break anywhere within or immediately following the transition interval may reflect the same process.
3. **Institutional Implementation & Behavioral Lag:** Statutory reforms, tariff schedules, or collective-bargaining restructurings often require contract-renewal cycles, capital-stock turnover, or administrative rollout before shifting macroeconomic aggregates.
4. **Data Frequency, Smoothing & Construction Provenance:** Annual averaging, fiscal-year definitions, or benchmark interpolation (`historical_source_criticism_protocol.md` §7) can shift the apparent timing of a statistical break relative to the underlying event.

**Project-Declared Tolerance Rule:** Any numerical alignment window used in a study must be **explicitly project-declared and method-justified** (via the Workspace Project Overlay or Design Brief `A1`) based on the specific mechanism's implementation lag and data frequency—never invoked as a universal architectural constant.

---

## 4. Supported vs. Mandatory Serialization (`A2 Periodization Ledger`)

In accordance with **`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`**:
- **Mandatory Reasoning Obligation:** Stating the period criterion, typing every boundary under §2, justifying `HISTORICAL_INSTITUTIONAL` boundaries with protocol-assessed evidence, respecting transition intervals, and honoring `EI-2`/`EI-3`/`EI-4`/`EI-6` without universal numeric alignment windows.
- **Supported (Optional) Artifact Serialization (`A2 Periodization Ledger`):** When periods carry analytical or causal weight in a study, chapter, or formal evaluation, serialize the periodization using the `A2` schema below. For purely descriptive timelines or brief consultations, inline boundary typing suffices.

### Supported Artifact Schema: `A2 Periodization Ledger` (`OPTIONAL SERIALIZATION`)
- **Ledger Header Fields:**
  - `period_criterion`: Dimension defining regime continuity and change.
  - `alternative_periodizations_considered`: Competing historiographical or theoretical periodizations.
  - `sensitivity_note`: How substantive conclusions change under alternative boundaries.
- **Per-Boundary Row Fields:**
  - `boundary_id`: Unique identifier.
  - `date_or_interval`: Point date or transition interval `[t_start, t_end]`.
  - `boundary_type`: `HISTORICAL_INSTITUTIONAL` | `STATISTICAL_BREAK` | `CYCLICAL_FLUCTUATION` | `CONVENIENCE` | `CONTESTED`.
  - `criterion_change_described`: Exact institutional/structural change at the boundary.
  - `historical_evidence`: Protocol-assessed documentary/institutional records.
  - `statistical_evidence`: Econometric break test results and confidence intervals (if applicable).
  - `set_before_estimation`: `true` | `false`.
  - `prompted_by_statistical_break`: `true` | `false`.
  - `alignment_justification`: Structural reconciliation of any lag/offset between historical transition and statistical break (or project-declared tolerance with justification).
  - `revision_log`: Provenance of any boundary changes.

---

## 5. Rotated Non-Canonical Illustrations (`ILLUSTRATION — NON-CANONICAL`)

1. **Illustration 1 (Postwar Japanese Industrial Finance — Transition Interval & Implementation Lag):**
   - *Period Criterion:* Regulatory ceiling on corporate bond issuance and main-bank credit allocation rules.
   - *Historical Boundary:* Phased deregulation spanning `[1979, 1984]` (`HISTORICAL_INSTITUTIONAL` transition interval).
   - *Statistical Break:* Bai–Perron break in manufacturing corporate bank-debt ratios detected in `1986Q2` (`STATISTICAL_BREAK`).
   - *Reconciliation:* Multi-year loan maturity rollover explains the 2-year lag between final bond-market deregulation (1984) and the balance-sheet break (1986); corroborated as `CONVERGENT` with lag justification, without forcing an artificial point date.
2. **Illustration 2 (Interwar Swedish Labor Compact — Institutional Boundary Without Immediate Aggregate Break):**
   - *Period Criterion:* Centralized peak-level collective bargaining governance (Saltsjöbaden Agreement, December 1938 — `HISTORICAL_INSTITUTIONAL`).
   - *Statistical Break:* Aggregate real-wage growth series exhibits a statistical break in 1940 (`STATISTICAL_BREAK`) driven by wartime mobilization and import blockade rather than the 1938 institutional pact.
   - *Reconciliation (`EI-2` & `EI-3`):* Keep December 1938 as the `HISTORICAL_INSTITUTIONAL` boundary of labor-regime governance, and record 1940 as a wartime shock break; do not conflate the two.
3. **Illustration 3 (Post-1970s Commodity Cycle vs. Institutional Regime — `CYCLICAL_FLUCTUATION` Guard):**
   - *Scenario:* Primary-exporting economy experiences a sharp 1986–1987 terms-of-trade dip while export-marketing board statutes, exchange-rate rules, and tax royalties remain unchanged.
   - *Classification:* Typed `CYCLICAL_FLUCTUATION` (`P-7`), not a new institutional period.
