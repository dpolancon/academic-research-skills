#!/usr/bin/env python3
"""Standalone ARS Pipeline Orchestrator.

Implements the repository-agnostic 10-stage state machine transitions,
scoped-write directory fencing, Obsidian vault front-end UI synchronization,
and watchdog active file observers.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import List, Dict, Any, Union

import yaml

# Ensure scripts folder is on PATH
sys.path.insert(0, str(Path(__file__).resolve().parent))

from llm_gateway import LLMGateway

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False
    # Stub class to avoid compilation NameError if watchdog is not installed
    class FileSystemEventHandler:
        pass


# ---------------------------------------------------------------------------
# Security: Scoped-Write Directory Fencing
# ---------------------------------------------------------------------------

def check_scoped_write(path: Union[str, Path], target_dir: Union[str, Path]):
    """Enforces directory fencing by preventing operations outside target_dir."""
    try:
        resolved_path = Path(path).resolve()
        resolved_target = Path(target_dir).resolve()
        # Check if the resolved path is inside the resolved target directory
        # Using relative_to will raise ValueError if resolved_path is not inside resolved_target
        resolved_path.relative_to(resolved_target)
    except (ValueError, TypeError):
        raise PermissionError(
            f"Security Block: Access denied. Path {path} lies outside the "
            f"scoped target workspace: {target_dir}"
        )


# ---------------------------------------------------------------------------
# Prompt Parser: Loading Markdown Agent Definitions
# ---------------------------------------------------------------------------

def load_agent_prompt(agent_name: str) -> str:
    """Locates and parses the markdown agent definition to return the system prompt."""
    repo_root = Path(__file__).resolve().parent.parent
    agent_folders = [
        repo_root / "deep-research" / "agents",
        repo_root / "academic-paper" / "agents",
        repo_root / "academic-paper-reviewer" / "agents",
        repo_root / "academic-pipeline" / "agents"
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


# ---------------------------------------------------------------------------
# Decision Parser
# ---------------------------------------------------------------------------

def parse_eic_decision(content: str) -> str:
    """Parses the Editorial Decision from the EIC output.
    Returns: 'accept', 'minor', 'major', or 'reject'.
    """
    content_upper = content.upper()
    if "REJECT" in content_upper:
        return "reject"
    elif "MAJOR REVISION" in content_upper or "MAJOR" in content_upper:
        return "major"
    elif "MINOR REVISION" in content_upper or "MINOR" in content_upper:
        return "minor"
    elif "ACCEPT" in content_upper:
        return "accept"
    return "minor" # Default to minor revision if unclear


# ---------------------------------------------------------------------------
# State Machine & Material Passport Manager
# ---------------------------------------------------------------------------

class PipelineState:
    """Manages the state transitions and passport.yaml updates."""

    def __init__(self, target_dir: Path):
        self.target_dir = Path(target_dir).resolve()
        self.passport_path = self.target_dir / "passport.yaml"
        self.state = {
            "current_stage": "1",
            "global_state": "initializing",
            "completed_stages": [],
            "failed_attempts": {},
            "history": []
        }
        self.load()

    def load(self):
        """Loads state from passport.yaml if it exists."""
        if self.passport_path.exists():
            try:
                with open(self.passport_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
                    self.state.update(data.get("pipeline_state", {}))
            except Exception as e:
                print(f"Warning: Failed to load passport.yaml state: {e}", file=sys.stderr)

    def save(self):
        """Saves current state back into passport.yaml (fenced)."""
        check_scoped_write(self.passport_path, self.target_dir)
        
        passport_data = {}
        if self.passport_path.exists():
            try:
                with open(self.passport_path, "r", encoding="utf-8") as f:
                    passport_data = yaml.safe_load(f) or {}
            except Exception:
                pass

        passport_data["pipeline_state"] = self.state
        
        # Safe atomic write in target_dir
        temp_path = self.passport_path.with_suffix(".tmp")
        check_scoped_write(temp_path, self.target_dir)
        
        with open(temp_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(passport_data, f, default_flow_style=False, sort_keys=False)
            
        if temp_path.exists():
            if self.passport_path.exists():
                self.passport_path.unlink()
            temp_path.rename(self.passport_path)

    def transition_to(self, new_stage: str, global_state: str = "running"):
        """Performs state machine transitions."""
        print(f"[*] State Transition: Stage {self.state['current_stage']} -> Stage {new_stage} ({global_state})")
        self.state["current_stage"] = new_stage
        self.state["global_state"] = global_state
        self.state["history"].append({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "stage": new_stage,
            "state": global_state
        })
        self.save()


# ---------------------------------------------------------------------------
# Standalone Pipeline Runner CLI Loop
# ---------------------------------------------------------------------------

class ARSPipelineRunner:
    """Orchestrates stage workflows and schedules model execution."""

    def __init__(self, target_dir: Path, is_obsidian: bool = False, config_path: Path = None,
                 resolved_provider: str = None, resolved_model: str = None, resolved_base_url: str = None):
        self.target_dir = Path(target_dir).resolve()
        self.is_obsidian = is_obsidian
        self.config_path = config_path
        
        # Initialize target directories
        self.target_dir.mkdir(parents=True, exist_ok=True)
        self.state_mgr = PipelineState(self.target_dir)
        self.gateway = LLMGateway(
            config_path=self.config_path,
            default_model=resolved_model,
            default_provider=resolved_provider,
            base_url=resolved_base_url
        )

    def get_active_task_prompt(self, default_prompt: str) -> str:
        """Reads the custom prompt from ARS/ARS_Active_Task.md if it exists."""
        task_file = self.target_dir / "ARS" / "ARS_Active_Task.md"
        if task_file.exists():
            try:
                with open(task_file, "r", encoding="utf-8") as f:
                    content = f.read()
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        prompt_part = parts[2].strip()
                        if prompt_part:
                            return prompt_part
                else:
                    prompt_part = content.strip()
                    if prompt_part:
                        return prompt_part
            except Exception as e:
                print(f"Warning: Failed to read active task file prompt: {e}", file=sys.stderr)
        return default_prompt

    def check_required_materials(self, stage: str) -> bool:
        """Verifies if the required input files for a stage exist.
        Returns True if all required materials exist, otherwise False.
        """
        missing = []
        if stage == "2":
            if not (self.target_dir / "phase1_research" / "RQ_Brief.md").exists():
                missing.append("RQ Brief (phase1_research/RQ_Brief.md)")
        elif stage == "2.5":
            if not (self.target_dir / "phase2_write" / "Manuscript_Draft.md").exists():
                missing.append("Paper Draft (phase2_write/Manuscript_Draft.md)")
        elif stage == "3":
            if not (self.target_dir / "phase2_write" / "Manuscript_Draft.md").exists():
                missing.append("Paper Draft (phase2_write/Manuscript_Draft.md)")
            if not (self.target_dir / "phase2_write" / "Integrity_Report.md").exists():
                missing.append("Integrity Report (phase2_write/Integrity_Report.md)")
        elif stage == "4":
            if not (self.target_dir / "phase2_write" / "Manuscript_Draft.md").exists():
                missing.append("Paper Draft (phase2_write/Manuscript_Draft.md)")
            if not (self.target_dir / "phase3_review" / "EIC_Decision.md").exists():
                missing.append("EIC Editorial Decision (phase3_review/EIC_Decision.md)")
        elif stage == "3'":
            if not (self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md").exists():
                missing.append("Revised Draft (phase4_revise/Manuscript_Draft_Revised.md)")
        elif stage == "4'":
            if not (self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md").exists():
                missing.append("Revised Draft (phase4_revise/Manuscript_Draft_Revised.md)")
            if not (self.target_dir / "phase3_review" / "ReReview_Report.md").exists():
                missing.append("ReReview Report (phase3_review/ReReview_Report.md)")
        elif stage == "4.5":
            rerevised = self.target_dir / "phase4_revise" / "Manuscript_Draft_ReRevised.md"
            revised = self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md"
            if not rerevised.exists() and not revised.exists():
                missing.append("Revised or Re-Revised Draft (phase4_revise/Manuscript_Draft_Revised.md or Manuscript_Draft_ReRevised.md)")
        elif stage == "5":
            rerevised = self.target_dir / "phase4_revise" / "Manuscript_Draft_ReRevised.md"
            revised = self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md"
            if not rerevised.exists() and not revised.exists():
                missing.append("Revised or Re-Revised Draft (phase4_revise/Manuscript_Draft_Revised.md or Manuscript_Draft_ReRevised.md)")
            if not (self.target_dir / "phase4_revise" / "Final_Integrity_Report.md").exists():
                missing.append("Final Integrity Report (phase4_revise/Final_Integrity_Report.md)")

        if missing:
            print("\n" + "!" * 50)
            print(" WARNING: Missing Required Pre-requisite Materials:")
            for item in missing:
                print(f" - {item}")
            print("!" * 50 + "\n")
            return False
        return True

    def write_deliverable(self, relative_path: str, content: str):
        """Writes deliverables inside target_dir (fully fenced)."""
        file_path = self.target_dir / relative_path
        # Enforce write fencing
        check_scoped_write(file_path, self.target_dir)
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Output written to: {file_path}")

        # If Obsidian mode is on, replicate to vault link directories
        if self.is_obsidian:
            self._write_obsidian_metadata(relative_path, content)

    def _get_obsidian_path(self, relative_path: str) -> Path:
        """Maps standard deliverable paths to Obsidian vault organization."""
        path_parts = Path(relative_path).parts
        if not path_parts:
            return self.target_dir / "ARS" / relative_path
            
        category = "General"
        if "research" in path_parts[0]:
            category = "Research"
        elif "write" in path_parts[0]:
            if "Integrity" in path_parts[-1]:
                category = "Integrity"
            else:
                category = "Drafts"
        elif "review" in path_parts[0]:
            category = "Reviews"
        elif "revise" in path_parts[0]:
            if "Integrity" in path_parts[-1]:
                category = "Integrity"
            else:
                category = "Drafts"
        elif "publication" in path_parts[0]:
            category = "Drafts"
            
        note_name = Path(relative_path).name
        return self.target_dir / "ARS" / category / note_name

    def _write_obsidian_metadata(self, relative_path: str, content: str):
        """Formats outputs with Obsidian wikilinks and graph mapping."""
        obsidian_path = self._get_obsidian_path(relative_path)
        check_scoped_write(obsidian_path, self.target_dir)
        
        obsidian_path.parent.mkdir(parents=True, exist_ok=True)
        
        note_name = Path(relative_path).stem
        
        # Generate custom Wikilinks depending on the note type
        links = ["[[ARS_Material_Passport]]"]
        if note_name == "Manuscript_Draft":
            links.extend(["[[RQ_Brief]]", "[[Methodology_Blueprint]]"])
        elif note_name == "Integrity_Report":
            links.append("[[Manuscript_Draft]]")
        elif note_name == "EIC_Decision":
            links.extend(["[[Manuscript_Draft]]", "[[Integrity_Report]]"])
        elif note_name == "Manuscript_Draft_Revised":
            links.extend(["[[Manuscript_Draft]]", "[[EIC_Decision]]"])
        elif note_name == "ReReview_Report":
            links.extend(["[[Manuscript_Draft_Revised]]", "[[EIC_Decision]]"])
        elif note_name == "Manuscript_Draft_ReRevised":
            links.extend(["[[Manuscript_Draft_Revised]]", "[[ReReview_Report]]"])
        elif note_name == "Final_Integrity_Report":
            if (self.target_dir / "phase4_revise" / "Manuscript_Draft_ReRevised.md").exists():
                links.append("[[Manuscript_Draft_ReRevised]]")
            else:
                links.append("[[Manuscript_Draft_Revised]]")
        elif note_name == "Manuscript_Final":
            if (self.target_dir / "phase4_revise" / "Manuscript_Draft_ReRevised.md").exists():
                links.append("[[Manuscript_Draft_ReRevised]]")
            else:
                links.append("[[Manuscript_Draft_Revised]]")
            links.append("[[Final_Integrity_Report]]")
            
        links_str = " | ".join(links)
        
        # Format note frontmatter and content
        tag = "ars-output"
        if "Research" in obsidian_path.parts:
            tag = "ars-research"
        elif "Drafts" in obsidian_path.parts:
            tag = "ars-draft"
        elif "Reviews" in obsidian_path.parts:
            tag = "ars-review"
        elif "Integrity" in obsidian_path.parts:
            tag = "ars-integrity"
            
        wikilink_front = (
            f"---\n"
            f"tags: [{tag}]\n"
            f"state: [[ARS_Material_Passport]]\n"
            f"connections: {links_str}\n"
            f"---\n\n"
        )
        
        # Add links header at the top
        header = f"Related: {links_str}\n\n---\n\n"
        
        with open(obsidian_path, "w", encoding="utf-8") as f:
            f.write(wikilink_front + header + content)
        print(f"[+] Replicated to Obsidian note: {obsidian_path}")

        # Update Obsidian Passport Note
        self.update_obsidian_passport()

    def update_obsidian_passport(self):
        """Updates the main Obsidian passport note with state and graph links."""
        passport_path = self.target_dir / "ARS" / "ARS_Material_Passport.md"
        check_scoped_write(passport_path, self.target_dir)
        
        passport_path.parent.mkdir(parents=True, exist_ok=True)
        
        stage = self.state_mgr.state.get("current_stage", "1")
        global_state = self.state_mgr.state.get("global_state", "initializing")
        completed = self.state_mgr.state.get("completed_stages", [])
        
        # Generate links to completed deliverables to show on the graph
        deliverable_links = []
        if "1" in completed:
            deliverable_links.append("[[RQ_Brief]]")
            deliverable_links.append("[[Methodology_Blueprint]]")
        if "2" in completed:
            deliverable_links.append("[[Manuscript_Draft]]")
        if "2.5" in completed:
            deliverable_links.append("[[Integrity_Report]]")
        if "3" in completed:
            deliverable_links.append("[[EIC_Decision]]")
        if "4" in completed:
            deliverable_links.append("[[Manuscript_Draft_Revised]]")
        if "3'" in completed:
            deliverable_links.append("[[ReReview_Report]]")
        if "4'" in completed:
            deliverable_links.append("[[Manuscript_Draft_ReRevised]]")
        if "4.5" in completed:
            deliverable_links.append("[[Final_Integrity_Report]]")
        if "5" in completed:
            deliverable_links.append("[[Manuscript_Final]]")
            
        links_str = "\n".join([f"- {link}" for link in deliverable_links])
        
        content = (
            f"---\n"
            f"title: ARS Material Passport\n"
            f"stage: \"{stage}\"\n"
            f"status: \"{global_state}\"\n"
            f"tags: [ars-passport]\n"
            f"---\n\n"
            f"# ARS Material Passport\n\n"
            f"**Current Stage:** Stage {stage}\n"
            f"**Status:** {global_state}\n\n"
            f"## Completed Deliverables\n\n"
            f"{links_str if links_str else 'No deliverables completed yet.'}\n"
        )
        with open(passport_path, "w", encoding="utf-8") as f:
            f.write(content)

    def update_active_task_note(self, next_stage: str):
        """Updates the stage in ARS_Active_Task.md and sets run_on_save to false to prevent loops."""
        task_file = self.target_dir / "ARS" / "ARS_Active_Task.md"
        check_scoped_write(task_file, self.target_dir)
        
        if not task_file.exists():
            return
            
        try:
            with open(task_file, "r", encoding="utf-8") as f:
                content = f.read()
                
            frontmatter_data = {}
            prompt_content = content
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    try:
                        frontmatter_data = yaml.safe_load(parts[1]) or {}
                    except Exception:
                        pass
                    prompt_content = parts[2]
            
            frontmatter_data["stage"] = next_stage
            frontmatter_data["run_on_save"] = False # Disable auto-run until user updates it
            
            # Reconstruct content
            front_str = yaml.safe_dump(frontmatter_data, default_flow_style=False, sort_keys=False)
            new_content = f"---\n{front_str}---\n{prompt_content}"
            
            with open(task_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"[*] Updated Obsidian active task note stage to {next_stage} (run_on_save set to false)")
        except Exception as e:
            print(f"Warning: Failed to update active task note: {e}", file=sys.stderr)

    def execute_stage(self, stage: str, override_provider: str = None, override_model: str = None):
        """Runs the generation logic for the active stage."""
        print(f"\n=================== STARTING STAGE {stage} ===================")
        
        # Check required materials
        if not self.check_required_materials(stage):
            if not self.is_obsidian and sys.stdin.isatty():
                ans = input("Would you like to force execution anyway? (y/N): ").strip().lower()
                if ans not in ("y", "yes"):
                    print("[*] Execution cancelled. Returning to dashboard.")
                    return
            else:
                print(f"[!] Blocking execution due to missing materials in Stage {stage}.")
                self.state_mgr.state["global_state"] = "blocked"
                self.state_mgr.save()
                return

        # Execute based on active stage
        if stage == "1":
            print("[*] Dispatching deep-research agent...")
            sys_prompt = load_agent_prompt("research_architect_agent")
            default_prompt = "Generate a Research Question Brief and Methodology Blueprint based on digital politics."
            user_prompt = self.get_active_task_prompt(default_prompt)
            
            response = self.gateway.generate(
                agent_name="research_architect",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            content = response.get("content", "")
            self.write_deliverable("phase1_research/RQ_Brief.md", content)
            self.write_deliverable("phase1_research/Methodology_Blueprint.md", "Methodology Blueprint:\n\n" + content)
            
            self.state_mgr.state["completed_stages"].append("1")
            self.state_mgr.transition_to("2", "awaiting_confirmation")
            if self.is_obsidian:
                self.update_active_task_note("2")

        elif stage == "2":
            print("[*] Dispatching academic-paper draft writer...")
            sys_prompt = load_agent_prompt("draft_writer_agent")
            
            # Load Stage 1 outputs
            rq_brief = ""
            rq_path = self.target_dir / "phase1_research" / "RQ_Brief.md"
            if rq_path.exists():
                with open(rq_path, "r", encoding="utf-8") as f:
                    rq_brief = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Instructions:\n{custom_instructions}\n\nRQ Brief Context:\n{rq_brief}"
            else:
                user_prompt = f"Write a research paper manuscript draft using this RQ brief:\n\n{rq_brief}"
                
            response = self.gateway.generate(
                agent_name="draft_writer",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            self.write_deliverable("phase2_write/Manuscript_Draft.md", response.get("content", ""))
            self.state_mgr.state["completed_stages"].append("2")
            self.state_mgr.transition_to("2.5", "awaiting_confirmation")
            if self.is_obsidian:
                self.update_active_task_note("2.5")

        elif stage == "2.5":
            print("[*] Dispatching integrity verification checks...")
            sys_prompt = load_agent_prompt("integrity_verification_agent")
            
            # Load draft
            draft = ""
            draft_path = self.target_dir / "phase2_write" / "Manuscript_Draft.md"
            if draft_path.exists():
                with open(draft_path, "r", encoding="utf-8") as f:
                    draft = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Instructions:\n{custom_instructions}\n\nManuscript to Verify:\n{draft}"
            else:
                user_prompt = f"Run reference, citation, and failure checklist verification against this manuscript:\n\n{draft}"
                
            response = self.gateway.generate(
                agent_name="integrity_verification_agent",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            self.write_deliverable("phase2_write/Integrity_Report.md", response.get("content", ""))
            self.state_mgr.state["completed_stages"].append("2.5")
            self.state_mgr.transition_to("3", "awaiting_confirmation")
            if self.is_obsidian:
                self.update_active_task_note("3")

        elif stage == "3":
            print("[*] Dispatching academic peer reviewers...")
            sys_prompt = load_agent_prompt("eic_agent")
            
            draft = ""
            draft_path = self.target_dir / "phase2_write" / "Manuscript_Draft.md"
            if draft_path.exists():
                with open(draft_path, "r", encoding="utf-8") as f:
                    draft = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Review Instructions:\n{custom_instructions}\n\nManuscript:\n{draft}"
            else:
                user_prompt = f"Review this draft and issue an Editorial Decision Letter:\n\n{draft}"
                
            response = self.gateway.generate(
                agent_name="editor_in_chief",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            decision_content = response.get("content", "")
            self.write_deliverable("phase3_review/EIC_Decision.md", decision_content)
            self.state_mgr.state["completed_stages"].append("3")
            
            # Parse outcome (Accept vs Revise vs Reject)
            verdict = parse_eic_decision(decision_content)
            print(f"[*] Parsed EIC Decision Verdict: {verdict.upper()}")
            
            if verdict == "accept":
                self.state_mgr.transition_to("4.5", "awaiting_confirmation")
                if self.is_obsidian:
                    self.update_active_task_note("4.5")
            elif verdict == "reject":
                print("[!] The manuscript has been REJECTED. Transitioning to ABORTED state.")
                self.state_mgr.transition_to("aborted", "aborted")
                if self.is_obsidian:
                    self.update_active_task_note("aborted")
            else: # minor / major
                self.state_mgr.transition_to("4", "awaiting_confirmation")
                if self.is_obsidian:
                    self.update_active_task_note("4")

        elif stage == "4":
            print("[*] Dispatching academic-paper revision writer...")
            sys_prompt = load_agent_prompt("draft_writer_agent")
            
            draft = ""
            draft_path = self.target_dir / "phase2_write" / "Manuscript_Draft.md"
            if draft_path.exists():
                with open(draft_path, "r", encoding="utf-8") as f:
                    draft = f.read()
            
            decision = ""
            decision_path = self.target_dir / "phase3_review" / "EIC_Decision.md"
            if decision_path.exists():
                with open(decision_path, "r", encoding="utf-8") as f:
                    decision = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Revision Instructions:\n{custom_instructions}\n\nDraft:\n{draft}\n\nCritique:\n{decision}"
            else:
                user_prompt = f"Revise this draft:\n{draft}\n\nBased on these reviewer critiques:\n{decision}"
                
            response = self.gateway.generate(
                agent_name="draft_writer",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            self.write_deliverable("phase4_revise/Manuscript_Draft_Revised.md", response.get("content", ""))
            self.state_mgr.state["completed_stages"].append("4")
            self.state_mgr.transition_to("3'", "awaiting_confirmation")
            if self.is_obsidian:
                self.update_active_task_note("3'")

        elif stage == "3'":
            print("[*] Dispatching EIC verification re-review...")
            sys_prompt = load_agent_prompt("eic_agent")
            
            revised_draft = ""
            rev_path = self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md"
            if rev_path.exists():
                with open(rev_path, "r", encoding="utf-8") as f:
                    revised_draft = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Re-Review Instructions:\n{custom_instructions}\n\nRevised Draft:\n{revised_draft}"
            else:
                user_prompt = f"Verify if all reviewer comments are satisfied in this revised draft:\n\n{revised_draft}"
                
            response = self.gateway.generate(
                agent_name="editor_in_chief",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            rereview_content = response.get("content", "")
            self.write_deliverable("phase3_review/ReReview_Report.md", rereview_content)
            self.state_mgr.state["completed_stages"].append("3'")
            
            # Parse re-review decision
            verdict = parse_eic_decision(rereview_content)
            print(f"[*] Parsed Re-Review Verdict: {verdict.upper()}")
            
            if verdict == "major":
                # Major revision in re-review triggers Stage 4' (Re-revise)
                self.state_mgr.transition_to("4'", "awaiting_confirmation")
                if self.is_obsidian:
                    self.update_active_task_note("4'")
            else: # accept / minor / reject (we map reject/minor in re-review to final verification)
                self.state_mgr.transition_to("4.5", "awaiting_confirmation")
                if self.is_obsidian:
                    self.update_active_task_note("4.5")

        elif stage == "4'":
            print("[*] Dispatching academic-paper re-revision writer (Stage 4')...")
            sys_prompt = load_agent_prompt("draft_writer_agent")
            
            revised_draft = ""
            rev_path = self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md"
            if rev_path.exists():
                with open(rev_path, "r", encoding="utf-8") as f:
                    revised_draft = f.read()
            
            rereview = ""
            rereview_path = self.target_dir / "phase3_review" / "ReReview_Report.md"
            if rereview_path.exists():
                with open(rereview_path, "r", encoding="utf-8") as f:
                    rereview = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Re-Revision Instructions:\n{custom_instructions}\n\nRevised Draft:\n{revised_draft}\n\nRe-Review Critiques:\n{rereview}"
            else:
                user_prompt = f"Perform the last round of revisions on this revised draft:\n{revised_draft}\n\nBased on these re-review comments:\n{rereview}"
                
            response = self.gateway.generate(
                agent_name="draft_writer",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            self.write_deliverable("phase4_revise/Manuscript_Draft_ReRevised.md", response.get("content", ""))
            self.state_mgr.state["completed_stages"].append("4'")
            self.state_mgr.transition_to("4.5", "awaiting_confirmation")
            if self.is_obsidian:
                self.update_active_task_note("4.5")

        elif stage == "4.5":
            print("[*] Dispatching Final Integrity Verification...")
            sys_prompt = load_agent_prompt("integrity_verification_agent")
            
            revised_draft = ""
            rerevised_path = self.target_dir / "phase4_revise" / "Manuscript_Draft_ReRevised.md"
            revised_path = self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md"
            
            if rerevised_path.exists():
                with open(rerevised_path, "r", encoding="utf-8") as f:
                    revised_draft = f.read()
            elif revised_path.exists():
                with open(revised_path, "r", encoding="utf-8") as f:
                    revised_draft = f.read()
            
            custom_instructions = self.get_active_task_prompt("")
            if custom_instructions:
                user_prompt = f"Custom Instructions:\n{custom_instructions}\n\nManuscript to Verify:\n{revised_draft}"
            else:
                user_prompt = f"Run final 100% verification checks against the final revised manuscript:\n\n{revised_draft}"
                
            response = self.gateway.generate(
                agent_name="integrity_verification_agent",
                system_prompt=sys_prompt,
                user_prompt=user_prompt,
                override_provider=override_provider,
                override_model=override_model
            )
            
            self.write_deliverable("phase4_revise/Final_Integrity_Report.md", response.get("content", ""))
            self.state_mgr.state["completed_stages"].append("4.5")
            self.state_mgr.transition_to("5", "awaiting_confirmation")
            if self.is_obsidian:
                self.update_active_task_note("5")

        elif stage == "5":
            print("[*] Formatting final accepted manuscript...")
            
            revised_draft = ""
            rerevised_path = self.target_dir / "phase4_revise" / "Manuscript_Draft_ReRevised.md"
            rev_path = self.target_dir / "phase4_revise" / "Manuscript_Draft_Revised.md"
            
            if rerevised_path.exists():
                with open(rerevised_path, "r", encoding="utf-8") as f:
                    revised_draft = f.read()
            elif rev_path.exists():
                with open(rev_path, "r", encoding="utf-8") as f:
                    revised_draft = f.read()
            
            self.write_deliverable("final_publication/Manuscript_Final.md", revised_draft)
            self.state_mgr.state["completed_stages"].append("5")
            self.state_mgr.transition_to("6", "completed")
            print("[+] Pipeline Execution Complete!")
            if self.is_obsidian:
                self.update_active_task_note("6")

        else:
            print(f"Error: Unknown or unsupported execution stage: {stage}")

    def run_dashboard(self) -> bool:
        """Renders the Decision Dashboard on stdout and prompts user for input."""
        current = self.state_mgr.state["current_stage"]
        completed = self.state_mgr.state["completed_stages"]
        
        print("\n" + "━" * 50)
        print(f" ARS Dashboard — Workspace: {self.target_dir.name}")
        print(f" Current Pipeline Stage: {current}")
        print(f" Completed Stages: {', '.join(completed) if completed else 'None'}")
        print(f" Status: {self.state_mgr.state['global_state']}")
        print("━" * 50)

        if self.state_mgr.state["global_state"] == "completed":
            print("[*] Pipeline has finished processing.")
            return False
        elif self.state_mgr.state["global_state"] == "aborted":
            print("[!] Pipeline was aborted.")
            return False

        # Prompt
        ans = input(f"Proceed with Stage {current}? (continue/pause/adjust/abort): ").strip().lower()
        if ans in ("continue", "yes", "y", ""):
            self.state_mgr.state["global_state"] = "running"
            self.state_mgr.save()
            self.execute_stage(current)
            return True
        elif ans == "pause":
            self.state_mgr.state["global_state"] = "paused"
            self.state_mgr.save()
            print("[*] Pipeline paused. Run this script again to resume.")
            return False
        elif ans == "adjust":
            stage_override = input("Enter target stage to jump to: ").strip()
            if stage_override in ("1", "2", "2.5", "3", "4", "3'", "4'", "4.5", "5"):
                self.state_mgr.transition_to(stage_override, "running")
                self.execute_stage(stage_override)
                return True
            else:
                print("Invalid stage selection. Returning to dashboard.")
                return True
        elif ans == "abort":
            self.state_mgr.state["global_state"] = "aborted"
            self.state_mgr.save()
            print("[!] Pipeline aborted.")
            return False
        else:
            print("Command unrecognized. Resurfacing dashboard...")
            return True


# ---------------------------------------------------------------------------
# Background File Observer (watchdog) for Obsidian vault UI
# ---------------------------------------------------------------------------

class ObsidianVaultHandler(FileSystemEventHandler):
    """Event handler watching for writes to Obsidian ARS_Active_Task.md."""

    def __init__(self, task_file: Path, runner: ARSPipelineRunner):
        self.task_file = Path(task_file).resolve()
        self.runner = runner
        self.last_triggered = 0.0

    def on_any_event(self, event):
        # Prevent double-firing by checking directory events
        if event.is_directory:
            return
            
        src_path = Path(event.src_path).resolve()
        dest_path = Path(event.dest_path).resolve() if hasattr(event, 'dest_path') and event.dest_path else None
        
        # Check if the event targets the task file
        if src_path == self.task_file or dest_path == self.task_file:
            current_time = time.time()
            # De-bounce to prevent double-firing during multi-write saves
            if current_time - self.last_triggered > 2.0:
                self.last_triggered = current_time
                print(f"\n[!] Change detected in Obsidian active note: {self.task_file} (Event: {event.event_type})")
                time.sleep(0.5) # Wait for write to finish settling
                self._trigger_run()

    def _trigger_run(self):
        try:
            # Parse Obsidian Note Frontmatter
            with open(self.task_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            stage = self.runner.state_mgr.state["current_stage"]
            run_on_save = False
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    try:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        stage = str(frontmatter.get("stage", stage))
                        run_on_save = frontmatter.get("run_on_save", False)
                    except Exception as e:
                        print(f"Warning: Failed to parse frontmatter: {e}", file=sys.stderr)
            
            if run_on_save:
                print(f"[*] Auto-triggering Pipeline Stage {stage} based on Obsidian note save...")
                self.runner.state_mgr.state["current_stage"] = stage
                self.runner.state_mgr.state["global_state"] = "running"
                self.runner.state_mgr.save()
                self.runner.execute_stage(stage)
            else:
                print("[*] Note saved, but 'run_on_save: true' is not set in frontmatter. Skipping run.")
        except Exception as e:
            print(f"Error reading/triggering from Obsidian: {e}", file=sys.stderr)


def run_obsidian_watcher(target_dir: Path, runner: ARSPipelineRunner):
    """Observer loop thread checking for modified events on active note."""
    if not WATCHDOG_AVAILABLE:
        print("Error: 'watchdog' library not found. Run 'pip install watchdog' to enable Obsidian file watching.", file=sys.stderr)
        return

    active_note_dir = target_dir / "ARS"
    active_note_dir.mkdir(exist_ok=True)
    task_file = active_note_dir / "ARS_Active_Task.md"
    check_scoped_write(task_file, target_dir)

    # Initialize task file if not existing
    if not task_file.exists():
        with open(task_file, "w", encoding="utf-8") as f:
            f.write("---\nstage: 1\nmode: socratic\nrun_on_save: true\n---\n\nWrite research prompt here...\n")
        print(f"[+] Created active task queue note inside vault: {task_file}")

    print(f"\n[*] Starting background Watchdog Observer watching folder: {active_note_dir}")
    event_handler = ObsidianVaultHandler(task_file, runner)
    observer = Observer()
    # Watch the directory containing the task file
    observer.schedule(event_handler, path=str(active_note_dir), recursive=False)
    observer.start()
    
    print("[*] Background file watcher is running. Modify and save ARS_Active_Task.md inside Obsidian to execute.")
    print("Press Ctrl+C to terminate the watcher.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[*] Stopping Watchdog Observer...")
    observer.join()


# ---------------------------------------------------------------------------
# Main CLI Entry Point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Standalone ARS Pipeline Orchestrator.")
    parser.add_argument("--target-dir", required=True, help="Generic target workspace folder for outputs (fenced)")
    parser.add_argument("--obsidian-vault", action="store_true", help="Enable Obsidian UI Graph Linkage Mode")
    parser.add_argument("--config", help="Optional path to agent_config.yaml")
    parser.add_argument("--provider", "--override-provider", dest="provider", help="Override LLM provider")
    parser.add_argument("--model", "--override-model", dest="model", help="Override LLM model ID")
    parser.add_argument("--base-url", dest="base_url", help="Override LLM base URL")
    parser.add_argument("--stage", help="Override pipeline state stage (1-6)")
    parser.add_argument("--mode", help="Execution mode (socratic/full)")

    args = parser.parse_args()

    target_dir = Path(args.target_dir).resolve()
    
    # Resolve config file path
    config_path = Path(args.config) if args.config else Path(__file__).resolve().parent.parent / "agent_config.yaml"
    config_data = {}
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = yaml.safe_load(f) or {}
        except Exception:
            pass

    global_cfg = config_data.get("global_settings", {})
    providers_cfg = config_data.get("providers", {})

    # Priority-based configuration resolution:
    # 1. CLI flags
    # 2. Environment variables
    # 3. Config file global defaults
    # 4. Hardcoded fallbacks
    resolved_provider = (
        args.provider or 
        os.getenv("DEFAULT_PROVIDER") or 
        global_cfg.get("default_provider") or
        "together"
    )
    resolved_model = (
        args.model or 
        os.getenv("DEFAULT_MODEL") or 
        global_cfg.get("default_model") or
        "Qwen/Qwen3.5-9B"
    )
    resolved_base_url = (
        args.base_url or 
        providers_cfg.get("together", {}).get("base_url") or
        "https://api.together.ai/v1"
    )

    # Instantiate Pipeline Runner
    runner = ARSPipelineRunner(
        target_dir=target_dir, 
        is_obsidian=args.obsidian_vault, 
        config_path=config_path if args.config else None,
        resolved_provider=resolved_provider,
        resolved_model=resolved_model,
        resolved_base_url=resolved_base_url
    )

    # Stage override handling
    if args.stage:
        runner.state_mgr.state["current_stage"] = str(args.stage)
        runner.state_mgr.state["global_state"] = "running"
        runner.state_mgr.save()

    # Launch Watcher Mode if requested, otherwise run CLI loop
    if args.obsidian_vault:
        run_obsidian_watcher(target_dir, runner)
    else:
        # Standard Interactive CLI Loop
        running = True
        while running:
            running = runner.run_dashboard()


if __name__ == "__main__":
    main()
