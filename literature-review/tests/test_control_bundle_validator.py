"""
Unit tests for control_bundle_validator.py.
Verifies validation of declarative project control bundles and state consistency.
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from control_bundle_validator import ControlBundleValidator


class TestControlBundleValidator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.schema_dir = SKILL_ROOT / "schemas"

        # Populate a valid minimal bundle
        (self.temp_dir / "00_BUNDLE_MANIFEST.md").write_text("# Manifest", encoding="utf-8")
        (self.temp_dir / "01_AUTHORITY_HIERARCHY.md").write_text("# Hierarchy", encoding="utf-8")
        (self.temp_dir / "04_CLAIM_PROVENANCE_AND_STATUS_RULES.md").write_text("# Rules", encoding="utf-8")
        (self.temp_dir / "06_HUMAN_SOVEREIGNTY_GATES.md").write_text("# Gates", encoding="utf-8")
        (self.temp_dir / "09_HUMAN_RATIFICATION_LEDGER.md").write_text(
            "# Ledger\n| Date | Gate | Target | Status | Notes |\n| 2026-10-20 | P01_GATE | P01 | LOCK | Verified |\n",
            encoding="utf-8"
        )
        (self.temp_dir / "10_ESCALATION_QUEUE.md").write_text("# Escalation Queue\n", encoding="utf-8")

        state_content = """schema_version: 1
architecture:
  canonical: "P01-P11"
  status: LOCK
paragraphs:
  P01: LOCK
  P02: PROPOSED
workflow:
  current_stage: "PARAGRAPH_ASSEMBLY"
  next_stage: "STAGED_PROSE"
  next_human_gate: "P02_RATIFICATION"
permissions:
  corpus_expansion: HUMAN_ONLY
  architecture_change: HUMAN_ONLY
  scholarly_lock: HUMAN_ONLY
  novelty_priority: HUMAN_ONLY
  contribution_hierarchy: HUMAN_ONLY
  prose_without_locked_ledger: FORBIDDEN
  commit: HUMAN_ONLY
  push: HUMAN_ONLY
"""
        (self.temp_dir / "08_CURRENT_STATE.yaml").write_text(state_content, encoding="utf-8")
        self.validator = ControlBundleValidator(self.temp_dir, self.schema_dir)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_valid_bundle_passes(self):
        passed, errors = self.validator.validate_all()
        self.assertTrue(passed, f"Valid bundle should pass, got errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_missing_critical_file_fails(self):
        (self.temp_dir / "06_HUMAN_SOVEREIGNTY_GATES.md").unlink()
        passed, errors = self.validator.validate_all()
        self.assertFalse(passed)
        self.assertTrue(any("06_HUMAN_SOVEREIGNTY_GATES.md" in e for e in errors))

    def test_unratified_lock_fails(self):
        # Tamper state so P02 is marked LOCK without ledger entry
        state_tampered = """schema_version: 1
architecture:
  canonical: "P01-P11"
  status: LOCK
paragraphs:
  P01: LOCK
  P02: LOCK
workflow:
  current_stage: "TEST"
  next_stage: "TEST"
  next_human_gate: "TEST"
permissions:
  corpus_expansion: HUMAN_ONLY
  architecture_change: HUMAN_ONLY
  scholarly_lock: HUMAN_ONLY
  novelty_priority: HUMAN_ONLY
  contribution_hierarchy: HUMAN_ONLY
  prose_without_locked_ledger: FORBIDDEN
  commit: HUMAN_ONLY
  push: HUMAN_ONLY
"""
        (self.temp_dir / "08_CURRENT_STATE.yaml").write_text(state_tampered, encoding="utf-8")
        passed, errors = self.validator.validate_all()
        self.assertFalse(passed)
        self.assertTrue(any("Paragraph P02 marked LOCK" in e for e in errors))

    def test_tampered_permission_fails(self):
        state_tampered = """schema_version: 1
architecture:
  canonical: "P01-P11"
  status: LOCK
paragraphs:
  P01: LOCK
workflow:
  current_stage: "TEST"
  next_stage: "TEST"
  next_human_gate: "TEST"
permissions:
  corpus_expansion: AGENT_AUTONOMOUS
  architecture_change: HUMAN_ONLY
  scholarly_lock: HUMAN_ONLY
  novelty_priority: HUMAN_ONLY
  contribution_hierarchy: HUMAN_ONLY
  prose_without_locked_ledger: FORBIDDEN
  commit: HUMAN_ONLY
  push: HUMAN_ONLY
"""
        (self.temp_dir / "08_CURRENT_STATE.yaml").write_text(state_tampered, encoding="utf-8")
        passed, errors = self.validator.validate_all()
        self.assertFalse(passed)
        self.assertTrue(any("corpus_expansion" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
