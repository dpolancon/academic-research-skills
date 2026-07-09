#!/usr/bin/env python3
"""Orchestrates the 7-agent mock peer review panel for the SSM refutation paper.

Reads the manuscript and runs:
1. Field Analyst
2. Panel Reviewers (EIC, Methodology, Domain, Perspective, Devil's Advocate)
3. Editorial Synthesizer
"""

import os
import sys
import re
from pathlib import Path

# Add root folder to sys.path to import LLMGateway
root_dir = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from scripts.llm_gateway import LLMGateway

# Paths
ars_dir = Path(__file__).resolve().parent.parent
manuscript_file = ars_dir / "03_Draft_Manuscript.tex"
field_report_file = ars_dir / "05_Field_Analysis_Report.md"
panel_reports_file = ars_dir / "05_Reviewer_Panel_Reports.md"
decision_package_file = ars_dir / "05_Editorial_Decision_Package.md"

# Model Selection
DEFAULT_MODEL = "Qwen/Qwen2.5-72B-Instruct-Turbo"
REASONING_MODEL = "Qwen/QwQ-32B"  # or Qwen/Qwen2.5-72B-Instruct-Turbo

def load_agent_prompt(agent_name: str) -> str:
    """Locates and parses the markdown agent definition to return the system prompt."""
    agent_folders = [
        root_dir / "deep-research" / "agents",
        root_dir / "academic-paper" / "agents",
        root_dir / "academic-paper-reviewer" / "agents",
        root_dir / "academic-pipeline" / "agents"
    ]
    
    for folder in agent_folders:
        file_path = folder / f"{agent_name}.md"
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Parse YAML frontmatter
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        return parts[2].strip()
                return content.strip()
    
    raise FileNotFoundError(f"Agent prompt file for '{agent_name}' not found.")

def main():
    print("[*] Initializing LLM Gateway...")
    gateway = LLMGateway(default_provider="together", default_model=DEFAULT_MODEL)
    
    if not manuscript_file.exists():
        print(f"[!] Error: Manuscript file {manuscript_file} not found.")
        sys.exit(1)
        
    with open(manuscript_file, "r", encoding="utf-8") as f:
        manuscript_content = f.read()
        
    # --- PHASE 0: FIELD ANALYSIS ---
    print("\n[*] Phase 0: Running Field Analyst...")
    field_analyst_prompt = load_agent_prompt("field_analyst_agent")
    user_prompt = f"Perform field analysis on this manuscript and output the configuration cards:\n\n{manuscript_content}"
    
    response = gateway.generate(
        agent_name="field_analyst_agent",
        system_prompt=field_analyst_prompt,
        user_prompt=user_prompt,
        override_model=DEFAULT_MODEL
    )
    
    field_report = response.get("content", "")
    with open(field_report_file, "w", encoding="utf-8") as f:
        f.write(field_report)
    print(f"[+] Saved Field Analysis Report to {field_report_file}")
    
    # --- PHASE 1: PANEL REVIEW ---
    print("\n[*] Phase 1: Dispatching 5 Panel Reviewers...")
    
    # Load reviewer agent prompts
    eic_prompt = load_agent_prompt("eic_agent")
    methodology_prompt = load_agent_prompt("methodology_reviewer_agent")
    domain_prompt = load_agent_prompt("domain_reviewer_agent")
    perspective_prompt = load_agent_prompt("perspective_reviewer_agent")
    da_prompt = load_agent_prompt("devils_advocate_reviewer_agent")
    
    # Enforce heterodox economics guidelines specifically in Methodology and Domain prompts
    heterodox_checklist = (
        "\n\n### METROECONOMICA & HETERODOX ECONOMIC AUDIT GUIDELINES:\n"
        "1. Verify handling of vector field singularity at capacity utilization \\mu = 1. "
        "Confirm that proper dynamic limits (L'Hopital's rule or desingularization) are applied.\n"
        "2. Check that the capital-capacity ratio growth rate \\xi(\\pi) = q^*(\\pi) - f(q^*(\\pi)) is derived from "
        "cost minimization under a Sraffian distributive schedule, and that endogenous distribution is bracketed appropriately.\n"
        "3. Ensure the dynamic stability / instability proof is mathematically rigorous near boundary conditions.\n"
        "4. Confirm that theorems/propositions use standard LaTeX structures (`\\begin{proposition}`, `\\begin{proof}`)."
    )
    methodology_prompt += heterodox_checklist
    domain_prompt += heterodox_checklist
    
    reviewers = [
        ("EIC", "eic_agent", eic_prompt, DEFAULT_MODEL),
        ("Methodology Reviewer (R1)", "methodology_reviewer_agent", methodology_prompt, DEFAULT_MODEL),
        ("Domain Reviewer (R2)", "domain_reviewer_agent", domain_prompt, DEFAULT_MODEL),
        ("Perspective Reviewer (R3)", "perspective_reviewer_agent", perspective_prompt, DEFAULT_MODEL),
        ("Devil's Advocate", "devils_advocate_reviewer_agent", da_prompt, REASONING_MODEL)
    ]
    
    reports = []
    
    for label, name, sys_prompt, model in reviewers:
        print(f"  [*] Running {label} ({name})...")
        user_msg = (
            f"Review the following manuscript content under the guidelines in your system prompt.\n"
            f"Refer to the configured reviewer role from the Field Analysis Report.\n\n"
            f"Field Analysis Context:\n{field_report}\n\n"
            f"Manuscript:\n{manuscript_content}"
        )
        
        resp = gateway.generate(
            agent_name=name,
            system_prompt=sys_prompt,
            user_prompt=user_msg,
            override_model=model
        )
        content = resp.get("content", "")
        reports.append((label, content))
        print(f"  [+] Completed {label}")
        
    # Consolidate reports
    consolidated_reports = ""
    for label, content in reports:
        consolidated_reports += f"# Reviewer: {label}\n\n{content}\n\n---\n\n"
        
    with open(panel_reports_file, "w", encoding="utf-8") as f:
        f.write(consolidated_reports)
    print(f"[+] Saved Panel Review Reports to {panel_reports_file}")
    
    # --- PHASE 2: EDITORIAL SYNTHESIS ---
    print("\n[*] Phase 2: Running Editorial Synthesizer...")
    synthesizer_prompt = load_agent_prompt("editorial_synthesizer_agent")
    
    synth_user_msg = (
        f"Consolidate and synthesize the following 5 peer reviewer reports for the manuscript.\n"
        f"Identify consensus, resolve disagreements, and produce a unified Editorial Decision Letter and a prioritized Revision Roadmap.\n\n"
        f"Reviewer Reports:\n{consolidated_reports}\n\n"
        f"Manuscript:\n{manuscript_content}"
    )
    
    resp = gateway.generate(
        agent_name="editorial_synthesizer_agent",
        system_prompt=synthesizer_prompt,
        user_prompt=synth_user_msg,
        override_model=DEFAULT_MODEL
    )
    
    decision_package = resp.get("content", "")
    with open(decision_package_file, "w", encoding="utf-8") as f:
        f.write(decision_package)
    print(f"[+] Saved Editorial Decision Package to {decision_package_file}")
    print("\n[+] Mock Peer Review Panel process completed successfully.")

if __name__ == "__main__":
    main()
