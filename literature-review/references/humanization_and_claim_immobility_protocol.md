# Humanization and Claim-Immobility Protocol

**Specification ID:** `literature-review/references/humanization_and_claim_immobility_protocol.md`  
**Lifecycle Stage:** `L11 — DISCIPLINARY REGISTER / HUMANIZATION`, `L12 — POST-HUMANIZATION CLAIM AUDIT`  
**Governing Schema:** `literature-review/schemas/post_humanization_audit_schema.json`  

---

## 1. The Humanization Invariant

> **THE CLAIM-IMMOBILITY LAW:**  
> **HUMANIZATION MAY VARY RHETORIC, SYNTAX, AND CADENCE; IT MAY NEVER ALTER EVIDENTIARY BOUNDS.**  
>  
> Any stylistic edit that increases causal certainty, broadens empirical scope, drops an explicit qualification, adds an unledgered factual assertion, or shifts concept ownership is an **EVIDENTIARY REGRESSION**.  
>  
> **A more beautifully written sentence that strengthens an unearned claim is a FAILURE, not an improvement.**

---

## 2. Permitted vs. Forbidden Transformations

### 2.1 Permitted Transformation Classes
During the humanization and disciplinary register polishing pass, only the following seven operations are authorized:

1. **`SYNTAX`:** Re-ordering clauses, transforming voice where appropriate, or breaking overly dense compound sentences into clear statements.
2. **`RHYTHM`:** Varying sentence length distribution to create natural, engaging academic cadence.
3. **`LEXICAL_REGISTER`:** Calibrating vocabulary to match scholarly disciplinary expectations (e.g., economics terminology vs sociological terminology).
4. **`TRANSITION_COMPRESSION`:** Replacing mechanical signposting (*"Having established X, we now proceed to consider Y"*) with direct conceptual links (*"This valuation indeterminacy directly shapes observed productivity ratios"*).
5. **`CITATION_PLACEMENT`:** Integrating author names into parenthetical or narrative positions smoothly without changing chunk boundaries.
6. **`PARAGRAPH_FLOW`:** Smoothing seams between sentences so propositions follow deductive or narrative logic.
7. **`REDUNDANCY_REMOVAL`:** Eliminating unintentional repetitive phrases or duplicate qualifiers across adjacent sentences.

### 2.2 Forbidden Transformation Classes (Hard Violations)
The following seven moves are strictly prohibited:

1. **`NEW_CLAIM`:** Introducing any substantive finding or argument not warranted by a locked ledger slot.
2. **`NEW_SOURCE`:** Citing any author or publication not present in the approved corpus perimeter.
3. **`NEW_CAUSAL_DIRECTION`:** Converting correlation or association into causal determination (e.g., transforming *"X is associated with Y"* into *"X causes Y"* or *"X determines Y"*).
4. **`NEW_GENERALIZATION`:** Dropping a boundary or threshold condition (e.g., dropping *"for multi-asset steady states within a given growth regime"* to claim *"in all economies"*).
5. **`NEW_NOVELTY_CLAIM`:** Adding claims of priority, originality, or unprecedented contribution (*"first to show"*, *"novel approach"*) without human authorization.
6. **`SOURCE_OWNERSHIP_CHANGE`:** Attributing the author's own metric or reformulation to an external source, or taking credit for an external author's theorem.
7. **`QUALIFICATION_DELETION`:** Removing explicit caveats, error bounds, or negative boundaries (`Does NOT Establish`).

---

## 3. Mandatory Post-Humanization Claim-Immobility Audit

Every humanized manuscript paragraph must undergo a sentence-by-sentence claim-immobility audit before it may be presented to the human author for final ratification.

### 3.1 Sentence-by-Sentence Classification
Each sentence is evaluated and classified into one of four mutually exclusive statuses:

1. **`SUPPORTED`:** The sentence expresses a substantive proposition that directly maps to one or more approved Paragraph Ledger slots and satisfies all qualification checks.
2. **`TRANSITION`:** The sentence connects substantive units without asserting new empirical or theoretical claims.
3. **`PURE_RHETORICAL_CONNECTIVE`:** The sentence serves an introductory, clarifying, or framing purpose without introducing facts or evidence.
4. **`UNSUPPORTED`:** The sentence introduces an empirical fact, theoretical claim, or causal link that lacks a corresponding locked ledger slot.

> **AUDIT GATE VERDICT:**  
> If even ONE sentence is classified as **`UNSUPPORTED`**, the entire paragraph **FAILS** the audit.  
> Execution must halt or revert to bounded local repair.

### 3.2 The Claim-Strengthening Detection Checklist
For every `SUPPORTED` sentence, the auditor runs five specific comparative checks against the underlying Staged Prose sentence:
- [ ] **Causal Direction Check:** Did verbs shift from descriptive/suggestive to definitive/causal?
- [ ] **Quantifier Check:** Did qualifiers shift (e.g., *"often"* $\to$ *"always"*, *"some"* $\to$ *"all"*)?
- [ ] **Prohibited Claim Check:** Does the sentence touch or cross the `prohibited_stronger_claim` boundary?
- [ ] **Attribution Check:** Is the citation attached to the exact claim supported by the primary source?
- [ ] **Qualification Check:** Are all necessary caveats intact?
