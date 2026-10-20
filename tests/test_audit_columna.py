"""
test_audit_columna.py — Unit Tests for Column and Public Essay Auditor
Verifies bounded authority: mechanical gates, heuristic warnings, venue profiles,
and assignment-specific flags.
"""

import sys
import tempfile
from pathlib import Path
import pytest

# Ensure editor-jacobin-lat/scripts is in sys.path
scripts_dir = Path(__file__).resolve().parent.parent / "editor-jacobin-lat" / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from audit_columna import auditar_columna


def create_temp_column(tmp_path: Path, title: str, paragraphs: list) -> Path:
    col_path = tmp_path / "columna_test.md"
    body = "\n\n".join(paragraphs)
    content = f"# {title}\n\n{body}\n"
    col_path.write_text(content, encoding="utf-8")
    return col_path


def make_paragraph(seed: str, word_count: int) -> str:
    """Generates clean prose paragraph with approximately target words."""
    words = (seed + " ") * (word_count // len(seed.split()) + 1)
    return " ".join(words.split()[:word_count])


def test_generic_op_ed_passes_generic_mode(tmp_path):
    """Generic op-ed with colon/subtitle passes cleanly under --venue generic."""
    # 900 words, colon in title, no Weber, no LatAm mentions
    title = "The Cost of Credit: Why Central Banks Overcorrected"
    paras = [
        make_paragraph("Recent interest rate hikes in 2024 have tightened credit conditions across domestic markets.", 120),
        make_paragraph("Commercial banks responded by restricting small business lending while expanding liquidity reserves.", 150),
        make_paragraph("The mechanism operates through wholesale interbank funding costs and collateral requirements.", 150),
        make_paragraph("When borrowing costs increase, business investment slows down and hiring plans are curtailed.", 150),
        make_paragraph("Policymakers must consider credit guidance and selective facilities to prevent productive contraction.", 150),
        make_paragraph("A balanced approach requires coordinating regulatory reserve requirements with broader industrial goals.", 180),
    ]
    path = create_temp_column(tmp_path, title, paras)
    result = auditar_columna(str(path), venue="generic", as_json=False)

    assert result["verdict"] in ["PASS", "PASS_WITH_WARNINGS"]
    assert len(result["mechanical_failures"]) == 0
    assert result["total_words"] >= 800


def test_jacobin_subtitle_fails_mechanical_gate(tmp_path):
    """Jacobin profile strictly bans colons and subtitles in titles."""
    title = "Socialismo e inflación: Las lecciones de la Unidad Popular chilena"
    paras = [make_paragraph("Durante los años recientes el debate sobre la inflación ha vuelto a ocupar el centro de la escena política.", 100)] * 18
    path = create_temp_column(tmp_path, title, paras)

    result = auditar_columna(str(path), venue="jacobin", as_json=False)
    assert result["verdict"] == "FAIL"
    failures = [f["check"] for f in result["mechanical_failures"]]
    assert "jacobin-subtitle-prohibited" in failures


def test_jacobin_title_length_exceeded(tmp_path):
    """Jacobin profile bans titles exceeding 12 words."""
    title = "Contra el mito persistente y generalizado de que todo gobierno popular produce necesariamente una gran inflación"
    assert len(title.split()) > 12
    paras = [make_paragraph("En los debates económicos contemporáneos sobre la inflación de oferta se observa una constante pugna distributiva.", 100)] * 18
    path = create_temp_column(tmp_path, title, paras)

    result = auditar_columna(str(path), venue="jacobin", as_json=False)
    assert result["verdict"] == "FAIL"
    failures = [f["check"] for f in result["mechanical_failures"]]
    assert "jacobin-title-length" in failures


def test_jacobin_valid_essay_passes(tmp_path):
    """Valid Jacobin essay with declarative title <= 12 words and 1800 words passes."""
    title = "Contra el mito de que el gasto social produce inflación"
    paras = [
        "En los últimos años entre 2022 y 2026 el debate sobre la inflación post-pandemia ha demostrado que los aumentos de precios respondieron a choques de costos y márgenes empresariales más que a excesos de demanda popular.",
    ] + [make_paragraph("La evidencia material confirma que las corporaciones concentradas trasladaron inmediatamente los costos externos hacia los precios finales.", 100)] * 18
    path = create_temp_column(tmp_path, title, paras)

    result = auditar_columna(str(path), venue="jacobin", as_json=False)
    assert len(result["mechanical_failures"]) == 0
    assert result["verdict"] in ["PASS", "PASS_WITH_WARNINGS"]


def test_agitprop_in_quotes_treated_as_heuristic_warning(tmp_path):
    """Blacklisted phrases inside quotations are flagged as quoted rather than uncritical author prose."""
    title = "El conflicto distributivo y los precios"
    paras = [
        "El debate contemporáneo sobre la inflación exige rigor analítico y distancia crítica.",
        '> El editorial acusó a los dirigentes de ser una "burguesía rapaz" empeñada en la desestabilización.',
        make_paragraph("Sin embargo, el análisis forense de los flujos de caja y las reservas del Banco Central revela que los precios aumentaron por estrangulamiento de divisas.", 120),
    ] + [make_paragraph("La política económica debe sustentarse en la evidencia y no en acusaciones morales vacías.", 100)] * 16
    path = create_temp_column(tmp_path, title, paras)

    result = auditar_columna(str(path), venue="jacobin", as_json=False)
    # Quotes should be recognized as quoted
    quoted_warnings = [w for w in result["heuristic_warnings"] if w.get("check") == "panfletary-cliche-quoted"]
    assert len(quoted_warnings) > 0
    assert quoted_warnings[0]["in_quote"] is True


def test_assignment_specific_flags(tmp_path):
    """Assignment-specific flags (multi-country, Weber) are disabled by default and fail only when enabled."""
    title = "La asfixia de divisas en la economía chilena"
    paras = [
        "El estrangulamiento de divisas en Chile durante los años setenta refleja una contradicción estructural permanente.",
    ] + [make_paragraph("Las reservas de divisas cayeron drásticamente ante el corte de créditos comerciales de los bancos de Wall Street.", 100)] * 17
    path = create_temp_column(tmp_path, title, paras)

    # 1. Default run: Passes without multi-country or Weber
    default_res = auditar_columna(str(path), venue="jacobin", as_json=False)
    assert "assignment-latam-comparisons" not in [f["check"] for f in default_res["mechanical_failures"]]
    assert "assignment-weber-citation" not in [f["check"] for f in default_res["mechanical_failures"]]

    # 2. Assignment flag activated: fails when requirement is not satisfied
    flagged_res = auditar_columna(str(path), venue="jacobin", require_latam_comparisons=True, require_weber=True, as_json=False)
    failures = [f["check"] for f in flagged_res["mechanical_failures"]]
    assert "assignment-latam-comparisons" in failures
    assert "assignment-weber-citation" in failures
