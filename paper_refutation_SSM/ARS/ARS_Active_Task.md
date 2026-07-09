---
stage: 5
mode: full
run_on_save: false
---

# Orchestration Task: SSM Refutation Paper Pipeline

## Objective
Develop a concise, formal analytical note for *Metroeconomica* demonstrating that the baseline Sraffian Supermultiplier (SSM) fails to achieve long-run convergence when the elasticity of capacity transformation ($\theta$) deviates from unity.

## Execution Rules
You must execute this task in 4 distinct, sequential stages. For each stage, you **MUST** use your internal model-calling tools to route the task to the specific model designated below. 

Save the output of each step to the `ARS/` directory before proceeding to the next step.

---

### Stage 1: Context Extraction & Mathematical Correction
- **Designated Tool/Model:** Gemini Flash (`gemini-1.5-flash` or `gemini-2.0-flash`)
- **Context:** Read the source file `../JMP_DemandAccumulationLR.pdf`.
- **Prompt to Model:** "Extract the core dynamic system of the Marxist Supermultiplier from the JMP, specifically focusing on the Okishio-Harrod investment function and the capacity utilization dynamics. 
CRITICAL MATHEMATICAL CORRECTION: The JMP contains a dimensional error in Equation 3.13. When log-differentiating the investment share $\phi$, the acceleration of capital $\hat{\hat{k}}$ must be divided by $\hat{k}$. The correct dynamic equation for the investment share is: 
$\hat{\phi} = \frac{1}{\mu - 1}\hat{\mu} + (1 - \theta)\gamma(\mu - 1)$.
Extract the $\hat{\mu}$ nullcline and the definition of $\theta$ as the elasticity of productive capacity with respect to capital. Exclude all institutional details, Marxist taxonomy, and microfoundations of distributive conflict."
- **Action:** Save the model's response to `ARS/01_Extracted_Math.md`.

### Stage 2: Formal Mathematical Proof
- **Designated Tool/Model:** OpenAI Reasoning (`o3-mini` or `o1`)
- **Context:** Read the file `ARS/01_Extracted_Math.md`.
- **Prompt to Model:** "Using the corrected dynamic system provided in the context, provide a rigorous step-by-step mathematical proof demonstrating that under unbalanced growth ($\xi \neq 0$), the system has no interior steady state. 
Specifically:
1. Set $\hat{\phi} = 0$ and isolate $\hat{\mu}$ using the dynamic equation $\hat{\phi} = \frac{1}{\mu - 1}\hat{\mu} + \xi$ to show that $\hat{\mu} = (\mu - 1)(-\xi)$.
2. Show that for a steady state, the growth rate of utilization must be zero ($\hat{\mu} = 0$).
3. Evaluate the system's nullclines. Show that setting $\hat{\mu} = 0$ and $\hat{\phi} = 0$ in the capacity utilization dynamics yields the condition $\mu - 1 = \frac{g_z + \xi}{\gamma}$.
4. Demonstrate the contradiction: setting $\hat{\mu} = 0$ requires $\mu^* = 1$ (since $\xi \neq 0$). Substituting $\mu^* = 1$ into the nullcline condition yields $\xi = -g_z$. However, at $\mu = 1$, the dynamic equation for $\phi$ has a division by zero singularity ($\frac{1}{\mu - 1}$ coefficient). Thus, $\mu = 1$ is mathematically invalid as a steady state in this system.
5. Conclude that if $\xi \neq 0$, no interior steady state exists, and capacity utilization rate must diverge.
Format strictly in LaTeX. Do not introduce heterogeneous demand or endogenous distribution; focus entirely on $\xi$."
- **Action:** Save the model's response to `ARS/02_Mathematical_Proof.md`.

### Stage 3: LaTeX Manuscript Drafting (CRITICAL FRAMING)
- **Designated Tool/Model:** Together AI - Llama 3.1 405B (`meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`)
- **Context:** Read TWO files: 
  1. `ARS/02_Mathematical_Proof.md` (The mathematical core)
  2. `ARS/Metroeconomica_Style_Guide.md` (The strict formatting rulebook)
- **Prompt to Model:** "Draft a complete academic manuscript in flawless LaTeX for *Metroeconomica*. 
Title: 'Unbalanced Growth and the Long-Run Limits of the Sraffian Supermultiplier: A Note on Capacity Transformation'.

CRITICAL INSTRUCTIONS FOR THEORETICAL FRAMING:
1. **The Role of $\xi$:** You MUST explicitly define $\xi$ not as an arbitrary accounting parameter, but as the constant growth rate of the capital-capacity ratio $v$ (where $\hat{v} = \xi \neq 0$). It represents the long-run presence of technical change and structural bottlenecks (where capital accumulation does not translate 1:1 into capacity expansion).
2. **Bracketing Endogeneity:** Explicitly state in the model setup that while $\xi$ is ultimately shaped by distributive conflict and induced technical change, this note treats $\xi$ as a given structural parameter to isolate its pure macroeconomic effect on the supermultiplier's convergence, leaving the endogeneity mechanism for future research.
3. **The Core Proof:** Integrate the mathematical proof from `02_Mathematical_Proof.md` seamlessly. Show that $\xi \neq 0$ structurally prevents the SSM from achieving long-run convergence due to the singularity at $\mu = 1$.
4. **Tone:** Maintain a highly formal, objective, and mathematically precise tone. Strictly adhere to the Metroeconomica style guide for propositions and proofs."
- **Action:** Save the model's response to `ARS/03_Draft_Manuscript.tex`.

### Stage 4: Mock Peer Review
- **Designated Tool/Model:** Together AI - Qwen 2.5 72B (`Qwen/Qwen2.5-72B-Instruct-Turbo`)
- **Context:** Read the file `ARS/03_Draft_Manuscript.tex`.
- **Prompt to Model:** "Act as a strict Referee 2 for Metroeconomica. Review this LaTeX manuscript. Evaluate: 
1) Mathematical Rigor (is the corrected derivation of $\hat{\phi}$ and the proof of non-convergence logically sound?). 
2) Economic Intuition (is the framing of $\xi$ as the constant growth rate of the capital-capacity ratio representing long-run technical change convincing, and is the decision to bracket out endogenous distribution well-justified for a short note?). 
3) Literature engagement. 
Provide a detailed referee report with specific, actionable revisions."
- **Action:** Save the model's response to `ARS/04_Peer_Review_Report.md`.

---

## Final Step
Once all 4 stages are complete and the files are saved, update the frontmatter of this file to `stage: 5` and output a brief summary of the pipeline execution.