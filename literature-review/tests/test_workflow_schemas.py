"""
Deterministic unit test suite for the generic literature-review skill.
Validates schemas, templates, replaceable ExtractionBackend behavior,
exception trigger guardrails, optimization metrics, and absence of project-specific hardcoding.
"""

import json
import unittest
from pathlib import Path
import sys

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from notebooklm_adapter import (  # noqa: E402
    ExtractionBackend,
    ALLOWED_EXCEPTION_TRIGGERS,
    compute_optimization_metrics,
)


class DummyBackend(ExtractionBackend):
    """In-memory mock backend proving ExtractionBackend replaceability without NotebookLM."""

    def list_sources(self):
        return [{"id": "src-1", "title": "Paper A"}, {"id": "src-2", "title": "Paper B"}]

    def ask(self, question: str, source_ids, start_new_session: bool = True):
        if not source_ids:
            raise ValueError("source_ids required")
        return {
            "answer": "Grounded mock response",
            "source_ids": list(source_ids),
            "prompt": question,
            "citations": [{"chunk_id": "chk-01", "offset": [0, 42]}],
        }


class TestLiteratureReviewSkillArchitecture(unittest.TestCase):
    def test_all_schemas_are_valid_json_and_generic(self):
        schemas_dir = SKILL_ROOT / "schemas"
        expected_schemas = [
            "corpus_registry_schema.json",
            "question_object_schema.json",
            "query_pack_schema.json",
            "cluster_citation_contract_schema.json",
            "exception_query_schema.json",
        ]
        for fname in expected_schemas:
            fpath = schemas_dir / fname
            self.assertTrue(fpath.exists(), f"Missing schema file: {fname}")
            content = fpath.read_text(encoding="utf-8")
            data = json.loads(content)
            self.assertEqual(data.get("$schema"), "http://json-schema.org/draft-07/schema#")
            self.assertNotIn("paper-k-stock", content.lower())
            self.assertNotIn("polanco_method", content.lower())

    def test_templates_contain_saturation_and_citation_chunk_locks(self):
        templates_dir = SKILL_ROOT / "templates"
        src_tpl = (templates_dir / "source_note_template.md").read_text(encoding="utf-8")
        clus_tpl = (templates_dir / "cluster_note_template.md").read_text(encoding="utf-8")
        synth_tpl = (templates_dir / "synthesis_note_template.md").read_text(encoding="utf-8")
        ledger_tpl = (templates_dir / "paragraph_ledger_template.md").read_text(encoding="utf-8")

        self.assertIn("EXTRACTION_SATURATED", src_tpl)
        self.assertIn("SOURCE_TIER", src_tpl)
        self.assertIn("CITATION_CHUNK_CONTRACT", clus_tpl)
        self.assertIn("ADJUDICATION_SATURATED", clus_tpl)
        self.assertIn("ADJUDICATED CROSS-LITERATURE HINGE", synth_tpl)
        self.assertIn("CLUSTER CITATION CHUNK", ledger_tpl)

    def test_loop_c_source_query_pack_execution(self):
        backend = DummyBackend()
        res = backend.run_source_query_pack(
            source_id="src-1",
            query_pack_id="QP_CONCEPTS",
            atomic_questions=[
                {"question_id": "Q_001", "question": "How is the concept defined?"},
                {"question_id": "Q_002", "question": "What are its boundaries?"},
            ],
        )
        self.assertEqual(res["pass_type"], "LOOP_C_SOURCE_PASS")
        self.assertEqual(res["atomic_question_ids"], ["Q_001", "Q_002"])
        self.assertIn("[Q_001]", res["backend_response"]["prompt"])
        self.assertIn("[Q_002]", res["backend_response"]["prompt"])

    def test_loop_d_cluster_comparison_requires_multiple_sources(self):
        backend = DummyBackend()
        with self.assertRaises(ValueError):
            backend.run_cluster_comparison(
                source_ids=["src-1"],
                cluster_key="CLUS_TEST",
                atomic_questions=[{"question_id": "Q_001", "question": "Compare definitions."}],
            )
        res = backend.run_cluster_comparison(
            source_ids=["src-1", "src-2"],
            cluster_key="CLUS_TEST",
            atomic_questions=[{"question_id": "Q_001", "question": "Compare definitions."}],
        )
        self.assertEqual(res["pass_type"], "LOOP_D_CLUSTER_PASS")
        self.assertEqual(res["source_ids"], ["src-1", "src-2"])

    def test_loop_e_exception_query_rejects_invalid_triggers(self):
        backend = DummyBackend()
        with self.assertRaises(ValueError):
            backend.run_exception_query(
                exception_record={
                    "exception_id": "EXC_001",
                    "trigger_type": "STARTED_NEW_PARAGRAPH",
                    "durable_notes_updated": ["03_source_notes/SRC_A.md"],
                },
                question="Query for P02",
                source_ids=["src-1"],
            )
        for valid_trigger in ALLOWED_EXCEPTION_TRIGGERS:
            res = backend.run_exception_query(
                exception_record={
                    "exception_id": "EXC_002",
                    "trigger_type": valid_trigger,
                    "durable_notes_updated": ["03_source_notes/SRC_A.md"],
                },
                question="Targeted verification",
                source_ids=["src-1"],
            )
            self.assertEqual(res["pass_type"], "LOOP_E_EXCEPTION_QUERY")

    def test_optimization_metrics_computation(self):
        metrics = compute_optimization_metrics(
            downstream_source_uses=32,
            source_passes_executed=13,
            downstream_query_claims=58,
            query_pack_executions=13,
            downstream_cluster_uses=9,
            cluster_passes_executed=2,
            exception_queries_triggered=1,
            paragraph_ledgers_constructed=6,
            requeried_saturated_sources=1,
            total_saturated_sources=12,
        )
        self.assertAlmostEqual(metrics["source_reuse"], 2.462)
        self.assertAlmostEqual(metrics["query_reuse"], 4.462)
        self.assertAlmostEqual(metrics["cluster_reuse"], 4.5)
        self.assertAlmostEqual(metrics["exception_rate"], 0.167)
        self.assertAlmostEqual(metrics["requery_rate"], 0.083)


if __name__ == "__main__":
    unittest.main()
