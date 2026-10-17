---
name: literature-review
description: Modular, grounded, source-and-cluster-first literature review workflow powered by replaceable extraction backends (e.g., NotebookLM), iterative question banks, query packs, canonical source notes, comparative cluster matrices, citation-chunk contracts, synthesis hinges, and paragraph ledgers.
version: 1.1.0
author: Diego Polanco / Antigravity
---

# Literature Review Skill (Source- & Cluster-First Grounded Architecture)

## Overview
This skill provides a rigorous, auditable, and pass-efficient workflow for producing academic literature reviews grounded in primary texts. It eliminates paragraph-by-paragraph source re-interrogation by operating extraction at the **Source Level** (via bundled **Query Packs**) and the **Cluster / Comparative Level** (via **Comparative Evidence Matrices** and **Citation-Chunk Contracts**). Manuscript paragraphs ($P_1 \dots P_J$) are downstream consumers of a saturated local evidence vault.

## Core Production Workflow
```
PROJECT GOVERNANCE / AUTHORITY MAP (Loop A)
        ↓
CORPUS REGISTRY + SOURCE TIERING (Tiers A, B, C, D)
        ↓
ITERATIVE QUESTION BANK (Loop B: Q_project ∪ Q_legacy ∪ Q_source)
        ↓
QUERY PACKS (Execution Bundles over Atomic Question IDs)
        ↓
SOURCE PASSES (Loop C: Bounded Extraction)
        ↓
CANONICAL SOURCE NOTES (EXTRACTION-SATURATED)
        ↓
CLUSTER PASSES (Loop D: Comparative Extraction)
        ↓
COMPARATIVE EVIDENCE MATRICES
        ↓
CLUSTER NOTES + CITATION-CHUNK CONTRACTS (ADJUDICATION-SATURATED)
        ↓
SYNTHESIS / HINGE NOTES
        ↓
PARAGRAPH LEDGERS P1...PJ (Loop E)
        ↓
HUMAN RATIFICATION GATE
        ↓
MANUSCRIPT PROSE
```
*Exception Loop:* After source/cluster saturation, the extraction backend may re-enter **only** via a formally logged **Exception Query** (Triggers A–F), which updates the canonical source or cluster note before consumption in a paragraph ledger.

---

## The Five Interacting Loops

### Loop A — Governance & Authority Map (`00_contract/`)
Routes claims to their canonical source of truth without sending internal project authorities through external-literature validation loops:
- **External Literature Claims (`TIER_A` / `TIER_B` / `TIER_C`):** Original primary text.
- **Author Methodological Reformulation (`TIER_D_INTERNAL_AUTHORITY`):** Project's foundational methodology text/monograph.
- **Executable Data / Code Implementation (`TIER_D_INTERNAL_AUTHORITY`):** Active data/code repository.
- **Paper Analytical Architecture (`TIER_D_INTERNAL_AUTHORITY`):** Ratified project design and empirical contracts.

### Loop B — Iterative Question Discovery & Query Packs (`02_questions/`)
Maintains an iterative Question Bank combining three streams:
$$Q_{\text{bank}} = Q_{\text{project}} \cup Q_{\text{legacy}} \cup Q_{\text{source}}$$
- **Atomic Question IDs (`Q_XXX_001`):** Irreducible unit of provenance; every extracted answer maps to an atomic ID.
- **Query Packs (`QP_<FAMILY>`):** Execution bundles grouping related atomic questions so a source can be interrogated in 1–2 bounded passes.

### Loop C — Source Extraction & Saturation (`01_corpus/`, `03_source_notes/`)
Schedules interrogation depth using **Source Tiers**:
- **`TIER_A_CORE`:** Supports multiple themes/sections; receives comprehensive Query Packs (1–2 passes).
- **`TIER_B_SUPPORTING`:** Serves one primary theme or cluster; receives targeted Query Packs (1 pass).
- **`TIER_C_CONTEXTUAL`:** Serves bounded contextual framing; receives lightweight identity + targeted claim pack (1 pass).
- **`TIER_D_INTERNAL_AUTHORITY`:** Internal authority; exempt from external extraction loops.

A source note (`SRC_<KEY>.md`) reaches **`EXTRACTION-SATURATED`** when all assigned atomic questions hold `EXPLICIT`, `PARTIAL`, or `NOT LOCATED` with verbatim anchors, preserved author terminology, and explicit negative boundaries (`Does NOT Establish`). Once saturated, default re-querying is locked.

### Loop D — Cluster Comparative Matrices, Citation-Chunk Contracts & Synthesis (`04_cluster_notes/`, `05_synthesis_notes/`)
- **Comparative Evidence Matrix:** Cross-tabulates saturated source notes (and bounded multi-source comparative passes when needed) across shared atomic questions.
- **Citation-Chunk Contract (`CITATION_CHUNK_CONTRACT`):** Enforces `Cluster Membership ≠ Common Claim Membership`. Specifies source-by-source support, common denominator, internal divergences, permitted joint citation strings `(Author1, Year; Author2, Year)`, excluded members when claims narrow, and prohibited overclaims.
- **`ADJUDICATION-SATURATED`:** Reached when all common propositions, divergences, and citation chunks for a cluster are locked.
- **Synthesis / Hinge Notes (`SYNTH_<KEY>.md`):** Adjudicates connections across distinct literature traditions against 4 criteria: (1) Conceptual Proximity, (2) Interpretive Value, (3) Non-Inflationary Boundary, and (4) Paragraph Necessity.

### Loop E — Manuscript Ledgers, Exception Queries & Recalibrated Human Gates (`06_paragraph_ledgers/`)
- **Paragraph Ledgers (`LEDGER_P<XX>.md`):** Map every planned sentence to provenance tags (`DIRECT SOURCE CLAIM`, `CLUSTER CITATION CHUNK`, `ADJUDICATED CROSS-LITERATURE HINGE`, `AUTHORIAL SYNTHESIS`, `TRANSITION`).
- **Exception Query Protocol:** Backend re-entry is allowed **only** under Triggers A–F (`REQUIRED_CLAIM_NOT_LOCATED`, `CONFLICT`, `PROVENANCE_GAP`, `CLAIM_EXCEEDS_NOTE`, `ATTRIBUTION_AMBIGUITY`, `NEW_QUESTION`) and must update the durable `SRC_*` or `CLUS_*` note first.
- **Recalibrated Human Gates:** Human ratification is concentrated at consequential checkpoints: (1) Cluster/Citation-Chunk Adjudication, (2) Novel Synthesis Hinges, (3) Paragraph Ledgers, (4) Manuscript Prose Insertion, and (5) Contribution/Novelty Claims.

---

## Optimization Metrics & Regression Fixture
Tracks efficiency subject to strict grounding and negative-boundary preservation:
- **Source Reuse ($R_{\text{source}}$):** Downstream themes/ledgers served per canonical source pass.
- **Query Reuse ($R_{\text{query}}$):** Downstream claims/matrix cells populated per query pack execution.
- **Cluster Reuse ($R_{\text{cluster}}$):** Citation chunks/hinges/ledgers served per cluster pass.
- **Exception Rate ($E_{\text{rate}}$):** Exception queries divided by total paragraph ledgers.
- **Requery Rate ($Q_{\text{re}}$):** Saturated sources re-queried divided by total saturated sources.
- **Regression Fixture Validation:** Any workflow update must reproduce existing gold-standard calibration ledgers (e.g., `P01`) purely from canonical source and synthesis notes without new paragraph-specific extraction passes.

## Replaceable Backend Adapter
External extraction is mediated via an abstract `ExtractionBackend` interface in `scripts/notebooklm_adapter.py` (with `NotebookLMAdapter` as the default implementation). Durable scholarly state lives exclusively in local version-controlled Markdown, CSV, JSON, and YAML artifacts.
