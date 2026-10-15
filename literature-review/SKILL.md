---
name: literature-review
description: Modular, grounded, question-driven literature review workflow powered by NotebookLM extraction, canonical source notes, cluster notes, synthesis notes, and paragraph ledgers.
version: 1.0.0
author: Diego Polanco / Antigravity
---

# Literature Review Skill (Grounded, Traceable, Question-First)

## Overview
This skill provides a rigorous, auditable, and modular workflow for producing academic literature reviews grounded directly in primary texts via Google NotebookLM. It avoids generic summaries, prevents hallucinated consensus, enforces strict source attribution at the sentence or clause level, and controls cross-literature interweaving through formal hinge adjudication.

## Core Canonical Workflow
$$\text{PROJECT CONTRACT} \longrightarrow \text{CORPUS REGISTRY} \longrightarrow \text{QUESTION BANK} \longrightarrow \text{QUESTION} \times \text{SOURCE MATRIX}$$
$$\longrightarrow \text{CANONICAL SOURCE NOTES} \longrightarrow \text{CLUSTER NOTES} \longrightarrow \text{SYNTHESIS NOTES} \longrightarrow \text{PARAGRAPH LEDGER} \longrightarrow \text{HUMAN RATIFICATION} \longrightarrow \text{PROSE}$$

## Architecture Components

### 1. Project Contract (`00_contract/`)
Defines:
- Epistemic boundaries and paper-specific contribution hierarchy.
- Authority hierarchy (External literature vs Author methodological formulation vs Executable data implementation vs Paper analytical use).
- Negative prohibitions and conceptual guardrails.

### 2. Corpus Registry (`01_corpus/`)
Maintains a reproducible, Git-diffable registry of all approved documents:
- Source key, filename, bibliographic key, author, year, file hash (SHA-256), NotebookLM source ID, authority class, literature role, readiness status.

### 3. Question Bank (`02_questions/`)
Formulates questions across three streams:
- **Stream A ($Q_{\text{project}}$):** Project-side inquiry, paragraph functions, empirical identities.
- **Stream B ($Q_{\text{legacy}}$):** Inherited notes and prior model syntheses.
- **Stream C ($Q_{\text{source\_discovered}}$):** Author-specific terminology, tables, unexpected issues.
Every question object possesses a stable ID (`Q_XXX_001`), explicit provenance requirements, and negative boundaries.

### 4. Question $\times$ Source Matrix (`02_questions/` & NotebookLM Backend)
Queries NotebookLM via `notebooklm-py` with strict source scoping (`-s <source_id>`) and `--json` structured outputs.
Preserves:
- Direct answer.
- Support level (`EXPLICIT / PARTIAL / NOT LOCATED`).
- Exact author terminology.
- Verbatim cited text and character offsets.
- What the source does NOT establish.

### 5. Canonical Source Notes (`03_source_notes/`)
Durable, Markdown notes (`SRC_<KEY>.md`) normalizing the grounded extractions into the local vault.
Downstream drafting draws evidence primarily from these verified vault notes; original PDFs serve as escalation authorities.

### 6. Cluster Notes (`04_cluster_notes/`)
Adjudicates **WHO** can be cited together in a citation chunk and for **WHICH** specific proposition.
*Hard Rule: Cluster Membership $\neq$ Common Claim Membership.*

### 7. Synthesis Notes (`05_synthesis_notes/`)
Adjudicates **HOW** independently established claims connect analytically across literature traditions.
A cross-literature hinge is admissible only if:
1. Sources address proximate conceptual or empirical objects.
2. One source genuinely interprets the other without distorting scope.
3. The relation does not create a proposition stronger than the sources support.
4. The paragraph strictly requires the connection.

### 8. Paragraph Ledger & Human Gate (`06_paragraph_ledgers/`)
Constructs a sentence-by-sentence evidence plan with provenance tags:
- `DIRECT SOURCE CLAIM`
- `AUTHORIAL SYNTHESIS`
- `ADJUDICATED CROSS-LITERATURE HINGE`
- `TRANSITION`
- `THEMATIC RESONANCE ONLY — DO NOT INTERWEAVE`

**Hard Stop:** Execution stops at the Human Ratification Gate after each paragraph ledger and before prose drafting.

## Backend Independence
NotebookLM is utilized strictly as a reading and extraction backend via the adapter in `scripts/notebooklm_adapter.py`. The durable scholarly state resides exclusively in version-controlled Markdown/YAML/CSV/JSON files.
