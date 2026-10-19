# ARS Shared Historical Source-Criticism Protocol

**Specification ID:** `shared/protocols/historical_source_criticism_protocol.md`
**Version:** 1.0.0
**Status:** CANONICAL SHARED PROTOCOL (Wave D4-A Implementation / Wave D4.1 Micro-Freeze; Ratified in Wave D1-LOCK-03)
**Date:** 2026-10-17
**Baseline Git Commit:** `917ee2f2332cef92015937bddd7337a52ef4b12d`
**Semantic Classification:** `CROSS_DOMAIN_SHARED_PROTOCOL`
**Consumers:** `political-economy-research`, `deep-research`, `academic-paper`, `academic-paper-reviewer`, future historical/institutional domain workflows

---

## 1. Purpose

The Academic Research Skills (ARS) Historical Source-Criticism Protocol establishes the canonical cross-domain evidentiary standard for evaluating archival, documentary, institutional, testimonial, and historically constructed statistical sources **relative to the specific claim they are invoked to support**.

Its central epistemic invariant is that **evidentiary reliability is a property of a `(source, claim)` pair, never an intrinsic, claim-independent rank of a document.** A source may be authoritative for one claim (e.g., that an actor made a specific argument in a cabinet memorandum) and weak or misleading for another (e.g., that the argument reflects the true consensus of the cabinet or the actual cause of the policy outcome).

---

## 2. Ownership Boundary & Three-Way Division of Labor

`shared/protocols/historical_source_criticism_protocol.md` is strictly classified as a **`CROSS_DOMAIN_SHARED_PROTOCOL`**:

```text
deep-research
    OWNS discovery, retrieval, bibliographic verification, citation existence,
    and dated-fact extraction (timeline.yaml).

shared/protocols/historical_source_criticism_protocol.md
    OWNS the claim-relative historical/documentary source-assessment standard
    for evaluating individual (source, claim) pairs.

political-economy-research
    OWNS aggregating assessed (source, claim) pairs across sources, mechanism
    steps, and rival explanations to construct periodizations, adjudicate
    historical mechanisms, and calibrate substantive causal claim strength.
```

1. **Protocol, Not Skill:** This protocol is a consultative evidentiary standard, not an autonomous retrieval agent, domain methodology skill, or peer-review engine.
2. **Pair-Level Scope Only:** This protocol evaluates individual `(source, claim)` pairs. It never aggregates across multiple sources to declare which rival historical mechanism won, nor does it calibrate overall manuscript causal claims (which belongs to `political-economy-research`).
3. **Consumer Application:** Any component holding a historical or documentary claim applies this protocol to evaluate the evidentiary warrant of the source for that specific claim:
   - `political-economy-research` applies it to period boundaries, mechanism steps, and relational linkages;
   - `deep-research` may apply it when fact-checking historical occurrence or timing claims;
   - `academic-paper-reviewer` may apply it when auditing whether a manuscript's archival citations support its factual assertions.

---

## 3. Conditional Activation Predicate

This protocol is **conditionally activated** when historical, documentary, archival, or institutional evidence materially bears on the claim under evaluation.

### 3.1 When the Protocol Is ACTIVE
Activate this protocol whenever a claim's support materially depends on:
- **Archival or Documentary Records:** Official state papers, diplomatic cables, cabinet minutes, treasury/central bank memoranda, corporate archives, union records, legal filings, or private correspondence.
- **Institutional & Regulatory Records:** Statutes, decrees, parliamentary debates, treaty texts, central bank annual reports, IMF/World Bank staff reports, or commission hearings.
- **Retrospective Testimony:** Memoirs, autobiographies, oral histories, diaries edited ex post, or retrospective interviews concerning past events or decisions.
- **Contemporaneous Non-Scholarly Accounts:** Newspapers, financial press, pamphlets, manifestos, or public speeches used as evidence of historical events, actor perceptions, or public framing.
- **Secondary Historiography Used as Factual Evidence:** Scholarly historical monographs when cited to establish that a specific historical event, sequence, or institutional rule existed (distinct from citing a monograph's *causal interpretation*, which enters `political-economy-research` as a rival hypothesis).
- **Construction Provenance of Historical Statistics:** Historical national accounts, decadal censuses, reconstructed price/wage series, or spliced long-run datasets where archival compilation, definitional shifts, or interpolation affect what substantive historical claims the series can bear (§7).

### 3.2 When the Protocol Is INACTIVE
Do **not** activate this protocol for:
- **Stochastic Time-Series & Econometric Inference:** Unit-root testing, cointegration, structural break tests, VAR/VECM/ARDL estimation, and estimator identification remain governed by `applied-econometrics-pe`.
- **Experimental / Quasi-Experimental Microeconometric Designs:** RCT, DID, IV, RDD, synthetic control, and related causal-identification methodologies. These methods are outside the historical-source-criticism protocol. They must be delegated to the applicable quantitative-method capability when such a capability is implemented and authorized. (Do not assign them to `applied-econometrics-pe`, because D2 explicitly limits its currently implemented scope to political-economy time-series methods. Broader causal-inference methodology ownership is recorded as: `CANDIDATE FUTURE CAPABILITY GAP — NOT AUTHORIZED`.)
- **Formal Mathematical Derivations:** Model equations, closures, accounting identities, and stability proofs remain governed by `heterodox-macro-modeling`.
- **Generic Literature Screening & Biomedical Evidence Hierarchies:** Existing literature-screening admission rules (`academic-paper/references/domain_evidence_profiles.md`) and non-historical evidence pyramids (`deep-research/references/source_quality_hierarchy.md`) remain unchanged for their respective domains.

---

## 4. Prohibition of Universal Source Hierarchies

> **CORE INVARIANT: NO UNIVERSAL SOURCE HIERARCHY (`PRIMARY > SECONDARY` IS PROHIBITED)**

This protocol strictly prohibits ranking sources along a context-free hierarchy such as:
- *"Primary sources are always superior to secondary sources"*;
- *"Archival documents are always more reliable than published sources"*;
- *"Official government statistics are always more accurate than private reconstructions"*; or
- *"Contemporaneous records always trump retrospective accounts regardless of the claim."*

### Why Universal Hierarchies Fail in Historical Inquiry
1. **Claim-Relativity:** A contemporaneous government press release (`primary source`) is strong evidence of *what the government publicly claimed at time $t$*, but weak or systematically distorted evidence of *actual covert policy motives* or *aggregate economic outcomes*. Conversely, a critical secondary monograph synthesizing multiple declassified archives (`secondary source`) may be far stronger evidence of the overall decision sequence than any single contemporaneous participant's partial view.
2. **Strategic Misrepresentation in Primary Records:** Contemporaneous internal memoranda are frequently written to persuade superiors, shift blame, create plausible deniability, or satisfy bureaucratic mandates.
3. **Epistemic Position vs. Temporal Proximity:** A low-level contemporaneous observer may lack access to closed-door negotiations, whereas a retrospective deposition by a direct participant—corroborated by procedural logs—may accurately report who spoke in the room.

---

## 5. Claim-Relative Evaluation Framework

### 5.1 Atomic Claim Specification & Claim Types
Before evaluating any source, decompose the assertion into an **atomic claim** and classify its `claim_type`:

| Claim Type | Analytical Question | Typical Evidentiary Vulnerability |
|:---|:---|:---|
| `OCCURRENCE` | Did event, meeting, transaction, or action $E$ take place? | Fabrication, rumor, second-hand reporting, confusion of planned vs. executed action. |
| `TIMING` | When did $E$ occur, or in what sequence did $E_1$ and $E_2$ unfold? | Retroactive dating, misdated drafts, reporting lags, ex-post telescoping in memoirs. |
| `ACTOR_BELIEF_OR_PERCEPTION` | What did actor $A$ know, believe, or perceive at time $t$? | Hindsight bias in retrospective accounts; strategic posturing in public statements. |
| `ACTOR_INTENTION` | What goal or motive drove actor $A$ to choose action $X$? | Self-serving rationalization, concealment of controversial motives, audience-tailored rhetoric. |
| `DECISION_PROCESS` | How was decision $D$ reached inside institution $I$ (who proposed, who opposed, what constraints bound)? | Formal minutes omitting informal pre-meetings; sanitization of internal dissent; partial vantage point. |
| `INSTITUTIONAL_RULE` | What formal or informal rule governed domain $R$ during period $P$? | Confusing statutory text (`de jure` rule) with actual enforcement (`de facto` practice). |
| `MAGNITUDE` | How large was flow, stock, price, or participation $M$? | Administrative undercounting, tax evasion, political manipulation of statistics, linear interpolation. |
| `ABSENCE` | Did action, debate, or consideration $X$ *fail* to occur? | Treating archival silence as proof of historical absence when records were never kept, purged, or held elsewhere. |
| `RELATION` | Did actor/case $A$ transmit resources, constraints, or pressure to actor/case $B$? | Inferring bilateral transmission from parallel movement without documentary or flow trace of the channel. |

### 5.2 Canonical Diagnostic Repertoire (`D1`–`D14`)

> **GOVERNANCE LOCK: `CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`**
>
> Dimensions `D1`–`D14` constitute a **canonical diagnostic repertoire**, not a requirement to produce fourteen explicit assessments for every source.
>
> Each dimension must be considered where relevant to the `(source, claim)` pair; **only applicable dimensions need explicit treatment**.
>
> **Mandatory Core Obligation:** The analyst must assess source warrant relative to the specific claim, including relevant questions of access, temporality, incentives, corroboration, provenance, and silence.

| # | Dimension | Diagnostic Question |
|:---|:---|:---|
| **D1** | **Provenance & Custody** | From which archive, collection, fonds, or publication does the source originate, and is its chain of custody intact? |
| **D2** | **Authenticity & Integrity** | Is the document authentic, complete, and free from unrecorded alterations, redactions, or misattributed dates? |
| **D3** | **Authorship & Institutional Position** | Who authored or compiled the source, and what was their formal role, rank, and mandate within the institution? |
| **D4** | **Temporal Proximity** | How close in time was the record created to the event, decision, or process it describes? |
| **D5** | **Contemporaneous vs. Retrospective Construction** | Was the source produced as an operational byproduct of the event itself, or reconstructed retrospectively (memoir, oral history, post-crisis commission) with knowledge of subsequent outcomes? |
| **D6** | **Access to the Reported Event/Process** | Was the author in a direct epistemic position to observe or participate in what the claim asserts, or relying on hearsay/intermediaries? |
| **D7** | **Intended Audience & Genre** | For whom was the document created (private diary, classified intra-ministry memo, diplomatic cable to headquarters, parliamentary speech, public press release), and how does genre shape what is said or unsaid? |
| **D8** | **Incentives & Strategic Interests** | What career, political, financial, legal, or ideological incentives did the author/institution have to exaggerate, downplay, conceal, or fabricate for this specific claim? *(Note: Admission against strategic interest strengthens evidentiary warrant.)* |
| **D9** | **Internal Consistency** | Is the source internally coherent in its chronology, logic, quantitative totals, and named participants? |
| **D10** | **External Corroboration & Independence** | Do genuinely independent sources corroborate or contradict the claim? *(Verify that corroborating sources do not merely repeat the same underlying informant or press report.)* |
| **D11** | **Archival Selection, Survival & Silence** | Why was this record created and preserved while others were not? If invoking archival silence (`ABSENCE`), is there a positive `trace_expectation_basis` proving that the event *would* have been recorded and *would* have survived in this repository? |
| **D12** | **Numerical Construction Provenance** | If the source is a historical statistic or series: how was it defined, collected, aggregated, deflated, spliced, or interpolated? (§7) |
| **D13** | **Conceptual & Temporal Fit to the Claim** | Do the source's institutional categories, geographic coverage, and exact timeframe match the scope of the claim without anachronistic projection? |
| **D14** | **Source Role in the Argument** | Is the source being used as a direct trace of the process (`primary operational trace`), as testimony about the process (`informant report`), as background context, or as a foil? |

---

## 6. Pair-Level Assessment Verdict & Qualifiers

### 6.1 Pair-Level Verdicts
Every `(source, claim)` evaluation concludes with a canonical pair-level verdict adhering to this taxonomy:

- **`SUPPORTS` (`STRONG` | `MODERATE` | `WEAK`):** The source provides positive evidentiary warrant for the specific claim at the stated strength after accounting for access, temporality, incentives, and corroboration.
- **`UNDERMINES` (`STRONG` | `MODERATE` | `WEAK`):** The source provides credible evidence contradicting the specific claim.
- **`SILENT`:** The source contains no direct trace of the claimed event/process.
  - `subtype: DIAGNOSTIC` — Diagnostic silence requires a verified `trace_expectation_basis` (D11) demonstrating that if the claim were true, this specific source/archive would have recorded and preserved it.
  - `subtype: NON_DIAGNOSTIC` — Non-diagnostic silence supplies no evidence for an absence claim (when the source's genre, mandate, classification rules, or survival history provide no expectation that the event would appear there).
- **`INDETERMINATE`:** Internal contradictions, severe provenance gaps, or unresolved authenticity problems prevent the source from bearing weight either way on this claim.

### 6.2 Mandatory Risk Qualifiers (Exported to Consumers)
When returning a pair-level assessment to `political-economy-research` or another consumer, attach all applicable risk qualifiers so downstream causal calibration can apply appropriate downgrade triggers:
- `SINGLE_SOURCE` — No independent corroborating record has been established for this claim.
- `INTERESTED_PARTY` — Author/institution had a strong strategic incentive aligned with the claim's direction.
- `ADMISSION_AGAINST_INTEREST` — Author/institution testified or recorded a fact contrary to their strategic interest (strengthens warrant).
- `RETROSPECTIVE_RECONSTRUCTION` — Source was produced significantly after the event with hindsight knowledge.
- `INDIRECT_ACCESS` — Author was not a direct participant/observer of the specific step claimed.
- `DE_JURE_ONLY` — Source establishes statutory/formal rules but not actual enforcement or practice.
- `INTERPOLATED_OR_SPLICED_SERIES` — Quantitative historical source relies on backward projection, benchmark interpolation, or unadjusted definitional breaks.

---

## 7. Historical Statistics Boundary: Construction Provenance vs. Stochastic Admissibility

Historical political economy frequently relies on long-run historical statistics, reconstructed national accounts, colonial/imperial fiscal ledgers, historical wage/price series, and spliced decadal censuses. These datasets are simultaneously **historical artifacts** and **quantitative inputs**.

To preserve `INFERENTIAL-TASK JURISDICTION` and `NO CROSS-METHOD OVERRIDE`, enforce the following strict boundary:

```text
HISTORICAL SOURCE CRITICISM (This Protocol)
    OWNS: CONSTRUCTION PROVENANCE
    (Who compiled the series, archival basis, coverage, institutional definitions,
     revisions, splicing across regimes, and benchmark interpolation.)
          │
          ▼   [Exports provenance flags; never rules on time-series properties]
APPLIED ECONOMETRICS (applied-econometrics-pe)
    OWNS: STOCHASTIC ADMISSIBILITY & ESTIMATION
    (Integration order I(d), unit-root testing, cointegration, structural break
     significance, estimator validity, and variance/uncertainty inference.)
```

### 7.1 What This Protocol May Assess (`CONSTRUCTION PROVENANCE`)
1. **Institutional & Archival Origin:** Who collected the underlying raw figures (tax authorities, customs houses, employer associations, central statistical offices, or later economic historians)?
2. **Coverage & Omissions:** Which sectors, regions, informal activities, or worker categories were excluded?
3. **Definitional & Regime Shifts:** Did accounting definitions (e.g., gross vs. net output, territory boundaries, industrial classification, fiscal year dates) change across historical periods?
4. **Interpolation & Reconstruction Artifacts:** Were annual observations between decennial censuses generated via linear interpolation or proxy-variable backcasting? *(Crucial: Linear interpolation artificially smooths variance and induces mechanical autocorrelation; this protocol flags `INTERPOLATED_OR_SPLICED_SERIES` so neither historical narrative nor econometric specification mistakes an interpolation artifact for historical stability.)*
5. **Reporting Incentives:** Were underlying units incentivized to underreport (e.g., tax avoidance, capital flight) or overreport (e.g., plan-fulfillment quotas)?

### 7.2 What This Protocol May NEVER Assess (`STOCHASTIC ADMISSIBILITY`)
This protocol must **never**:
- Declare a series $I(0)$, $I(1)$, trend-stationary, or difference-stationary;
- Rule on whether two historical series cointegrate;
- Certify whether a historical jump in a series is a statistically significant structural break; or
- Validate or invalidate an econometric estimator (OLS, VAR, VECM, ARDL, Toda–Yamamoto).

All stochastic and econometric determinations belong exclusively to `applied-econometrics-pe`.

---

## 8. Proportionality & Serialization (`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`)

In accordance with the repository-wide governance principle **`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`**:

1. **Mandatory Reasoning Obligation:** Whenever historical or documentary sources are used to support a substantive claim, the analyst must evaluate the source *relative to that specific claim* (checking access, temporality, strategic incentives, corroboration, and archival silence) and avoid any mechanical `primary > secondary` assumption. Dimensions `D1`–`D14` provide the diagnostic repertoire to draw upon where relevant; producing all fourteen explicit evaluations is never required.
2. **Supported (Optional) Serialization Format:** For high-stakes adjudications, contested archival evidence, or formal evaluations, consumers may serialize pair assessments using the structured **Source–Claim Assessment Record** below. For routine or exploratory tasks, compact inline source-claim annotations fully satisfy the protocol without requiring full table serialization.

### Supported Template: Source–Claim Assessment Record (`OPTIONAL SERIALIZATION`)

```markdown
| Pair ID | Atomic Claim & Type | Source Descriptor | Key Dimensions (Access, Proximity, Incentives, Corroboration, Silence/Provenance) | Pair Verdict & Risk Qualifiers |
|:---|:---|:---|:---|:---|
| `SC-01` | [Exact claim] (`[CLAIM_TYPE]`) | [Author, document, archive/source, date] | • Proximity/Construction: [Contemporaneous / Retrospective]<br>• Access: [Direct participant / Indirect]<br>• Incentives: [Candor vs. strategic interest]<br>• Corroboration/Silence: [Independent records / Trace expectation] | `SUPPORTS (MODERATE)`<br>Qualifiers: `[INTERESTED_PARTY]` |
```

---

## 9. Worked Claim-Relative Contrasts (`ILLUSTRATION — NON-CANONICAL`)

### Illustration A: Contemporaneous Government Memorandum vs. Retrospective Memoir
- **Source 1:** Confidential Treasury memorandum authored by the Deputy Finance Minister during an exchange-rate crisis (1967).
- **Source 2:** Published memoirs of the Prime Minister written fifteen years later (1982).
- **Claim 1 (`ACTOR_POSITION_IN_PROCESS`):** *"The Treasury formally warned the Cabinet in October 1967 that foreign-exchange reserves would be exhausted within six weeks without import surcharges."*
  - **Source 1 Assessment:** Contemporaneous operational document (`D4`, `D5`), direct institutional authorship (`D3`, `D6`), preserved in cabinet registry (`D1`). **Verdict:** `SUPPORTS (STRONG)` for what the Treasury formally communicated.
  - **Source 2 Assessment:** Retrospective (`D5`), prone to date telescoping and self-justification (`D8`). **Verdict:** `SUPPORTS (WEAK)` if uncorroborated; redundant once Source 1 is present.
- **Claim 2 (`DECISION_PROCESS` / `CAUSAL_MOTIVE`):** *"The Cabinet rejected import surcharges solely because of foreign creditor threats rather than domestic electoral pressure."*
  - **Source 1 Assessment:** Written *before* the final Cabinet vote by one bureaucratic faction advocating surcharges; the author had a strategic incentive (`D8`) to portray rival objections as capitulation to external pressure. **Verdict:** `SUPPORTS (WEAK)` with qualifiers `[INTERESTED_PARTY, SINGLE_SOURCE]`. Even though it is a contemporaneous archival primary source, it cannot by itself establish the Cabinet's decisive collective motive.
  - **Source 2 Assessment:** The Prime Minister's memoir admits that fear of losing marginal industrial constituencies in the upcoming by-election blocked the surcharge (`ADMISSION_AGAINST_INTEREST` relative to statesmanship narrative, corroborated by party whip logs `D10`). **Verdict:** `UNDERMINES (MODERATE)` Claim 2's "solely foreign creditor threats" assertion.

### Illustration B: Corporate Archive Silent on Labor Conflict
- **Source:** Complete board of directors' formal annual reports of a textile conglomerate (1920–1930).
- **Claim (`ABSENCE`):** *"Shop-floor labor unrest did not factor into management's decision to relocate production to rural mills in 1926."*
- **Protocol Assessment:**
  - Under `D7` (Intended Audience & Genre) and `D8` (Strategic Interests), published annual reports to shareholders routinely omit or sanitize internal labor strife to maintain investor confidence.
  - Under `D11` (Archival Selection & Silence), the `trace_expectation_basis` fails for annual shareholder reports: shop-floor unrest would instead be recorded in plant-manager correspondence, strike insurance ledgers, local labor ministry inspectorate files, or union press.
  - **Verdict:** `SILENT` (`subtype: NON_DIAGNOSTIC`). The silence of the board's annual reports provides **zero evidentiary support** for the claim that labor conflict was absent.
