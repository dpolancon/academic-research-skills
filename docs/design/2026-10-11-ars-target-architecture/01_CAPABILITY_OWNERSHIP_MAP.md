# Academic Research Skills — Capability Ownership Map

**Status:** Design target v0.1  
**Date:** 2026-10-11  
**Purpose:** Assign one canonical owner to each major capability and identify where current components should become consumers, profiles, or tools rather than parallel implementations.

---

## 1. Ownership rules

1. **One capability → one canonical owner.**
2. Consumers may add domain constraints but may not reimplement the owner.
3. A profile may configure behavior but may not own a workflow.
4. A tool may verify or transform bounded objects but may not become an implicit orchestrator.
5. A project-specific rule must stay in the project unless it can be generalized and regression-tested.
6. Cross-cutting invariants belong in `shared/`, not copied into every skill.

---

## 2. Capability map

| Capability | Canonical target owner | Current relevant components | Target relationship | Duplication / drift to prevent |
|---|---|---|---|---|
| Full research-to-publication state machine | `academic-pipeline` | `academic-pipeline`, parts of `academic-paper` | `academic-pipeline` orchestrates; other skills expose bounded entry points | parallel end-to-end workflows |
| Literature search / research synthesis | `deep-research` | `deep-research`, `academic-paper` literature strategist | `academic-paper` consumes corpus/search outputs; may perform bounded paper-specific gap fill | duplicate systematic research engines |
| Academic manuscript workflow | `academic-paper` | `academic-paper`, `econ-write` | `academic-paper` owns paper lifecycle; `econ-write` supplies economics discipline policy | two independent paper writers |
| Economics writing conventions | `econ-write` | `econ-write`, parts of `umass-applied-econometrics`, `prose-register-critic` | other skills call or inherit economics writing rules | multiple style rulebooks with conflicting phrasing bans |
| External simulated peer review | `academic-paper-reviewer` | `academic-paper-reviewer`, `academic-paper.peer_reviewer`, `advisor-reviewer`, `PE-phd-committee` | reviewer owns external review; academic-paper internal review becomes writer self-check; advisor/committee become profiles | multiple peer-review engines |
| Revision verification / re-review | `academic-paper-reviewer` + shared governance | `academic-paper-reviewer re-review`, `revision_guard.py`, pipeline | reviewer verifies substantive resolution; guard verifies persistence/authorization contracts | reviewer rubber-stamp; verifier overclaim |
| Revision writing | `academic-paper` revision mode | `academic-paper`, advisor-specific rewrite rules | profiles and review roadmaps configure revision; writer executes | reviewers editing manuscript directly |
| Citation identity verification | shared verification tool | `academic-paper citation-check`, pipeline integrity, claim audit | one tool/API layer used by all | several inconsistent DOI/reference checks |
| Claim ↔ source faithfulness | shared evidence protocol + `claim_ref_alignment_audit_agent` | pipeline claim audit, reviewer, Chapter-1 adjudication logic | shared contract; reviewer/pipeline consume | identity check mistaken for support check |
| Compound-claim decomposition | shared evidence protocol | reviewer examples, Chapter-1 repair logic | central protocol + fixtures | partial support treated as full support |
| Source-role classification | shared evidence protocol | current claim audit, editorial governance Phase 1 | use-scoped source-role contract | source role drifting across revisions |
| Intellectual ownership / attribution | shared evidence protocol + `econ-write` | Chapter-1 source adjudication, reviewer | shared contract distinguishes source proposition vs author extension | attributing author notation/derivation to literature |
| Causal-language calibration | shared evidence protocol + domain adapters | `econ-write`, `prose-register-critic`, applied econometrics | shared evidence ladder; domain layers map designs to allowed verbs | “predicts” → “causes”; cointegration → causal law |
| Human editorial decision persistence | shared governance / passport | Phase-1 editorial governance artifacts, pipeline passport | human-adjudicated decisions become durable obligations | later model silently reopening settled decisions |
| Scope authorization / HOLD semantics | shared governance | Chapter-1 workflow, revision guard | proposal, hold, authorized edit and verification states are distinct | model edits discovered issues without approval |
| Final pass / release verification | shared verification composition | `final_pass.py` pattern, pipeline gates, formatter | generic composition layer; project-specific tests plug in | paper-specific final checker copied wholesale |
| Writing register / AI-scaffolding leakage | shared prose protocol + deterministic tools | `prose-register-critic`, `econ-write` | prose critic becomes protocol/tool layer; econ-write owns economics prose | duplicate banned-word systems; global find-replace damage |
| Author voice calibration | author profile + `academic-paper` style calibration | `academic-paper`, prose critic | author profile stores durable preferences; skill applies them | workflow-specific style memory scattered in skills |
| Political-economy research methodology | **candidate `political-economy-research`** | fragments in UMass econometrics, committee, Jacobin skill | design and validate new domain owner only if gap persists | treating econometrics skill as full PE methodology |
| Applied econometrics for political economy | target `applied-econometrics-pe` | `umass-applied-econometrics` | retain/refactor as domain skill + deterministic tools | theory priors becoming empirical conclusions |
| Heterodox macro modeling | target `heterodox-macro-modeling` | `heterodox-economics-review`, UMass skill | broaden from project-specific review into reusable model reasoning | chapter-specific theta/ODE assumptions becoming universal |
| Time-series cointegration audit | deterministic econometrics tool | UMass embedded cointegration tool | tool owned under `tools/econometrics` | prose-only repeated diagnostic instructions |
| Toda–Yamamoto specification mapping | deterministic econometrics tool | UMass embedded TY tool | tool owned under `tools/econometrics` | method implementation duplicated in prompts |
| IRF / GIRF plotting | `tools/plotting` | `irf-plotting` | convert/retain as specialized tool interface | plotting logic duplicated in writing skill |
| LaTeX compile / build verification | `tools/latex` | `latex-compilation`, formatter | deterministic build tool; formatter consumes | LaTeX build logic in many skills |
| Rendered-output / visual verification | `tools/rendering` + pipeline release gate | econ-slides checks, PDF final passes, Phase-1 governance design | separate source-validity from rendered-validity | source PASS incorrectly implying visual PASS |
| Scholarly slide production | `econ-slides` | `econ-slides`, econ-write presentation guidance | `econ-slides` owns decks; econ-write may advise on economics content only | two slide workflows |
| Public scholarship | **candidate `public-scholarship`** | `editor-jacobin-lat`, econ-write policy/op-ed guidance | generic public-writing skill + venue profiles | Jacobin-specific rules treated as universal |
| Jacobin América Latina editorial style | `profiles/venues/jacobin-lat` | `editor-jacobin-lat` | extract venue-specific profile; public-scholarship consumes | one venue as general writing ontology |
| Advisor calibration | `profiles/advisors/michael-ash` | `advisor-reviewer` | profile consumed by reviewer/writer | chapter-specific advisor rules as global skill |
| Committee simulation | generic reviewer/defense workflow + committee profile | `PE-phd-committee` | convert named-persona skill into profile + simulation mode | separate review engine per committee |
| Journal targeting / venue rules | profiles/journals + reviewer | econ-write, reviewer, ad hoc prompts | journal profile supplies current requirements; reviewer owns fit assessment | static journal claims scattered across files |
| Client installation / discovery | `clients/*` + installer | `.agents`, `.claude`, junction installers | one canonical skill tree, generated/linked client views | committed duplicate canonical copies |
| Upstream synchronization | repo governance | current sync registry, manual fork history | `UPSTREAMS.yaml` + adopt/adapt/reject protocol | blind merging or permanent undocumented forks |
| Learning from completed workflows | shared learning protocol + evals | `UPDATE_REGISTRY.md`, Phase-1 governance work | incident → abstraction → owner → fixture → test → approval | update log mistaken for epistemic learning system |

---

## 3. Current top-level skill disposition

| Current top-level component | Current role | Target type | Recommended disposition |
|---|---|---|---|
| `deep-research` | research engine | Core skill | KEEP; track upstream selectively |
| `academic-paper` | writing pipeline | Core skill | KEEP; make generic owner of manuscript workflow |
| `academic-paper-reviewer` | peer-review pipeline | Core skill | KEEP; own simulated external review and re-review |
| `academic-pipeline` | full workflow | Orchestrator | KEEP; remain lightweight control plane |
| `econ-write` | economics writing | Domain skill | KEEP; narrow ownership to economics discipline rules and bounded writing tasks |
| `umass-applied-econometrics` | PE econometrics + writing + theory interpretation | Domain skill | REFACTOR; split method/tool rules from interpretive priors |
| `heterodox-economics-review` | narrow heterodox theory review | Domain skill | REDESIGN; broaden, remove chapter-specific assumptions |
| `prose-register-critic` | lexical/AI-trace audit | Shared protocol + tool | REFACTOR; retain technical-vocabulary protection and deterministic audits |
| `advisor-reviewer` | advisor + Chapter 1 calibration | Profile / project overlay | DECOMPOSE; durable advisor preferences → profile; paper-specific rules → project repo |
| `PE-phd-committee` | named committee simulator | Profile + generic simulation workflow | DECOMPOSE; committee expertise → profile; reviewer engine remains canonical |
| `editor-jacobin-lat` | public-writing + venue rules | Dissemination skill + venue profile | SPLIT; generic public scholarship vs Jacobin-specific configuration |
| `econ-slides` | scholarly presentation | Dissemination skill | KEEP; owner of academic presentation workflows |
| `irf-plotting` | plot/report routine | Tool | RETYPE; bounded specialized tool |
| `latex-compilation` | build process | Tool | RETYPE; shared deterministic infrastructure |

---

## 4. Routing rules in target state

### Example A — bounded economics prose edit

```text
User request
  → econ-write
  → optional author profile
  → prose verification tool
```

No need to invoke `academic-paper` or the full pipeline.

### Example B — revise a working paper after referee comments

```text
academic-paper-reviewer output
  → shared editorial-governance obligations
  → academic-paper revision mode
  → econ-write domain layer
  → relevant method/domain adapters
  → re-review
  → release verification
```

### Example C — political-economy historical section

```text
academic-paper
  + econ-write
  + political-economy-research
  + author profile
  → claim/source audit
```

### Example D — Jacobin América Latina essay

```text
public-scholarship
  + profiles/venues/jacobin-lat
  + profiles/author/diego-public
  + political-economy-research as needed
  → public-facing draft/revision
```

### Example E — dissertation defense simulation

```text
academic-paper-reviewer / generic defense mode
  + profiles/committees/umass-pe
  + profiles/advisors/michael-ash
  + relevant domain skills
```

No separate committee-specific review engine is required.

---

## 5. Shared invariants that no domain layer may override

These belong above all disciplinary profiles:

1. **Bibliographic identity ≠ claim support.**
2. **Support for one subclaim ≠ support for a compound claim.**
3. **Theoretical motivation ≠ ownership of the author’s formalization.**
4. **Association / prediction / cointegration ≠ structural causality.**
5. **Human approval ≠ scientific truth.**
6. **Prior editorial adjudication cannot disappear silently.**
7. **A missing evidence layer produces INDETERMINATE, not PASS.**
8. **A tool may certify only the scope it actually inspected.**
9. **Heterodox orientation may widen hypotheses; it may not force outcomes.**
10. **Reviewers do not edit the manuscript unless explicitly routed into a writing skill.**

---

## 6. Proposed `CAPABILITY_REGISTRY.yaml` fields

A future machine-readable registry should minimally support:

```yaml
capability_id: claim_source_faithfulness
owner: shared/evidence
kind: protocol
consumers:
  - academic-pipeline
  - academic-paper-reviewer
  - econ-write
status: active
forbidden_duplicate_owners: true
requires:
  - reference_identity
  - source_locator
verification:
  deterministic: partial
  semantic: required
```

For profiles:

```yaml
capability_id: jacobin_lat_style
owner: profiles/venues/jacobin-lat
kind: profile
consumer: public-scholarship
status: active
```

For tools:

```yaml
capability_id: cointegration_specification_audit
owner: tools/econometrics/cointegration
kind: tool
consumers:
  - applied-econometrics-pe
  - academic-paper-reviewer
```

---

## 7. Ownership decision tests

When a new feature is proposed, ask in order:

1. Does an existing owner already perform this capability?
2. Is this a reusable intellectual workflow or a bounded deterministic operation?
3. Is the difference substantive, or merely a user/venue/persona configuration?
4. Is the rule globally valid, discipline-specific, or project-specific?
5. Would a new skill create a second state machine or second reviewer/writer?
6. Can the new behavior be represented as a profile, protocol, tool, or test instead?

A new top-level skill should be the **last** option, not the first.

