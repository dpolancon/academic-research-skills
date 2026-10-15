"""
NotebookLM Backend Adapter for Literature-Review Skill.

This module provides an isolated, robust wrapper around notebooklm-py,
enforcing source scoping, readiness checks, JSON output validation,
and clean separation between external LLM querying and internal scholarly state.
"""

import json
import subprocess
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional

class NotebookLMAdapter:
    def __init__(self, notebook_id: str, cli_path: Optional[str] = None):
        self.notebook_id = notebook_id
        self.cli_path = cli_path or self._find_cli()

    def _find_cli(self) -> str:
        # Check standard user local bin first, then PATH
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
        Query NotebookLM with explicit source scoping.
        """
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
