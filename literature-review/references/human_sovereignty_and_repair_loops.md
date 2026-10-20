# Human Sovereignty and Bounded Autonomous Repair Loops

**Specification ID:** `literature-review/references/human_sovereignty_and_repair_loops.md`  
**Lifecycle Stage:** `GOVERNANCE & STATE-MACHINE CONTROL`  
**Governing Schema:** `literature-review/schemas/control_bundle_manifest_schema.json`  

---

## 1. The Sovereign Perimeter Principle

> **FOUNDATIONAL PRINCIPLE:**  
> **THE HUMAN AUTHOR APPROVES CHANGES TO THE EPISTEMIC PERIMETER, NOT EVERY MECHANICAL TRANSFORMATION WITHIN IT.**  
>  
> The human author exercises absolute, unshared sovereignty over the boundaries of admissible evidence, the architectural spine of the paper, claims of novelty and priority, and the acceptance of manuscript text.  
>  
> Within that authorized perimeter, autonomous agents execute bounded, self-auditing, and deterministically verifiable evidentiary operations without generating unnecessary interruptions.

---

## 2. Seven Exclusive Human Reserved Powers

Under no circumstances may an AI agent execute, assume, or bypass any of the following seven reserved powers without prior explicit human command:

1. **Corpus Admission:** Admitting new external sources, publications, or candidate literature into the active corpus perimeter.
2. **Architecture Modification:** Altering the canonical sequence, scope, numbering, splitting, or merging of argumentative units / paragraphs ($P_1 \dots P_J$).
3. **Scholarly Lock Ratification:** Transitioning any cluster note, citation contract, paragraph ledger, argument assembly, or staged prose unit to the immutable `LOCK` status.
4. **Contribution Hierarchy Adjudication:** Defining or changing which contribution is primary (e.g. data infrastructure) vs secondary (e.g. empirical demonstration).
5. **Novelty and Priority Claims:** Authorizing claims that a finding, method, or dataset is "the first", "unique", or "unprecedented".
6. **Manuscript Prose Acceptance:** Final approval and insertion of manuscript prose into target paper draft files.
7. **Irreversible Repository Actions:** Executing `git commit` or `git push` against version control.

---

## 3. Fourteen Bounded Autonomous Operations

Within an authorized perimeter and prior to human gates, agents possess full autonomy to execute the following fourteen operations:

1. **Wording Narrowing:** Restricting proposition claims to match exact source locators and proofs.
2. **Source-Set Narrowing:** Removing a source from a joint claim when the claim exceeds that source's evidence.
3. **Provenance Correction:** Reclassifying misidentified claims (e.g., changing an unearned `HINGE` to a `DIRECT SOURCE CLAIM`).
4. **Locator and Page Repair:** Auditing and correcting volume, issue, page, table, and paragraph numbers against primary PDFs.
5. **Proposition Splitting:** Breaking a compound sentence into atomic claims to isolate distinct warrants.
6. **Cluster Construction:** Tabulating comparative matrices across saturated source notes.
7. **Citation-Contract Construction:** Formulating `CCC_*` contracts specifying common denominators and excluded members.
8. **Paragraph Ledger Construction:** Populating proposition slots ($S_1 \dots S_n$) from saturated cluster notes and source notes.
9. **Argument Assembly Compilation:** Choreographing claim ordering, weave decisions, do-not-weave boundaries, and citation placement.
10. **Staged Prose Generation:** Drafting restrained, plain-syntax sentences stabilizing claim boundaries and citations.
11. **Manuscript Prose Drafting:** Transforming staged prose into target register prose based on locked ledgers.
12. **Style-Risk Auditing:** Deterministically scanning manuscript prose for the 18 structural style-risk families.
13. **Register / Humanization Polishing:** Smoothing syntax, rhythm, and cadence without altering evidentiary bounds.
14. **Post-Humanization Claim-Immobility Auditing:** Verifying sentence-by-sentence that humanization did not strengthen claims.

---

## 4. The Bounded Local Repair State Machine

When an audit fails (e.g. in cluster notes, paragraph ledgers, or staged prose), agents execute bounded local repair rather than immediately halting or escalating:

```
[FAILED AUDIT]
       ↓
[1. IDENTIFY EXACT DEFECT]
Pinpoint failed contract, provenance mismatch, or unsupported clause.
       ↓
[2. SMALLEST VALID REPAIR]
Narrow claim, split proposition, correct locator, or adjust weave boundary.
       ↓
[3. RE-AUDIT FROM AUTHORITY]
Verify repaired artifact against saturated primary source note.
       ↓
[4. CONVERGENCE CHECK]
Did the repair resolve the defect without introducing new violations?
```

### 4.1 Strict Convergence Invariants
- **Default Maximum Iterations:** **4 cycles** per artifact.
- **Zero Progress Rule:** If two consecutive repair cycles fail to make measurable progress or oscillate between competing formulations, the loop halts immediately.

### 4.2 Mandatory Escalation Triggers
The repair loop MUST immediately abort and escalate to human review (`HUMAN_REVIEW_REQUIRED`) if:
1. Repair requires admitting an external source not in the corpus perimeter;
2. Repair would modify or weaken an existing human `LOCK`;
3. Repair requires an architectural change to the paragraph spine;
4. Repair touches contribution hierarchy or priority claims;
5. Evidence in the saturated note remains genuinely insufficient after 4 iterations;
6. An unresolvable contradiction emerges between internal methodology and external sources.
