# CLUSTER NOTE: {{CLUSTER_TITLE}}

**Cluster Key:** `CLUS_{{KEY}}`  
**Saturation Status:** `ADJUDICATION_SATURATED` / `IN_PROGRESS`  
**Literature Theme:** `THEME_{{THEME}}`  
**Date:** {{DATE}}  

---

## 1. Cluster Definition & Analytical Scope
{{DEFINITION_OF_THE_CLUSTER_LITERATURE_DOMAIN}}

---

## 2. Comparative Evidence Matrix (Source $\times$ Atomic Question)

| Source Key | Author & Year | `{{Q_ID_1}}` ({{Q_TOPIC_1}}) | `{{Q_ID_2}}` ({{Q_TOPIC_2}}) | `{{Q_ID_3}}` ({{Q_TOPIC_3}}) | Key Methodological / Scope Divergence |
|---|---|---|---|---|---|
| `SRC_{{KEY_1}}` | {{AUTHOR_1}} | {{CELL_1_1}} (p. {{P}}) | {{CELL_1_2}} (p. {{P}}) | {{CELL_1_3}} (p. {{P}}) | {{DIVERGENCE_1}} |
| `SRC_{{KEY_2}}` | {{AUTHOR_2}} | {{CELL_2_1}} (p. {{P}}) | {{CELL_2_2}} (p. {{P}}) | {{CELL_2_3}} (p. {{P}}) | {{DIVERGENCE_2}} |
| `SRC_{{KEY_3}}` | {{AUTHOR_3}} | {{CELL_3_1}} (p. {{P}}) | {{CELL_3_2}} (p. {{P}}) | {{CELL_3_3}} (p. {{P}}) | {{DIVERGENCE_3}} |

---

## 3. Citation-Chunk Contracts (Hard Lock: Cluster Membership $\neq$ Common Claim Membership)

### CITATION_CHUNK_CONTRACT: `CHUNK_{{KEY}}_001`
- **Candidate Proposition:** "{{CANDIDATE_COMMON_CLAIM}}"
- **Source-by-Source Support:**
  - `SRC_{{KEY_1}}` ({{AUTHOR_1}}): {{SUPPORT_1}} (`{{Q_ID_1}}`, p. {{PAGE_1}})
  - `SRC_{{KEY_2}}` ({{AUTHOR_2}}): {{SUPPORT_2}} (`{{Q_ID_1}}`, p. {{PAGE_2}})
  - `SRC_{{KEY_3}}` ({{AUTHOR_3}}): {{SUPPORT_3}} (`{{Q_ID_1}}`, p. {{PAGE_3}})
- **Common Denominator:** {{GENUINELY_SHARED_INTERSECTION}}
- **Meaningful Internal Differences:** {{INTERNAL_DISAGREEMENTS_OR_SCOPE_VARIATIONS}}
- **Permitted Citation Chunk:** `({{AUTHOR_1}}; {{AUTHOR_2}}; {{AUTHOR_3}})` — *Permitted ONLY for the Common Denominator proposition above.*
- **Excluded Members When Proposition Narrows:**
  - Exclude `SRC_{{KEY_3}}` ({{AUTHOR_3}}) when claiming "{{NARROWED_CLAIM}}" because {{EXCLUSION_REASON}}.
- **Prohibited Stronger Formulation (Overclaim Guardrail):**
  - DO NOT cite `({{AUTHOR_1}}; {{AUTHOR_2}}; {{AUTHOR_3}})` together to claim "{{PROHIBITED_OVERCLAIM}}".

---

## 4. Adjudication Saturation Checklist
- [x] Bounded common propositions identified.
- [x] Meaningful internal differences tabulated in Comparative Evidence Matrix.
- [x] Terminology conflicts explicitly mapped across authors.
- [x] Source-by-source support verified against `EXTRACTION-SATURATED` source notes.
- [x] Permissible citation chunks and narrowed exclusions locked in `CITATION_CHUNK_CONTRACT`.
- [x] Prohibited collective overclaims explicitly listed.
- **Saturation Lock:** `ADJUDICATION_SATURATED` (Do NOT rerun comparative cluster queries unless Exception Trigger B or F applies).
