# LITERATURE-REVIEW WORKFLOW SPECIFICATION

## Purpose
This document specifies the exact protocol for executing an evidence-grounded literature review.

## Sequence of Operations

### Step 1: Establish Project Contract (`00_contract/`)
- Define literature review research questions.
- Fix authority hierarchy and data sources of truth.
- Define negative prohibitions and conceptual bounds.

### Step 2: Establish Corpus Registry (`01_corpus/`)
- Audit all candidate PDF files.
- Compute SHA-256 hashes.
- Ingest into NotebookLM and record stable `source_id`.
- Maintain dual-format registry (`.csv` and `.md`).

### Step 3: Populate Question Bank (`02_questions/`)
- Tri-stream question generation ($Q = Q_{\text{project}} \cup Q_{\text{legacy}} \cup Q_{\text{source}}$).
- Assign stable question IDs (`Q_XXX_001`).
- Enforce negative boundaries for each question.

### Step 4: Execute Question $\times$ Source Matrix (`02_questions/`)
- Query NotebookLM backend using explicit source scoping (`-s <id>`).
- Capture JSON output preserving cited text, chunk IDs, and character offsets.
- Record outputs in version-controlled run artifacts.

### Step 5: Materialize Canonical Source Notes (`03_source_notes/`)
- Normalize extractions into `SRC_<KEY>.md`.
- Classify support level (`EXPLICIT`, `PARTIAL`, `NOT LOCATED`).
- Audit legacy model notes against grounded extractions (`CONFIRMED`, `NARROWED`, `CONFLICT`, etc.).
- Source notes become the local operational source of truth.

### Step 6: Formulate Cluster Notes (`04_cluster_notes/`)
- Group sources by common literature objects.
- Adjudicate permitted citation chunks.
- Forbid joint citation where sources diverge conceptually.

### Step 7: Formulate Synthesis Notes (`05_synthesis_notes/`)
- Evaluate cross-literature hinges against the 4 admissibility criteria:
  1. Conceptual proximity.
  2. Genuine interpretive value.
  3. Non-inflationary claim boundary.
  4. Paragraph necessity.
- Tag with `ADJUDICATED CROSS-LITERATURE HINGE` or reject.

### Step 8: Build Paragraph Ledger (`06_paragraph_ledgers/`)
- Map out each sentence with provenance tags (`DIRECT SOURCE CLAIM`, `AUTHORIAL SYNTHESIS`, `TRANSITION`, etc.).
- Audit negative guardrails.

### Step 9: Human Ratification Gate
- **STOP.** Present ledger and calibration report to human adjudicator.
- No prose drafting permitted prior to explicit ratification.

### Step 10: Draft Prose & Sentence-Level Audit
- Draft paragraph strictly to match ratified ledger.
- Audit each sentence against cited source notes.
