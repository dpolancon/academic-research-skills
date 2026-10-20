# Manuscript Prose Adaptation Protocol

**Specification ID:** `literature-review/references/manuscript_prose_protocol.md`  
**Lifecycle Stage:** `L9 — MANUSCRIPT PROSE`  
**Governing Schema:** `literature-review/schemas/manuscript_prose_contract_schema.json`  

---

## 1. The Governed Transformation Equation

Manuscript prose is the final publication-ready text integrated into the target paper. It is generated through a deterministic, governed transformation:

$$\begin{aligned}
\text{Manuscript Prose} = \mathcal{T}(&\text{Locked Ledgers } [L_6], \\
&\text{Argument Assembly } [L_7], \\
&\text{Staged Prose } [L_8], \\
&\text{Local Manuscript Context}, \\
&\text{Project / Author Register})
\end{aligned}$$

---

## 2. Permitted Adaptations (Rhetorical & Stylistic Space)

During the transformation from Staged Prose to Manuscript Prose, the author/agent is permitted to perform the following stylistic operations:

1. **Syntactic Compression:** Consolidate redundant introductory clauses and trim unnecessary exposition.
2. **Sentence Combination:** Merge two closely linked staged sentences into a compound or complex periodic sentence to improve rhythm and flow.
3. **Natural Citation Integration:** Embed parenthetical citations seamlessly into the narrative cadence (e.g., converting `"Robinson asserts X. Robinson (1953)"` into `"As Robinson (1953) demonstrates, X"`).
4. **Disciplinary Register Alignment:** Calibrate sentence rhythm, transition words, and terminology to match target publication venues (e.g., Top-5 Economics, Cambridge Journal of Economics, Heterodox Review).
5. **Cadence Variation:** Vary sentence length and clause structures naturally to avoid monotonous rhythmic pacing.
6. **Local Contextual Weaving:** Smooth the seams between the current unit and surrounding paragraphs in the active manuscript section.

---

## 3. Strict Negative Boundaries (Forbidden Transformations)

Under NO circumstances may stylistic adaptation violate evidentiary boundaries. The following moves are strictly prohibited:

```text
========================================================================
FORBIDDEN TRANSFORMATION                        REASON FOR HARD REJECTION
========================================================================
1. Invent New Claims                            Breaks ledger authority
2. Add Unwarranted Evidence                     Violates corpus perimeter
3. Strengthen Causal Language                   Alters empirical epistemic status
   (e.g., "suggests" -> "proves")
4. Weaken or Delete Qualifications              Violates negative boundary
5. Shift Source Ownership                       Fails provenance audit
   (e.g., attributing paper metric to cited source)
6. Inject Unearned Novelty Claims               Infringes human-sovereign gate
   (e.g., "groundbreaking", "first time")
7. Alter Contribution Hierarchy                 Distorts paper analytical spine
========================================================================
```

---

## 4. The Sentence-Level Provenance Mapping Rule

Every sentence in the final manuscript prose must maintain an unbroken traceable mapping back to:
1. The corresponding **Staged Prose sentence index**;
2. The governing **Paragraph Ledger slot ID** ($S_1, S_2, \dots$);
3. The governing **Argument Assembly move ID**.

If a newly drafted manuscript sentence cannot be mapped back to a locked ledger slot or classified as an authorized rhetorical connective, execution MUST halt for human review.
