"""
Replaceable Extraction Backend & NotebookLM Adapter for Literature-Review Skill.

This module defines a generic ExtractionBackend interface and provides an
isolated, robust NotebookLM implementation around notebooklm-py.
It enforces source scoping, query-pack bundling, comparative cluster passes,
exception query trigger validation (Triggers A-F), and optimization metric calculation.
"""

from abc import ABC, abstractmethod
import json
import subprocess
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional


ALLOWED_EXCEPTION_TRIGGERS = {
    "REQUIRED_CLAIM_NOT_LOCATED",
    "CONFLICT",
    "PROVENANCE_GAP",
    "CLAIM_EXCEEDS_NOTE",
    "ATTRIBUTION_AMBIGUITY",
    "NEW_QUESTION",
}


class ExtractionBackend(ABC):
    """Abstract interface for replaceable grounded reading & extraction backends."""

    @abstractmethod
    def list_sources(self) -> List[Dict[str, Any]]:
        """List available sources in the backend workspace."""

    @abstractmethod
    def ask(
        self,
        question: str,
        source_ids: List[str],
        start_new_session: bool = True,
    ) -> Dict[str, Any]:
        """Execute a source-scoped query and return structured citations."""

    def build_query_pack_prompt(
        self,
        query_pack_id: str,
        atomic_questions: List[Dict[str, str]],
    ) -> str:
        """
        Format a bundle of atomic questions (each with 'question_id' and 'question')
        into a single structured prompt that preserves atomic ID traceability.
        """
        if not atomic_questions:
            raise ValueError(f"Query pack {query_pack_id} must contain at least one atomic question.")
        lines = [
            f"Query Pack [{query_pack_id}]: Answer each atomic question below using ONLY the selected source(s).",
            "Provide exact author terminology, page/section/equation locators, verbatim quotes, and explicit negative boundaries.",
            "",
        ]
        for idx, q in enumerate(atomic_questions, start=1):
            qid = q["question_id"]
            qtext = q["question"]
            lines.append(f"{idx}. [{qid}]: {qtext}")
        return "\n".join(lines)

    def run_source_query_pack(
        self,
        source_id: str,
        query_pack_id: str,
        atomic_questions: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        """
        Loop C: Execute a bounded Query Pack against a single source ID.
        """
        if not source_id or not isinstance(source_id, str):
            raise ValueError("Loop C source pass requires exactly one valid source_id.")
        prompt = self.build_query_pack_prompt(query_pack_id, atomic_questions)
        result = self.ask(question=prompt, source_ids=[source_id], start_new_session=True)
        return {
            "pass_type": "LOOP_C_SOURCE_PASS",
            "source_id": source_id,
            "query_pack_id": query_pack_id,
            "atomic_question_ids": [q["question_id"] for q in atomic_questions],
            "backend_response": result,
        }

    def run_cluster_comparison(
        self,
        source_ids: List[str],
        cluster_key: str,
        atomic_questions: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        """
        Loop D: Execute a comparative query across an explicit set of cluster member source IDs.
        """
        if not source_ids or len(source_ids) < 2:
            raise ValueError("Loop D comparative cluster pass requires at least two explicit source_ids.")
        prompt = self.build_query_pack_prompt(cluster_key, atomic_questions)
        result = self.ask(question=prompt, source_ids=source_ids, start_new_session=True)
        return {
            "pass_type": "LOOP_D_CLUSTER_PASS",
            "cluster_key": cluster_key,
            "source_ids": source_ids,
            "atomic_question_ids": [q["question_id"] for q in atomic_questions],
            "backend_response": result,
        }

    def run_exception_query(
        self,
        exception_record: Dict[str, Any],
        question: str,
        source_ids: List[str],
    ) -> Dict[str, Any]:
        """
        Loop E -> C/D: Execute an Exception Query only if an allowed trigger (A-F) is provided
        and a durable target note is specified for write-back.
        """
        trigger = exception_record.get("trigger_type")
        if trigger not in ALLOWED_EXCEPTION_TRIGGERS:
            raise ValueError(
                f"Invalid exception trigger '{trigger}'. Allowed triggers: {sorted(ALLOWED_EXCEPTION_TRIGGERS)}"
            )
        durable_notes = exception_record.get("durable_notes_updated", [])
        if not durable_notes:
            raise ValueError("Exception query must specify at least one durable note in 'durable_notes_updated'.")
        if not source_ids:
            raise ValueError("Exception query requires explicit source_ids.")

        result = self.ask(question=question, source_ids=source_ids, start_new_session=True)
        return {
            "pass_type": "LOOP_E_EXCEPTION_QUERY",
            "exception_record": exception_record,
            "source_ids": source_ids,
            "backend_response": result,
        }


def compute_optimization_metrics(
    downstream_source_uses: int,
    source_passes_executed: int,
    downstream_query_claims: int,
    query_pack_executions: int,
    downstream_cluster_uses: int,
    cluster_passes_executed: int,
    exception_queries_triggered: int,
    paragraph_ledgers_constructed: int,
    requeried_saturated_sources: int,
    total_saturated_sources: int,
) -> Dict[str, float]:
    """Calculate the five canonical workflow efficiency and saturation stability metrics."""
    return {
        "source_reuse": round(downstream_source_uses / max(source_passes_executed, 1), 3),
        "query_reuse": round(downstream_query_claims / max(query_pack_executions, 1), 3),
        "cluster_reuse": round(downstream_cluster_uses / max(cluster_passes_executed, 1), 3),
        "exception_rate": round(exception_queries_triggered / max(paragraph_ledgers_constructed, 1), 3),
        "requery_rate": round(requeried_saturated_sources / max(total_saturated_sources, 1), 3),
    }


class NotebookLMAdapter(ExtractionBackend):
    """Concrete adapter wrapping the notebooklm-py CLI."""

    def __init__(self, notebook_id: str, cli_path: Optional[str] = None):
        self.notebook_id = notebook_id
        self.cli_path = cli_path or self._find_cli()

    def _find_cli(self) -> str:
        local_bin = Path.home() / ".local" / "bin" / "notebooklm.exe"
        if local_bin.exists():
            return str(local_bin)
        which_path = shutil.which("notebooklm")
        if which_path:
            return which_path
        raise FileNotFoundError("notebooklm CLI not found in ~/.local/bin or system PATH.")

    def auth_check(self) -> Dict[str, Any]:
        cmd = [self.cli_path, "auth", "check", "--test", "--json"]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            return {"status": "error", "stderr": res.stderr}
        return json.loads(res.stdout)

    def list_sources(self) -> List[Dict[str, Any]]:
        cmd = [self.cli_path, "source", "list", "-n", self.notebook_id, "--json"]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            raise RuntimeError(f"Failed to list sources: {res.stderr}")
        data = json.loads(res.stdout)
        return data.get("sources", [])

    def add_source_file(self, file_path: str, title: Optional[str] = None) -> Dict[str, Any]:
        cmd = [self.cli_path, "source", "add", "-n", self.notebook_id, str(file_path), "--json"]
        if title:
            cmd.extend(["--title", title])
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            raise RuntimeError(f"Failed to add source {file_path}: {res.stderr}")
        return json.loads(res.stdout)

    def wait_for_source(self, source_id: str, timeout: int = 120) -> Dict[str, Any]:
        cmd = [
            self.cli_path, "source", "wait",
            "-n", self.notebook_id, source_id,
            "--timeout", str(timeout),
            "--json"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            raise RuntimeError(f"Source {source_id} failed to reach ready state: {res.stderr}")
        return json.loads(res.stdout)

    def ask(self, question: str, source_ids: List[str], start_new_session: bool = True) -> Dict[str, Any]:
        """
        Query NotebookLM with explicit source scoping (-s <source_id>).
        Unscoped queries across the whole notebook are strictly forbidden.
        """
        if not source_ids:
            raise ValueError("Strict source scoping required: source_ids cannot be empty.")
        cmd = [
            self.cli_path, "ask",
            "-n", self.notebook_id,
            "--json"
        ]
        if start_new_session:
            cmd.append("--new")
        for sid in source_ids:
            cmd.extend(["-s", sid])
        cmd.append(question)

        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            raise RuntimeError(f"Ask query failed: {res.stderr}")
        return json.loads(res.stdout)
