# Academic Research Skills (ARS) Standalone Pipeline

Academic Research Skills (ARS) is a standalone, cross-model, and repository-agnostic Python pipeline designed to automate and verify the academic research lifecycle. ARS operates independently of any specific developer client and can run on any execution runner (such as CLI, Codex, or Antigravity).

---

## Key Features

- **Orchestration Agnostic**: Run the research pipeline from any terminal or environment as a direct Python command.
- **Multi-Model Gateway**: Seamlessly route queries to Together AI (e.g. Qwen models) and native Google Gemini APIs with built-in structured function/tool-calling support.
- **Obsidian Vault UI Integration**: Turns any Obsidian Vault into your front-end UI. Real-time file watching (`watchdog`) listens for saves to `ARS_Active_Task.md` and automatically runs pipeline stages. Delivers outputs organized by category with automatic Obsidian Wikilink (`[[Link]]`) connections for graph visualization.
- **Cross-Repo Execution & Fencing**: Run the pipeline against *any* directory on your system using the `--target-dir` flag. Scoped-write directory fencing prevents any file access or edits from leaking outside your target workspace.

---

## Installation & Prerequisites

To run the pipeline locally, install the required Python packages:

```bash
pip install openai google-generativeai watchdog pyyaml
```

*Note: Ensure your Python environment is version 3.8 or higher.*

---

## Credential & Configuration Management

ARS resolves model, provider, and endpoint configurations using a strict priority-based hierarchy.

### Configuration Priority Resolution
1. **CLI Flags (Highest Priority)**:
   - `--model` / `--override-model`: Specify the LLM model ID.
   - `--provider` / `--override-provider`: Specify the API provider (`together` or `gemini`).
   - `--base-url`: Specify Together AI (OpenAI-compatible) endpoint URL.
2. **Environment Variables**:
   - `DEFAULT_MODEL`: Fallback model ID.
   - `DEFAULT_PROVIDER`: Fallback provider ID.
3. **Configuration File**:
   - Parsed from `agent_config.yaml` if it exists in the repository root or passed via `--config`.
4. **Hardcoded Fallbacks (Lowest Priority)**:
   - Default Provider: `together`
   - Default Model: `Qwen/Qwen3.5-9B`
   - Default Together base URL: `https://api.together.ai/v1`

### Setting API Keys
Set your provider API keys in your environment variables:

```bash
export TOGETHER_API_KEY="your-together-api-key"
export GEMINI_API_KEY="your-gemini-api-key"
```

#### Gitignored Key Fallback
For local testing convenience, if `TOGETHER_API_KEY` is not present in the environment, the gateway will attempt to read keys from `docs/together_AI_baseURL_APIKEY.txt`. Ensure this file is formatted as:
```text
TOGETHER_API_KEY=your-api-key
TOGETHER_BASE_URL=https://api.together.ai/v1
```
*Note: This file is protected and listed in `.gitignore` to prevent key leakage.*

---

## Usage Examples

### 1. Run the Pipeline Dashboard (Interactive CLI)
Runs the interactive dashboard where you can check status, start stages, jump to specific points, or pause execution:

```bash
python scripts/run_pipeline.py --target-dir C:\Users\User\Projects\MacroeconomicsRepo
```

### 2. Pointing to an External Workspace
Execute the pipeline against a different directory path:

```bash
python scripts/run_pipeline.py --target-dir C:\Users\User\Projects\ChileanInequalityRepo
```

### 3. Run in Obsidian Vault Mode
Watches the vault and triggers automatically when the active note is saved:

```bash
python scripts/run_pipeline.py --target-dir C:\Users\User\Obsidian\MyResearchVault --obsidian-vault
```

#### Obsidian Active Task Format
Write prompts and configure settings in `ARS/ARS_Active_Task.md` inside the target directory:
```markdown
---
stage: 1
mode: socratic
run_on_save: true
---

I want to review the literature regarding AI-driven central banking tools and financial stability.
```
When `run_on_save: true` is present in the frontmatter, saving the file will automatically trigger the pipeline. The runner will update the frontmatter to the next stage and toggle `run_on_save` to `false` upon completion to prevent execution loops.

### 4. Overriding Models on the Fly
Use CLI overrides to bypass configuration files:

```bash
python scripts/run_pipeline.py \
  --target-dir C:\Users\User\Projects\MacroeconomicsRepo \
  --provider gemini \
  --model gemini-1.5-pro
```

---

## Pipeline Overview (10-Stage State Machine)

The orchestrator enforces the 10-stage lifecycle defined in [pipeline_state_machine.md](file:///c:/ReposGitHub/academic-research-skills/academic-pipeline/references/pipeline_state_machine.md). State data, timestamps, and history are recorded atomically inside `passport.yaml` at your target workspace:

```
  Stage 1 (RESEARCH)      -> Generates RQ Brief & Methodology Blueprint
         ↓
  Stage 2 (WRITE)         -> Generates Manuscript Draft
         ↓
  Stage 2.5 (INTEGRITY)   -> Pre-Review citation, reference & claim checks (Mandatory Gate)
         ↓
  Stage 3 (REVIEW)        -> Generates Peer Review reports & EIC Decision
         ↓
  Stage 4 (REVISE)        -> Generates Revised Draft & Response to Reviewers
         ↓
  Stage 3' (RE-REVIEW)    -> EIC verification. Can route to Stage 4' if decision is Major
         ↓
  Stage 4' (RE-REVISE)    -> Performs last round of revisions (if requested)
         ↓
  Stage 4.5 (FINAL CHECK) -> Final citation & reference integrity checks (Mandatory Gate)
         ↓
  Stage 5 (FINALIZE)      -> Converts draft to final manuscript layout
         ↓
  Stage 6 (COMPLETED)     -> Final paper produced successfully
```

---

## Companion Tools

1. **Verify Citation**:
   Verify an academic reference against online databases (Crossref, OpenAlex, Semantic Scholar, arXiv):
   ```bash
   python scripts/cross_model_client.py verify \
     --reference "Walters, W. H. (2023). Fabrication in ChatGPT citations. Scientific Reports, 13, 14045." \
     --context "ChatGPT citations are often fabricated (Walters, 2023)."
   ```

2. **Devil's Advocate Critique**:
   Stress-test your research arguments and retrieve counter-arguments:
   ```bash
   python scripts/cross_model_client.py critique \
     --material "Your manuscript draft or outline content here."
   ```

---

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
