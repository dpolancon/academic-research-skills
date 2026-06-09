# Cross-Model Verification Protocol (v3.0)

## Overview

This protocol enables optional cross-model verification for high-stakes AI judgments. When enabled, a second AI model independently reviews outputs from the primary model, reducing shared-bias blind spots.

**This is entirely optional.** All ARS skills work with the primary Claude model alone. Cross-model verification is an additional layer for users who want higher confidence in integrity checks, devil's advocate challenges, and review judgments.

**Consent boundary:** Before unpublished manuscripts, private notes, corpus text,
reviewer comments, decision letters, response letters, or other review material
is sent to an external provider, the agent must identify the provider, model,
and content class that would be sent, then obtain explicit user consent. An
environment variable alone is not consent to upload user content. If consent is
not granted, continue with single-model verification.

## Why Cross-Model Verification

A stress test of 68 AI-generated citations found 31% had problems — and all passed three rounds of same-model integrity checks. The root cause: the verifying AI and the generating AI share the same training data distribution, so they share the same blind spots. A different model (trained on overlapping but not identical data, with different RLHF tuning) can catch errors that the primary model systematically misses.

**What it improves:** Error rate reduction (estimated 31% → ~5-10%). Different models catch different types of hallucination patterns.

**What it doesn't solve:** Frame-lock (all LLMs share most training data), sycophancy (all RLHF models have this tendency). These are degree improvements, not kind improvements.

## Supported Models

| Model | API ID | Provider | Best For |
|-------|--------|----------|----------|
| Claude Opus 4.8 | _(inherited Claude Code session model)_ | Anthropic | Primary model (default for all ARS skills) |
| GPT-5.4 Pro | `gpt-5.4-pro` | OpenAI | Cross-verification — strongest reasoning |
| GPT-5.4 | `gpt-5.4` | OpenAI | Cross-verification — balanced cost/performance |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | Google | Cross-verification — strong at factual verification |

**Recommended cross-verification pair:** Claude Opus 4.8 (primary) + GPT-5.4 Pro or Gemini 3.1 Pro (verifier).

Using two non-Anthropic models as primary+verifier is possible but not tested with ARS prompts.

## Setup Guide

### Prerequisites

You need API keys from at least one additional provider. ARS itself runs inside Claude Code, so Claude is always available as the primary model.

### Step 1: Get API Keys

**OpenAI (GPT-5.4):**
1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key (starts with `sk-`)

**Google (Gemini 3.1 Pro):**
1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Create a new API key
3. Copy the key (starts with `AIza`)

### Step 2: Set Environment Variables

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
# Optional: Cross-model verification for ARS
export OPENAI_API_KEY="<your-openai-api-key>"
export GOOGLE_AI_API_KEY="<your-google-ai-api-key>"

# Choose your preferred cross-verification model
# Options: gpt-5.4-pro, gpt-5.4, gemini-3.1-pro-preview
export ARS_CROSS_MODEL="gpt-5.4-pro"
```

Then reload: `source ~/.zshrc`

### Step 3: Verify Setup

In Claude Code, you can test by asking:
```
Check if cross-model verification is available for ARS
```

The system will check for the environment variables and report which models are available.

### Step 4: Enable Per-Session (Optional)

If you don't want cross-model verification running all the time, you can enable it per session:

```bash
# Enable for this session only
export ARS_CROSS_MODEL="gpt-5.4-pro"

# Disable for this session
unset ARS_CROSS_MODEL
```

## How It Works in Each Skill

### Integrity Verification (academic-pipeline, Stage 2.5 / 4.5)

**When `ARS_CROSS_MODEL` is set:**
- Primary model (Claude) runs full Phase A-E verification as normal
- After Phase A completes, a random 30% sample of references is sent to the cross-model for independent verification
- Cross-model receives only the reference text and paper context — not Claude's verification result (to prevent anchoring)
- Disagreements are flagged as `[CROSS-MODEL-DISAGREEMENT]` and prioritized for human review

**When `ARS_CROSS_MODEL` is not set:**
- Standard single-model verification (unchanged from v2.7+)

**Implementation for agents:**

When the integrity_verification_agent detects `ARS_CROSS_MODEL` in the environment, it should:

1. Complete Phase A verification normally
2. Select 30% of references randomly (minimum 5, maximum 15). If total references < 5, sample all of them.
3. Issue **one API call per reference** — not a batch. (Batching hides which reference the model actually grounded: a single grounding-metadata trace on a 5-reference response proves *something* was searched, not that *each* reference was. One reference per call makes the grounding evidence 1:1 with the verdict.) For each reference, construct a verification prompt:
   ```
   Verify this academic reference. Check: Does it exist? Are the author
   names, year, title, journal, and DOI correct? Search the web to
   confirm — do not answer from memory.

   Respond with exactly one verdict:
   - VERIFIED  — found online; include at least one source URL or DOI you found
   - MISMATCH  — found, but a field is wrong (state which); include the source
   - NOT_FOUND — searched, no matching record exists
   - NOT_SEARCHED — you could not actually search the web for this reference

   Reference: [full reference text] — Context: [sentence where cited]
   ```
   A `VERIFIED` verdict with no accompanying source URL/DOI is treated as `NOT_SEARCHED` (the model claimed a result it cannot evidence).
4. Send to the cross-model via the appropriate API (see API Call Patterns below). **The call patterns enable the provider's web-search/grounding tool and reject the response as `NOT_SEARCHED` when the API returns no grounding evidence** — a model that ignores the "search the web" instruction cannot fake an absent grounding trace, so this is the real safety boundary, not the prompt wording.
5. Compare results: if Claude said VERIFIED but cross-model said NOT_FOUND or MISMATCH, flag as `[CROSS-MODEL-DISAGREEMENT]`. Treat `NOT_SEARCHED` / ungrounded exactly as **not verified** — it never counts as agreement with a Claude `VERIFIED`, and a sample that returns `NOT_SEARCHED` is surfaced for re-run or human review, never silently passed.
6. Include disagreements in the integrity report under a new section:
   ```markdown
   ### Cross-Model Verification Results
   - References sampled: X/Y (Z%)
   - Agreements: N
   - Disagreements: M (listed below, prioritized for human review)
   - Ungrounded (NOT_SEARCHED): U (the cross-model could not actually search — these are NOT confirmations; re-run or human-review)

   | # | Reference | Claude | Cross-Model | Source (URL/DOI) | Status |
   |---|-----------|--------|-------------|------------------|--------|
   ```
   The `Source` column carries the URL/DOI the cross-model returned for a `VERIFIED` row; a blank source on a `VERIFIED` verdict downgrades it to `NOT_SEARCHED`.

### Devil's Advocate (deep-research + academic-paper-reviewer)

**When `ARS_CROSS_MODEL` is set:**
- After the DA completes its standard review/checkpoint, the cross-model receives the same material and generates an independent critique
- The DA then compares: any CRITICAL or MAJOR issues found by the cross-model but not by the DA are added as `[CROSS-MODEL-FINDING]`
- This directly addresses frame-lock — a different model may attack from a different angle

**When `ARS_CROSS_MODEL` is not set:**
- Standard single-model DA (unchanged)

**Implementation:**

The DA agent, after completing its checkpoint report, should:

1. Send the reviewed material + a simplified DA prompt to the cross-model:
   ```
   You are a devil's advocate reviewing this [research/paper].
   Find the 3 most serious weaknesses. For each, state:
   - What the weakness is
   - Why it matters
   - What the strongest counter-argument would be

   Material: [the reviewed content]
   ```
2. Compare cross-model findings with own findings
3. Any cross-model finding not already covered → add to report as `[CROSS-MODEL-FINDING]`
4. Log: `[CROSS-MODEL: X findings received, Y novel (not in primary DA report)]`

### Peer Review (academic-paper-reviewer) — Future

> **Status: Planned, not yet implemented.** No agent currently owns the 6th reviewer behavior. This will be added in a future version, likely as a cross-model section in `eic_agent.md`. For now, cross-model verification in peer review is limited to the DA's independent critique (above).

**Planned behavior when `ARS_CROSS_MODEL` is set:**
- Cross-model acts as an additional independent reviewer (6th reviewer)
- Its scores are shown separately, not averaged into the existing 5-reviewer consensus
- Significant score divergence (>15 points on any dimension) is flagged

## Python-Based Cross-Model Client (`cross_model_client.py`)

To decouple the shell/curl commands, ARS uses a unified Python client at [cross_model_client.py](file:///c:/ReposGitHub/academic-research-skills/scripts/cross_model_client.py). This wrapper programmatically interfaces with Together AI (Qwen) and Gemini via the `llm_gateway.py` client and performs searches on bibliographic indexes using python clients (`crossref_client.py`, `openalex_client.py`, `arxiv_client.py`, and `semantic_scholar_client.py`).

### Commands

1. **Verify Academic Citation**:
   ```bash
   python scripts/cross_model_client.py verify \
     --reference "Author, A. (Year). Title. Journal, Vol(Issue), Page-Page." \
     --context "The sentence where the reference is cited in the paper." \
     --override-provider together \
     --override-model Qwen/Qwen2.5-72B-Instruct-Turbo
   ```

2. **Devil's Advocate Critique**:
   ```bash
   python scripts/cross_model_client.py critique \
     --material "Your manuscript draft or outline content to be challenged." \
     --override-provider gemini \
     --override-model gemini-1.5-pro
   ```

### API Call Patterns (SDK-Based Alternatives)

While raw `curl` commands were initially designed to demonstrate REST execution:
- **Together AI (OpenAI-compatible) and Gemini API routing** is handled directly via `scripts/llm_gateway.py`.
- **Bibliographic tool-calling** is natively executed as standard functions parsed and executed within `cross_model_client.py`.

> **Why `temperature: 0.1`:** reference existence/metadata checking is a deterministic factual task, so low temperature reduces run-to-run variance in the verdict. It is not a grounding control — the grounding guard above is what enforces an actual lookup.

### Detecting Available Models

Agents should check at the start of a verification/review session:

```bash
# Check which cross-model APIs are available
# Requires: jq (for JSON parsing). Fallback: python3 -c "import sys,json; ..."
if ! command -v jq &>/dev/null; then
  echo "WARNING: jq not installed. Cross-model API calls will use python3 fallback."
fi

if [ -n "$ARS_CROSS_MODEL" ]; then
  case "$ARS_CROSS_MODEL" in
    gpt-5.4*) 
      [ -n "$OPENAI_API_KEY" ] && echo "CROSS_MODEL_AVAILABLE=openai" \
        || echo "WARNING: ARS_CROSS_MODEL=$ARS_CROSS_MODEL but OPENAI_API_KEY is not set" ;;
    gemini*) 
      [ -n "$GOOGLE_AI_API_KEY" ] && echo "CROSS_MODEL_AVAILABLE=google" \
        || echo "WARNING: ARS_CROSS_MODEL=$ARS_CROSS_MODEL but GOOGLE_AI_API_KEY is not set" ;;
    *) echo "WARNING: ARS_CROSS_MODEL=$ARS_CROSS_MODEL is not a supported model. Supported: gpt-5.4, gpt-5.4-pro, gemini-3.1-pro-preview"
       echo "CROSS_MODEL_AVAILABLE=none" ;;
  esac
else
  echo "CROSS_MODEL_AVAILABLE=none"
fi
```

If `ARS_CROSS_MODEL` is set but the corresponding API key is missing or the model name is unsupported, the agent should warn the user and proceed with single-model verification.

## Cost Considerations

Cross-model verification adds API costs from the second provider:

| Scenario | Additional Calls | Estimated Additional Cost |
|----------|-----------------|--------------------------|
| Integrity verification (60 refs → 30% = 18, capped at max 15; **one call per reference**) | ~15 calls | ~$1.15-2.35 |
| DA cross-check (1 per checkpoint, 3 checkpoints) | 3 calls | ~$0.30-0.50 |
| Peer review (planned, not yet implemented) | — | — |
| **Full pipeline** | **~18 calls** | **~$1.45-2.85** |

These are rough estimates based on GPT-5.4 Pro pricing ($5/1M input, $20/1M output) and typical prompt sizes. One-call-per-reference (rather than batching) is a deliberate cost-for-provenance trade: it is the only way the grounding-evidence check maps 1:1 to each verdict. Web-search-tool calls also cost more than plain completions.

## Limitations

1. **Does not solve frame-lock fully.** All major LLMs share substantial training data. Cross-model catches different surface errors but may share deep structural biases.
2. **API latency.** Cross-model calls add 2-5 seconds per call, plus web-search round-trip time. With one call per reference (no batching) and a web-search tool, integrity verification of up to 15 sampled references (the sample cap) adds several minutes; the calls can be issued concurrently to bound wall-clock time.
3. **Response format differences.** Different models structure responses differently. The agent must parse varied formats — keep verification prompts simple and structured to minimize parsing issues.
4. **Cost scales with paper size.** Longer papers with more references = more cross-model calls.

## Graceful Degradation

If cross-model verification fails **at the transport level** (API error, rate limit, key expired):
- Log the failure: `[CROSS-MODEL-ERROR: reason]`
- Continue with single-model verification — never block the pipeline on cross-model failure
- Include a note in the report: "Cross-model verification was configured but unavailable for this run. Results are single-model only."

A `NOT_SEARCHED` result is **not** a transport failure and is handled differently. It means the call succeeded but the model could not (or did not) ground the lookup, so its verdict carries no evidence. Do not fall back to single-model and do not treat it as agreement: record the reference as `NOT_SEARCHED` in the results table, count it separately from agreements/disagreements, and surface it for re-run or human review. The distinction matters — a transport failure means "we have no cross-model opinion"; a `NOT_SEARCHED` means "the cross-model gave an opinion we have decided not to trust as a confirmation."
