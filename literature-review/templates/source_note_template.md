# CANONICAL SOURCE NOTE: {{AUTHOR_YEAR}}

**Source Key:** `SRC_{{KEY}}`  
**Bibliographic Key:** `{{BIB_KEY}}`  
**Full Citation:** {{FULL_CITATION}}  
**File:** `{{LOCAL_PATH}}`  
**SHA-256:** `{{SHA256}}`  
**NotebookLM Source ID:** `{{NOTEBOOKLM_SOURCE_ID}}`  
**Source Tier:** `{{SOURCE_TIER}}` (`TIER_A_CORE` / `TIER_B_SUPPORTING` / `TIER_C_CONTEXTUAL`)  
**Assigned Query Packs:** `{{ASSIGNED_QUERY_PACKS}}`  
**Ingestion Status:** `{{INGESTION_STATUS}}`  
**Saturation Status:** `{{SATURATION_STATUS}}` (`EXTRACTION_SATURATED` / `IN_PROGRESS`)  
**Adjudication Date:** {{DATE}}  

---

## 1. Identity & Bibliographic Context
- **Author:** {{AUTHOR}}
- **Institutional Context:** {{INSTITUTION}}
- **Core Research Question:** {{CORE_QUESTION}}

---

## 2. Authority & Project Role (Loop A & Loop C)
- **Authority Class:** `EXTERNAL_LITERATURE` / `INTERNAL_METHODOLOGY` / `DATASET_IMPLEMENTATION`
- **Source Tier:** `{{SOURCE_TIER}}`
- **Project Literature Role:** `THEME_{{THEME}}`
- **Downstream Reuse Targets:** {{DOWNSTREAM_THEMES_AND_PARAGRAPHS}}

---

## 3. Atomic Question Responses (Unpacked from Assigned Query Packs)

### {{QUESTION_ID}} ({{QUERY_PACK_ID}}) — {{QUESTION_TITLE}}
- **Status:** `EXPLICIT / PARTIAL / NOT LOCATED`
- **Answer:** {{ANSWER_TEXT}}
- **Author Terminology:** {{EXACT_AUTHOR_TERMS}}
- **Evidence Anchor:**
  > "{{ANCHOR_QUOTE}}" ({{SECTION_OR_PAGE}}, chunk `{{CHUNK_ID}}`)
- **Page / Section:** {{PAGE_OR_SECTION}}
- **Qualification / Nuance:** {{QUALIFICATIONS}}
- **Does NOT Establish:** {{NEGATIVE_BOUNDARIES}}

---

## 4. Source-Specific Issues Discovered ($Q_{\text{source}}$ Feedback to Question Bank)
- {{UNANTICIPATED_ISSUE_1}}
- {{UNANTICIPATED_ISSUE_2}}

---

## 5. Candidate Cross-Source Relations & Secondary Citations
- **{{COMPARATOR_SOURCE}}:** {{PROPOSED_RELATION}} (`ADJUDICATED CROSS-LITERATURE HINGE` / `THEMATIC RESONANCE ONLY`)

### 5.1 Referenced Literature / Citations Within Source (Mediated Attribution Only)
- **{{SECONDARY_AUTHOR_YEAR}}:** Cited on p. {{PAGE}} for {{TOPIC}} (`candidate_references_ledger.md`). Permitted in prose **only** via mediated attribution (`{{SECONDARY_AUTHOR_YEAR}}, cited in {{AUTHOR_YEAR}}`).

---

## 6. Extraction Saturation & Provenance Audit Trail
- [x] Every assigned atomic question has `EXPLICIT`, `PARTIAL`, or `NOT LOCATED`.
- [x] Verbatim quotes, chunk IDs, and page/section anchors recorded.
- [x] Exact author terminology preserved.
- [x] Negative boundaries (`Does NOT Establish`) recorded.
- [x] Legacy discovery notes cross-checked (`CONFIRMED` / `NARROWED` / `EXPANDED` / `CONFLICT` / `OUT OF SCOPE`).
- **Primary Text Inspected:** `{{LOCAL_PATH}}`
- **Query Packs Executed:** `{{ASSIGNED_QUERY_PACKS}}`
- **Saturation Lock:** `EXTRACTION_SATURATED` (Do NOT re-query by default; requires Exception Trigger A–F).
