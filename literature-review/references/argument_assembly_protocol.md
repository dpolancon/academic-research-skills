# Argument Assembly Protocol

**Specification ID:** `literature-review/references/argument_assembly_protocol.md`  
**Lifecycle Stage:** `L7 — ARGUMENT ASSEMBLY`  
**Governing Schema:** `literature-review/schemas/argument_assembly_schema.json`  

---

## 1. Epistemic Role of Argument Assembly

The central defect of naive, prompt-driven literature reviews is jumping directly from raw notes or proposition ledgers to drafted prose. This creates severe scholarly hazards:
1. **Unearned Weaving:** Distinct literature traditions are conflated simply because they appear in the same paragraph.
2. **Hidden Rhetorical Drift:** Sentences are ordered for stylistic cadence rather than logical necessity.
3. **Citation Collapsing:** Citations are lumped together at sentence ends, creating unearned joint claims.
4. **Metadiscourse Creep:** The text narrates the research process rather than developing the scholarly argument.

**Argument Assembly** is a dedicated, first-class intermediate representation between the **Paragraph Ledger** ($L_6$) and **Staged Academic Prose** ($L_8$).

```
[PARAGRAPH LEDGER]
"What may be claimed?"
       ↓
[ARGUMENT ASSEMBLY]
"Why is each claim here? In what order?
 How may sources be related? What must remain separate?"
       ↓
[STAGED PROSE]
"What is the simplest scholarly expression with boundaries stabilized?"
       ↓
[MANUSCRIPT PROSE]
"How should this author/project actually express it?"
```

> **CORE INVARIANT: ARGUMENT ASSEMBLY IS NOT PROSE.**  
> It does not draft flowing paragraphs. It defines the architectural, relational, and rhetorical choreography that will govern subsequent prose generation.

---

## 2. Required Core Dimensions

Every Argument Assembly unit must formally specify the following dimensions:

### 2.1 The Argumentative Job & Strategic Placement
- **`unit_id`:** Unique identifier (e.g., `P01`, `P02`).
- **`argumentative_job`:** The exact functional burden this unit bears in the overarching paper spine (e.g., "Establish capital heterogeneity as an accounting valuation problem rather than an engineering primitive").
- **`reason_for_inclusion`:** Why the paper requires this specific argumentative move rather than omitting it or jumping directly to the next point.
- **`incoming_dependency`:** The upstream concepts, metrics, or empirical facts that must already be established for this unit to make sense.

### 2.2 Claim Ordering & Hierarchy
- **`opening_move`:** The conceptual entry point that anchors the paragraph.
- **`foreground_claims`:** The primary propositions (derived from the Paragraph Ledger) that must carry the main argumentative weight.
- **`subordinate_claims`:** Secondary, qualifying, or contextual claims.
- **`internal_claim_order`:** The strict logical sequence of claims (e.g., $[S_1 \to S_2 \to S_4 \to S_3 \to S_5]$), ensuring deductive or evidentiary progression.

### 2.3 Relational Choreography: Weaving vs. Separation
- **`cross_literature_weave_decisions`:** Explicit authorizations to connect authors or traditions. Every weave MUST reference a ratified **Comparative Citation Contract** (`CCC_*`) or **Adjudicated Hinge** (`SYNTH_*`). Without an explicit hinge, interweaving is strictly prohibited.
- **`do_not_weave_boundaries`:** Explicit negative boundaries identifying distinct traditions, metrics, or authors that appear in the unit but must NOT be blended or equated (e.g., "Keep Harcourt plant-level appraisal distinct from Robinson macro aggregation").

### 2.4 Citation Choreography & Ownership
- **`citation_choreography`:** Exact rules for where citations attach. Forbids citation dumping. Specifies whether joint parenthetical citations `(Author A, Year; Author B, Year)` are permitted or if separate attribution is required.
- **`source_ownership_boundaries`:** Maps concepts to their governing authority:
  - *External Literature Authority:* The cited author owns the concept/finding.
  - *Internal Methodological Authority:* The author's foundational monograph/dissertation governs method provenance.
  - *Current Manuscript Ownership:* The current paper claims ownership of the analytical adaptation or empirical contribution.

### 2.5 Discipline & Safeguards
- **`required_qualifications`:** Caveats, scope conditions, or empirical bounds that must accompany specific claims.
- **`terminology_to_preserve`:** Author-specific or mathematically precise terminology that must not be paraphrased into generic synonyms.
- **`terms_to_avoid`:** Conflating, unearned, or misleading phrases forbidden in the unit.
- **`prohibited_stronger_argument`:** The forbidden overclaim that prose drafters might be tempted to make (e.g., "Do not claim capital aggregation is mathematically impossible in national accounting").
- **`evidence_lock_references`:** Durable references to ratified ledger slots and cluster contracts.

---

## 3. Lifecycle Status & Transitions

Argument Assembly units move through standardized states:
1. `DRAFT`: Initial architectural proposal.
2. `PROPOSED`: Fully populated and checked against governing ledger slots.
3. `RATIFICATION_READY`: All boundaries, hinge warrants, and citation choreographies verified.
4. `LOCK`: Human author has explicitly ratified the unit.

Transition to `L8 STAGED PROSE` is permitted only when the Argument Assembly unit is at `RATIFICATION_READY` or `LOCK`.
