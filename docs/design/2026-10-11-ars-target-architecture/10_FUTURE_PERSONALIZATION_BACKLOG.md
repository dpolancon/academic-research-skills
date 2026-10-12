# ARS Future Personalization Backlog & Shell Architecture

**Document ID:** `10_FUTURE_PERSONALIZATION_BACKLOG.md`  
**Status:** NON-BLOCKING FUTURE DESIGN BACKLOG  
**Date:** 2026-10-12  
**Scope:** Design specification for user personalization, authorial calibration, and institutional persona shells  
**Implementation State:** NOT IMPLEMENTED (Future Architecture / Non-blocking for Wave B)

---

## 1. Executive Summary & Design Scope

The ARS core architecture is intentionally generic and domain-neutral. However, scholarly research workflows often require fine-grained calibration to specific authorial voices, advisor expectations, dissertation committee preferences, and venue-specific editorial standards.

This document records the prospective architecture for **Personalized ARS Shells**. It establishes how researchers can eventually construct and maintain personalized profiles without modifying core skill code, compromising repository hygiene, or introducing ungrounded persona hallucinations.

> [!IMPORTANT]
> This document is a non-blocking future backlog item. No schemas, agent code, profile directories, or runtime dependencies are created in Wave B0 or Wave B1. Implementation is strictly deferred until future human authorization.

---

## 2. Personalized Shell Taxonomy

Future personalization will be organized into four distinct profile shell archetypes:

1. **Author Profile Builder (`profiles/author/<scholar-id>`):**
   - Calibrates authorial voice, stylistic habits, preferred theoretical idioms, argumentative velocity, and Spanish-English bilingual phrasing defaults.
   - Distinct from core manuscript logic in `academic-paper`.
2. **Advisor Shell (`profiles/advisors/<advisor-id>`):**
   - Encapsulates durable scholarly guidance heuristics (e.g. simplicity, forensic replication standards, Marglin macro grounding, aversion to black-box mechanisms).
   - Distinct from dissertation chapter-specific project overlays.
3. **Committee Shell (`profiles/committees/<institution-field>`):**
   - Represents the composite multi-perspective expectations of specific departmental defense committees (e.g. UMass Amherst political economy defense committee personas: Ash, Basu, Young).
4. **Prospective Editor / Referee Shell (`profiles/venues/<venue-id>` or `profiles/referees/<referee-id>`):**
   - Calibrates peer review panels and editorial standards against specific journal editorial boards or public intellectual venues (e.g. Jacobin América Latina vs Cambridge Journal of Economics).

---

## 3. Approved Corpus Evidence Sources

To prevent superficial or stereotype-driven persona modeling, profile construction must be grounded in an approved scholarly corpus. Permissible evidence sources include:

- **Authored Peer-Reviewed Manuscripts:** High-confidence evidence for empirical methodology, model formulation, and stylistic cadence.
- **Methodological Articles & Syllabi:** Definitive evidence for pedagogical rules, statistical standards, and preferred analytical frameworks.
- **Published Editorials & Public Essays:** Evidence for normative framing, policy translation, and vocabulary discipline.
- **Transcribed Public Lectures & Academic Interviews:** Evidence for conversational heuristics and diagnostic reactions.
- **Direct Written Supervisory Feedback:** Explicit annotations and revisions on student drafts (when legitimately available and authorized for private use).
- **Official Referee Reports:** Peer review reports from past submission rounds.

---

## 4. Epistemic Confidence & Invariant Hierarchy

Profiles must not fabricate an academic's likely opinion merely because a sparse text corpus is supplied. Every inferred preference in a profile must be tagged with an explicit epistemic status:

| Epistemic Classification | Definition | Application Standard |
| :--- | :--- | :--- |
| **`DIRECTLY_OBSERVED_PREFERENCE`** | Verbatim written guidance, explicit rule in a syllabus, or direct feedback memo. | Can be enforced as a hard review or drafting gate. |
| **`SUPPORTED_INFERENCE`** | Pattern systematically observed across multiple published papers or lectures. | Applied as advisory guidance with explicit citations. |
| **`WEAK_INFERENCE`** | Plausible extrapolation from theoretical school or co-author tradition. | Must be labeled as hypothetical; cannot block workflow gates. |
| **`UNKNOWN`** | Preference on a topic where corpus contains no direct or inferential evidence. | Agent must explicitly declare ignorance and prompt the user rather than guess. |

---

## 5. Provenance & Attribution Schema

When profile construction is implemented, every preference record must support structured metadata:

```yaml
preference_id: "ash_marglin_grounding"
profile_id: "profiles/advisors/michael-ash"
epistemic_status: "DIRECTLY_OBSERVED_PREFERENCE"
claim: "Every macro-econometric model must be grounded in an explicit accounting or growth framework (Marglin tradition)."
confidence: 0.95
scope: "empirical_macroeconomics"
provenance:
  source: "Dissertation supervisory memo / ECON 700 syllabus"
  location: "Section 3.2, p. 4"
  date: "2024-09-15"
  author: "Michael Ash"
```

---

## 6. Privacy, Security & Boundary Isolation

Personalization data must respect three strict isolation boundaries:

1. **Public Reusable Profiles (`profiles/public/`):**
   - Generic profiles based entirely on published, open-access academic writings.
   - May be shared in public repositories and upstream distributions.
2. **Private User Profiles (`profiles/private/`):**
   - Calibrations derived from private supervisor feedback, unpublished student drafts, or internal department communications.
   - Must be gitignored (`.gitignore` rule: `profiles/private/`) to prevent unintended repository leakage.
3. **Project-Specific Overlays (`projects/<project-id>/`):**
   - Ephemeral working notes, specific equation discussions, and chapter draft refutations (e.g. Chapter 1 land-rent specifics).
   - Stored in the project's own repository, completely outside the canonical ARS monorepo.

---

## 7. User-Facing Guide: Building a Custom Shell

A non-technical researcher should eventually be able to construct their own ARS shell via a straightforward 3-step workflow without modifying core skills:

1. **Corpus Assembly:** Place 3–5 representative papers or feedback memos in a local folder.
2. **Profile Generation:** Run the prospective `ars-profile-builder` CLI command to extract preferences into `profiles/author/<my-name>.yaml`.
3. **Execution Routing:** Pass `--profile <my-name>` to `academic-pipeline` or set `ARS_ACTIVE_PROFILE=<my-name>` in `.env`.

---

## 8. Explicit Non-Goals for the Current Roadmap

The following tasks are explicitly **out of scope** for Wave B and will not be started without separate human authorization:
- No physical profile files or directories created.
- No automated profiling scripts or scraping tools implemented.
- No modifications to `academic-paper` or `academic-paper-reviewer` to parse external profile schemas.
- No dependency on personalization is introduced into the Wave B capability routing contract.
