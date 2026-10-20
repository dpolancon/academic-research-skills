# PARAGRAPH LEDGER: {{PARAGRAPH_ID}} — {{TITLE}}

**Paragraph ID:** `{{PARAGRAPH_ID}}`  
**Paragraph Theme:** {{PARAGRAPH_THEME}}  
**Governing Clusters:** `{{CLUSTER_LIST}}`  
**Governing Contracts:** `{{CONTRACT_LIST}}`  
**Human Gate Status:** `{{STATUS}}` <!-- DRAFT | PROPOSED | RATIFICATION_READY | LOCK -->  
**Target Section:** {{MANUSCRIPT_SECTION}}  

---

## 1. Paragraph Function & Architectural Context
{{PARAGRAPH_FUNCTION_EXPLANATION}}

---

## 2. Upstream Saturated Evidence Perimeter

| Evidence Artifact | Saturation Status | Role in {{PARAGRAPH_ID}} | Gate Status |
|---|---|---|---|
| `SRC_{{KEY_1}}` | `EXTRACTION_SATURATED` | {{ROLE_1}} | `LOCK` |
| `CLUS_{{KEY_1}}` | `ADJUDICATION_SATURATED` | {{CLUSTER_CHUNK_ROLE}} (`CCC_{{KEY}}_01`) | `LOCK` |
| `SYNTH_{{KEY}}_HINGE` | `RATIFIED_HINGE` | {{HINGE_ROLE}} | `LOCK` |

---

## 3. Proposition Slots Ledger

| Slot ID | Proposition Statement | Provenance Class | Primary Warrant / Locators | Prohibited Stronger Claim | Scholarly Status |
|---|---|---|---|---|---|
| **{{PARAGRAPH_ID}}.S1** | {{PROPOSITION_1}} | `AUTHORIAL_SYNTHESIS` | `AUTH_PAPER_GOVERNANCE` | Do NOT {{PROHIBITION_1}} | `LOCK` |
| **{{PARAGRAPH_ID}}.S2** | {{PROPOSITION_2}} | `DIRECT_SOURCE_CLAIM` | `SRC_{{KEY_1}}` (pp. {{LOCATORS}}) | Do NOT {{PROHIBITION_2}} | `LOCK` |
| **{{PARAGRAPH_ID}}.S3** | {{PROPOSITION_3}} | `ADJUDICATED_CROSS_LITERATURE_HINGE` | `CCC_{{KEY}}_01` / `SRC_A`, `SRC_B` | Do NOT {{PROHIBITION_3}} | `LOCK` |
| **{{PARAGRAPH_ID}}.S4** | {{PROPOSITION_4}} | `TRANSITION` | Transition to {{NEXT_PARAGRAPH}} | Do NOT {{PROHIBITION_4}} | `LOCK` |

---

## 4. Human Invariants & Explicit Prohibitions
1. **Provenance Discipline:** Single-author claims must never be misclassified as cross-literature hinges.
2. **Concept Ownership:** External literature warrants empirical/theoretical context, but does not own current manuscript constructs.
3. **Negative Boundaries:** Explicit limits of what is *not* proved must be strictly preserved during downstream prose generation.

---

## 5. Human Sovereignty Gate
- [x] Assembled strictly from saturated source notes and ratified cluster contracts.
- [x] Zero unlogged backend queries executed.
- [x] Proposition slots audited against primary text anchors.
- [ ] **HUMAN RATIFICATION GATE:** Recommended Status $\longrightarrow$ **`LOCK`**
