# PARAGRAPH LEDGER: {{PARAGRAPH_ID}} — {{TITLE}}

**Paragraph ID:** `{{PARAGRAPH_ID}}`  
**Status:** `EVIDENCE LEDGER RATIFIED — PAUSED AT HUMAN GATE`  
**Date:** {{DATE}}  
**Manuscript Section:** {{SECTION}}  
**Reader Question:** {{READER_QUESTION}}  
**Prose Drafting Status:** `DO NOT DRAFT (Awaiting Human Ratification)`  

---

## 1. Paragraph Function & Architectural Context
{{EXPLANATION_OF_PARAGRAPH_ROLE}}

---

## 2. Evidence Perimeter

| Evidence Artifact | Role in {{PARAGRAPH_ID}} | Admissibility Status |
|---|---|---|
| `SRC_{{KEY_1}}` | {{ROLE_1}} | `LOCK` |
| `SRC_{{KEY_2}}` | {{ROLE_2}} | `LOCK` |
| `SYNTH_{{KEY}}_HINGE` | {{HINGE_ROLE}} | `LOCK` |

---

## 3. Sentence-Level Claim & Evidence Ledger

| Sentence Plan | Core Claim Content | Provenance Label | Source Grounding | Boundary / Exclusion |
|---|---|---|---|---|
| **S1 (Opener)** | {{CLAIM_1}} | `AUTHORIAL SYNTHESIS` / `TRANSITION` | {{GROUNDING_1}} | {{BOUNDARY_1}} |
| **S2 (Primary Claim)** | {{CLAIM_2}} | `DIRECT SOURCE CLAIM` | `SRC_{{KEY_1}}` (p. {{PAGE}}) | {{BOUNDARY_2}} |
| **S3 (Supporting Claim)**| {{CLAIM_3}} | `DIRECT SOURCE CLAIM` | `SRC_{{KEY_2}}` (p. {{PAGE}}) | {{BOUNDARY_3}} |
| **S4 (Hinge Claim)** | {{CLAIM_4}} | `ADJUDICATED CROSS-LITERATURE HINGE` | `SYNTH_{{KEY}}_HINGE` | {{BOUNDARY_4}} |
| **S5 (Closer/Transition)**| {{CLAIM_5}} | `TRANSITION` | {{TRANSITION_LOGIC}} | {{BOUNDARY_5}} |

---

## 4. Negative Guardrails for Manuscript Drafting
- [ ] {{GUARDRAIL_1}}
- [ ] {{GUARDRAIL_2}}
- [ ] {{GUARDRAIL_3}}

---

## 5. Human Gate Check
- [x] Canonical source notes verified and locked.
- [x] Adjudicated hinge verified and locked.
- [x] Sentence ledger audited against primary text.
- [ ] **HUMAN RATIFICATION GATE:** Awaiting explicit user approval before drafting manuscript prose.
