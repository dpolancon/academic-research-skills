---
name: prose-register-critic
description: "Audits academic drafts and dissertation chapters for internal LLM-scaffolding terminology, meta-commentary, machine cadence, and lexical drift using the AI-Trace Lexical Discipline Protocol. Triggers: audit register, check jargon, check prose register, find metadata leaks, style audit, de-trace, lexical discipline, audit AI traces."
metadata:
  version: "2.1.0"
  status: active
---

# Prose Register Critic & Lexical Discipline Auditor

This skill audits academic manuscripts, dissertation chapters, and applied econometric papers to remove recurring LLM rhetorical habits without flattening theoretical vocabulary, depoliticizing political-economy arguments, or degrading technical precision. It prevents internal workflow commands, agent-routing labels, and pipeline scaffolding terms from leaking into final prose.

---

## 1. Core Invariant: Technical Language is Not Guilty by Association

A word or phrase must never be removed merely because an automated tool flags it as abstract or frequent.

Before editing, classify every flagged term into one of three tiers:

* **Category A: Technical / Conceptual (RETAIN)**  
  Names a legitimate theoretical, empirical, mathematical, institutional, or historical concept.  
  *Examples:* `rate of exploitation`, `transformation elasticity`, `balance-of-payments constraint`, `companion matrix eigenvalues`, `Sraffa-Kurz choice of technique`, `reserve army of labor`, `Johansen trace test`, `supermultiplier`, `effective demand`.
* **Category B: Legitimate but Optional (REVIEW)**  
  Defensible academic phrasing that becomes an AI tell through excessive local repetition.  
  *Examples:* `under an unbalanced growth closure`, `institutional framework`, `transmission mechanism`.
* **Category C: Rhetorical Scaffolding (REWRITE DIRECTLY)**  
  Adds zero analytical content; exists solely to organize, intensify, or narrate the prose.  
  *Examples:* `therapeutic`, `empirical objects`, `black-box screening protocol`, `deliberately stress test`, `system-admissibility gates`, `crucially`, `profound institutional divergence`.

> **Rule:** Only Category C is presumptively editable. Category B is edited only when clustered. Category A is protected. Never execute global find-and-replace.

---

## 2. Core Directives & Empirical Grounding

1. **Purge Metadata Leakage:** Scrutinize the text for terms that sound like an editing ledger (e.g., "retained criteria", "empirical object", "system-admissibility gates", "authorization gate").
2. **Enforce Direct Empirical Naming:** The author must write about the *empirical* system, not the *editing* system.
   - *Bad:* "The empirical object is the cointegration vector."
   - *Good:* "The cointegration vector is the relationship under test."
3. **Scan for Meta-Commentary:** Remove throat-clearing statements where the AI describes its own process (e.g., "This interpretive move reads...").
4. **Purge Melodramatic & Moralizing Rhetoric:** Banish dramatic, emotional, or moralizing characterizations of macroeconomic policy. Enforce sober, institutional, and structural macroeconomic terminology.
   - *Bad:* "The crisis was attributed to fiscal and monetary profligacy."
   - *Good:* "The crisis was attributed to macroeconomic mismanagement and the lack of a macroprudential framework."
5. **Banish Pretentious & Obscurantist Jargon ("Down-to-Earth" Rule):** Purge snobbish, literary, or overly decorative academic vocabulary when direct, standard disciplinary terms exist. Prioritize plain, rigorous institutional and economic clarity over stylistic posturing.
   - *Bad:* "Neo-structuralism became the progressive vernacular through which the regime was stabilized."
   - *Good:* "Neo-structuralism became the progressive framework (or language) through which the regime was stabilized."

---

## 3. The 11 Auditing Pattern Families

### 1. The Boundary Family
* **Flagged:** `bounded`, `boundary`, `boundaries`, `limiting`, `limits`, `constrained`, `constraints`.
* **Retain (A):** Literal intervals, mathematical parameter bounds, external balance-of-payments constraints, boundary conditions in differential equations.
* **Rewrite (C):** When used as generic shorthand for an empirical limitation or sample restriction (e.g., `bounded lag search` $\to$ `lag search over k = 1,...,12`).

### 2. Secondary Branded Metaphors
* **Flagged:** `architecture`, `tournament`, `gate`, `shield`, `trap`, `atlas`, `transmission belt`, `corridor`, `frontier`, `horizon`, `hand-off`, `scaffold`, `lens`, `terrain`, `constellation`, `nexus`.
* **Rewrite (C):** When branding ordinary econometric steps (e.g., `empirical tournament` $\to$ `model comparison`; `admissibility gates` $\to$ `cointegration and stability criteria`).

### 3. Over-Intensification & Evaluative Adjectives
* **Flagged:** `decisive`, `crucial`, `fundamental`, `profound`, `deep`, `stark`, `striking`, `dramatic`, `severe`, `powerful`, `remarkable`, `central`, `key`, `critical`, `precisely`, `systematically`.
* **Rule:** If the adjective is doing work that evidence should do, delete it. Let test statistics and point estimates convey significance.

### 4. Contrast Templates
* **Flagged:** `X, not Y`; `not X but Y`; `rather than X, Y`; `not merely X; it also Y`; `far from X, Y`; `instead of X, Y`.
* **Rule:** Convert to direct positive declarative statements unless distinguishing genuinely competing theoretical models.

### 5. Triads & Rhetorical Parallelism
* **Flagged:** Repeated three-part noun/verb/adjective structures, especially after colons or at paragraph conclusions.
* **Rule:** Retain only if all three components represent distinct, necessary analytical categories. Otherwise, collapse or vary syntax.

### 6. Signposting & Metanarrative
* **Flagged:** `taken together`, `in this sense`, `in this context`, `at stake`, `what matters here`, `the key point is`, `this reveals`, `this highlights`, `importantly`, `crucially`, `significantly`.
* **Rule:** Delete the signpost and begin the sentence directly with the substantive claim.

### 7. Evidential Claim-Strength Calibration
Match verbs strictly to empirical research designs:
* **Descriptive / Stylized Facts:** `documents`, `records`, `shows`, `is consistent with` (Never: `proves`, `confirms`).
* **Granger Causality / VAR:** `predicts`, `precedes conditionally`, `contains incremental predictive information` (Never: `causes`, `drives`).
* **VECM Cointegration:** `identifies a long-run relation`, `rejects the zero-rank null hypothesis`, `estimates the cointegrating vector` (Never: `validates the true production law`).
* **Impulse Responses (GIRF):** `conditional dynamic response`, `exhibits persistent response over reported horizons`.

### 8. Nominalization Clusters
* **Flagged:** Sentences overloaded with abstract nouns (`operationalization`, `conceptualization`, `institutionalization`, `articulation`, `reconfiguration`, `decomposition`).
* **Rule:** Convert at least one nominalization into an active verb.

### 9. Over-Branded Subheadings
* **Rule:** Replace headings combining a metaphor, colon, and punchline with direct descriptions of the empirical object.

### 10. Repetitive Authorial Moves
* **Flagged:** Recurrent paragraph templates: Literature claim $\to$ `Yet...` $\to$ Author's correction $\to$ Grand concluding aphorism (`This distinction is decisive`).
* **Rule:** Vary paragraph endings; allow paragraphs to close quietly with evidence or descriptive data.

### 11. Human Cadence & Sentence Variation
* **Rule:** Avoid uniform sentence lengths (e.g., all 22–26 words). Interlock short declarative sentences (6–12 words) with compound analytical sentences (25–35 words).

---

## 4. Expanded Production Scaffolding Catalog

Scrutinize and immediately purge these workflow tells discovered in production academic drafts:
- **Gate & Admission Scaffolding:** "authorization gate", "admissibility gate", "system-admissibility criteria", "retained criteria", "selection filter".
  - *Replace with:* "stationarity classification", "specification diagnostics", "selection benchmark", "relationship under test".
- **Internal Repository & Pipeline Leaks:** File paths in table notes, figure captions, or prose (e.g., `(\texttt{output/report_...})`, `codes/...`), script mentions, or agent prompt echoes.
  - *Replace with:* Direct academic citation or methodological description ("Sourced from counterfactual estimations").
- **Editing Apparatus References:** "editing ledger", "interpretive move", "analytical move", "editing apparatus", "scaffolding".
  - *Replace with:* Direct subject-matter analysis of the historical or empirical system.
- **Melodramatic & Moralizing Policy Language:** "profligacy", "recklessness", "fiscal orgy", "printing spree", "unbridled spendthrift".
  - *Replace with:* "policy mismanagement", "lack of macroprudential framework/approach", "uncoordinated fiscal-monetary expansion", "unhedged balance-sheet expansion", "macroeconomic disequilibrium".
- **Pretentious & Obscurantist Literary Vocabulary:** "vernacular" (when meaning framework, language, or idiom), "plethora" (use "multiple" or "many"), "paucity" (use "scarcity" or "lack"), "panoply" (use "array" or "range"), "hermeneutic" (use "interpretive" or "analytical"), "rubric" (use "framework" or "category").
  - *Replace with:* Plain, rigorous disciplinary terms: "framework", "language", "vocabulary", "discourse", "array", "scarcity".
- **Non-Native Translation Calques (ES $\to$ EN):** "renounce to" (use "renunciation of" or "abandonment of"), "accorded to" (use "agreed upon" or "in accordance with"), "prevision" (use "forecast" or "prudence").
  - *Replace with:* Standard English macroeconomic phrasing.

---

## 5. The Stateful Learning Loop Protocol

When executing sequential multi-section revisions across an academic manuscript:
1. **Persistent Memory Ledger:** Maintain a synchronized `prose_learning_ledger.json` storing dynamic blacklist terms.
2. **Cumulative Immunity:** Ensure that any newly discovered tell in Section $N$ is logged and automatically enforced across Sections $N+1$ through the Appendices to prevent stylistic regression.
3. **Dual-Critic Integration:** Articulate `/prose-register-critic` (as the structural/object filter) alongside `/humanize-writing` (as the voice/cadence filter) before compiling LaTeX quality gates.

---

## 6. Mandatory Pre-Edit Audit Ledger Workflow

Before modifying any manuscript file, produce an audit ledger in the session log or draft notes using this schema:

| ID | Location | Exact phrase | Pattern family | Class (A/B/C) | Proposed action | Meaning preserved? | Execute? |
|:---|:---|:---|:---|:---|:---|:---|:---|
| L01 | Section 4.3 | "triple confirmation gate" | BRANDED_JARGON | C | Replace with "cointegration rank and stability criteria" | Yes | YES |
| L02 | Section 4.6 | "transformation elasticity $\theta$" | TECHNICAL | A | Retain intact | Yes | NO (RETAIN) |

### Stopping Rule
Stop the audit when:
1. All Category C rhetorical scaffolding is eliminated.
2. Category A technical vocabulary is verified intact.
3. Evidential verbs match the econometric design.
4. No paragraph exhibits conspicuous template repetitions across adjacent pages.

---

## 7. Integrated Verification Tools
- Run `python scripts/check_jargon_leakage.py <file>` or `python scripts/audit_prose_humanize.py <file>` to automatically scan for standard and dynamic blocklist terms.
