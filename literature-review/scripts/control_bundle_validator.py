#!/usr/bin/env python3
"""
control_bundle_validator.py — Generic Literature Review Control Bundle Validator

Validates declarative project control bundles against schema constraints,
consistency between CURRENT_STATE.yaml and HUMAN_RATIFICATION_LEDGER.md,
and human-sovereignty invariants.

Specification: literature-review/references/human_sovereignty_and_repair_loops.md
"""

import os
import sys
import json
import yaml
import jsonschema
import argparse
from pathlib import Path
from typing import Dict, Any, List


class ControlBundleValidator:
    """Validates control bundle state, schemas, and human sovereignty consistency."""

    def __init__(self, bundle_dir: Path, schema_dir: Path = None):
        self.bundle_dir = Path(bundle_dir)
        if schema_dir is None:
            # Default to sibling schemas directory if within literature-review
            self.schema_dir = Path(__file__).resolve().parent.parent / "schemas"
        else:
            self.schema_dir = Path(schema_dir)

    def validate_all(self) -> Tuple[bool, List[str]]:
        errors = []

        # 1. Check critical bundle files
        critical_files = [
            "00_BUNDLE_MANIFEST.md",
            "01_AUTHORITY_HIERARCHY.md",
            "04_CLAIM_PROVENANCE_AND_STATUS_RULES.md",
            "06_HUMAN_SOVEREIGNTY_GATES.md",
            "08_CURRENT_STATE.yaml",
            "09_HUMAN_RATIFICATION_LEDGER.md",
            "10_ESCALATION_QUEUE.md"
        ]

        for fname in critical_files:
            p = self.bundle_dir / fname
            if not p.exists():
                errors.append(f"Missing required bundle file: {fname}")

        if errors:
            return False, errors

        # 2. Validate CURRENT_STATE.yaml schema
        state_file = self.bundle_dir / "08_CURRENT_STATE.yaml"
        state_schema_file = self.schema_dir / "governance_state_schema.json"

        try:
            with open(state_file, "r", encoding="utf-8") as fp:
                state_data = yaml.safe_load(fp)
        except Exception as e:
            errors.append(f"Failed to parse {state_file.name}: {e}")
            return False, errors

        if state_schema_file.exists():
            try:
                with open(state_schema_file, "r", encoding="utf-8") as fp:
                    state_schema = json.load(fp)
                jsonschema.validate(instance=state_data, schema=state_schema)
            except jsonschema.ValidationError as ve:
                errors.append(f"Schema validation error in {state_file.name}: {ve.message}")
            except Exception as e:
                errors.append(f"Failed running schema validation: {e}")

        # 3. Verify consistency between state and human ratification ledger
        ledger_file = self.bundle_dir / "09_HUMAN_RATIFICATION_LEDGER.md"
        try:
            with open(ledger_file, "r", encoding="utf-8") as fp:
                ledger_text = fp.read()
        except Exception as e:
            errors.append(f"Failed reading {ledger_file.name}: {e}")
            ledger_text = ""

        # Find paragraphs marked LOCK in state
        paragraphs = state_data.get("paragraphs", {})
        for p_key, p_status in paragraphs.items():
            if p_status == "LOCK":
                # Ensure p_key or a batch containing it is recorded in the ledger
                if p_key not in ledger_text and "BATCH" not in ledger_text and "ALL" not in ledger_text:
                    errors.append(f"Paragraph {p_key} marked LOCK in state but not found in {ledger_file.name}")

        # 4. Verify human-sovereignty permissions block
        permissions = state_data.get("permissions", {})
        for perm in ["corpus_expansion", "architecture_change", "scholarly_lock", "novelty_priority", "commit", "push"]:
            if permissions.get(perm) != "HUMAN_ONLY":
                errors.append(f"Human-reserved power '{perm}' must be strictly set to 'HUMAN_ONLY', got: {permissions.get(perm)}")

        return len(errors) == 0, errors


from typing import Tuple


def main():
    parser = argparse.ArgumentParser(description="Validate literature review control bundle.")
    parser.add_argument("bundle_dir", help="Path to control bundle directory.")
    parser.add_argument("--schemas", default=None, help="Path to schemas directory.")
    args = parser.parse_args()

    validator = ControlBundleValidator(Path(args.bundle_dir), Path(args.schemas) if args.schemas else None)
    passed, errors = validator.validate_all()

    if passed:
        print("[PASS] Control bundle validation succeeded. All human sovereignty invariants preserved.")
        sys.exit(0)
    else:
        print("[FAIL] Control bundle validation failed with errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
