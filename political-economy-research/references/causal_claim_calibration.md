# Module M4: Historical Causal-Strength Calibration & Mixed-Methods Synthesis

- **Reference ID:** `political-economy-research/references/causal_claim_calibration.md`
- **Owned Capabilities:** `O6` (Historical Causal-Strength Calibration) & `O7` (Historical Inferential Synthesis)
- **Downstream Consumers:** [`academic-paper`](file:///c:/ReposGitHub/academic-research-skills/academic-paper/SKILL.md), [`econ-write`](file:///c:/ReposGitHub/academic-research-skills/econ-write/SKILL.md), [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md), [`academic-paper-reviewer`](file:///c:/ReposGitHub/academic-research-skills/academic-paper-reviewer/SKILL.md)

---

## 1. Binding Causal-Strength Calibration Obligation (`O6`)

> **CANONICAL OBLIGATION:** Every substantive historical causal conclusion must be explicitly calibrated against (1) step-level evidence, (2) rival mechanisms, (3) negative evidence, (4) downgrade conditions, and (5) scope conditions.
>
> **`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`:** The underlying calibration reasoning is **MANDATORY**. Discrete class labels (`C0`–`C8`) and explicit `A6` tables are **SUPPORTED / OPTIONAL** serialization tools for high-stakes manuscripts, chapters, or formal evaluations—never a mandatory bureaucratic code requirement for every response.

### 1.1 The Five Mandatory Calibration Dimensions
Before emitting any historical causal conclusion, evaluate:
1. **Step-Level Evidentiary Warrant:** Is every critical link in the `ANTECEDENT → MECHANISM → INTERMEDIATE PROCESS → ACTOR/INSTITUTIONAL RESPONSE → CONSEQUENCE` chain supported by protocol-assessed evidence (`historical_source_criticism_protocol.md`)?
2. **Rival-Mechanism Adjudication:** Have plausible rival explanations (`M3`) been evaluated against discriminating evidence, or do the observed traces fit multiple rivals equally?
3. **Negative Evidence & Archival Silences:** Did the mechanism fail any diagnostic test where a trace was expected to be produced and preserved (`DIAGNOSTIC_SILENCE` or direct contradicting records)?
4. **Downgrade Conditions:** Do any of the eight mandatory downgrade triggers (§3) cap the admissible claim strength?
5. **Scope Conditions:** For which exact cases (`M1`) and historical periods (`M2`) is the causal claim warranted?

### 1.2 Fundamental Calibration Rules
- **Weakest Critical Link Rule:** A mechanism-level causal claim cannot exceed the evidentiary warrant of its weakest critical intermediate step. Strong evidence that an antecedent existed and an outcome occurred (`CHRONOLOGICAL_ASSOCIATION`) without evidence for the intermediate transmission link cannot sustain a `MECHANISM_SUPPORTED_CONTRIBUTION` or `STRONG_CAUSAL_ATTRIBUTION` claim.
- **No Rhetorical Upgrade from Narrative Abundance:** Multiplying vivid contextual detail or non-discriminating observations (`NON_DISCRIMINATING_EVIDENCE`) never elevates causal entitlement.
- **Upgrade Path Transparency:** State clearly what specific missing documentary trace, independent corroboration, or quantitative test would be required to move the claim to a stronger tier.
- **Division of Labor with Prose Protocols:** `M4` determines the **substantive causal-strength ceiling** (what level of causal claim the evidence entitles the author to make). Selecting specific sentence-level verbs and syntax within that ceiling belongs to [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md) (§8) and [`econ-write`](file:///c:/ReposGitHub/academic-research-skills/econ-write/SKILL.md).

---

## 2. Substantive Calibration Spectrum (`C0`–`C8` Optional Shorthand)

Analysts may calibrate claims using the substantive analytical categories below (optionally tagged with `C0`–`C8` shorthand codes when structured tables are used):

### 2.1 Contribution-Type Calibration Spectrum (Ascending Warrant)

| Substantive Calibration Category (Optional Code) | Analytical Meaning | Minimum Evidentiary & Methodological Warrant Required |
|:---|:---|:---|
| **Chronological Association** (`C0`) | $A$ preceded or co-occurred with $B$ in time. | Verified dating of $A$ and $B$ (`TIMING`). **Zero causal entitlement.** |
| **Institutional Compatibility** (`C1`) | Institutional configuration $A$ was structurally coherent with outcome or model closure $B$. | Documented institutional rules of $A$ and features of $B$ showing structural fit (including formal-model closure compatibility `MI-1`). Asserts no causal direction. |
| **Constraint** (`C2`) | $A$ narrowed the feasible choice set or eliminated specific policy options for actors producing $B$. | Protocol-assessed evidence that actors perceived, debated, or were bound by limit $A$ within the relevant decision window. Does not claim $A$ uniquely determined which remaining option was chosen. |
| **Facilitation** (`C3`) | $A$ lowered the cost of, enabled, or created institutional capacity for $B$. | Evidence that actors producing $B$ actively utilized or relied upon resource/institution $A$ in sequence. |
| **Contribution** (`C4`) | $A$ was one operative causal factor among others shaping $B$. | Mechanism specified (`M3`); protocol-assessed evidence for key links; at least one rival evaluated and shown not to account fully for $B$. *(Maximum ceiling for an econometric coefficient without within-case process evidence under `EI-1`, or when single-source / retrospective downgrades apply.)* |
| **Mechanism-Supported Contribution** (`C5`) | $A$ contributed to $B$ specifically *through* traced mechanism $M$. | All requirements of `Contribution` + protocol-assessed evidence for **every critical link** of $M$ + discriminating evidence favoring $M$ over plausible rivals + no unresolved cross-method contradiction (`METHOD_DIVERGENCE` absent). |
| **Strong Causal Attribution** (`C8`) | $A$ (operating via $M$) was the primary/decisive driver of $B$ within stated scope. | All requirements of `Mechanism-Supported Contribution` + principal rival mechanisms **substantially eliminated** by high-diagnosticity evidence + corroboration across **genuinely independent sources** + robustness to removing the single most interested source + method status not `DIVERGENT`. |

### 2.2 Logical-Condition Categories (Scope-Bound, Non-Linear)

| Substantive Calibration Category (Optional Code) | Analytical Meaning | Minimum Evidentiary & Methodological Warrant Required |
|:---|:---|:---|
| **Necessary Condition** (`C6`) | Within stated scope, $B$ would not have occurred in the absence of $A$. | Disciplined counterfactual analysis + process evidence showing the causal pathway to $B$ required $A$ with no viable substitute path in scope + no in-scope comparative case exhibiting $B$ without $A$. |
| **Sufficient Condition** (`C7`) | Within stated scope and background conditions, $A$ reliably produces $B$. | Cross-case and within-case evidence demonstrating that $B$ followed from $A$ across all in-scope realizations independently of idiosyncratic confounders. *(Single-case studies rarely warrant sufficiency claims and cap at `Mechanism-Supported Contribution` unless structural invariance is independently established.)* |

---

## 3. Mandatory Downgrade Triggers

Whenever any of the following eight evidentiary vulnerabilities is present on a critical link, the claim's substantive ceiling **must** be downgraded accordingly:

| Downgrade Trigger ID | Evidentiary Condition | Mandatory Calibration Effect |
|:---|:---|:---|
| **`SINGLE_SOURCE_DEPENDENCE`** | A critical mechanism step rests on a single uncorroborated document or informant (`[SINGLE_SOURCE]`). | Cap at **Contribution** (`C4`) or below; cannot support **Strong Causal Attribution** (`C8`). |
| **`INTERESTED_SOURCE_ONLY`** | Supporting records all share a strategic incentive to promote the claimed narrative (`[INTERESTED_PARTY]`). | Cap at **Contribution** (`C4`); cap at **Facilitation/Constraint** (`C3`/`C2`) if incentives for distortion or self-exculpation are severe. |
| **`RETROSPECTIVE_ONLY`** | Critical process steps are evidenced exclusively by memoirs, oral histories, or post-hoc testimony (`[RETROSPECTIVE_RECONSTRUCTION]`). | Cap at **Contribution** (`C4`); flag hindsight-reconstruction risk. |
| **`UNRESOLVED_CONTRADICTION`** | One source (even an apparent "smoking gun") is contradicted by multiple independent records whose divergence is unexplained. | Cap at **Facilitation/Constraint** (`C3`/`C2`) or mark link **Indeterminate** until contradiction is resolved. |
| **`METHOD_DIVERGENCE`** | Econometric estimates or formal-model consistency checks contradict the historical mechanism's observable implications (§4.3). | Cap at **Contribution** (`C4`); explicitly report and diagnose the cross-method divergence. |
| **`DATA_INFORMED_PERIODIZATION`** | The causal claim depends on a period boundary that was revised after observing econometric estimates (`set_before_estimation: false`). | Cap at **Contribution** (`C4`); disclose post-estimation boundary adjustment (`EI-6`). |
| **`IGNORED_INTERDEPENDENCE`** | Cross-case parallel comparison ignores documented transnational/systemic linkages (`M1` §3). | Cap cross-case causal inference at **Institutional Compatibility** (`C1`) until relational/hybrid controls are incorporated. |
| **`NON_DISCRIMINATING_EVIDENCE`** | Observed traces are predicted equally by the proposed mechanism and its principal rival(s). | Cap at **Constraint / Compatibility** (`C2`/`C1`) for the contested mechanism link. |

---

## 4. Historical Inferential Synthesis & Cross-Method Composition (`O7`)

### 4.1 Inferential-Task Jurisdiction
Integration authority across Political Economy, Applied Econometrics, and Heterodox Macro Modeling is governed strictly by **inferential-task jurisdiction**:
- When the inferential question asks **what historical mechanism or institutional sequence operated**, `political-economy-research` synthesizes the already-adjudicated historical, econometric, and formal inputs—while preserving each input's native verdict intact.
- When the inferential question asks **whether a time series has a unit root, cointegrates, or exhibits a statistically significant break**, `applied-econometrics-pe` is the sole authority.
- When the inferential question asks **whether a formal macro model's closure is mathematically consistent or dynamically stable**, `heterodox-macro-modeling` is the sole authority.

### 4.2 Unbreachable Non-Override Rules (`NO CROSS-METHOD OVERRIDE`)

```text
PE cannot revise an econometric verdict.
Econometrics cannot establish a historical mechanism.
Formal models cannot constitute historical evidence.
Historical evidence cannot establish stochastic admissibility.
```

1. **`NO-1` (No Historical Override of Econometrics):** If an econometric test rejects cointegration, finds an insignificant parameter, or detects a structural break at an unexpected date, `political-economy-research` must **never** dismiss, overwrite, or reinterpret that statistical result as a positive confirmation of its preferred narrative.
2. **`NO-2` / `EI-1` (No Econometric Override of Process Tracing):** A statistically significant coefficient corroborates an observable implication of a mechanism, but without within-case documentary/process evidence (`M3`), a statistical estimate alone can support at most **Contribution** (`C4`) for a historical mechanism claim.
3. **`NO-3` / `MI-1` (No Formal-Model Override of History):** A formal macroeconomic model (`heterodox-macro-modeling`) predicting that Mechanism $X$ generates outcome $Y$ provides a *theoretical hypothesis*, never historical evidence that $X$ actually operated in a specific country or period. Without historical traces, model-data coherence supports at most **Institutional Compatibility** (`C1`).
4. **`NO-4` / `EI-4` (No Conversion of Non-Findings into Findings):** Neither econometric failure nor archival silence without a `trace_expectation_basis` may be inverted into positive proof of a structural regime shift or covert conspiracy.

### 4.3 Multi-Method Reconciliation States
When synthesizing historical process tracing with econometric or formal-model inputs, classify their relationship into one of four states:

| Method Status | Condition | Mandatory Handling in Synthesis |
|:---|:---|:---|
| **`CONVERGENT`** | Historical process evidence and quantitative/formal implications independently align. | Record mutual corroboration; each method contributes within its own jurisdiction. |
| **`COMPLEMENTARY`** | Methods address distinct facets of the inquiry (e.g., PE traces cabinet decision sequence; econometrics estimates post-reform elasticity magnitude). | Combine without cross-substitution; maintain distinct evidentiary entitlements for each facet. |
| **`DIVERGENT`** | Historical narrative and econometric findings (or model implications) conflict. | **Never resolve by fiat.** Report both findings transparently, apply `METHOD_DIVERGENCE`, and systematically diagnose candidate sources of divergence:<br>1. *Scope / Sample Mismatch* (different years, sectors, or sub-populations);<br>2. *Implementation / Transmission Lag* (`M2` §3.2);<br>3. *Historical Data Construction Provenance* (interpolation, coverage gaps, or definitional splices flagged under `historical_source_criticism_protocol.md` §7);<br>4. *Archival Source Bias* (uncorroborated or strategic testimony);<br>5. *Econometric Specification / Power Limits* (routed back to `applied-econometrics-pe`). |
| **`ABSENT`** | Only historical/qualitative evidence (or only quantitative evidence) was employed. | Record which method was not applied; draw no positive inference from an unexecuted method. |

---

## 5. Supported Artifact Schema: `A6 Causal Claim Calibration Table` (`OPTIONAL SERIALIZATION`)

For theses, dissertation chapters, journal manuscripts, or formal evaluations, export calibrated causal claims using the `A6` table schema below. For shorter analytical responses, inline calibration statements containing the same five mandatory calibration dimensions (§1.1) are fully compliant.

```markdown
| Claim ID | Neutral Claim Summary | Calibrated Strength Ceiling (Optional C-Code) | Evidentiary Basis & Rivals Eliminated | Downgrade Triggers Applied | Method Status | Scope (Cases & Periods) | Upgrade Path |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `CL-01` | [Claim stated without loaded verbs] | `Constraint` (`C2`) | [Summary of protocol-assessed traces & rival test] | `[SINGLE_SOURCE_DEPENDENCE]` | `COMPLEMENTARY` | [Cases, Period ID] | [Specific archival/quantitative evidence needed to reach `C5`] |
```

---

## 6. Rotated Non-Canonical Illustrations (`ILLUSTRATION — NON-CANONICAL`)

1. **Illustration 1 (Formal Macro Model Without Historical Trace — `MI-1` / `NO-3` Guard):**
   - *Scenario:* A formal Kaleckian/Goodwin model shows that a profit-squeeze mechanism *could* mathematically generate the 1970s investment slowdown in Country $X$, but archival records of employer federations and bank credit committees have not yet been examined.
   - *Calibration:* Capped at **Institutional Compatibility** (`C1`) as a plausible theoretical hypothesis; cannot be presented as an established historical mechanism until `M3` process evidence is gathered.
2. **Illustration 2 (Econometric Finding Contradicting Preferred Historical Narrative — `NO-1` & `DIVERGENT` Handling):**
   - *Scenario:* Archival union correspondence suggests a 1985 labor law weakened strike leverage, but an admissible `applied-econometrics-pe` estimation finds no statistically significant change in the wage share or strike incidence series across 1980–1995.
   - *Calibration:* Classify `method_status: DIVERGENT`, apply `METHOD_DIVERGENCE` (capping the historical impact claim at `Constraint` / `Contribution` for union bargaining strategy rather than aggregate distributive shift), preserve the econometric non-finding intact, and diagnose whether `de facto` firm-level wage drift offset `de jure` statutory changes.
3. **Illustration 3 (Calibrated Claim Without `C0`–`C8` Codes — Proportional Execution):**
   - *Scenario:* Author-side check of a paragraph on 1930s Nordic farmer-labor coalition formation.
   - *Calibration Output:* States directly in prose that the evidence warrants a **mechanism-supported contribution** claim within the 1932–1936 parliamentary window (corroborated across independent party executive minutes, with rival employer-split explanations discriminated against), noting that single-country scope precludes a universal sufficiency claim—without requiring `C0`–`C8` code tags.
