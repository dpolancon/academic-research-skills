# Staged Academic Prose Protocol

**Specification ID:** `literature-review/references/staged_prose_protocol.md`  
**Lifecycle Stage:** `L8 — STAGED ACADEMIC PROSE`  
**Governing Schema:** `literature-review/schemas/staged_prose_schema.json`  

---

## 1. Definition and Purpose

> **DEFINITION:**  
> **Staged Academic Prose** is a deliberately restrained, highly inspectable intermediate prose state designed to stabilize:
> 1. Exact claim boundaries and qualifications;
> 2. Argumentative progression and sentence order;
> 3. Specific attribution and citation placement;
> 4. Negative evidentiary boundaries (`prohibited stronger claims`);
> 5. Proportional paragraph density.

**Staged Prose is NOT publication-ready manuscript prose.**  
It is the bridge that translates the structural instructions of Argument Assembly into transparent, verifiable English sentences before any stylistic tailoring, rhetorical compression, or disciplinary register adaptation is applied.

---

## 2. Default Staged-Prose Stylistic Principles

To maximize inspectability and prevent premature rhetorical drift, Staged Prose enforces strict drafting discipline:

### 2.1 Plain Subject-Verb Syntax
- Prefer direct, unadorned declarative structures: `[Subject] [Action/Finding] [Scope/Qualification]`.
- Avoid inverted syntax, periodic sentences, or dramatic rhetorical delays.

### 2.2 Explicit Attribution Where Required
- If a proposition represents a single author's claim (`DIRECT SOURCE CLAIM`), make the attribution explicit at the beginning or core of the sentence.
- If a proposition represents the current paper's construct (`AUTHORIAL SYNTHESIS`), explicitly state: *"In this paper, we define..."* or *"Our framework treats..."* to prevent concept-ownership confusion.

### 2.3 Minimal Ornament and Signposting
- Strip all decorative adjectives, intensifiers, and emotional commentary (*"profound insight"*, *"masterful synthesis"*, *"crucial cornerstone"*).
- Minimize meta-narrative signposting (*"It is important to note that"*, *"As will be seen below"*, *"We now turn our attention to"*).

### 2.4 No Stylistic Synonym Games
- Use consistent, precise technical terms across sentences.
- Never substitute an imprecise synonym simply to avoid repeating a technical noun (e.g., do not alternate between *capital stock*, *physical machines*, *wealth asset*, and *productive instrument* unless the theoretical distinction is substantive).

### 2.5 Evidentiary Boundaries Remain Fully Visible
- Every caveat, threshold condition, or qualification specified in the Paragraph Ledger must appear explicitly in the staged sentence.
- Sentences must plainly exhibit their negative boundaries: what is *not* established must be as clear as what *is* established.

---

## 3. Transformation Interface: Ledger $\to$ Assembly $\to$ Staged Prose

```
[PARAGRAPH LEDGER SLOT]
Slot ID: P03.S3
Proposition: While Author Alpha asserts net stock depresses asset value, Author Beta (2019)
mathematically proves that in multi-asset steady states the Gross-to-Net stock ratio
is time-invariant within a given growth regime (1.79 at g=0; 1.695 at g=0.10)...
       ↓
[ARGUMENT ASSEMBLY CHOREOGRAPHY]
Unit: P03
Job: Confront gross vs net depletion assumptions.
Order: Follow S2 (Author Alpha gross capacity) with S3 (Author Beta steady-state invariance).
Boundary: Time-invariant WITHIN a growth regime, NOT invariant across regimes.
Citation: (Author Alpha, 2016; Author Beta, 2019) under CCC_DEP_02.
       ↓
[STAGED PROSE SENTENCE]
"The choice between gross and net capital stock fundamentally alters measured
productivity paths: while Author Alpha (2016) asserts that net stock artificially
depresses capital value, Author Beta (2019) proves that in multi-asset steady states
the Gross-to-Net stock ratio is time-invariant within a given growth regime (1.79
at g=0; 1.695 at g=0.10), notes that growth slowdowns can widen observed gaps, and
suggests that net stock may reflect declining performance of aging equipment."
```

---

## 4. Inspection Checklist Before Advancing to Manuscript Prose

Before a Staged Prose unit is accepted for Manuscript Prose styling, it must pass five verification checks:
1. **Plain Syntax Observed:** Sentences follow direct, verifiable subject-verb structures.
2. **Ornament Minimized:** Zero decorative prose or unearned evaluative adjectives.
3. **Signposting Restrained:** Zero procedural meta-narrative.
4. **Citations Stabilized:** Citations attach directly to their supporting clauses.
5. **Boundaries Visible:** Qualifications and negative scope limits are transparently readable.
