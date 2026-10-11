# Academic Research Skills — Target-State Architecture

**Status:** Design target v0.1  
**Date:** 2026-10-11  
**Scope:** `dpolancon/academic-research-skills`  
**Purpose:** Define the desired architecture toward which the repository should evolve before further skill expansion.

---

## 1. Design objective

The target repository is a **modular, human-led research copilot for economics and political economy** that combines:

1. a general academic-research core;
2. economics-specific writing and research expertise;
3. political-economy and heterodox-macro domain knowledge;
4. deterministic research and verification tools;
5. reusable profiles for author, advisor, committee, journal, and public-facing venue calibration;
6. dissemination workflows for slides and public scholarship;
7. regression tests and governance that allow the system to learn from completed research workflows without turning case-specific fixes into universal rules.

The repository should not become a collection of equally weighted top-level “skills.” It should become a layered system in which **skills, profiles, tools, protocols, and tests have distinct responsibilities**.

---

## 2. Primary architectural rule

> **One capability, one canonical owner.**

A capability may be consumed by many components, but its authoritative logic should live in one place.

Examples:

- simulated external peer review → `academic-paper-reviewer`;
- economics prose conventions → `econ-write`;
- full research workflow orchestration → `academic-pipeline`;
- cointegration specification diagnostics → deterministic econometrics tooling;
- advisor-specific expectations → advisor profile;
- Jacobin América Latina conventions → venue profile consumed by a general public-scholarship skill.

This rule is the main defense against capability duplication and inconsistent behavior.

---

## 3. Component ontology

Every repository component should be classified into exactly one of the following types.

### 3.1 Core skill

A reusable reasoning workflow with a clearly defined intellectual task.

Examples:

- `deep-research`
- `academic-paper`
- `academic-paper-reviewer`
- `econ-write`
- `econ-slides`

A core skill may invoke tools, profiles, or shared protocols. It should not hard-code manuscript-specific facts.

### 3.2 Orchestrator

A state machine that routes work among skills and tools but does not become the main source of substantive disciplinary reasoning.

Canonical owner:

- `academic-pipeline`

The orchestrator owns transitions, state, gates, handoffs, and resumability. It should not duplicate writing, reviewing, econometric, or source-evaluation logic.

### 3.3 Domain skill / adapter

A reusable body of disciplinary reasoning that modifies or enriches a general skill.

Target examples:

- `econ-write`
- `applied-econometrics-pe`
- `heterodox-macro-modeling`
- candidate `political-economy-research`

Domain layers may provide priors, theories, terminology, method-specific checks, and literature traditions. They may **not predetermine empirical conclusions**.

### 3.4 Profile

A configuration layer containing contingent preferences or institutional context.

Examples:

- author voice and preferences;
- advisor expectations;
- dissertation committee composition;
- journal conventions;
- Jacobin América Latina editorial conventions.

Profiles configure skills. They do not reproduce workflow logic.

### 3.5 Tool

A bounded, preferably deterministic operation.

Examples:

- citation verifier;
- `revision_guard.py`;
- cointegration specification audit;
- Toda–Yamamoto specification map;
- IRF/GIRF plotting;
- LaTeX compilation;
- rendered-output checker;
- prose leakage scanner.

A useful test:

> If the component can do its job without deciding what the scholar’s argument means, it is probably a tool rather than a skill.

### 3.6 Shared protocol / contract

Cross-cutting invariants used by multiple skills.

Examples:

- claim-evidence contract;
- citation identity and source-role rules;
- editorial-governance contract;
- human-adjudication persistence;
- source-role drift detection;
- authorship/ownership boundaries;
- PASS / FAIL / INDETERMINATE semantics.

### 3.7 Evaluation / regression fixture

A concrete positive or negative case proving that a rule remains effective.

A workflow lesson is not considered integrated until it has at least one testable example or regression fixture where practical.

---

## 4. Target logical architecture

The following is the **logical target**, not an immediate file-move instruction.

```text
academic-research-skills/
│
├── skills/
│   ├── core/
│   │   ├── deep-research/
│   │   ├── academic-paper/
│   │   ├── academic-paper-reviewer/
│   │   └── academic-pipeline/
│   │
│   ├── domain/
│   │   ├── econ-write/
│   │   ├── political-economy-research/      # candidate gap
│   │   ├── applied-econometrics-pe/
│   │   └── heterodox-macro-modeling/
│   │
│   └── dissemination/
│       ├── econ-slides/
│       └── public-scholarship/
│
├── profiles/
│   ├── author/
│   │   ├── diego-academic/
│   │   └── diego-public/
│   ├── advisors/
│   │   └── michael-ash/
│   ├── committees/
│   │   └── umass-pe/
│   ├── journals/
│   └── venues/
│       └── jacobin-lat/
│
├── tools/
│   ├── econometrics/
│   ├── plotting/
│   ├── verification/
│   ├── prose/
│   ├── rendering/
│   └── latex/
│
├── shared/
│   ├── contracts/
│   ├── schemas/
│   ├── protocols/
│   └── evidence/
│
├── evals/
│   ├── gold/
│   └── regression/
│
├── clients/
│   ├── antigravity/
│   ├── claude/
│   └── codex/
│
└── docs/
    ├── TARGET_ARCHITECTURE.md
    ├── CAPABILITY_REGISTRY.yaml
    ├── UPSTREAMS.yaml
    ├── PROVENANCE.md
    ├── RISK_REGISTER.md
    ├── LEARNING_PROTOCOL.md
    └── migration/
```

### Migration rule

Do **not** immediately reorganize the physical tree into this structure. Existing clients, slash commands, junctions, and imports may depend on current paths.

First establish logical ownership through registries and compatibility mappings. Physical consolidation comes only after path-dependency tests exist.

---

## 5. Target intellectual architecture

### 5.1 General research core

The core remains methodologically plural and falsification-oriented.

It should provide:

- literature search and source verification;
- claim decomposition;
- evidence mapping;
- academic drafting and revision;
- peer review and re-review;
- stateful revision workflows;
- source and output integrity checks;
- human decision checkpoints.

The core should remain relatively close to upstream ARS architecture so that future upstream improvements remain adoptable.

### 5.2 Economics layer

`econ-write` should own economics-specific prose, paper architecture, result presentation, and disciplinary conventions.

It should be usable directly for bounded economics writing tasks and as a dependency of `academic-paper` when `discipline=economics`.

It should not maintain an independent end-to-end paper workflow parallel to `academic-paper`.

### 5.3 Political-economy research layer

The target repository currently lacks a mature reusable skill for comparative-historical and institutional political economy.

A candidate `political-economy-research` layer should eventually cover:

- comparative-historical political economy;
- periodization and historical sequencing;
- process tracing;
- institutional and archival source criticism;
- triangulation of quantitative, documentary, and historical evidence;
- center–periphery analysis;
- class relations and distributional institutions;
- distinction between chronology, mechanism, interpretation, and causal identification;
- relational comparison rather than case-description alone.

This skill should be created only after a bounded design pass confirms that these capabilities are not already adequately owned elsewhere.

### 5.4 Heterodox macro modeling layer

The present heterodox-macro material should evolve from paper-specific safeguards into a general modeling skill covering:

- Post-Keynesian growth and distribution;
- Marxian reproduction and profitability;
- Sraffian / surplus-approach modeling;
- demand-led growth;
- capacity utilization and normal utilization debates;
- Harrodian instability;
- stock-flow and accounting consistency;
- dynamic-system consistency and boundary behavior;
- separation of literature-owned propositions from author-derived formal extensions.

It must not encode project-specific conclusions as universal theoretical truths.

### 5.5 Applied econometrics in political economy

The existing UMass-applied-econometrics material contains reusable strengths:

- forensic replication;
- specification-space mapping;
- visual/descriptive grounding;
- integration-order governance;
- system-level time-series diagnostics.

The target skill should distinguish three layers explicitly:

1. **methodological requirement** — e.g. integration-order testing;
2. **theoretical prior** — e.g. distribution may enter accumulation dynamics;
3. **empirical conclusion** — determined by evidence, not by the skill’s ideological orientation.

A heterodox prior should expand the hypotheses under consideration. It must not force the empirical interpretation.

---

## 6. Dissemination architecture

Academic research should have a dedicated dissemination branch.

### 6.1 `econ-slides`

Retain as the owner of scholarly presentation workflows:

- seminars;
- conferences;
- job talks;
- working sessions;
- grant-team presentations;
- discussant decks.

### 6.2 `public-scholarship`

Create only after design validation.

It should own the generic transformation from scholarly research to public-facing intellectual work:

- opinion essays;
- magazine essays;
- policy briefs;
- research blogs;
- public talks;
- scripted media appearances.

Venue-specific requirements belong in profiles.

Example:

```text
public-scholarship skill
       +
profiles/venues/jacobin-lat
       +
profiles/author/diego-public
       =
Jacobin América Latina editing workflow
```

This avoids hard-coding one publication’s conventions into a general public-writing capability.

---

## 7. Profile architecture

### 7.1 Author profile

The author profile should contain durable preferences rather than paper facts:

- preferred voice and cadence;
- first-person conventions;
- tolerance for jargon;
- citation density preferences;
- recurring theoretical vocabulary;
- bilingual usage;
- rules for public vs academic prose.

It should not contain empirical findings that belong to individual projects.

### 7.2 Advisor profile

Advisor feedback belongs in a profile when it is reusable across projects.

Example categories:

- preference for descriptive grounding;
- preference for econometric transparency;
- recurring objections to over-formalization;
- expectations about explanation of cointegration.

Chapter-specific items such as exact page references, exact dummy years, or one manuscript’s notation belong in the project repository, not the global ARS repo.

### 7.3 Committee profile

A committee profile may describe member expertise and likely lines of questioning. It should be consumed by a generic defense/review workflow.

It should not duplicate a full peer-review engine.

### 7.4 Venue and journal profiles

Profiles may contain:

- genre;
- word limits;
- preferred structure;
- tone;
- audience assumptions;
- submission requirements;
- journal-specific conventions.

Profiles must be date-stamped where conventions can change.

---

## 8. Evidence and adjudication architecture

The Chapter 1 editing experience motivates a general evidence-governance layer.

### Required distinctions

The system must preserve the difference between:

1. **reference identity** — is this the correct source?
2. **claim support** — does the source support the sentence?
3. **subclaim support** — does it support all parts of a compound sentence?
4. **source role** — background, empirical result, theoretical proposition, interpretation, method;
5. **intellectual ownership** — source-derived proposition vs author-derived extension;
6. **causal strength** — association, prediction, cointegration, mechanism, causality;
7. **editorial decision** — KEEP / REWRITE / HOLD / REMOVE / PROPOSE;
8. **human adjudication** — which proposed decision has been accepted by the researcher;
9. **verification state** — whether the current revision still satisfies the accepted decision.

A reference may be bibliographically real and still be misused. A claim may be individually supported while a compound sentence overstates the source. A theory source may motivate an author’s framework without owning the author’s notation or derivation.

These distinctions should live in shared contracts and regression fixtures rather than in a single paper-specific prompt.

---

## 9. Learning architecture

The desired repo should learn through a controlled cycle:

```text
real workflow incident
        ↓
extract failure or successful control
        ↓
ask whether it generalizes
        ↓
assign one canonical owner
        ↓
write rule / protocol / tool change
        ↓
add positive + negative fixture
        ↓
run tests
        ↓
human approve
        ↓
integrate
        ↓
protect against regression
```

### Learning rule

> A case-specific lesson should not enter the global repo until its paper-specific details can be removed without losing the rule.

Example:

**Case-specific incident:** A source on Marxian reproduction was incorrectly cited as if it defined the author’s scalar transformation elasticity.

**Generalized lesson:** Literature that motivates a conceptual problem does not automatically own the author’s formal translation of that problem.

**Repository integration:** authorship/ownership protocol + claim-audit fixture.

---

## 10. Upstream architecture

The repository has at least two important upstream lineages:

1. `Imbad0202/academic-research-skills`
2. `hanlulong/econ-writing-skill`

The target repo should add explicit upstream records, for example:

```yaml
component: academic-pipeline
upstream_repo: Imbad0202/academic-research-skills
upstream_base_sha: <sha>
tracking_policy: track-core
local_divergence: bounded

component: econ-write
upstream_repo: hanlulong/econ-writing-skill
upstream_base_sha: <sha>
tracking_policy: track-selectively
local_divergence: domain-personalized
```

Updates should follow:

```text
discover
→ diff
→ classify
→ adopt / adapt / reject
→ regression-test
→ human approve
```

Never assume that “newer upstream” means “better for this fork.”

---

## 11. Client integration architecture

The canonical skill implementation must exist once.

Client-specific installations for:

- Antigravity;
- Claude;
- Codex;

should be generated, linked, or represented by thin adapters.

The public Git tree should not present multiple identical copies as if each were authoritative.

### Target invariant

> **One canonical source tree; many client views.**

Local NTFS junctions are acceptable implementation infrastructure, but the repository must clearly distinguish canonical files from generated or installed mirrors.

---

## 12. Non-goals

The target architecture explicitly rejects:

- autonomous end-to-end research without human state transitions;
- treating AI-generated review as equivalent to human peer review;
- encoding political-economy priors as predetermined empirical conclusions;
- creating a new skill whenever a profile or tool would suffice;
- maintaining parallel implementations of the same capability;
- storing manuscript-specific findings in global domain skills;
- using “humanization” as detection evasion rather than writing improvement;
- allowing a verifier to certify claims outside the evidence scope it actually inspected;
- silently weakening previously adjudicated editorial decisions.

---

## 13. Desired-state acceptance criteria

The repository reaches the first target-state milestone when all of the following are true:

### Architecture
- every top-level capability has one declared owner;
- every component is typed as skill, orchestrator, domain layer, profile, tool, protocol, or eval;
- overlapping skills have explicit routing rules;
- project-specific knowledge is removed from generic global skills or quarantined in profiles/project overlays.

### Evidence integrity
- source identity and source support are separate checks;
- source-role drift is detectable;
- authorial-ownership drift is detectable;
- prior human adjudications persist across revision rounds;
- PASS cannot mean more than the verifier actually checked.

### Domain quality
- economics writing conventions are owned by `econ-write`;
- political-economy research methodology has an explicit home;
- heterodox macro rules distinguish theory, prior, and evidence;
- historical claims receive source-criticism rules appropriate to non-econometric evidence.

### Tooling
- deterministic tasks are tools rather than duplicated prose instructions;
- each executable verifier has regression tests;
- canonical versions and supported Python/runtime contracts are explicit.

### Dissemination
- scholarly slides and public scholarship have distinct owners;
- venue-specific requirements are profiles rather than hard-coded general rules.

### Repository governance
- upstream provenance is recorded;
- licensing and attribution are internally consistent;
- security links point to the correct fork;
- secrets and `.env` handling are unambiguous;
- canonical vs installed/generated skill copies are unambiguous.

---

## 14. Immediate design stance

Do **not** begin by creating new skills.

The next sequence should be:

1. establish repo identity and governance baseline;
2. create the capability registry;
3. classify all existing components by ontology;
4. identify overlaps and project-specific leakage;
5. define migration actions without moving paths yet;
6. integrate the Chapter 1 lessons into shared evidence-governance contracts and tests;
7. only then decide whether the political-economy and public-scholarship gaps warrant new skills.

