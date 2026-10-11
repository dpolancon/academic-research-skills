# Academic Research Skills — Current → Target Gap Matrix

**Status:** Design target v0.1  
**Date:** 2026-10-11  
**Repository:** `dpolancon/academic-research-skills`  
**Purpose:** Convert the target architecture into a prioritized, continuously improvable backlog.

---

## 1. Priority scale

- **P0 — Repository integrity / identity:** must be resolved before large structural migration.
- **P1 — Architecture / ownership:** needed before adding or expanding skills.
- **P2 — Intellectual capability:** domain-quality improvements once ownership is clear.
- **P3 — Optimization / packaging:** useful after core architecture stabilizes.

Status vocabulary:

- `OPEN`
- `PARTIAL`
- `SATISFIED`
- `DEFER`

---

## 2. Gap matrix

| ID | Priority | Area | Current state | Desired state | Gap / risk | Concrete next artifact or action | Acceptance criterion |
|---|---|---|---|---|---|---|---|
| G01 | P0 | Repository identity | README identifies repo as standalone 14-skill ARS; positioning and upstream lineage remain mixed | Fork identity, scope, maintainer, provenance and relationship to upstream are explicit | User cannot tell what is upstream vs Diego-specific | `PROVENANCE.md` + fork identity block | every major component has provenance status |
| G02 | P0 | License consistency | README and positioning communicate different license identities | One legally and textually consistent license story | contradictory public metadata | license audit and explicit fork licensing decision | README, LICENSE, NOTICE, POSITIONING agree |
| G03 | P0 | Security ownership | Security guidance can point to upstream repository | Security reporting belongs to this fork or explicitly delegates | reports may go to wrong maintainer | update security ownership after license/provenance decision | all links resolve to intended fork process |
| G04 | P0 | Secret/config hygiene | root tree contains tracked `.env` path; contents not assessed in this design pass | no tracked secret-bearing environment file; public-safe example config only | possible credential/config ambiguity | dedicated secret-hygiene audit; do not inspect/print secrets in architecture pass | tracked files contain no live credentials; `.env.example` pattern documented |
| G05 | P0 | Canonical copies | skills appear both at root and client mirror paths, including identical blobs | one canonical source tree; mirrors generated/linked/thin | multiple authoritative-looking copies | canonical-path decision + client adapter map | no committed duplicate full skill trees unless explicitly generated and verified |
| G06 | P1 | Component ontology | 14 top-level items are all presented as “skills” | skill / orchestrator / domain / profile / tool / protocol / eval types explicit | architecture conflates different object types | `COMPONENT_REGISTRY.yaml` or extend capability registry | 100% of top-level components typed |
| G07 | P1 | Capability ownership | modes registry exists, but not full capability ownership | one canonical owner for each major capability | overlapping writer/reviewer/style functions | `CAPABILITY_REGISTRY.yaml` | no capability has two unqualified owners |
| G08 | P1 | `academic-paper` vs `econ-write` | both can draft/rewrite/review broad economics papers | academic-paper owns workflow; econ-write owns economics discipline policy and bounded writing | duplicate paper-writing logic | ownership refactor plan | routing examples and tests choose one owner consistently |
| G09 | P1 | Peer-review duplication | academic-paper internal review, academic-paper-reviewer, advisor-reviewer, committee skill all review | external peer review has one owner; self-check and profiles clearly distinct | divergent review criteria and duplicate revision loops | review-layer architecture note | each review layer has unique purpose and handoff |
| G10 | P1 | Advisor specialization | advisor-reviewer includes durable preferences plus Chapter-1-specific rules | reusable advisor profile + project-local overlays | manuscript facts leak into global skill | advisor decomposition ledger | no chapter-specific page/parameter rules in global profile |
| G11 | P1 | Committee specialization | PE-phd-committee implements named personas and its own workflow | generic defense/review workflow + committee profile | one review engine per committee | committee decomposition ledger | persona file contains expertise/preferences, not duplicated orchestration |
| G12 | P1 | Jacobin specialization | venue-specific public writing is a standalone skill | generic public-scholarship skill + Jacobin profile | publication conventions mixed with generic genre logic | public-scholarship design study | generic skill can support >1 venue profile without copied workflow |
| G13 | P1 | Editorial decision persistence | Phase-1 governance core exists but is not yet integrated | approved editorial decisions persist as cumulative obligations | future edits can reopen resolved issues | complete human review of Phase-1 governance then bounded integration | locked decision cannot disappear without explicit supersession |
| G14 | P1 | Final-pass generalization | Chapter-1 `final_pass.py` pattern was effective but paper-specific | generic verifier composition framework with project plug-ins | temptation to copy project checker into every repo | extract invariant catalog, not script wholesale | generic layer contains only reusable checks; project checks remain local |
| G15 | P1 | Upstream management | fork history and local sync registry exist; no explicit per-component upstream policy | `UPSTREAMS.yaml` with base SHA + adopt/adapt/reject policy | drift becomes undocumented | upstream registry | every imported core component has upstream and divergence policy |
| G16 | P1 | Learning loop | update registry records changes and sync events | workflow incidents become generalized rules + fixtures + ownership | change log ≠ learning system | `LEARNING_PROTOCOL.md` | every promoted lesson records incident, abstraction, owner, test, approval |
| G17 | P1 | Epistemic hierarchy | domain skills can mix theory, methodology and interpretation | explicit separation of theory prior, measurement, test, result, interpretation | domain priors can predetermine outcomes | shared `EPISTEMIC_LAYER_PROTOCOL.md` | no domain rule forces empirical verdict from theoretical preference |
| G18 | P1 | Claim/source adjudication | citation identity, claim audit and Chapter-1 lessons exist in several places | shared contract covers identity, support, subclaims, source role, ownership and causal strength | same source can be “correct” yet misattributed | extend editorial-governance / claim-audit contracts | regression fixtures catch source-role and ownership drift |
| G19 | P2 | Political-economy methodology | capabilities dispersed across econometrics, committee and public-writing files | reusable PE research skill or protocol family | comparative-historical and institutional methods underdeveloped | bounded gap study before creating skill | coverage includes process tracing, periodization, source criticism, triangulation |
| G20 | P2 | Historical source criticism | no clear canonical owner | dedicated protocol within political-economy research | historical assertions can inherit econometric evidence logic inappropriately | historical-evidence protocol | claims distinguish chronology, interpretation, mechanism and causal evidence |
| G21 | P2 | Heterodox macro modeling | existing heterodox skill is narrow and project-specific | reusable heterodox macro model reasoning | project-specific theta/Harrod rules risk becoming generic dogma | redesign specification | skill supports multiple heterodox frameworks without one paper’s conclusions |
| G22 | P2 | PE econometrics | UMass skill has strong forensic rules but also over-determined interpretations | reusable applied-econometrics PE domain layer + deterministic tools | “class struggle/regime switching” can be treated as mandatory interpretation | rule-by-rule epistemic audit | each rule tagged method / prior / interpretation / project-specific |
| G23 | P2 | Comparative methods | not explicit | comparative-relational method guidance | current suite skews toward paper writing and econometrics | add to PE methodology design | comparison logic, case selection, relational mechanisms represented |
| G24 | P2 | Center–periphery methods | present in user work, not systematic repo capability | reusable external-constraint / center-periphery research guidance | intellectual specialization underrepresented | domain design artifact | capability exists without forcing one theoretical school’s conclusion |
| G25 | P2 | Public scholarship | Jacobin skill exists but generic dissemination layer absent | public-scholarship owner + profiles | venue lock-in | generic public scholarship spec | same engine supports Jacobin + one additional genre/venue fixture |
| G26 | P2 | Author style | style calibration exists but Diego-specific durable academic/public profiles not formalized | versioned author profiles | style learned ad hoc across projects | author-profile schema | profile contains durable preferences, excludes project findings |
| G27 | P2 | Prose governance | econ-write + prose critic overlap and use many lexical rules | economics prose owner + shared leakage scanner | duplicated bans and over-edit risk | prose ownership consolidation | technical vocabulary protected; global find-replace prohibited; one lexical source of truth |
| G28 | P2 | Rendered artifact verification | available in some workflows but not unified | source verification and rendered verification are separate release layers | source PASS can hide PDF/slide defect | rendering attestation design | final certification records source hash + rendered artifact hash/status |
| G29 | P2 | Tool interfaces | deterministic tools are embedded within skills or standalone top-level folders | coherent `tools/*` ownership and stable CLI/contracts | logic difficult to reuse/test independently | tool inventory + interface contract | tools callable independently and by skills without copied instructions |
| G30 | P2 | Evals | repo has multiple tests/evals, Phase-1 governance adds gold fixtures | every critical learned invariant has positive + negative regression case | prose rules can drift silently | eval coverage matrix | high-risk invariants mapped to fixture/test IDs |
| G31 | P3 | Physical tree | current paths optimized for existing clients | logical architecture eventually reflected physically where safe | migration can break Antigravity/Claude/Codex discovery | path-dependency test + staged migration plan | clients pass install/discovery tests after each move |
| G32 | P3 | Client packaging | local junction strategy reduces drift, public tree still exposes duplicates | canonical tree + generated/thin client adapters | local vs Git semantics diverge | client packaging redesign | one canonical blob per skill implementation |
| G33 | P3 | Runtime compatibility | current README states Python 3.8+ while new tooling may be developed on newer Python | declared and tested support window | silent runtime incompatibility | runtime support matrix | CI/tests cover declared minimum or declaration is intentionally raised |
| G34 | P3 | Documentation scale | README, CHANGELOG and skill docs are large and partially overlapping | layered docs with concise entry points and authoritative registries | documentation itself becomes source of drift | docs information-architecture pass | one authoritative location per architecture fact |

---

## 3. Highest-priority gap clusters

### Cluster A — Repo identity and canonical source

**G01–G05** should be addressed before a large file-tree redesign.

Reason: an architecture migration is unsafe if the repository still has ambiguous licensing, upstream ownership, security destination, configuration hygiene, or multiple canonical-looking copies.

This is a repository-governance task, not an academic-content task.

### Cluster B — Ownership before expansion

**G06–G18** are the actual architecture foundation.

The repository should not add `political-economy-research` or `public-scholarship` until capability ownership and component typing are explicit. Otherwise every new capability increases overlap.

### Cluster C — Intellectual specialization

**G19–G30** is where the fork becomes substantively distinct from upstream.

The likely highest-value intellectual gaps are:

1. political-economy research methodology;
2. historical evidence/source criticism;
3. heterodox macro modeling generalized beyond one paper;
4. epistemically disciplined applied time-series econometrics;
5. public scholarship as a reusable dissemination workflow;
6. stateful evidence and attribution governance learned from completed editing workflows.

### Cluster D — Packaging and maintenance

**G31–G34** should follow logical stabilization.

Do not perform a visually attractive folder migration before ownership rules and client-path tests exist.

---

## 4. Chapter 1 lessons mapped to target gaps

The completed editing workflow should contribute to the repo only through generalized lessons.

| Learned lesson | Target gap | Correct repository home |
|---|---|---|
| Correct citation identity does not imply claim support | G18 | shared evidence contract + claim audit eval |
| A source can support one clause but not a compound sentence | G18 | subclaim decomposition protocol + fixture |
| A source’s role can drift across revisions | G13 / G18 | editorial governance + source-role invariant |
| Literature can motivate a formal problem without owning the author’s formalization | G18 / G21 | ownership protocol + econ-write / heterodox macro examples |
| Cointegration or predictive ordering does not identify structural causality | G17 / G22 | epistemic layer + PE econometrics |
| A held issue must not be silently “fixed” later | G13 | editorial governance |
| Reviewer repair must be re-verified, not assumed | G09 / G13 | reviewer re-review + governance |
| Source correctness and rendered PDF correctness are different layers | G28 | rendering attestation |
| Final verification should be composed from stable checks rather than prose confidence | G14 / G29 | shared verification framework |
| Editing ledgers and workflow vocabulary must not leak into manuscript prose | G27 | prose protocol/tool |

No Chapter-1-specific year, coefficient, source, section number, or title should be required for these lessons to function.

---

## 5. Proposed continuous-improvement loop

Each future repo-improvement session should select a bounded subset of gap IDs.

Recommended cycle:

```text
1. select gap IDs
2. inspect only owning components and dependencies
3. write desired-state contract
4. design positive/negative cases
5. implement bounded changes
6. run affected + regression tests
7. human review
8. commit as one coherent capability increment
9. update gap status
```

### Anti-drift rule

A pass must not opportunistically “clean up” unrelated skills merely because the model notices issues there. New findings go to the gap backlog unless they block the authorized change.

---

## 6. Recommended next three repo passes

### Pass A — P0 identity and canonical-source audit

Target: `G01–G05`.

Deliverables:

- fork provenance decision;
- license consistency report;
- security ownership correction plan;
- `.env`/secret-hygiene assessment;
- canonical-vs-mirror source map.

No intellectual skill rewriting.

### Pass B — Capability registry and component typing

Target: `G06–G12`, `G15`.

Deliverables:

- `CAPABILITY_REGISTRY.yaml`;
- component ontology registry;
- upstream registry;
- routing conflict report;
- decomposition plans for advisor, committee, Jacobin, prose critic.

No large physical moves.

### Pass C — Evidence/governance learning integration

Target: `G13–G18`.

Use the completed editorial-governance Phase 1 artifacts and Chapter-1 learning set as evidence.

Deliverables:

- source-role + intellectual-ownership invariants;
- human-adjudication persistence contract;
- final-pass generalization design;
- positive/negative regression fixtures;
- bounded integrations into writer, reviewer and pipeline.

Only after these passes should the repo design new domain skills for `G19+`.

---

## 7. Target-state scorecard

Use this as a recurring high-level progress check.

| Dimension | Current directional assessment | Target |
|---|---:|---:|
| Core research workflow | Strong | Strong + current upstream selectively integrated |
| Economics writing | Strong | Strong, clearly owned |
| Peer review | Strong | Strong, single canonical owner |
| Revision governance | Emerging | Durable human-adjudicated state |
| Citation identity | Strong | Strong |
| Claim/source faithfulness | Emerging | Strong + regression-protected |
| Political-economy methodology | Fragmented | Strong reusable domain layer |
| Heterodox macro modeling | Narrow/project-specific | Generalized, plural, falsifiable |
| Historical research method | Weak/implicit | Explicit protocol |
| Public scholarship | Venue-specific | General skill + profiles |
| Author/advisor/committee personalization | Strong but hard-coded | Profile-driven |
| Deterministic tools | Numerous but dispersed | Clear tool layer + stable interfaces |
| Capability ownership | Weak | Explicit registry |
| Upstream provenance | Partial | Explicit per-component tracking |
| Canonical source structure | Ambiguous | One canonical implementation per capability |
| Learning from completed work | Emerging | Incident → abstraction → fixture → integration loop |

---

## 8. Decision rule for “gap closed”

A gap is not closed because a Markdown rule was added.

For architectural or integrity gaps, closure normally requires:

1. explicit owner;
2. written contract;
3. implementation or routing change;
4. at least one regression test or fixture where feasible;
5. human review;
6. no conflicting duplicate rule remains active;
7. documentation updated at the authoritative source.

For domain-knowledge gaps, closure additionally requires examples demonstrating that the skill can distinguish:

- theory from evidence;
- source interpretation from source attribution;
- heterodox hypothesis from empirical verdict;
- authorial contribution from literature-owned proposition.

