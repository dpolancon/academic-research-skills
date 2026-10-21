#!/usr/bin/env python3
"""
audit_columna.py (Legacy Forwarding Wrapper)
Location: editor-jacobin-lat/scripts/audit_columna.py

This module provides a backward-compatible CLI and Python import wrapper
pointing to the canonical standalone auditor at tools/audit_columna/audit_columna.py.
"""

import sys
import subprocess
import importlib.util
from pathlib import Path

# Locate canonical auditor tool relative to this wrapper
_WRAPPER_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _WRAPPER_DIR.parent.parent
_CANONICAL_AUDITOR_DIR = _REPO_ROOT / "tools" / "audit_columna"
_CANONICAL_AUDITOR_FILE = _CANONICAL_AUDITOR_DIR / "audit_columna.py"

if not _CANONICAL_AUDITOR_FILE.exists():
    raise ImportError(f"Canonical auditor not found at: {_CANONICAL_AUDITOR_FILE}")

# Dynamically load the canonical module to avoid circular name collision in sys.modules
_spec = importlib.util.spec_from_file_location("tools_audit_columna", str(_CANONICAL_AUDITOR_FILE))
if _spec is None or _spec.loader is None:
    raise ImportError(f"Failed to load spec for canonical auditor at {_CANONICAL_AUDITOR_FILE}")
_canonical_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_canonical_mod)

# Expose public API symbols from canonical auditor
auditar_columna = _canonical_mod.auditar_columna
PAISES_LATAM = _canonical_mod.PAISES_LATAM
JERGA_ACADEMICA = _canonical_mod.JERGA_ACADEMICA
CLICHES_PANFLETARIOS = _canonical_mod.CLICHES_PANFLETARIOS
KEYWORDS_CONTEMPORANEO = _canonical_mod.KEYWORDS_CONTEMPORANEO

__all__ = [
    "auditar_columna",
    "PAISES_LATAM",
    "JERGA_ACADEMICA",
    "CLICHES_PANFLETARIOS",
    "KEYWORDS_CONTEMPORANEO"
]

if __name__ == "__main__":
    # Forward CLI invocation to the canonical script with identical arguments
    cmd = [sys.executable, str(_CANONICAL_AUDITOR_FILE)] + sys.argv[1:]
    result = subprocess.run(cmd)
    sys.exit(result.returncode)
