# ARS Design Note: The Governed Evidence-to-Prose Pipeline
## `LEDGER → ARGUMENT ASSEMBLY → STAGED PROSE → MANUSCRIPT PROSE`

- **Document ID:** `docs/design/2026-10-20-literature-review-consolidation/02_DESIGN_NOTE_LEDGER_TO_PROSE.md`
- **Date:** 2026-10-20
- **Status:** RATIFIED ARCHITECTURAL SPECIFICATION

---

## 1. The Core Architectural Problem

In naive LLM-assisted scholarly writing, prompts typically instruct the model: *"Here are my sources/notes; write a literature review section."*

This unstructured leap produces four catastrophic scholarly failure modes:
1. **Unearned Weaving:** Authors from distinct traditions are casually blended in compound sentences simply because they share a broad topic, erasing theoretical disagreements.
2. **Hidden Rhetorical Drift:** Claims are subtly strengthened, broadened, or modified to fit the rhythmic flow or dramatic cadence of the prose.
3. **Citation Collapsing:** Citations are lumped together at sentence ends, creating false impressions of consensus and obscuring which author demonstrated what.
4. **Metadiscourse Inflation:** The text fills with empty procedural announcements (*"In this section we examine..."*, *"Taken together, it is important to observe..."*) rather than substantive argumentation.

To eliminate these hazards, the ARS Literature Review Architecture decomposes the transition from evidence to prose into **four discrete, governed intermediate representations**.

---

## 2. The Four Governed Layers

```
========================================================================================
LAYER                         CORE QUESTION ANSWERED                GOVERNING SCHEMA
========================================================================================
L6: PARAGRAPH LEDGER          What may be claimed?                  paragraph_ledger_schema.json
L7: ARGUMENT ASSEMBLY         Why here? What order? What separate?  argument_assembly_schema.json
L8: STAGED ACADEMIC PROSE     What is the simplest bounded form?    staged_prose_schema.json
L9: MANUSCRIPT PROSE          How should the author express it?     manuscript_prose_contract_schema.json
========================================================================================
```

### Layer 1: Paragraph Ledger ($L_6$) — *What May Be Claimed?*
- **Role:** Pure proposition inventory.
- **Content:** An array of proposition slots ($S_1 \dots S_n$). Each slot contains an atomic proposition, an explicit provenance class (`DIRECT SOURCE CLAIM`, `AUTHORIAL SYNTHESIS`, `ADJUDICATED CROSS-LITERATURE HINGE`, `TRANSITION`), primary warrants with page locators, and a mandatory `prohibited_stronger_claim`.
- **Discipline:** It defines the epistemic ceiling. No claim outside the ledger may ever appear downstream.

### Layer 2: Argument Assembly ($L_7$) — *Why Here, In What Order, and What Must Remain Separate?*
- **Role:** Architectural choreography.
- **Content:** Argumentative job, reason for inclusion, incoming dependencies, opening move, claim sequence, permitted cross-literature weave decisions, strict do-not-weave boundaries, citation choreography, concept ownership demarcations, required qualifications, and terms to avoid.
- **Discipline:** **ARGUMENT ASSEMBLY IS NOT PROSE.** It does not draft sentences; it establishes the logical, relational, and rhetorical rules that govern sentence production.

### Layer 3: Staged Academic Prose ($L_8$) — *What Is the Simplest Bounded Expression?*
- **Role:** Evidentiary stabilization and inspectability.
- **Content:** Plain, direct subject-verb-object declarative sentences. Explicit attribution where necessary. Zero decorative ornament, zero synonym games, zero signposting.
- **Discipline:** **STAGED PROSE IS NOT PUBLICATION PROSE.** Its purpose is transparency. Every caveat, boundary, and citation sits plainly in view, allowing deterministic verification before stylistic tailoring.

### Layer 4: Manuscript Prose ($L_9$) — *How Should the Author Actually Express It?*
- **Role:** Publication-grade text adapted to target disciplinary registers.
- **Content:** Flowing academic prose integrating natural cadence, varied sentence lengths, syntactic compression, and disciplinary phrasing.
- **Discipline:** Governed by the **Claim-Immobility Law**. Stylistic polishing may adapt syntax and rhythm, but may NEVER invent claims, add evidence, strengthen causality, or delete qualifications.

---

## 3. Why Intermediate Representations Insulate Scholarly Sovereignty

By separating *evidentiary validity* ($L_6$) from *argumentative choreography* ($L_7$), *boundary stabilization* ($L_8$), and *stylistic polishing* ($L_9$), the pipeline creates complete transparency:
- If a sentence sounds unnatural, the author polishes the stylistic layer ($L_9$) without re-interrogating sources.
- If a sentence makes an unearned claim, the auditor checks the staged prose ($L_8$) and ledger ($L_6$) to pinpoint exactly where the drift occurred.
- If distinct authors are incommensurate, the Argument Assembly ($L_7$) prevents them from ever being woven together in prose.

This guarantees that stylistic elegance never comes at the expense of scholarly integrity.
