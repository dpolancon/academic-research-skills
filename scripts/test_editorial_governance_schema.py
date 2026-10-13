#!/usr/bin/env python3
"""
scripts/test_editorial_governance_schema.py

Schema validation and structural regression test suite for Wave C2:
1. Validates editorial_governance.schema.json and revision_verification.schema.json
2. Enforces Three-Axis State Model semantics
3. Enforces Release Policy enums (optional, recommended, required)
4. Enforces Material Passport Summary Port structure and sidecar/passport separation
5. Confirms removal of mandatory DAG and schema self-pinning requirements
"""

import sys
import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts import revision_guard as guard


def valid_sidecar_sample() -> dict:
    return {
        "schema_version": "1.0",
        "governance_id": "gov-sample-01",
        "release_policy": "optional",
        "active_decision_count": 1,
        "unresolved_decision_count": 0,
        "decisions": [
            {
              "decision_id": "D-001",
              "resolution": "ACCEPT",
              "authorization": "ALLOWED",
              "action": "IMPLEMENTED",
              "rationale": "Clarify baseline methodology.",
              "scope": {
                "artifact_id": "manuscript",
                "locations": [
                  {
                    "location_id": "LOC-01",
                    "start": "START",
                    "end": "END"
                  }
                ]
              }
            }
        ]
    }


def valid_verification_result_sample() -> dict:
    return {
        "schema_version": "1.0",
        "verifier_version": "1.0.0",
        "governance_id": "gov-sample-01",
        "overall": "PASS",
        "verdict": "PASS",
        "release_policy": "optional",
        "release_certified": False,
        "passport_summary": {
            "governance_id": "gov-sample-01",
            "verification_verdict": "PASS",
            "active_decision_count": 1,
            "unresolved_decision_count": 0,
            "source_hash": "a" * 64
        },
        "checks": [
            {
                "check_id": "scope_check",
                "status": "PASS",
                "detail": "All changes within authorized regions."
            }
        ]
    }


def test_schemas_well_formed():
    """Confirms that both schemas are syntactically valid Draft 2020-12 JSON schemas."""
    for schema_name in ("editorial_governance", "revision_verification"):
        val = guard.validator(schema_name)
        Draft202012Validator.check_schema(val.schema)
    print("  [PASS] Both schemas are valid Draft 2020-12 JSON schemas.")


def test_valid_sidecar_accepted():
    """Confirms that a compliant lightweight sidecar passes validation."""
    sample = valid_sidecar_sample()
    val = guard.validator("editorial_governance")
    errors = list(val.iter_errors(sample))
    assert not errors, f"Valid sidecar failed schema: {errors}"
    print("  [PASS] Compliant lightweight sidecar accepted.")


def test_malformed_sidecar_rejected():
    """Confirms that invalid structures are caught and rejected."""
    val = guard.validator("editorial_governance")

    # Missing decisions
    sample = valid_sidecar_sample()
    del sample["decisions"]
    assert list(val.iter_errors(sample)), "Missing 'decisions' must fail schema."

    # Invalid version
    sample = valid_sidecar_sample()
    sample["schema_version"] = "2.0"
    assert list(val.iter_errors(sample)), "Invalid schema_version must fail schema."

    # Unknown root property
    sample = valid_sidecar_sample()
    sample["unrecognized_root_property"] = True
    assert list(val.iter_errors(sample)), "additionalProperties: false must reject unknown root."
    print("  [PASS] Malformed sidecars properly rejected.")


def test_required_fields_enforced():
    """Confirms that schema_version, governance_id, and decisions are mandatory."""
    val = guard.validator("editorial_governance")
    for field in ("schema_version", "governance_id", "decisions"):
        sample = valid_sidecar_sample()
        del sample[field]
        assert list(val.iter_errors(sample)), f"Missing required field '{field}' must fail schema."
    print("  [PASS] Mandatory sidecar fields enforced.")


def test_three_axis_enum_semantics():
    """Confirms valid enums for Resolution, Authorization, and Action axes."""
    val = guard.validator("editorial_governance")

    # Valid values
    valid_resolutions = ["ACCEPT", "REJECT", "DEFER", "UNRESOLVED"]
    valid_authorizations = ["ALLOWED", "FORBIDDEN", "CONDITIONAL", "NOT_SPECIFIED"]
    valid_actions = ["IMPLEMENTED", "NOT_IMPLEMENTED", "PARTIAL", "OUT_OF_SCOPE_CHANGE"]

    for r in valid_resolutions:
        sample = valid_sidecar_sample()
        sample["decisions"][0]["resolution"] = r
        assert not list(val.iter_errors(sample)), f"Resolution '{r}' must be valid."

    for a in valid_authorizations:
        sample = valid_sidecar_sample()
        sample["decisions"][0]["authorization"] = a
        assert not list(val.iter_errors(sample)), f"Authorization '{a}' must be valid."

    for act in valid_actions:
        sample = valid_sidecar_sample()
        sample["decisions"][0]["action"] = act
        assert not list(val.iter_errors(sample)), f"Action '{act}' must be valid."

    # Invalid values
    sample = valid_sidecar_sample()
    sample["decisions"][0]["resolution"] = "INVALID_RESOLUTION"
    assert list(val.iter_errors(sample)), "Invalid resolution enum must fail."

    sample = valid_sidecar_sample()
    sample["decisions"][0]["authorization"] = "INVALID_AUTH"
    assert list(val.iter_errors(sample)), "Invalid authorization enum must fail."

    sample = valid_sidecar_sample()
    sample["decisions"][0]["action"] = "INVALID_ACTION"
    assert list(val.iter_errors(sample)), "Invalid action enum must fail."

    print("  [PASS] Three-axis enum semantics validated.")


def test_release_policy_enum():
    """Confirms supported release policies: optional, recommended, required."""
    val = guard.validator("editorial_governance")
    for policy in ("optional", "recommended", "required"):
        sample = valid_sidecar_sample()
        sample["release_policy"] = policy
        assert not list(val.iter_errors(sample)), f"Policy '{policy}' must be valid."

    sample = valid_sidecar_sample()
    sample["release_policy"] = "mandatory_blocker"
    assert list(val.iter_errors(sample)), "Unsupported release policy must be rejected."
    print("  [PASS] Release policy enum semantics validated.")


def test_verdict_enum():
    """Confirms verification verdicts are strictly PASS, FAIL, INDETERMINATE."""
    val = guard.validator("revision_verification")
    for v in ("PASS", "FAIL", "INDETERMINATE"):
        sample = valid_verification_result_sample()
        sample["overall"] = v
        sample["passport_summary"]["verification_verdict"] = v
        assert not list(val.iter_errors(sample)), f"Verdict '{v}' must be valid."

    sample = valid_verification_result_sample()
    sample["overall"] = "APPROVED_BY_REFEREE"
    assert list(val.iter_errors(sample)), "Overloaded referee verdict must fail schema."
    print("  [PASS] Verdict enum strictly limited to PASS, FAIL, INDETERMINATE.")


def test_material_passport_summary_structure():
    """Confirms structure of the 5-field Material Passport Summary Port."""
    val = guard.validator("revision_verification")
    sample = valid_verification_result_sample()
    summary = sample["passport_summary"]

    required_passport_fields = [
        "governance_id",
        "verification_verdict",
        "active_decision_count",
        "unresolved_decision_count",
        "source_hash",
    ]
    for field in required_passport_fields:
        assert field in summary, f"Missing required passport summary field: {field}"
        sub_sample = copy.deepcopy(sample)
        del sub_sample["passport_summary"][field]
        assert list(val.iter_errors(sub_sample)), f"Omitting passport field '{field}' must fail schema."

    # Null source_hash is allowed if not yet calculated
    sample["passport_summary"]["source_hash"] = None
    assert not list(val.iter_errors(sample)), "Nullable source_hash must be valid."

    print("  [PASS] 5-field Material Passport Summary Port structure validated.")


def test_sidecar_passport_separation():
    """Confirms passport summary does not permit detailed decision records or sentence diffs."""
    val = guard.validator("revision_verification")
    sample = valid_verification_result_sample()
    sample["passport_summary"]["decisions"] = [{"decision_id": "D-01"}]
    assert list(val.iter_errors(sample)), "Passport summary must NOT contain detailed decision records."
    print("  [PASS] Sidecar vs. Passport separation enforced.")


def test_no_dag_or_self_pinning_mandatory():
    """Confirms that DAG predecessor_id and receipt approval_events are not mandatory."""
    val = guard.validator("editorial_governance")
    sample = valid_sidecar_sample()
    assert "predecessor_id" not in sample["decisions"][0]
    assert "approval_events" not in sample
    assert not list(val.iter_errors(sample)), "Sidecar must be valid without predecessor_id or approval_events."
    print("  [PASS] Cryptographic DAG and receipt networks are non-mandatory.")


def main():
    print("=" * 60)
    print("Running ARS Wave C2 Editorial Governance Schema Tests")
    print("=" * 60)
    try:
        test_schemas_well_formed()
        test_valid_sidecar_accepted()
        test_malformed_sidecar_rejected()
        test_required_fields_enforced()
        test_three_axis_enum_semantics()
        test_release_policy_enum()
        test_verdict_enum()
        test_material_passport_summary_structure()
        test_sidecar_passport_separation()
        test_no_dag_or_self_pinning_mandatory()
        print("=" * 60)
        print("ALL EDITORIAL GOVERNANCE SCHEMA TESTS PASSED.")
        print("=" * 60)
        sys.exit(0)
    except AssertionError as e:
        print(f"\n[FAIL] Test failure: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
