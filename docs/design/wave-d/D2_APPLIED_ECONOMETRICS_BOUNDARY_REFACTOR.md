# WAVE D2 — APPLIED-ECONOMETRICS EPISTEMIC BOUNDARY AUDIT & BOUNDED REFACTOR
# Architectural Design, Forensic Audit Ledger, and Implementation Report

**Governing Checkpoint:** `917ee2f2332cef92015937bddd7337a52ef4b12d`
**Current Runtime Component:** `umass-applied-econometrics`
**Future Semantic Target:** `applied-econometrics-pe`
**Authorized Live Surface:**
- `umass-applied-econometrics/SKILL.md`
- `umass-applied-econometrics/tools/cointegration_specification_audit.md`
- `umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md`
**Status:** HUMAN-RATIFIED BINDING BOUNDARY — WAVE D2 CLOSED

---

## 0. EXECUTIVE VERDICT

Wave D2 executes a forensic audit and bounded refactor of the live econometrics capability `umass-applied-econometrics` toward its future canonical semantic role as `applied-econometrics-pe`.

The core operational objective of D2 is to establish and enforce an unbreachable epistemic boundary:

```text
THEORY
    proposes mechanisms, variables, hypotheses,
    restrictions, contrasts, and rival expectations
        ↓
EMPIRICAL METHOD
    determines stochastic admissibility, estimation,
    uncertainty, robustness, specification disposition,
    and empirical findings
        ↓
INTERPRETATION
    is conditioned on what the empirical evidence supports
```

### Key Audit Findings & Architectural Tightening:
1. **Purge of Critical Epistemic Inversion (Rule 2.H.4):** The live skill contained a direct epistemic defect requiring failed cointegration tests in peripheral economies to be interpreted as positive evidence of structural regime switching and foreign-exchange bottlenecks. This inversion has been completely purged. An empirical non-finding is an empirical non-finding; it may motivate alternative hypotheses, but cannot confirm the theory that was rejected.
2. **Purge and Demotion of Project-Specific Dissertational Leakage:** Specific mathematical parameter values and regime labels ($\hat{\gamma} \approx 1$ as Fordist mechanization, $\hat{\gamma} \gg 1$ as post-Fordist acceleration, $\hat{\gamma} < 0$ as institutional incoherence, specific Chilean monetary variables, and private specification tags like $D_7, D_9$) have been demoted to illustrative examples.
3. **Decoupling Method from School/Department Calibration:** The skill's identity has been shifted from an insular "UMass Amherst approach" to a reusable domain capability for applied political-economy econometrics, preserving its institutional lineage without turning faculty practices into rigid dogmatic requirements.
4. **Decoupling Toda–Yamamoto from Binary Ideological Tournaments:** The Toda–Yamamoto specification mapping protocol has been generalized to support arbitrary project-declared rival theoretical hypotheses rather than mandating a binary "Orthodox vs. Heterodox" tournament or a fixed 5-row table. The core procedure ($(k + d_{\max})$ augmentation, ex-ante openness, MWALD testing, and residual diagnostics) is cleanly separated from optional reporting layers (dynamic sign sums, information criterion conventions, comparison tables).
5. **Deduplication of Prose and Style Governance:** Generic writing instructions (BLUF, active voice, sentence structure, lexical transition bans) have been removed from the econometrics capability and delegated to their canonical owners (`econ-write` and `shared/protocols/prose_discipline_protocol.md`), preserving strict econometric reporting disciplines (forensic transparency, non-finding reporting, specification-space mapping).
6. **Preservation of Protocol Semantic Typing:** Embedded Markdown protocols in `tools/` are recognized as methodological reasoning protocols rather than deterministic executable tools. In Wave F, their physical home will be determined preserving this semantic type: they remain owned by `applied-econometrics-pe` as methodological references/protocols; only genuinely deterministic executable operations extracted from them may become canonical `tools/econometrics/` components.
7. **Exploratory vs. Confirmatory Demarcation:** The conceptual admissibility gate governs confirmatory / structural estimation. In exploratory / descriptive mode, data patterns may be inspected prior to a fully developed theoretical mechanism for pattern discovery and anomaly detection, but causal mechanism attribution without independent support is forbidden.
8. **Subsample Selection Anti-Cherry-Picking:** Historically motivated subsample windows must, where feasible, be justified by ex-ante independent evidence (`EX-ANTE / INDEPENDENTLY MOTIVATED PERIODIZATION`). Result-responsive window selection must be disclosed as exploratory/post-hoc with window sensitivity reported.
9. **Bootstrap Decision Rule Clarification:** Repository-wide universal override thresholds (such as $p > 0.10$) are rejected. When a validated bootstrap procedure is part of the declared inferential design, it governs according to its justified rule; otherwise, asymptotic and bootstrap inference are reported separately and disagreements are transparently explained.
10. **Scope Boundary Demarcation:** The current implemented domain is strictly political-economy time-series econometrics. Cross-sectional causal inference, panel microeconometrics, IV, RDD, DID, synthetic control, and matching are not claimed by this skill.

---

## 1. GOVERNING LOCKS AND BASELINE

### 1.1 Architectural Doctrine Locks
- **Component Typing:** Skills are reusable reasoning capabilities; Profiles are calibration inputs; Tools are deterministic operations; Shared Protocols are cross-skill constraints; Orchestrators are workflow control only.
- **Canonical Ownership:** One capability $\to$ one canonical owner.
- **Physical Topology Lock:** No physical directory moves or renames during Wave D (`umass-applied-econometrics/` remains the runtime path; protocol files remain in `tools/`; physical relocation is deferred to Wave F).

### 1.2 D1 Composition Doctrine Locks
- **Inferential-Task Jurisdiction:** Primary analytic ownership belongs to the component owning the requested inferential operation, not merely the substantive object or historical explanandum.
- **No Cross-Method Override:** Econometrics owns statistical estimation and stochastic admissibility. Political-economy research cannot override an econometric verdict; historical evidence cannot establish stochastic admissibility; formal models cannot substitute for empirical estimation; and an econometric coefficient cannot alone establish a historical causal mechanism.

### 1.3 Repository Baseline Verification
- **Governing Checkpoint:** `917ee2f` confirmed at HEAD.
- **Working Tree:** Tracked files 100% clean. Untracked design artifacts from Waves D0 and D1 preserved in `docs/design/wave-d/`.

---

## 2. INSPECTED SURFACE

The forensic audit inspected 100% of the normative lines across the authorized live surface:
1. `umass-applied-econometrics/SKILL.md` (130 lines post-refactor)
2. `umass-applied-econometrics/tools/cointegration_specification_audit.md` (92 lines post-refactor)
3. `umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md` (116 lines post-refactor)

---

## 3. BEFORE-STATE NORMATIVE RULE LEDGER (D2-A FORENSIC CLASSIFICATION)

Every substantive rule across the three target files has been classified into exactly one primary type:
- `G1 — GENERIC ECONOMETRIC METHOD`
- `G2 — METHOD-SPECIFIC HEURISTIC`
- `G3 — THEORY-CONDITIONED INTERPRETATION`
- `G4 — PROJECT-SPECIFIC CONTENT`
- `G5 — PROSE / WRITING GOVERNANCE`
- `G6 — PROFILE / SCHOOL CALIBRATION`
- `G7 — EPISTEMIC LEAKAGE`
- `G8 — UNSUPPORTED OR OVER-STRONG TECHNICAL RULE`
- `G9 — COMPATIBILITY / PATH METADATA`

| Rule ID | File & Location | Current Wording / Behavior Summary | Primary Class | Evidence for Classification | Current Architectural Risk | Disposition | Target Owner | Reason & Scope |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **R01** | `SKILL.md` line 3 | "synthesizing Plamen Nikolov's IZA guidelines with the UMass Amherst school of thought..." | `G6` | Frontmatter description | Ties skill definition to department identity and writing guide | `REWRITE` | `applied-econometrics-pe` | Reframe as applied political-economy econometrics. |
| **R02** | `SKILL.md` lines 6–8 | "defines the distinctive UMass Amherst approach to applied econometrics and political economy writing. It functions as a layer modifying standard economics writing tips..." | `G6` | Section title & opening prose | Conflates school identity with canonical method; couples econometrics with prose writing | `REWRITE` | `applied-econometrics-pe` | Establish canonical purpose: empirical rigor and theory-empirics boundary in political economy. |
| **R03** | `SKILL.md` lines 10–13 | "> **Embedded Tools:** Cointegration Audit Protocol... Toda–Yamamoto Protocol..." | `G9` | Blockquote callouts | Misclassifies reasoning protocols as executable tools (Lesson L1) | `REWRITE` | `applied-econometrics-pe` | Relabel as Methodological Reasoning Protocols while preserving links. |
| **R04** | `SKILL.md` line 20 | BLUF Principle: State thesis, empirical strategy, key results early; second paragraph must have "This paper examines..." | `G5` | §1 Prose layer | Direct duplication of `econ-write` and `prose-discipline` | `DELEGATE` | `econ-write` | Econometrics does not own introduction paragraph structure. |
| **R05** | `SKILL.md` line 21 | Simplicity Over Complexity: Cut math clutter, avoid passive voice, use active voice, subjects/verbs early | `G5` | §1 Prose layer | Direct duplication of `prose_discipline_protocol.md` | `DELEGATE` | `prose-discipline` | Cross-domain prose protocol owns voice and syntax. |
| **R06** | `SKILL.md` line 22 | Banish AI-isms & Snobbish Posturing: Eliminate "Furthermore, Moreover"; avoid defensive/patronizing heterodox framing | `G5` | §1 Prose layer | Lexical ban duplicate; framing tone is editorial | `DELEGATE` / `REWRITE` | `prose-discipline` (lexical) / `applied-econometrics-pe` (tone) | Lexical bans delegated; reframe as dispassionate reporting discipline. |
| **R07** | `SKILL.md` line 23 | Variable Definition: Define mathematical symbols immediately upon introduction (e.g., $\theta, u_t$) | `G5` | §1 Prose layer | Writing rule with dissertation variable examples | `GENERALIZE` | `applied-econometrics-pe` | Generalize into formal construct operationalization. |
| **R08** | `SKILL.md` lines 27–29 | "treats econometrics as a site of critical forensic investigation. Apply these six rules from the `09_papers_PDF` corpus" | `G6` | §2 Intro | Refers to local private folder and departmental brand | `REWRITE` | `applied-econometrics-pe` | Ground forensic econometrics as a general methodological standard. |
| **R09** | `SKILL.md` lines 31–33 | Rule 2.A Forensic Transparency: Avoid black-box models; justify data exclusions, weights, outliers; sensitivity checks | `G1` | §2.A | High-value reusable empirical discipline | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Preserves empirical replication and transparency. |
| **R10** | `SKILL.md` lines 35–37 | Rule 2.B Data-First Visualization: Non-parametric plots before parametric models; regressions must justify, "not contradict them" | `G1` | §2.B | "Not contradict" could block discovery of conditional/multivariate effects | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Direct descriptive grounding; qualify that regressions test and condition raw trends. |
| **R11** | `SKILL.md` lines 39–41 | Rule 2.C Endogenous Class Struggle: Treat class struggle/distribution as endogenous drivers; supplement ARDL with VECM | `G7` | §2.C | Mandates endogeneity by fiat; forces VECM for all single-equation studies | `REWRITE` | `applied-econometrics-pe` | Reframe as empirical testing of feedback hypotheses rather than dogmatic fiat. |
| **R12** | `SKILL.md` lines 43–45 | Rule 2.D Specification-Space Mapping: Display search boundaries; report alternative lags, deterministics, failed tests | `G1` | §2.D | High-value anti-p-hacking methodology | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Essential for empirical honesty. |
| **R13** | `SKILL.md` lines 47–49 | Rule 2.E Descriptive Macro Grounding: Historical growth indicators in main text; residuals/utilization must align with trends | `G1` | §2.E | "Must align" could tempt researchers to force alignment | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Ground econometrics in macro aggregates; reconcile divergences transparently. |
| **R14** | `SKILL.md` lines 51–53 | Rule 2.F Institutional Deconstruction: Critique mainstream indicators by revealing class/institutional mechanisms (labor intensity, schedule conflict) | `G3` | §2.F | Assumes every indicator critique must be grounded in labor intensity | `GENERALIZE` | `applied-econometrics-pe` | Generalize to Measurement Validity Assessment across institutional contexts. |
| **R15** | `SKILL.md` lines 55–58 | Rule 2.G Integration Order Governance: Theory is necessary but not sufficient; integration order binds; ADF + KPSS on levels & diffs | `G1` | §2.G | Overstates that all regressors must be $I(1)$ without scoping to estimator | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserve theory $\ne$ admissibility gate; scope $I(1)$ to standard cointegration. |
| **R16** | `SKILL.md` line 59 | Rule 2.G.2 Collinearity check: $r > 0.99$ or Condition Number $> 30$ blocks candidate regardless of theory | `G2` | §2.G.2 | Numerical cutoffs stated as universal physical laws | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Retain screening gate, but label thresholds as diagnostic heuristics/defaults. |
| **R17** | `SKILL.md` line 60 | Rule 2.G.3 $I(2)$ risk: Products/ratios/sums of $I(1)$ series may inherit $I(2)$; test directly | `G1` | §2.G.3 | Standard time-series econometric safeguard | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Prevents spurious regressions from compound integrated series. |
| **R18** | `SKILL.md` line 61 | Rule 2.G.4 Consolidated verdict table: Map candidate to theoretical basis, integration evidence, disposition | `G1` | §2.G.4 | Standard reporting artifact | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Ensures transparent accounting of all candidate variables. |
| **R19** | `SKILL.md` line 62 | Rule 2.G.5 Economic explanation of blocks: Theory describes decision mechanism; stochastic evidence determines proxy admissibility | `G1` | §2.G.5 | Core demarcation between concept and proxy | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Critical expression of theory $\to$ empirics boundary. |
| **R20** | `SKILL.md` line 65 | Rule 2.H Political Economy Interpretation: Read parameters through surplus approach, class struggle, institutional periodization | `G3` | §2.H | Monolithic theoretical framing | `GENERALIZE` | `applied-econometrics-pe` | Frame as interpreting parameters through explicit theoretical models without dogma. |
| **R21** | `SKILL.md` line 67 | Rule 2.H.1 Analytical meaning of coefficient: State analytical meaning (e.g., intensive to extensive margin elasticity) | `G3` | §2.H.1 | Project example ($K^{\text{ME}}, K^{\text{NRC}}$) embedded as canonical text | `DEMOTE_TO_EXAMPLE` | `applied-econometrics-pe` | Principle preserved; specific capital elasticity demoted to example. |
| **R22** | `SKILL.md` line 68 | Rule 2.H.2 Regime signatures: $\hat{\gamma} \approx 1$ = Fordist; $\hat{\gamma} \gg 1$ = post-Fordist; $\hat{\gamma} < 0$ = institutional incoherence | `G4` | §2.H.2 | Severe project leakage; hardcodes dissertation parameter values as universal truth | `DEMOTE_TO_EXAMPLE` | `applied-econometrics-pe` | Demote to illustrative example of subsample stability interpretation. |
| **R23** | `SKILL.md` line 69 | Rule 2.H.3 Distributional conditioning: Rising wages drive mechanization through FOC, not exogenous tech shocks | `G3` | §2.H.3 | Predetermines empirical outcome of induced innovation | `REWRITE` | `applied-econometrics-pe` | Frame as a testable empirical hypothesis regarding distributional mechanisms. |
| **R24** | `SKILL.md` line 70 | Rule 2.H.4 Epistemic inversion on periphery: Interpret failure to cointegrate as structural regime-switching (FX constraint) | `G7` | §2.H.4 | Critical epistemic defect; converts rejection into positive confirmation | `REMOVE` / `REWRITE` | `applied-econometrics-pe` | Purge completely. Non-finding is a non-finding; cannot confirm rejected theory. |
| **R25** | `SKILL.md` lines 72–73 | Rule 2.I Small-Sample Bootstrap: Asymptotic critical values over-reject; use residual bootstrap in macro panels with $N \le 30$ | `G1` | §2.I | Treats $N \le 30$ as universal hard cutoff | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserve bootstrap safeguard; qualify $N \le 30$ as a rule-of-thumb heuristic. |
| **R26** | `SKILL.md` line 75 | Rule 2.I.1 Report both asymptotic and bootstrap $p$-values for $N \le 30$ | `G1` | §2.I.1 | Dual reporting prevents false certainty | None (Core strength) | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserve dual reporting; label $N \le 30$ as sample-size heuristic. |
| **R27** | `SKILL.md` line 76 | Rule 2.I.2 Bootstrap replications: Residual resampling under null of no cointegration; min 300, 1000 preferred | `G2` | §2.I.2 | Rigid replication counts | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Qualify 300 / 1000 as recommended simulation defaults. |
| **R28** | `SKILL.md` line 77 | Rule 2.I.3 Size distortion decision rule: If asymptotic trace rejects but bootstrap $p > 0.10$, flag as size distortion and overrule | `G2` | §2.I.3 | Universal $p > 0.10$ override threshold | `REWRITE` / `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Declare bootstrap design rule; report disagreement transparently without universal $p > 0.10$ mandate. |
| **R29** | `SKILL.md` line 78 | Rule 2.I.4 Bootstrap reporting: Dedicated table, not buried in footnotes | `G1` | §2.I.4 | Reporting transparency | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Preserves transparency. |
| **R30** | `SKILL.md` lines 80–81 | Rule 2.J Toda–Yamamoto Benchmark: Execute levels-augmented $(k + d_{\max})$ VAR following Amiri & Ventelou (2012) | `G1` | §2.J | Sound econometric causality method | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Retains $(k+d_{\max})$ levels augmentation standard. |
| **R31** | `SKILL.md` line 83 | Rule 2.J.1 $d_{\max}$ confirmation: Confirm $d_{\max}$ across series via ADF/KPSS ($d_{\max}=1$) | `G1` | §2.J.1 | Hardcodes $d_{\max}=1$ as universal fact | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserve testing requirement; $d_{\max}$ is determined empirically, not hardcoded. |
| **R32** | `SKILL.md` line 84 | Rule 2.J.2 Ex-ante openness: Zero exogeneity restrictions ex-ante; block exogeneity identified strictly ex-post via MWALD | `G1` | §2.J.2 | Strong epistemic safeguard against confirmation bias | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Core epistemic safeguard: models remain open ex-ante. |
| **R33** | `SKILL.md` line 85 | Rule 2.J.3 Specification map across lags: Grid $k \in \{1, \dots, p_{\max}\}$, mark optimal $k^*$ with $^a$ | `G1` | §2.J.3 | Anti-p-hacking lag transparency | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Retains full lag-space reporting as recommended layer. |
| **R34** | `SKILL.md` line 86 | Rule 2.J.4 MWALD stats and dynamic signs: Report MWALD $\chi^2/F$, exact $p$, and $\sum_{i=1}^k \hat{\beta}_i$ for every lag | `G1` | §2.J.4 | Essential for dynamic economic interpretation | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Retains structural sum reporting as recommended layer. |
| **R35** | `SKILL.md` line 87 | Rule 2.J.5 Lakatosian Five-Sign Tournament: Contrast Orthodox vs Heterodox predictions in rigid table | `G3` | §2.J.5 | Forces binary Orthodox/Heterodox framing and fixed 5-row table | `GENERALIZE` / `REWRITE` | `applied-econometrics-pe` | Generalize to Theoretical Sign & Precedence Comparison with arbitrary rival theories (optional layer). |
| **R36** | `SKILL.md` line 88 | Rule 2.J.6 Residual diagnostics: Verify white noise (BG LM, ARCH, JB, White) at optimal lag $k^*$ | `G1` | §2.J.6 | Essential diagnostic gate for asymptotic validity | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Preserves diagnostic integrity. |
| **R37** | `SKILL.md` line 96 | Checklist Item 1 (BLUF Check): Contribution stated by 2nd paragraph of introduction | `G5` | §3 Checklist | Prose style duplication | `REMOVE` / `DELEGATE` | `econ-write` | Delegated to economics writing policy. |
| **R38** | `SKILL.md` line 97 | Checklist Item 2 (Variable Audit): Parameters defined in-text immediately | `G1` | §3 Checklist | Construct operationalization | `PRESERVE` | `applied-econometrics-pe` | Retain as operationalization requirement. |
| **R39** | `SKILL.md` line 98 | Checklist Item 3 (Active Voice Check): Passive constructions and generic AI transitions removed | `G5` | §3 Checklist | Prose discipline duplication | `REMOVE` / `DELEGATE` | `prose-discipline` | Delegated to cross-domain prose protocol. |
| **R40** | `SKILL.md` line 99 | Checklist Item 4 (Visual-First Test): Raw non-parametric plots before parametric regressions | `G1` | §3 Checklist | High-value empirical inspection | None | `PRESERVE` | `applied-econometrics-pe` | Preserves descriptive grounding inspection. |
| **R41** | `SKILL.md` line 100 | Checklist Item 5 (Forensic Transparency Check): Data exclusions, outliers, weighting justified | `G1` | §3 Checklist | Empirical replication discipline | None | `PRESERVE` | `applied-econometrics-pe` | Preserves forensic transparency. |
| **R42** | `SKILL.md` line 101 | Checklist Item 6 (Endogeneity Audit): Discuss feedback; check system validity of single-equation models | `G1` | §3 Checklist | Endogeneity checking | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Reframe as evaluating feedback hypotheses where theoretically motivated. |
| **R43** | `SKILL.md` line 102 | Checklist Item 7 (Specification Map): Summarize failed models; report full lag grid with optimal marker $^a$ | `G1` | §3 Checklist | Specification-space reporting | None | `PRESERVE` | `applied-econometrics-pe` | Preserves specification transparency. |
| **R44** | `SKILL.md` line 103 | Checklist Item 8 (Descriptive Grounding Check): Raw macro growth rates integrated into narrative | `G1` | §3 Checklist | Contextual macro grounding | None | `PRESERVE` | `applied-econometrics-pe` | Preserves descriptive grounding. |
| **R45** | `SKILL.md` line 104 | Checklist Item 9 (Institutional Critique): Deconstruct indicators to show class/political mechanisms | `G3` | §3 Checklist | Monolithic mechanism assumption | `GENERALIZE` | `applied-econometrics-pe` | Generalize to Measurement Validity Assessment. |
| **R46** | `SKILL.md` line 105 | Checklist Item 10 (Tone Balance): Authoritative, critical, free of defensive heterodox posturing | `G5` | §3 Checklist | Editorial style rule | `REWRITE` | `applied-econometrics-pe` | State as objective, dispassionate empirical reporting standard. |
| **R47** | `SKILL.md` line 106 | Checklist Item 11 (Integration Order Gate): Test candidate regressors on levels and diffs; report blocked candidates | `G1` | §3 Checklist | Fundamental stochastic admissibility gate | None | `PRESERVE` | `applied-econometrics-pe` | Preserves integration order screening; adds mode check. |
| **R48** | `SKILL.md` line 107 | Checklist Item 12 (Coefficient PE Interpretation): Interpret parameters through theory, not just statistical magnitudes | `G3` | §3 Checklist | Theory-guided interpretation | `GENERALIZE` | `applied-econometrics-pe` | Interpret parameters through explicit analytical models without dogma. |
| **R49** | `SKILL.md` line 108 | Checklist Item 13 (Bootstrap Sensitivity): Report bootstrap $p$-values alongside asymptotic values for $N \le 30$ | `G1` | §3 Checklist | Small-sample sensitivity check | None | `PRESERVE` | `applied-econometrics-pe` | Preserves bootstrap sensitivity check. |
| **R50** | `SKILL.md` line 109 | Checklist Item 14 (Consolidated Verdict Table): Summary table mapping theoretical basis, integration, disposition | `G1` | §3 Checklist | Transparent candidate accounting | None | `PRESERVE` | `applied-econometrics-pe` | Preserves candidate disposition ledger. |
| **R51** | `SKILL.md` line 110 | Checklist Item 15 (Toda–Yamamoto Check): $(k+d_{\max})$ levels augmentation, full lag grid, $\sum\hat{\beta}_i$, sign tournament table | `G1` | §3 Checklist | Comprehensive TY protocol audit | `GENERALIZE` | `applied-econometrics-pe` | Generalize tournament table to arbitrary rival theories. |
| **C01** | `cointegration_specification_audit.md` lines 1–4 | Header & metadata: "Operational tool embedded within `/umass-applied-econometrics`..." | `G9` | File header | Misclassifies protocol as an executable tool (Lesson L1) | `REWRITE` | `applied-econometrics-pe` | Relabel as Methodological Reasoning Protocol. |
| **C02** | `cointegration_specification_audit.md` lines 9–31 | Audit Sequence Flowchart: 7-step sequence (Enumeration $\to$ Gates 1–4 $\to$ LOESS $\to$ Verdict) | `G1` | §1 Flowchart | Structured reasoning workflow | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Keep sequence; qualify Gate 4 and LOESS as conditional diagnostics. |
| **C03** | `cointegration_specification_audit.md` lines 37–41 | Gate 1 Theoretical Admissibility: Differentiate decision mechanisms ($q^*$) from observable proxies ($K^{\text{ME}}/L$) | `G1` | §2 Gate 1 | Methodological demarcation with project examples | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserves mechanism vs. proxy gate; mark formulas as examples; add mode check. |
| **C04** | `cointegration_specification_audit.md` lines 42–46 | Gate 2 Integration Order Screen: ADF + KPSS; regressors must be $I(1)$ in levels and $I(0)$ in diffs | `G1` | §2 Gate 2 | Overstates $I(1)$ requirement without scoping to estimator | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserves unit root screening; scope $I(1)$ to standard cointegration. |
| **C05** | `cointegration_specification_audit.md` lines 47–51 | Gate 3 Collinearity & $I(2)$ Filter: $r > 0.99$, $\text{CN} > 30$ blocks; $I(2)$ tests on products/ratios; project examples | `G2` | §2 Gate 3 | Hardcoded numeric thresholds and private dissertation variables ($k^{\text{ME}}, k^{\text{NRC}}, Q_t^\omega$) | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Label thresholds as screening heuristics; demote variables to examples. |
| **C06** | `cointegration_specification_audit.md` lines 52–57 | Gate 4 Interaction & FWL: FWL regression on $\tilde{x}_t \cdot \tilde{d}_t$; substitute $\hat{u}_t$ for raw interaction ($D_7, D_9$); $\text{VIF} < 10$ | `G2` | §2 Gate 4 | Universal residual substitution alters parameter meaning; dissertation tags | `REWRITE` / `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Reframe as conditional collinearity remediation; purge $D_7, D_9$ tags. |
| **C07** | `cointegration_specification_audit.md` lines 60–68 | §3 Descriptive Diagnostics & Deterministic Combinatorics: LOESS inflection on $\tau_t$; drift vs trend VECMs; bootstrap $N \le 30$ | `G2` | §3 | Mandatory inflection analysis on private variable $\tau_t$ | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Frame LOESS inflection as an optional non-parametric diagnostic; demote $\tau_t$. |
| **C08** | `cointegration_specification_audit.md` lines 71–83 | §4 Standardized Verdict Ledger Format: Table format with Promoted/Held/Blocked/Rejected and dissertation codes | `G1` | §4 | Embedded private variable tags ($D_7, D_9, q_t, Q_t^q, k^{\text{ME}}$) | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserve 4-status ledger; purge private codes from status definitions. |
| **T01** | `toda_yamamoto_specification_mapping.md` lines 1–4 | Header & metadata: "Operational tool embedded within `/umass-applied-econometrics`..." | `G9` | File header | Misclassifies protocol as an executable tool (Lesson L1) | `REWRITE` | `applied-econometrics-pe` | Relabel as Methodological Reasoning Protocol. |
| **T02** | `toda_yamamoto_specification_mapping.md` lines 7–23 | §1 Methodological Foundation: $(k + d_{\max})$ levels VAR augmentation and Asymptotic Invariance Theorem | `G1` | §1 | Rigorous econometric foundation | None (Core strength) | `PRESERVE` | `applied-econometrics-pe` | Preserves mathematical foundation. |
| **T03** | `toda_yamamoto_specification_mapping.md` lines 28–47 | §2 Benchmark Sequence: Core procedure vs optional reporting layers | `G1` | §2 | Rigorous reporting workflow | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Preserve sequence; separate core procedure from optional reporting layers. |
| **T04** | `toda_yamamoto_specification_mapping.md` lines 49–63 | Benchmark Principles: Ex-ante openness; Lag map $k \in \{1..4\}$ with optimal $^a$; Dynamic sign $\sum\hat{\beta}_i$; 4-way decision rule | `G1` | §2 Principles | Strong epistemic openness and reporting rigor; $k \in \{1..4\}$ is heuristic | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Retain openness and 4-way rule; label $k \in \{1..4\}$ as illustrative grid. |
| **T05** | `toda_yamamoto_specification_mapping.md` lines 68–70 | Table 1 Standard: Unit root battery reporting ADF/KPSS and identifying $d_{\max}=1$ | `G1` | §3 Table 1 | Hardcodes $d_{\max}=1$ | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Retain unit root battery; note $d_{\max}$ is determined empirically. |
| **T06** | `toda_yamamoto_specification_mapping.md` lines 71–85 | Table 2 Standard: Specification mapping table reporting $k, F, \chi^2, p, \sum\hat{\beta}_i$, direction with Chilean money example | `G1` | §3 Table 2 | High-value reporting format with project example data | `PRESERVE_WITH_QUALIFICATION` | `applied-econometrics-pe` | Retain table architecture; label base money/inflation data as example. |
| **T07** | `toda_yamamoto_specification_mapping.md` lines 88–99 | §4 Lakatosian Five-Sign Tournament Table: Rigid 5-row table contrasting Orthodox vs Heterodox on Chilean monetary variables | `G4` | §4 Tournament Table | Severe project leakage; forces binary Orthodox/Heterodox framing on all papers | `GENERALIZE` / `DEMOTE_TO_EXAMPLE` | `applied-econometrics-pe` | Generalize to Theoretical Sign & Precedence Comparison; demote 5-row table to example. |

---

## 4. EPISTEMIC LEAKAGE FINDINGS

The forensic audit identified three major forms of epistemic leakage where theoretical preferences previously overstepped empirical boundaries:

### 4.1 Inversion of Empirical Rejection into Theoretical Confirmation (Rule 2.H.4)
- **Observed Behavior:** Rule 2.H.4 stated: *"For peripheral economies, interpret failures to cointegrate as evidence of structural regime-switching (e.g., FX-constrained accumulation) rather than data deficiency."*
- **Epistemic Defect:** This is a classic epistemic inversion. When a statistical test rejects the null hypothesis of cointegration (or fails to find a stationary linear combination), the empirical finding is strictly a non-finding: the proposed long-run equilibrium relationship is not supported by the data under the tested specification and sample. Instructing the researcher to treat this failure as positive proof of "structural regime-switching" or "FX constraints" immunizes the theoretical prior against empirical falsification.
- **Remediation:** Purged in full. The refactored capability establishes that failed cointegration is an empirical non-finding. Researchers may discuss failure as motivation to investigate structural breaks, nonlinearities, measurement errors, or regime changes, but each candidate explanation requires independent empirical verification.

### 4.2 Dogmatic Assertion of Endogenous Feedback (Rule 2.C)
- **Observed Behavior:** Rule 2.C stated: *"Treat class struggle and distributional variables (profit rate, wage share) as endogenous drivers of accumulation, rather than exogenous dummy controls... supplement single-equation models... with system-level models (VECM/VAR)..."*
- **Epistemic Defect:** Asserting that distributional variables are always endogenous drivers dictates the causal structure by theoretical fiat. Furthermore, mandating that every single-equation model must be supplemented with a VECM ignores situations where single-equation methods (e.g., distributed lag, instrumental variables, ARDL with exogenous controls) possess well-defined identification strategies.
- **Remediation:** Reframe as an empirical hypothesis and diagnostic obligation: when political-economy frameworks postulate bidirectional feedback between distribution and accumulation, researchers must explicitly evaluate plausible feedback rather than assuming exogeneity mechanically. Estimator choice depends on identification assumptions, sample size, and diagnostic testing.

### 4.3 Theoretical Predetermination of Parameter Signs (Rule 2.H.3)
- **Observed Behavior:** Rule 2.H.3 stated: *"Connect distributional conditioning to the induced innovation mechanism: rising wages drive mechanization through the FOC, not through exogenous technology shocks."*
- **Epistemic Defect:** Asserting that rising wages drive mechanization treats a specific theoretical mechanism (induced technical change) as an established empirical fact prior to estimation.
- **Remediation:** Reframe as a testable empirical hypothesis: specify the predicted sign under the induced innovation hypothesis, estimate the parameters neutrally, and evaluate whether the empirical evidence supports or contradicts the theoretical expectation.

---

## 5. PROJECT-SPECIFIC LEAKAGE FINDINGS

The audit identified heavy contamination from a specific dissertation and working-paper corpus (the author's work on machinery vs. structures accumulation in Chile and the US, and Chilean monetary policy):

1. **Hardcoded Parameter Thresholds as Universal Regime Signatures (Rule 2.H.2):**
   - *Leakage:* $\hat{\gamma} \approx 1$ defined as "balanced Fordist mechanization"; $\hat{\gamma} \gg 1$ as "post-Fordist machinery acceleration"; $\hat{\gamma} < 0$ as "institutional incoherence".
   - *Remediation:* Demoted to an illustrative example of how a project may interpret subsample parameter stability. Canonical methodology requires evaluating parameter stability across historically motivated subsamples or structural breaks, but forbids hardcoding universal numeric thresholds.
2. **Private Specification Tags and Variable Codes (Cointegration Protocol §2, §4):**
   - *Leakage:* Explicit references to specific model specifications ($D_7, D_9$) and specific dissertation variables ($k^{\text{ME}}, k^{\text{NRC}}, Q_t^\omega, q_t, Q_t^q, \tau_t$).
   - *Remediation:* Purged from normative gate definitions. Retained solely in clearly labeled illustrative tables demonstrating how real variables are evaluated.
3. **Mandatory Lakatosian Five-Sign Tournament Table (Toda–Yamamoto Protocol §4):**
   - *Leakage:* A fixed 5-row table contrasting Monetarism against Post-Keynesian structuralism across Chilean monetary transmission channels ($\pi \leftrightarrow g_H, M1 \leftrightarrow H, m \leftrightarrow \pi, g_H \leftrightarrow Q_{\text{manuf}}, \text{SolvR}^H \leftrightarrow g_H$).
   - *Remediation:* Generalized into a reusable *Theoretical Sign & Precedence Comparison Table Protocol* that accepts arbitrary project-declared rival hypotheses ($H_A$ vs. $H_B$ vs. $H_0$) and arbitrary transmission channels. The 5-row monetary table is demoted to an illustrative example.

---

## 6. METHOD VS HEURISTIC CLASSIFICATION

A critical source of past confusion was the failure to distinguish between *methodological invariants* and *context-dependent heuristics*:

| Threshold / Procedure | Original Live Status | Forensic Evaluation | Refactored Status | Methodological Rationale |
|:---|:---|:---|:---|:---|
| **ADF + KPSS Pairing** | Mandatory rule | Methodological Invariant | Methodological Invariant | Dual testing against complementary null hypotheses (unit root vs. stationarity) guards against low power of ADF and size distortion of KPSS. |
| **Pairwise Correlation $r > 0.99$** | Unconditional blocking rule | Diagnostic Heuristic / Default | Recommended Screening Heuristic | Near-perfect collinearity severely inflates variance, but $0.99$ is a pragmatic screening threshold, not a theoretical law. |
| **Condition Number $\text{CN} > 30$** | Unconditional blocking rule | Diagnostic Heuristic / Default | Recommended Screening Heuristic | Standard Belsley, Kuh, & Welsch (1980) diagnostic for moderate-to-severe multicollinearity in design matrices. |
| **Variance Inflation Factor $\text{VIF} < 10$** | Universal mandate | Diagnostic Heuristic / Default | Recommended Screening Heuristic | Standard diagnostic rule-of-thumb; not an absolute physical barrier. |
| **Small Sample $N \le 30$** | Rigid boundary | Context-Dependent Heuristic | Recommended Heuristic / Default | Asymptotic distributions of Johansen trace tests exhibit severe size distortion in small samples; $N \le 30$ (or $T \le 50$) marks high-risk territory. |
| **Bootstrap 300 / 1000 Replications** | Rigid requirement | Computational Default | Recommended Computational Default | 300 replications provides adequate screening stability; 1,000 replications is standard for publication tables. |
| **Bootstrap Decision Rule** | Mandatory override rule | Method-Specific Decision Rule | Context-Dependent Decision Rule / Screening Heuristic | When a validated bootstrap procedure is part of the declared design, it governs; otherwise report both transparently without a universal repository-wide override threshold ($p > 0.10$ is illustrative). |
| **Maximal Integration Order $d_{\max} = 1$** | Hardcoded universal constant | Context-Dependent Empirical Result | Empirically Determined Parameter | While most macroeconomic time series are $I(0)$ or $I(1)$, $d_{\max}$ must be confirmed by empirical testing, never assumed as a universal constant. |
| **Lag Battery $k \in \{1, 2, 3, 4\}$** | Fixed grid mandate | Illustrative Annual/Quarterly Default | Recommended Default Grid | A lag range of 1 to 4 is typical for annual or quarterly macro series, but $p_{\max}$ must adapt to data frequency and degrees of freedom. |
| **LOESS 2nd Derivative Inflection** | Mandatory preprocessing step | Optional Diagnostic Technique | Optional Non-parametric Diagnostic | Calculating zero-crossings of LOESS curvature is a creative way to detect structural change, but cannot be mandatory for all time-series studies. |
| **FWL Interaction Residualization** | Universal mandate for interactions | Conditional Collinearity Remediation | Conditional Remediation Technique | Orthogonalizing interactions via FWL alters the baseline interpretation of main effects (Balli & Sørensen 2013); it is a remediation for extreme collinearity, not a universal law. |

---

## 7. PROSE / OWNERSHIP DUPLICATION FINDINGS

The audit confirmed substantial prose and writing governance duplication in `umass-applied-econometrics/SKILL.md`:

- **Section 1 (The Prose & Tone Layer):** Lines 16–24 reproduced generic composition rules (BLUF, active voice, sentence structure, deletion of "Furthermore/Moreover", paragraph flow).
- **Section 3 (Diagnostic Checklist):** Checklist items 1, 3, and 10 audited generic prose features rather than econometric methodology.

### Ownership Boundary Resolution:
1. **Delegated to `econ-write`:** Academic paragraph structuring, BLUF placement in introductions, economics narrative clarity, and section design.
2. **Delegated to `shared/protocols/prose_discipline_protocol.md`:** Active voice, lexical bans on mechanical transitions, sentence simplicity, and anti-inflationary tone.
3. **Retained by `applied-econometrics-pe`:** *Econometric Reporting Disciplines*—transparent reporting of failed specifications, dual reporting of asymptotic and bootstrap $p$-values, reporting structural dynamic sums $\sum \hat{\beta}_i$, explicit parameter operationalization, and dispassionate empirical non-finding presentation.

---

## 8. COINTEGRATION PROTOCOL AUDIT (`cointegration_specification_audit.md`)

The audit of `cointegration_specification_audit.md` yielded four specific refactoring mandates:
1. **Type Clarification:** Update header and metadata to define the document as a *Methodological Reasoning Protocol* rather than an executable tool (preserving Inherited Lesson L1 while maintaining physical path for Wave F).
2. **Scope of Integration Order & Mode Check:** Qualify Gate 1 to distinguish confirmatory/structural mode from exploratory/descriptive mode. Qualify Gate 2 so that $I(1)$ levels requirement is explicitly scoped to standard cointegration frameworks (Johansen, Engle-Granger), acknowledging that bounds testing (ARDL) accommodates mixed $I(0)/I(1)$ systems.
3. **Gate 4 Refactoring:** Convert the mandatory FWL interaction residual substitution into a conditional remediation protocol for multicollinearity, noting the interpretive implications for main effects.
4. **Generalization of Verdict Ledger:** Remove private dissertation specification tags ($D_7, D_9, q_t, Q_t^q$) from canonical gate and status definitions, relocating them to clearly labeled illustrative examples.

---

## 9. TODA–YAMAMOTO PROTOCOL AUDIT (`toda_yamamoto_specification_mapping.md`)

The audit of `toda_yamamoto_specification_mapping.md` yielded four specific refactoring mandates:
1. **Type Clarification:** Update header to define the document as a *Methodological Reasoning Protocol* rather than an executable tool.
2. **Core vs. Optional Reporting Separation:** Explicitly separate the core estimation procedure ($(k + d_{\max})$ augmentation, ex-ante openness, MWALD testing, and residual diagnostics) from optional reporting layers (dynamic sign sums, information criterion conventions, comparison tables).
3. **Decoupling from Binary Ideological Tournament:** Replace the mandatory "Lakatosian Five-Sign Tournament Table" with a generalized *Theoretical Sign & Precedence Comparison Table Protocol*. The protocol must support arbitrary project-declared competing hypotheses ($H_A$ vs. $H_B$ vs. $H_0$) and arbitrary empirical domains.
4. **Demotion of Private Application Data:** Demote the Chilean monetary policy table to a clearly labeled illustrative example showing how the table architecture is operationalized.

---

## 10. REFACTOR DECISION LEDGER (D2-A $\to$ D2-B BRIDGE)

The following bridge table maps every forensic finding directly to the live refactor edits executed in D2-B and validated in D2.1:

| Rule IDs | Target File | Action Taken | Rationale & Ledger Bridge |
|:---|:---|:---|:---|
| **R01, R02, R08** | `SKILL.md` | Rewrite Title, Frontmatter, and Introduction | Reframe skill as canonical applied political-economy econometrics (`applied-econometrics-pe`), preserving institutional lineage without insularity. |
| **R03, C01, T01** | `SKILL.md`, `cointegration...`, `toda...` | Relabel "Embedded Tools" to "Methodological Protocols" | Enforce Inherited Lesson L1: behavior, not path, determines component type. |
| **R04, R05, R06, R37, R39** | `SKILL.md` §1, §3 | Purge generic prose rules; delegate to `econ-write` and `prose-discipline` | Enforce clean architectural ownership; retain only econometric reporting disciplines. |
| **R07, R38** | `SKILL.md` §1, §3 | Generalize variable definition to construct operationalization | Demarcate formal theoretical constructs from observable empirical series. |
| **R10, R13** | `SKILL.md` §2.B, §2.E | Direct descriptive grounding; qualify non-parametric plots and macro grounding | Direct descriptive grounding inspects relevant observed quantities; plots and aggregates are illustrative diagnostics, not mandatory forms. |
| **R11, R42** | `SKILL.md` §2.C, §3 | Reframe endogeneity as testable hypothesis and diagnostic check | Purge dogmatic assertion of endogeneity; restore empirical testing of feedback. |
| **R14, R45** | `SKILL.md` §2.F, §3 | Generalize indicator critique to Measurement Validity Assessment | Allow institutional, aggregation, and construction critiques across all indicators. |
| **R15, C04** | `SKILL.md` §2.G, `cointegration...` | Qualify integration order gate to specific estimator scope; add mode check | Clarify that $I(1)$ requirement applies to standard cointegration, not all time-series methods. Demarcate confirmatory from exploratory mode. |
| **R16, R25, R27, R31, C05, T04, T05** | All 3 files | Qualify numerical thresholds ($r>0.99, \text{CN}>30, N\le 30, k=1..4, d_{\max}=1$) | Explicitly label thresholds as diagnostic heuristics or computational defaults. |
| **R20, R21, R48** | `SKILL.md` §2.H, §3 | Reframe parameter interpretation through analytical models | Interpret parameters through explicit models; demote machinery elasticity to example. |
| **R22** | `SKILL.md` §2.H.2 | Demote Fordist parameter thresholds ($\hat{\gamma} \approx 1, \hat{\gamma} \gg 1$); add anti-cherry-picking | Demote thresholds; require ex-ante justification or post-hoc disclosure for subsamples. |
| **R23** | `SKILL.md` §2.H.3 | Reframe induced innovation from dogmatic fact to empirical hypothesis | Epistemic safeguard: theory motivates hypothesis; data determines outcome. |
| **R24** | `SKILL.md` §2.H.4 | Complete purge and replacement of peripheral cointegration rule | Mandatory removal of epistemic inversion. Non-finding = non-finding. |
| **R28** | `SKILL.md` §2.I.3, `cointegration...` §3 | De-freeze universal bootstrap override rule | Declare bootstrap design rule; report disagreement transparently without universal $p > 0.10$ mandate. |
| **R30, R35, R51, T03, T07** | `SKILL.md` §2.J, `toda...` §2, §4 | Generalize sign tournament to arbitrary rival theories; separate core from optional | Decouple Toda–Yamamoto from binary Orthodox/Heterodox framing; separate core estimation from reporting layers. |
| **C06** | `cointegration...` Gate 4 | Reframe FWL interaction residualization as conditional remediation | Prevent mandatory residualization from distorting main effect interpretation. |
| **C07** | `cointegration...` §3 | Reframe LOESS inflection as optional diagnostic; demote $\tau_t$ | Prevent private ratio analysis from becoming universal mandate. |
| **C08** | `cointegration...` §4 | Generalize verdict ledger definitions; demote private codes | Clean candidate accounting protocol applicable to any research project. |
| **T06** | `toda...` Table 2 | Demote Chilean base money/inflation data to illustrative example | Clean table standard applicable to any time-series system. |

---

## 11. IMPLEMENTED CHANGES

The bounded refactor executed in D2-B and finalized in D2.1 modified only the three authorized files on disk:

### 11.1 Changes in `umass-applied-econometrics/SKILL.md`:
1. **Title, Scope, & Identity Clarification:**
   - Shifted title and frontmatter from "UMass Amherst approach" synthesizing IZA tips to "Applied Econometrics in Political Economy: Epistemic Standards & Forensic Methodology".
   - Formalized semantic identity as `applied-econometrics-pe` while retaining runtime frontmatter name `umass-applied-econometrics` for Wave-F compatibility.
   - Clarified scope boundary: currently implements political-economy time-series econometrics; does not automatically claim cross-sectional or panel causal inference, IV, RDD, DID, etc.
   - Clarified that embedded documents are *Methodological Reasoning Protocols*, not deterministic executable tools.
2. **Prose Layer Deduplication (§1):**
   - Replaced generic prose composition rules (BLUF, active voice, sentence structure, lexical transition bans) with *Econometric Reporting Disciplines*: forensic accounting of exclusions, operationalization transparency, specification-space exposure, and dispassionate reporting of non-findings.
3. **Epistemic Inversion Purged (§2.H.4):**
   - Completely purged Rule 2.H.4 (interpreting peripheral cointegration failure as structural regime switching).
   - Replaced with explicit non-finding rule: an empirical non-finding is strictly a non-finding for the tested relationship; it cannot confirm a rejected theory by fiat.
4. **Endogeneity Reframed (§2.C):**
   - Replaced dogmatic assertion of endogeneity with an empirical obligation to test for feedback where theoretically motivated.
5. **Project-Specific Thresholds Demoted & Subsample Safeguard Added (§2.H.1, §2.H.2):**
   - Demoted Fordist parameter thresholds ($\hat{\gamma} \approx 1, \hat{\gamma} \gg 1, \hat{\gamma} < 0$) and machinery-structures elasticities to explicitly marked illustrative examples.
   - Added anti-cherry-picking discipline distinguishing ex-ante independently motivated periodization from ex-post result-responsive window selection (which must be disclosed with sensitivity reported).
6. **Exploratory vs. Confirmatory Demarcation (§2.G):**
   - Conceptual-admissibility gate governs confirmatory / structural estimation. Exploratory pattern discovery is permitted but causal mechanism attribution without independent support is forbidden.
7. **Heuristics Qualified & Bootstrap Rule De-Frozen (§2.G.2, §2.I, §2.J.1, §2.J.3):**
   - Qualified collinearity cutoffs ($r > 0.99, \text{CN} > 30$), sample size thresholds ($N \le 30$), bootstrap replications ($300 / 1000$), and lag ranges ($k \in \{1..4\}$) as recommended heuristics and computational defaults.
   - De-froze the universal bootstrap override: bootstrap-adjusted inference governs when part of declared design; otherwise report both transparently without universal $p > 0.10$ threshold.
   - Stated that $d_{\max}$ is determined empirically, not assumed as $d_{\max}=1$.
8. **Toda–Yamamoto Core vs. Optional Reporting Layers (§2.J):**
   - Separated methodological core (determination of $d_{\max}$, unrestricted levels VAR, MWALD testing on $k$ lags, residual diagnostics) from optional reporting layers (dynamic sign sums, information criteria conventions, comparison tables open to arbitrary rival hypotheses).
9. **Checklist Realignment (§3):**
   - Re-aligned 15 checklist items to focus strictly on econometric methodology, data inspection, and epistemic demarcation, purging generic prose items.

### 11.2 Changes in `tools/cointegration_specification_audit.md`:
1. **Document Classification:** Updated header to define the document as a *Methodological Reasoning Protocol* embedded within `/umass-applied-econometrics`.
2. **Construct Operationalization & Mode Check (Gate 1):** Demarcated latent theoretical decision mechanisms from observable macroeconomic proxies; added confirmatory vs exploratory mode demarcation; demoted $q^*$ and $K^{\text{ME}}/L$ to illustrative examples.
3. **Integration Order Scope (Gate 2):** Scoped $I(1)$ levels requirement to standard cointegration estimators, noting mixed-order handling in alternative frameworks (ARDL).
4. **Collinearity Heuristics & $I(2)$ Safeguards (Gate 3):** Labeled $r > 0.99$ and $\text{CN} > 30$ as recommended diagnostic screening thresholds; demoted private dissertation variables to illustrative examples.
5. **FWL Interaction Orthogonalization (Gate 4):** Reframe FWL residualization as a conditional collinearity remediation technique; purged private specification tags ($D_7, D_9$); added interpretive caution regarding base coefficients.
6. **Descriptive Diagnostics & Bootstrap Rule (Section 3):** Generalized descriptive grounding to observed relevant quantities; reframed 2nd-derivative inflection as an optional non-parametric diagnostic (demoted $\tau_t$); updated bootstrap rule to remove universal $p > 0.10$ threshold.
7. **Standardized Verdict Ledger (Section 4):** Purged private dissertation codes from canonical status definitions; provided clean illustrative application row.

### 11.3 Changes in `tools/toda_yamamoto_specification_mapping.md`:
1. **Document Classification:** Updated header to define the document as a *Methodological Reasoning Protocol* embedded within `/umass-applied-econometrics`.
2. **Core vs. Optional Reporting Separation:** Explicitly distinguished core estimation procedure ($(k + d_{\max})$ augmentation, ex-ante openness, MWALD testing on first $k$ lags, and residual diagnostics) from optional reporting layers (specification map grid, dynamic sign sums $\sum \hat{\beta}_i$, four-way directional rule, comparison tables).
3. **Empirical Determination of $d_{\max}$:** Replaced hardcoded $d_{\max}=1$ with requirement to establish $d_{\max}$ empirically across candidate series.
4. **Theoretical Sign & Precedence Comparison (Section 4):** Replaced rigid "Lakatosian Five-Sign Tournament Table" with a generalized optional protocol accepting arbitrary project-declared rival hypotheses ($H_A$ vs. $H_B$ vs. $H_0$). Demoted the 5-row Chilean monetary table to an illustrative example.

---

## 12. PRESERVED CAPABILITIES

The refactor avoided overcorrection, vigorously preserving the high-value empirical forensic capabilities that make the skill uniquely powerful:

1. **Forensic Replication Transparency:** Retained mandatory disclosure of data exclusions, country selections, date trimmings, and weighting choices with sensitivity checks (Herndon, Ash, & Pollin 2014).
2. **Direct Descriptive Grounding:** Retained inspection of directly observed quantities relevant to the question alongside descriptive visualizations (LOESS, binscatters) to establish baseline facts (Ash, Basu, & Dube 2017).
3. **Specification-Space Exposure:** Retained comprehensive mapping of specification boundaries, reporting failed models and alternative lag/deterministic structures (Maziarz 2017).
4. **Descriptive Macro Grounding:** Retained integration of observed growth aggregates into the narrative to contextualize econometric estimates (Marglin).
5. **Measurement Validity Critique:** Retained critical institutional evaluation of statistical indicators and aggregation methods (Pollin 1998).
6. **Strict Integration Order Governance:** Retained the foundational principle that theoretical motivation does not establish stochastic admissibility.
7. **Small-Sample Bootstrap Sensitivity:** Retained dual reporting of asymptotic and bootstrap $p$-values to detect size distortion in short macro panels.
8. **Toda–Yamamoto Causality Mapping:** Retained levels lag augmentation $(k + d_{\max})$, ex-ante openness, lag-grid reporting with optimal marker $^a$, dynamic sign tracking $\sum \hat{\beta}_i$, four-way directional decision rules, and post-estimation residual diagnostic gates.

---

## 13. REMOVED / GENERALIZED / DELEGATED RULES

| Original Rule | Action | Destination / Refactored Status | Rationale |
|:---|:---|:---|:---|
| **Rule 2.H.4 (Peripheral Cointegration Inversion)** | **REMOVED** | Replaced by strict non-finding handling (§2.H.4) | Severe epistemic defect. Converting empirical failure into theory confirmation immunizes priors against evidence. |
| **Section 1 Prose Rules (BLUF, Active Voice, AI Transitions)** | **DELEGATED** | `econ-write` and `prose_discipline_protocol.md` | Prose style is owned by shared protocols and economics writing skills, not econometrics. |
| **Checklist Items 1, 3, 10 (Prose Checks)** | **REMOVED** | Delegated to cross-domain prose verification | Econometric checklist must audit econometric methods. |
| **Rule 2.C (Mandatory Endogeneity by Fiat)** | **GENERALIZED** | Reframe as empirical testing of feedback hypotheses (§2.C) | Causal feedback must be evaluated empirically, not dictated by theoretical doctrine. |
| **Rule 2.H.2 (Fordist $\hat{\gamma}$ Thresholds)** | **DEMOTED** | Illustrative example in §2.H.2 | Numerical parameter values from a single dissertation cannot serve as universal canonical truths. |
| **Rule 2.H.3 (Induced Innovation Predetermination)** | **GENERALIZED** | Testable empirical hypothesis in §2.H.3 | Theory provides the hypothesis; empirical data determines whether mechanization responded to wages. |
| **Rule 2.I.3 (Universal Bootstrap $p > 0.10$ Override)** | **REWRITTEN** | Context-dependent decision rule in §2.I.3 | De-freeze universal threshold; declare bootstrap rule or report disagreement transparently. |
| **Rule 2.J.5 (Rigid 5-Row Lakatosian Tournament)** | **GENERALIZED** | Generalized Theoretical Comparison Table (§2.J.5, `toda...` §4) | Enables testing arbitrary project-declared competing theories, not just a binary Orthodox/Heterodox schema. |
| **Cointegration Gate 4 (Mandatory FWL Residualization)** | **GENERALIZED** | Conditional remediation protocol in Gate 4 | Orthogonalizing interactions alters main effect interpretation; it is a collinearity fix, not a universal mandate. |
| **Cointegration §3 (Mandatory LOESS Inflection)** | **GENERALIZED** | Optional diagnostic technique in §3 | Non-parametric inflection is a valuable diagnostic tool, not an obligatory step for every time-series paper. |
| **Private Dissertation Codes ($D_7, D_9, q_t, Q_t^q, \tau_t$)** | **DEMOTED** | Clearly marked illustrative examples | Project-specific artifacts must not leak into canonical domain protocols. |

---

## 14. BEFORE $\to$ AFTER EPISTEMIC CONTRACT

```text
========================================================================================
BEFORE D2 (VULNERABLE STATE)                     AFTER D2 (EPISTEMICALLY BOUNDED)
========================================================================================

THEORY:                                          THEORY:
- Dictated that class struggle is an             - Proposes mechanisms, latent constructs,
  endogenous driver by fiat.                       variables, and testable hypotheses.
- Dictated that rising wages drive               - Defines rival expectations and contrasts.
  mechanization through FOC.                     - Motivates variables conceptually.
- Hardcoded Fordist regimes to                   - NEVER dictates empirical results.
  specific numerical values (γ ≈ 1).              - NEVER converts rejection into confirmation.

EMPIRICS:                                        EMPIRICS:
- Subordinate to theory on failure:              - Strictly owns stochastic admissibility,
  failed cointegration was redefined as            estimation, uncertainty, diagnostics,
  proof of structural regime switching.           and empirical findings.
- Bivariate visual plots forced parametric       - Evaluates candidate variables across
  regressions to "not contradict them".            transparent gates.
- Interaction terms subjected to mandatory       - Reports empirical non-findings neutrally.
  FWL residualization regardless of goals.        - Rejection of cointegration is a non-finding.
- Universal p > 0.10 override enforced.          - Bootstrap inference governed by declared design
                                                   or dual reporting without universal cutoff.

INTERPRETATION:                                  INTERPRETATION:
- Filtered through mandatory binary              - Follows the empirical record.
  "Orthodox vs. Heterodox" tournament.           - Evaluates findings against arbitrary
- Parochial school calibration presented           project-declared rival theories.
  as canonical universal truth.                  - Reconciles econometric estimates with
                                                   macro aggregates transparently.
                                                 - Preserves empirical uncertainty.
========================================================================================
```

---

## 15. ADVERSARIAL SELF-AUDIT (D2-C FAILURE MODE EVALUATION)

The refactored capability was audited against the eight required failure scenarios:

### Case A — Theory strongly predicts cointegration; tests reject it
- **Audited Scenario:** A political-economy model insists that nominal wages and consumer prices must share a stable long-run cointegrating relationship. However, both Johansen trace tests and Engle-Granger tests fail to reject the null of no cointegration across multiple lag specifications.
- **Audited Behavior in Refactored Skill:** Under Rule 2.H.4 and Checklist Item 11, the skill explicitly mandates reporting the result as an empirical non-finding for the tested specification and sample. The researcher is expressly forbidden from converting this failure into positive evidence of "structural regime switching" or "foreign-exchange bottlenecks" by fiat. While the researcher may discuss the rejection as motivation to evaluate structural breaks or alternative specifications, each explanation requires separate empirical verification.
- **Verdict:** **PASS.**

### Case B — Theory predicts wage-led mechanization; coefficient has opposite sign
- **Audited Scenario:** An induced-innovation model predicts that rising wage share ($\omega_t$) accelerates machinery accumulation ($\beta_{\omega} > 0$). Estimation yields a statistically significant negative coefficient ($\hat{\beta}_{\omega} < 0$).
- **Audited Behavior in Refactored Skill:** Under Rule 2.H.3, Checklist Item 8, and Checklist Item 12, the skill requires reporting the empirical finding neutrally. The researcher cannot rewrite the sign's meaning or adjust the theory post-hoc to claim that a negative coefficient confirms induced innovation. The empirical non-support or contradiction must be reported dispassionately.
- **Verdict:** **PASS.**

### Case C — Variable is theoretically central but incompatible with stochastic framework
- **Audited Scenario:** A researcher considers an accumulated capital ratio $q_t = K^{\text{ME}}/L$ essential to their theoretical model of mechanization. However, unit root tests confirm that $q_t$ is $I(2)$, making it non-admissible in a standard $I(1)$ Johansen VECM.
- **Audited Behavior in Refactored Skill:** Under Rule 2.G and Cointegration Protocol Gate 1–3, the variable clears Gate 1 (conceptual relevance) but is definitively marked **Blocked** at Gate 3 due to confirmed $I(2)$ risk. Theoretical importance cannot bypass stochastic admissibility. The researcher must retain the variable's conceptual importance while selecting a valid econometric alternative (e.g., differencing, stationary transformation).
- **Verdict:** **PASS.**

### Case D — Strong statistical relationship with weak theoretical interpretation (Exploratory vs. Confirmatory)
- **Audited Scenario:** Data mining reveals a strong, statistically significant cointegrating relationship between two macro series, but there is no economic or institutional mechanism linking them.
- **Audited Behavior in Refactored Skill:** Under Rule 2.G and Cointegration Protocol Gate 1, the capability applies a strict mode distinction. In *Confirmatory / Structural Mode*, variables entering a structural or causal cointegration specification must have an explicit conceptual construct mapping; ungrounded correlations are blocked from structural interpretation. In *Exploratory / Descriptive Mode*, data patterns and empirical associations may be inspected for pattern discovery, anomaly detection, or hypothesis generation, but causal mechanism attribution or post-hoc structural storytelling without independent support is strictly prohibited.
- **Verdict:** **PASS.**

### Case E — User supplies dependency-theory interpretation
- **Audited Scenario:** A user analyzing Latin American time-series data requests a dependency-theory interpretation of trade deficits and interest rates.
- **Audited Behavior in Refactored Skill:** The econometrics capability preserves empirical rigor: it estimates the time series, reports stochastic properties, and conducts Toda–Yamamoto or cointegration tests without bias. The dependency-theory hypotheses can be evaluated in the Theoretical Comparison Table against rival hypotheses, but the theory cannot dictate the empirical findings, and downstream political economy cannot override the econometric verdict (`NO CROSS-METHOD OVERRIDE`).
- **Verdict:** **PASS.**

### Case F — Project-specific numeric heuristic treated as universal law
- **Audited Scenario:** A researcher insists that because an earlier study found $\hat{\gamma} \approx 1$ represented Fordist mechanization, any estimate where $\hat{\gamma} \ne 1$ proves the economy is not Fordist.
- **Audited Behavior in Refactored Skill:** Under Rule 2.H.2, numerical thresholds like $\hat{\gamma} \approx 1$ are explicitly classified as project-specific illustrative examples. Canonical methodology requires evaluating parameter stability across subsamples without imposing universal numeric labels.
- **Verdict:** **PASS.**

### Case G — Toda–Yamamoto with rival theories not described as Orthodox/Heterodox
- **Audited Scenario:** A paper evaluates three competing institutional theories of central bank reaction functions (e.g., Electoral Cycle Theory vs. Bureaucratic Autonomy vs. Financial Dominance), none of which match an "Orthodox vs. Heterodox" binary.
- **Audited Behavior in Refactored Skill:** Under Rule 2.J.5 and Toda–Yamamoto Protocol Section 4, the protocol cleanly accommodates arbitrary project-declared competing hypotheses ($H_A$ vs. $H_B$ vs. $H_C$), testing directional precedence and dynamic signs without requiring ideological pigeonholing.
- **Verdict:** **PASS.**

### Case H — Short sample with asymptotic over-rejection (Non-Universal Bootstrap Decision)
- **Audited Scenario:** An annual macroeconomic panel has $T = 28$ observations. Johansen trace tests reject the null of no cointegration ($p < 0.01$), but a residual bootstrap indicates potential size distortion.
- **Audited Behavior in Refactored Skill:** Under Rule 2.I.3 and Cointegration Protocol Section 3.4, when a validated bootstrap procedure is part of the declared inferential design, bootstrap-adjusted inference governs according to that procedure's justified decision rule. Otherwise, asymptotic and bootstrap inference are reported separately, disagreement is transparently exposed, and the privileged procedure is justified without applying a rigid repository-wide override threshold (e.g., $p > 0.10$ is treated as an illustrative screening heuristic, not a universal law).
- **Verdict:** **PASS.**

---

## 16. CANDIDATE DOWNSTREAM CHANGES — NOT AUTHORIZED

During the D2 audit, several cross-domain and downstream improvements were identified outside the authorized D2 surface. In accordance with Section 2 of the D2 Mission, these are recorded here without implementation:

```text
CANDIDATE DOWNSTREAM CHANGE:
EVALS-01: Add Toda–Yamamoto vs. Writing Routing Case (ADV-D4 / ROUTE-021)
TARGET: evals/gold/routing/cases.yaml
REASON: Test disambiguation between econometric Toda-Yamamoto lag specification and prose drafting.
STATUS: PROPOSED — NOT AUTHORIZED (Slated for Wave D5)

CANDIDATE DOWNSTREAM CHANGE:
EVALS-02: Add Epistemic Non-Finding Gold Eval Fixture
TARGET: evals/gold/
REASON: Behaviorally verify that agents auditing cointegration failures report non-findings rather than inventing regime-switching explanations.
STATUS: PROPOSED — NOT AUTHORIZED (Slated for Wave D5)

CANDIDATE DOWNSTREAM CHANGE:
REGISTRY-01: Update Registry Metadata to v1.2.0 reflecting applied-econometrics-pe
TARGET: docs/governance/ars_registry.yaml
REASON: Reflect refactored capability description and future semantic ID while preserving runtime compatibility.
STATUS: PROPOSED — NOT AUTHORIZED (Slated for Wave D6)

CANDIDATE DOWNSTREAM CHANGE:
TOPOLOGY-01: Physical Migration of umass-applied-econometrics to skills/domain/applied-econometrics-pe
TARGET: Repository directory layout
REASON: Harmonize physical directory layout with target logical architecture.
STATUS: PROPOSED — NOT AUTHORIZED (Locked for Wave F)
```

---

## 17. REMAINING METHODOLOGICAL QUESTIONS

The D2 audit highlighted two subtle methodological frontiers requiring attention in later passes:
1. **Cointegration with Structural Breaks:** While the refactored capability provides LOESS inflection diagnostics and subsample stability checks, a formal protocol for Gregory–Hansen (1996) or Saikkonen–Lütkepohl cointegration tests with endogenous regime shifts should be considered if structural breaks are central to long-run political economy.
2. **Panel Cointegration Heterogeneity:** In short panel settings, cross-sectional dependence (Pesaran CD test) and second-generation panel unit root tests (CIPS) represent potential future extensions for multi-country political-economy studies.

---

## 18. D2 FINAL BOUNDARY LOCK

The substantive boundary contract for the refactored capability is now locked:

```text
========================================================================================
FINAL ARCHITECTURAL BOUNDARY LOCK — applied-econometrics-pe
========================================================================================

WHAT DOES applied-econometrics-pe OWN?
- Authoritative ownership of empirical time-series econometrics in political economy.
- Stochastic admissibility screening, unit root diagnostics, and integration order gates.
- Specification-space mapping, lag-length sensitivity, and deterministic combinatorics.
- Small-sample bootstrap sensitivity testing and asymptotic size-distortion prevention.
- Toda–Yamamoto levels-augmented VAR causality testing and dynamic sign tracking.
- Transparent reporting of empirical non-findings and model rejections.

CURRENT IMPLEMENTED DOMAIN:
- Political-economy time-series econometrics, including:
  * integration-order analysis;
  * cointegration;
  * VAR / VECM reasoning;
  * Toda–Yamamoto;
  * specification-space diagnostics;
  * small-sample sensitivity;
  * time-series empirical interpretation.

NOT AUTOMATICALLY CLAIMED BY D2:
- cross-sectional causal inference;
- panel causal inference;
- Instrumental Variables (IV);
- Regression Discontinuity (RDD);
- Difference-in-Differences (DID) / event-study designs;
- synthetic control;
- matching;
- microeconometric treatment-effect methods;
- other empirical domains not presently implemented.

WHAT MAY THEORY DO?
- Motivate variables conceptually and define latent behavioral constructs.
- Propose causal mechanisms, first-order conditions, and structural restrictions.
- Formulate rival hypotheses and predict directional precedence and dynamic signs.
- Guide subsample selection based on historically motivated institutional breaks.
  * Anti-Cherry-Picking Rule: Historically motivated windows should, where feasible,
    be justified using evidence independent of the focal econometric result
    (EX-ANTE / INDEPENDENTLY MOTIVATED PERIODIZATION). If a window or breakpoint is
    selected after inspecting the focal result (EX-POST RESULT-RESPONSIVE WINDOW SELECTION),
    its status must be explicitly disclosed as exploratory/post-hoc, and sensitivity to
    alternative plausible windows must be reported.
- Structure interpretation questions conditioned on empirical results.

WHAT MAY THEORY NOT DO?
- Dictate empirical findings or parameter magnitudes prior to estimation.
- Redefine empirical rejections or cointegration failures as positive confirmation of theory.
- Bypass stochastic admissibility screening on grounds of conceptual importance.
- Hardcode universal ideological or regime labels to specific numeric parameter values.

WHAT DOES EMPIRICS OWN?
- The determination of stochastic admissibility for the selected estimator.
- Point estimation, standard errors, test statistics, and uncertainty bounds.
- Specification diagnostics, residual white-noise tests, and bootstrap distributions.
- The ultimate disposition of empirical hypotheses (supported, contradicted, or non-finding).

HOW ARE NON-FINDINGS HANDLED?
- Reported transparently as empirical non-findings for the specified relation and sample.
- Rejections may motivate exploring structural breaks, measurement errors, or alternative
  dynamic specifications, but each candidate explanation requires independent verification.
- Rejection of the null never converts automatically into acceptance of an untested prior.

WHAT MAY INTERPRETATION DO?
- Discuss the consistency of empirical findings with underlying theoretical models.
- Contrast empirical signs and precedence against arbitrary project-declared rival theories.
- Reconcile econometric estimates with descriptive macroeconomic growth aggregates.
- Generate new hypotheses for future research based on empirical anomalies.

WHAT MUST REMAIN PROJECT-SPECIFIC?
- Specific parameter value meanings (e.g., γ ≈ 1 as Fordist mechanization).
- Private model specifications and variable designations (e.g., D7, D9, specific capital codes).
- Particular geographic or historical application data (e.g., Chilean monetary transmission).
- Workspace and dataset overlays.

WHAT DOES THE SKILL DELEGATE?
- Generic prose composition, paragraph architecture, and BLUF: delegated to econ-write.
- Lexical bans, voice, and sentence discipline: delegated to prose_discipline_protocol.md.
- Mathematical dynamical macro modeling and closures: delegated to heterodox-macro-modeling (D3).
- Qualitative historical process tracing and archival evaluation: delegated to political-economy-research (D4).
- Simulated peer review: delegated to academic-paper-reviewer.

FUTURE WAVE-F DISPOSITION:
The physical home of the methodological econometrics protocols will be determined after
semantic typing is preserved.
Current default expectation: they remain owned by applied-econometrics-pe as methodological
references/protocols.
Only genuinely deterministic executable operations extracted from those protocols may
become canonical tools/econometrics components.
Physical directory rename: umass-applied-econometrics/ -> skills/domain/applied-econometrics-pe/ (Wave F).
========================================================================================
```

---

## 19. REGRESSION & WORKING-TREE VERIFICATION

### 19.1 Regression Test Results:
All six test suites executed after D2-B and D2-C passed 100%:
- `scripts/test_wave_c_reconciliation.py`: **11/11 PASS**
- `scripts/validate_ars_registry.py`: **18 components, 20 capabilities PASS**
- `scripts/test_routing_contract.py`: **17/17 cases PASS**
- `scripts/test_prose_discipline.py`: **11/11 gold fixtures PASS**
- `scripts/test_profile_contract.py`: **19/19 assertions PASS**
- `scripts/test_revision_guard.py`: **12/12 cases PASS**

### 19.2 Working Tree Inspection:
- `git diff --check`: **0 errors** (all trailing whitespace eliminated).
- Tracked file diffs: restricted exclusively to authorized files (`SKILL.md`, `cointegration...`, `toda...`).
- Git status: zero commits, zero pushes. Synchronized baseline `917ee2f` maintained.

---

# 20. ARCHITECT LEARNING DELTA

This section executes the mandatory **Architect-Mediated Learning Loop** for Wave D2.

## Lessons Inherited

The following binding lessons from Waves B, C, D0, and D1 materially constrained and shaped D2:
- **L1 — Behavior, Not Path, Determines Component Type:** The Markdown files in `umass-applied-econometrics/tools/` were recognized as methodological reasoning protocols rather than executable tools, preventing improper retyping while preserving file paths for Wave F.
- **L2 — Useful Implementation $\ne$ Universal Architectural Rule:** Specific numerical thresholds ($r > 0.99, \text{CN} > 30, N \le 30$) and dissertational tables were prevented from being frozen as universal architectural laws.
- **L3 — Theory is Active but Non-Doctrinal:** Theory actively structures hypotheses and contrasts, but cannot dictate empirical findings or predetermine signs.
- **L4 — Inferential-Task Jurisdiction:** Econometrics retains monopoly over stochastic admissibility and estimation; other components cannot override econometric verdicts.
- **L5 — No Cross-Method Override:** Qualitative historical analysis or formal modeling cannot alter an empirical rejection.
- **L6 — Project-Specific Content Must Not Leak into Reusable Architecture:** Private dissertation codes ($D_7, D_9, q_t, Q_t^q$) were purged from canonical rules.
- **L7 — Lock Reasoning Obligations, Not Arbitrary Serialization:** Toda–Yamamoto sign comparison was generalized to arbitrary rival theories rather than freezing a rigid 5-row table.
- **L8 — Human Sovereignty:** All cross-domain candidate changes are reported as `PROPOSED — NOT AUTHORIZED`.

## Lessons Newly Learned

1. **Epistemic Inversion Guard:** When an empirical test rejects a long-run equilibrium or null hypothesis, the outcome is strictly a non-finding. A methodology skill must explicitly guard against "epistemic inversion"—the tendency of researchers to interpret empirical failure as positive evidence of unmodeled structural friction (e.g., regime switching or FX constraints).
2. **Three-Tier Variable Gate (Conceptual $\to$ Stochastic $\to$ Empirical):** Variables must pass through three distinct, non-fungible analytical gates:
   - *Conceptual Admissibility:* Does the variable operationalize a legitimate construct?
   - *Stochastic Admissibility:* Does the variable's time-series order match estimator assumptions?
   - *Empirical Disposition:* What did estimation and diagnostics demonstrate?
3. **Exploratory vs. Confirmatory Demarcation:** Conceptual-admissibility gates govern structural/confirmatory estimation. In exploratory mode, data patterns may be inspected for anomaly detection and pattern discovery, but causal mechanism attribution without independent evidence is prohibited.
4. **Conditional Remediation vs. Universal Mandate:** Remediation techniques designed to solve specific econometric pathologies (e.g., FWL interaction residualization for severe collinearity, or LOESS inflection for trend breaks) must not be codified as universal execution mandates for all models, because mathematical orthogonalization alters the substantive interpretation of base parameters.
5. **Decoupling Theory Comparison from Binary Pigeonholing:** Empirical testing of competing hypotheses should not be locked into an "Orthodox vs. Heterodox" binary. Research questions frequently evaluate rival heterodox theories, rival neoclassical theories, or distinct institutional mechanisms.
6. **Subsample Selection Anti-Cherry-Picking:** Periodization windows must distinguish ex-ante independently motivated periodization from ex-post result-responsive selection, requiring post-hoc disclosure and sensitivity reporting for the latter.

## Local-Only Lessons

- The specific Belsley, Kuh, & Welsch condition number threshold ($\text{CN} > 30$) and pairwise correlation ($r > 0.99$) are diagnostic screening heuristics specific to multicollinearity in time-series design matrices. They must not propagate outside quantitative empirical skills.
- The Amiri & Ventelou (2012) reporting table format ($^a$ optimal lag marker, MWALD stats, structural coefficient sum $\sum \hat{\beta}_i$) is local to Toda–Yamamoto Granger causality testing and does not apply to non-time-series econometric skills.

## Proposed Promotions

```text
CANDIDATE LEARNING PROMOTION:
LESSON: Epistemic Inversion Prohibition
PROPOSED SCOPE: DOMAIN & CROSS-DOMAIN
PROPOSED ENFORCEMENT: ARCHITECTURE LOCK & BEHAVIORAL EVAL
DOWNSTREAM CONSUMERS: political-economy-research (D4), heterodox-macro-modeling (D3), academic-paper-reviewer
EVIDENCE: Purge of Rule 2.H.4 in umass-applied-econometrics/SKILL.md. Empirical failure cannot confirm a theoretical prior.
STATUS: PROPOSED — NOT AUTHORIZED

CANDIDATE LEARNING PROMOTION:
LESSON: Three-Tier Variable Screening Architecture (Conceptual -> Stochastic -> Empirical)
PROPOSED SCOPE: DOMAIN
PROPOSED ENFORCEMENT: METHODOLOGICAL PROTOCOL
DOWNSTREAM CONSUMERS: applied-econometrics-pe, academic-paper-reviewer
EVIDENCE: Cointegration Specification Audit Protocol Gates 1-3. Prevents conceptual relevance from overriding stochastic integration order.
STATUS: PROPOSED — NOT AUTHORIZED

CANDIDATE LEARNING PROMOTION:
LESSON: Conditional Remediation vs Universal Execution Distinction
PROPOSED SCOPE: GOVERNANCE
PROPOSED ENFORCEMENT: ARCHITECTURE LOCK
DOWNSTREAM CONSUMERS: All Wave D domain skills and shared protocols
EVIDENCE: Demotion of mandatory FWL interaction residualization. Remediation techniques must not be mandated when they alter parameter semantics.
STATUS: PROPOSED — NOT AUTHORIZED

CANDIDATE LEARNING PROMOTION:
LESSON: Self-Reported Learning Is Not Self-Ratifying
PROPOSED SCOPE: GOVERNANCE
PROPOSED ENFORCEMENT: ARCHITECTURE LOCK
DOWNSTREAM CONSUMERS: D3, D4, D5, D6
EVIDENCE: D2.1 audit caught residual tool-taxonomy regression in Wave-F clause despite claimed L1 inheritance. An agent's statement that a prior lesson was successfully inherited must be validated against the resulting artifact through: PRIOR LESSON -> CLAIMED CONSUMPTION -> ARTIFACT CONSISTENCY CHECK -> ARCHITECT RATIFICATION.
STATUS: PROPOSED — NOT AUTHORIZED
```

## Enforcement Mechanisms

- **Deterministic Tests:**
  - Automated verification that registry components maintain valid runtime paths (`scripts/validate_ars_registry.py`).
  - Automated verification that prose discipline is not owned by econometrics (`scripts/test_prose_discipline.py`).
- **Behavioral Evals (Slated for Wave D5):**
  - Eval test verifying that when an agent is prompted with failed cointegration, it reports a non-finding rather than asserting regime switching (testing Epistemic Inversion Prohibition).
  - Eval test verifying that Toda–Yamamoto routing directs to econometrics while manuscript drafting routes to `academic-paper` / `econ-write`.

## Downstream Consumers

- **Wave D3 (`heterodox-macro-modeling`):** Can formulate mathematical models and closures knowing that applied econometrics will test empirical parameters without dogmatic predetermination or forced regime switching.
- **Wave D4 (`political-economy-research` & source criticism):** Consumes econometric findings under inferential-task jurisdiction, respecting `NO CROSS-METHOD OVERRIDE`.
- **Wave D5 (Adversarial Evals):** Will implement gold eval cases testing the refactored epistemic boundary.
- **Wave D6 (Governance Reconciliation):** Will update registry and routing docs to v1.2.0.
- **Wave F (Physical Migration):** Will execute physical rename to `skills/domain/applied-econometrics-pe/` while preserving protocol semantic typing.

## Unresolved Architect Decisions

- None. All D2.1 architect validation points were implemented and resolved cleanly within the authorized live surface without requiring architectural overreach.

## Self-Improvement Validation Scores

```text
MEMORY:
PASS — Fully consumed and respected all prior locks from Waves B, C, D0, and D1.

CORRECTION:
PASS — Architect lessons and D2-A forensic audit directly reshaped live files: purged Rule H.4, demoted Fordist thresholds, generalized Toda–Yamamoto, deduplicated prose, and resolved residual D2 contradictions in D2.1.

GENERALIZATION:
PASS — Extracted reusable principles (Epistemic Inversion Prohibition, Three-Tier Variable Screening, Exploratory vs Confirmatory Demarcation, Subsample Anti-Cherry-Picking) without globalizing triggering examples.

ENFORCEMENT:
PARTIAL — D2 has correctly identified future behavioral evals and deterministic checks, but the new Wave-D behavioral eval layer is not yet implemented. D5 owns that implementation. Do not claim full behavioral enforcement before those safeguards exist.

TRANSFER:
PASS — The complete D2 audit, before-state ledger, refactor decisions, and learning delta are recorded durably in docs/design/wave-d/D2_APPLIED_ECONOMETRICS_BOUNDARY_REFACTOR.md, enabling future agents to consume lessons without conversational memory.
```
