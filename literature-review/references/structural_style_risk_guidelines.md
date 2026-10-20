# Structural Style-Risk Guidelines (No-AI-Trace Editorial Principles)

**Specification ID:** `literature-review/references/structural_style_risk_guidelines.md`  
**Lifecycle Stage:** `L10 — PROVENANCE AUDIT`, `L11 — DISCIPLINARY REGISTER / HUMANIZATION`  
**Consumes:** `shared/protocols/prose_discipline_protocol.md`  

---

## 1. Editorial Philosophy: Diagnostic Signals vs. "AI Detection"

> **CORE PRINCIPLE:**  
> This specification explicitly rejects "AI detection" algorithms, perplexity scores, and mechanical synonym-substitution "humanizers."  
>  
> Instead, it establishes **Structural Style-Risk Diagnostics**: identifying repetitive rhetorical formulas, syntactic symmetry, workflow metadata leaks, and rhythmic monotony that degrade scholarly prose quality.

Style risk flags are **editorial diagnostics**, not automatic scholarly errors. They highlight passages that require authorial attention and naturalization.

---

## 2. The 18 Structural Style-Risk Pattern Families

### Family 1: Abstract Topic-Sentence Monotony (`RISK_TOPIC_SENTENCE_MONOTONY`)
- **Diagnostic:** Every paragraph begins with an identical high-level abstract announcement rather than entering through concrete empirical, methodological, or conceptual problems.

### Family 2: Annotated-Bibliography Author Sequencing (`RISK_ANNOTATED_BIB_SEQUENCING`)
- **Diagnostic:** Sentences follow an unvaried roster: *"Smith (2010) examines... Jones (2014) finds... Williams (2018) shows..."* without establishing logical or comparative necessity.

### Family 3: Binary Antithesis Symmetry (`RISK_BINARY_SYMMETRY`)
- **Diagnostic:** Repetitive use of *"While Author A argues X, Author B contends Y"* across consecutive paragraphs.

### Family 4: Mechanical Synthesis Triggers (`RISK_MECHANICAL_SYNTHESIS`)
- **Diagnostic:** Repeated reliance on stock summary transitional phrases: *"Taken together..."*, *"In summary..."*, *"Collectively, these studies..."*, *"Ultimately, this literature..."*.

### Family 5: Formulaic Triadic Enumeration (`RISK_TRIADIC_ENUMERATION`)
- **Diagnostic:** Chronic clustering of nouns, adjectives, or clauses in three-part lists: *"theoretical, methodological, and empirical..."*, *"prices, quantities, and distribution..."*.

### Family 6: Procedural Metadiscourse Overload (`RISK_EXCESSIVE_METADISCOURSE`)
- **Diagnostic:** Narrating the research apparatus rather than the scholarly content: *"In this section we undertake a review of..."*, *"It is pertinent to observe that..."*, *"Having established X, we now examine Y"*.

### Family 7: Workflow Vocabulary Leaks (`RISK_WORKFLOW_VOCABULARY_LEAK`)
- **Diagnostic:** Internal pipeline terminology escaping into manuscript prose: `ledger`, `proposition slot`, `cluster note`, `query pack`, `CCC_`, `SRC_`, `provenance tag`, `saturation lock`.

### Family 8: Next-Paragraph Announcements (`RISK_PROSPECTIVE_ANNOUNCEMENTS`)
- **Diagnostic:** Ending paragraphs with trailer announcements of what the next paragraph will do: *"The following paragraph turns to the empirical results."*

### Family 9: Generic Buzzword Clustering (`RISK_GENERIC_BUZZWORD_CLUSTER`)
- **Diagnostic:** Over-reliance on generic academic nouns: *framework, architecture, dimension, lens, nexus, intervention, tapestry, mosaic, paradigm*.

### Family 10: Monotonous Sentence Length Distribution (`RISK_UNIFORM_SENTENCE_LENGTH`)
- **Diagnostic:** Lack of cadence variation (e.g., all sentences hovering uniformly between 22 and 26 words).

### Family 11: Monotonous Paragraph Length (`RISK_UNIFORM_PARAGRAPH_LENGTH`)
- **Diagnostic:** Blocks of paragraphs having virtually identical word and sentence counts, producing visual and cognitive fatigue.

### Family 12: Repeated Concession Templates (`RISK_REPEATED_CONCESSIONS`)
- **Diagnostic:** Predictable oscillation: *"Although X is true, nonetheless Y must be emphasized."* repeated across multiple sections.

### Family 13: Generic Novelty and Gap Rhetoric (`RISK_INFLATED_NOVELTY`)
- **Diagnostic:** Unwarranted promotional language: *"groundbreaking study"*, *"vital lacuna"*, *"unprecedented breakthrough"*, *"novel nexus"*.

### Family 14: Citation Dumping (`RISK_CITATION_DUMPING`)
- **Diagnostic:** Piling four or more unadjudicated citations at the end of a single sentence without specifying each source's exact contribution.

### Family 15: Colon-Scaffolded Lists (`RISK_COLON_LIST_CONSTRUCTION`)
- **Diagnostic:** Frequent sentences ending in colons followed by enumerated points or clauses.

### Family 16: Em-Dash Parenthetical Scaffolding (`RISK_EM_DASH_SCAFFOLDING`)
- **Diagnostic:** Excessive reliance on paired em-dashes to inject supplementary commentary into basic declarative sentences.

### Family 17: Polished but Substantively Hollow Connectives (`RISK_HOLLOW_CONNECTIVES`)
- **Diagnostic:** Smooth-sounding transitional phrases that conceal the absence of a genuine logical connection (*"Importantly, this dynamic aligns with..."*, *"Crucially, the aforementioned considerations..."*).

### Family 18: Uniform Passive Constructions (`RISK_UNIFORM_PASSIVE`)
- **Diagnostic:** Endless strings of unanchored passive verbs (*"It has been argued"*, *"It was observed"*, *"It should be noted"*).

---

## 3. Automated Detection Architecture

These 18 pattern families are evaluated deterministically by the offline Python script:
`literature-review/scripts/style_risk_auditor.py`

The auditor produces an inspectable markdown report flagging specific sentence numbers, matched trigger patterns, and actionable naturalization suggestions.
