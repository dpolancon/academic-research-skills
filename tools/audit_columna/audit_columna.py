#!/usr/bin/env python3
"""
audit_columna.py — Auditor Determinístico Editorial de Prosa Pública y Ensayo

Herramienta de diagnóstico estático para verificar requisitos formales, heurísticas
de registro y preguntas de revisión sustantiva en columnas y ensayos públicos.

Soporta perfiles de medio (ej. Jacobin América Latina) y modo genérico para
diversos formatos de divulgación académica.

Autoridad delimitada:
  1. Fallos Mecánicos: Infracciones formales demostrables contra reglas aplicables.
  2. Advertencias Heurísticas: Patrones o términos que ameritan inspección editorial.
  3. Preguntas Sustantivas: Asuntos de mérito y causalidad que ningún script puede verificar.

Uso:
    python audit_columna.py ruta/a/tu_columna.md [--venue {jacobin,generic}] [--require-latam-comparisons] [--require-weber] [--json]
"""

import sys
import re
import argparse
import json
from pathlib import Path
from typing import List, Dict, Tuple, Any

# Países de América Latina para inspección geográfica regional
PAISES_LATAM = [
    "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Costa Rica",
    "Cuba", "Ecuador", "El Salvador", "Guatemala", "Honduras", "México",
    "Nicaragua", "Panamá", "Paraguay", "Perú", "Puerto Rico",
    "República Dominicana", "Uruguay", "Venezuela"
]

# Términos de jerga académica endogámica a traducir a relaciones materiales
JERGA_ACADEMICA = [
    ("historiografía", "historia oficial / relato dominante"),
    ("populismo macroeconómico", "el mito del derroche fiscal popular"),
    ("veto estructural", "huelga patronal de inversiones / salida de capitales"),
    ("estudio de evento", "seguimiento diario de la reacción del mercado"),
    ("señoreaje", "creación de dinero / emisión"),
    ("emisión inorgánica", "creación monetaria sin respaldo productivo"),
    ("rigideces estructurales", "límites físicos de la oferta / atraso productivo"),
    ("choques exógenos", "agresiones externas deliberadas / estrangulamiento financiero"),
    ("admisibilidad", "solidez empírica / coherencia material"),
    ("balance de pagos", "asfixia de divisas / escasez de dólares")
]

# Clichés panfletarios y adjetivos viscerales (específicos de Jacobin AL)
CLICHES_PANFLETARIOS = [
    "burguesía rapaz", "pueblo heroico", "lacayos", "la lucha continúa",
    "a las calles", "odio de clase", "planes siniestros", "salvaje capitalismo",
    "vilmente", "parasitaria oligarquía"
]

# Fórmulas de contemporaneización indicativas
KEYWORDS_CONTEMPORANEO = [
    "2020", "2021", "2022", "2023", "2024", "2025", "2026",
    "post-pandemia", "pospandemia", "pandemia", "hoy", "actual",
    "reciente", "contemporáneo", "isabella weber", "sellers' inflation",
    "inflación de vendedores", "márgenes empresariales", "márgenes de ganancia"
]

# Fórmulas meta-académicas de tesis doctoral prohibidas en apertura o cierre
CLICHES_ACADEMICOS = [
    "la historiografía ha establecido",
    "la literatura económica ha debatido",
    "este trabajo analiza",
    "en este artículo sostengo",
    "es necesario seguir investigando",
    "futuras investigaciones deberán",
    "queda por estudiar",
    "se requieren más estudios"
]


def strip_markdown(text: str) -> str:
    """Remueve formato markdown pesado para conteo limpio de palabras de prosa."""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\|.*?\|', '', text)
    return text


def extract_sections(raw_text: str) -> Tuple[str, List[str], str, str]:
    """Extrae título H1, párrafos, texto de apertura y texto de cierre."""
    lines = raw_text.splitlines()
    title = ""
    for line in lines:
        if line.strip().startswith("# "):
            title = line.strip()[2:].strip()
            break

    # Párrafos de prosa sustantiva (omitir encabezados o líneas vacías)
    raw_paras = [p.strip() for p in raw_text.split("\n\n")]
    paragraphs = []
    for p in raw_paras:
        clean_p = strip_markdown(p).strip()
        if len(clean_p.split()) >= 15:
            paragraphs.append(p)

    opening = " ".join(paragraphs[:2]) if len(paragraphs) >= 2 else (paragraphs[0] if paragraphs else "")
    closing = " ".join(paragraphs[-2:]) if len(paragraphs) >= 2 else (paragraphs[-1] if paragraphs else "")
    return title, paragraphs, opening, closing


def is_in_quotes_or_block(match_span: Tuple[int, int], raw_text: str) -> bool:
    """Detecta si un término aparece dentro de una cita explícita (bloque > o comillas)."""
    start, end = match_span
    line_start = raw_text.rfind('\n', 0, start)
    line_start = 0 if line_start == -1 else line_start + 1
    line_prefix = raw_text[line_start:start].strip()
    if line_prefix.startswith('>'):
        return True

    # Verificar comillas dobles o angulares cercanas
    surrounding_start = max(0, start - 200)
    surrounding_end = min(len(raw_text), end + 200)
    snippet_before = raw_text[surrounding_start:start]
    snippet_after = raw_text[end:surrounding_end]
    quotes_before = snippet_before.count('"') + snippet_before.count('«')
    quotes_after = snippet_after.count('"') + snippet_after.count('»')
    if (quotes_before % 2 == 1) and (quotes_after % 2 == 1):
        return True

    return False


def auditar_columna(filepath: str, venue: str = "jacobin",
                    require_latam_comparisons: bool = False,
                    require_weber: bool = False,
                    as_json: bool = False) -> Dict[str, Any]:
    path = Path(filepath)
    if not path.exists():
        err_msg = f"Error: El archivo '{filepath}' no existe."
        if as_json:
            print(json.dumps({"error": err_msg}))
            sys.exit(1)
        else:
            print(f"❌ {err_msg}")
            sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    clean_text = strip_markdown(raw_text)
    words = clean_text.split()
    total_words = len(words)

    title, paragraphs, opening_text, closing_text = extract_sections(raw_text)
    title_words = len(title.split()) if title else 0
    has_subtitle = (":" in title) or ("—" in title) or (" - " in title)

    # Inicializar las tres capas de salida
    mechanical_failures: List[Dict[str, Any]] = []
    heuristic_warnings: List[Dict[str, Any]] = []
    substantive_questions: List[str] = []

    # -------------------------------------------------------------
    # 1. EVALUACIÓN MECÁNICA (Hard Gates del Medio / Formato)
    # -------------------------------------------------------------
    if not title:
        mechanical_failures.append({
            "check": "missing-title",
            "message": "No se detectó encabezado principal H1 (# Título)."
        })

    if venue.lower() in ["jacobin", "jacobin-lat", "profiles/venues/jacobin-lat.md"]:
        # Título Jacobin: <= 12 palabras, sin subtítulo ni dos puntos
        if title:
            if has_subtitle:
                mechanical_failures.append({
                    "check": "jacobin-subtitle-prohibited",
                    "message": f"El título contiene ':' o guión de subtítulo. Jacobin prohíbe subtítulos: debe ser tesis declarativa."
                })
            if title_words > 12:
                mechanical_failures.append({
                    "check": "jacobin-title-length",
                    "message": f"El título tiene {title_words} palabras (máximo estricto: 12 palabras)."
                })

        # Extensión Jacobin: rango admisible 1.400 - 2.600 palabras
        if total_words < 1400:
            mechanical_failures.append({
                "check": "word-count-underflow",
                "message": f"Extensión insuficiente: {total_words} palabras (mínimo Jacobin: 1.400; meta: 1.800–2.000)."
            })
        elif total_words > 2600:
            mechanical_failures.append({
                "check": "word-count-overflow",
                "message": f"Extensión excesiva: {total_words} palabras (máximo Jacobin: 2.600)."
            })

    elif venue.lower() == "generic":
        # En modo genérico se permiten subtítulos y colons; límites de palabra son heurísticos
        if total_words < 600:
            mechanical_failures.append({
                "check": "word-count-underflow",
                "message": f"Extensión demasiado breve para ensayo u op-ed: {total_words} palabras."
            })
        elif total_words > 4000:
            mechanical_failures.append({
                "check": "word-count-overflow",
                "message": f"Extensión excede el marco estándar de divulgación: {total_words} palabras."
            })

    # Requisitos de encargo explícitos (Commissions específicas)
    if require_latam_comparisons:
        paises_detectados = [p for p in PAISES_LATAM if re.search(r'\b' + re.escape(p) + r'\b', raw_text, re.IGNORECASE)]
        if len(paises_detectados) < 3:
            mechanical_failures.append({
                "check": "assignment-latam-comparisons",
                "message": f"Encargo requiere comparar >= 3 países de la región; se detectaron {len(paises_detectados)}: {', '.join(paises_detectados)}."
            })

    if require_weber:
        has_weber = bool(re.search(r'\bweber\b', raw_text, re.IGNORECASE))
        if not has_weber:
            mechanical_failures.append({
                "check": "assignment-weber-citation",
                "message": "Encargo requiere citar a Isabella Weber / sellers' inflation para debate de costos."
            })

    # -------------------------------------------------------------
    # 2. ADVERTENCIAS HEURÍSTICAS (Alertas de Revisión Editorial)
    # -------------------------------------------------------------
    # Clichés académicos en apertura o cierre
    for cliche in CLICHES_ACADEMICOS:
        if cliche in opening_text.lower():
            heuristic_warnings.append({
                "check": "academic-opening-phrase",
                "pattern": cliche,
                "location": "opening",
                "message": f"Apertura contiene fórmula meta-académica: '{cliche}'."
            })
        if cliche in closing_text.lower():
            heuristic_warnings.append({
                "check": "academic-closing-phrase",
                "pattern": cliche,
                "location": "closing",
                "message": f"Cierre contiene fórmula evasiva académica: '{cliche}' (rematar con balance político)."
            })

    # Detección de jerga técnica a des-especializar
    for termino, sugerencia in JERGA_ACADEMICA:
        matches = list(re.finditer(r'\b' + re.escape(termino) + r'\b', raw_text, re.IGNORECASE))
        for m in matches:
            in_quote = is_in_quotes_or_block(m.span(), raw_text)
            heuristic_warnings.append({
                "check": "academic-jargon",
                "term": termino,
                "in_quote": in_quote,
                "suggestion": sugerencia,
                "message": f"Término especializado '{termino}' detectado {'(en cita)' if in_quote else ''}. Considerar sugerencia: '{sugerencia}'."
            })

    # Detección de clichés panfletarios / eslóganes (en perfil Jacobin)
    if venue.lower() in ["jacobin", "jacobin-lat", "profiles/venues/jacobin-lat.md"]:
        for panfleto in CLICHES_PANFLETARIOS:
            matches = list(re.finditer(r'\b' + re.escape(panfleto) + r'\b', raw_text, re.IGNORECASE))
            for m in matches:
                in_quote = is_in_quotes_or_block(m.span(), raw_text)
                if in_quote:
                    heuristic_warnings.append({
                        "check": "panfletary-cliche-quoted",
                        "term": panfleto,
                        "in_quote": True,
                        "message": f"Frase panfletaria '{panfleto}' detectada en cita/bloque textual. Verificar encuadre crítico."
                    })
                else:
                    heuristic_warnings.append({
                        "check": "panfletary-cliche",
                        "term": panfleto,
                        "in_quote": False,
                        "message": f"Cliché panfletario en voz de autor: '{panfleto}'. Reemplazar por explicación forense del mecanismo material."
                    })

    # Anclaje contemporáneo heurístico
    has_contemporary_opening = any(kw in opening_text.lower() for kw in KEYWORDS_CONTEMPORANEO)
    if not has_contemporary_opening and venue.lower() in ["jacobin", "jacobin-lat"]:
        heuristic_warnings.append({
            "check": "contemporary-hook-absent",
            "message": "Los primeros párrafos no contienen anclajes temporales recientes explícitos (revisar si conecta con el presente)."
        })

    # -------------------------------------------------------------
    # 3. PREGUNTAS SUSTANTIVAS (Materias que el script no puede certificar)
    # -------------------------------------------------------------
    substantive_questions.append("¿Se preservan fielmente los mecanismos y límites empíricos del estudio sin exagerar la certeza causal?")
    substantive_questions.append("¿Las cifras y relaciones de balance citadas cuentan con respaldo documental o estadístico trazable?")
    if venue.lower() in ["jacobin", "jacobin-lat"]:
        substantive_questions.append("¿El encuadre teórico sitúa la disputa en el eje de clase (economía burguesa vs. crítica de la economía política)?")
    else:
        substantive_questions.append("¿El tono y nivel de detalle corresponden adecuadamente al público y género seleccionado?")

    # -------------------------------------------------------------
    # 4. DETERMINACIÓN DE VEREDICTO
    # -------------------------------------------------------------
    if mechanical_failures:
        verdict = "FAIL"
    elif any(w.get("check") == "panfletary-cliche" and not w.get("in_quote") for w in heuristic_warnings):
        verdict = "REVIEW_REQUIRED"
    elif heuristic_warnings:
        verdict = "PASS_WITH_WARNINGS"
    else:
        verdict = "PASS"

    result = {
        "file": path.name,
        "venue": venue,
        "verdict": verdict,
        "total_words": total_words,
        "title": title,
        "title_words": title_words,
        "mechanical_failures": mechanical_failures,
        "heuristic_warnings": heuristic_warnings,
        "substantive_review_questions": substantive_questions
    }

    if as_json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result

    # Salida formateada de terminal
    print("=" * 75)
    print(f"📋 REPORTE DE AUDITORÍA EDITORIAL DE PROSA PÚBLICA")
    print(f"Archivo: {path.name} | Perfil: {venue.upper()} | Palabras: {total_words}")
    print("=" * 75)
    if verdict == "PASS":
        print("VEREDICTO: ✅ APROBADO (Sin infracciones mecánicas)")
    elif verdict == "PASS_WITH_WARNINGS":
        print("VEREDICTO: ⚠️ APROBADO CON ADVERTENCIAS (Revisar observaciones heurísticas)")
    elif verdict == "REVIEW_REQUIRED":
        print("VEREDICTO: ⚠️ REQUIERE REVISIÓN (Detectadas expresiones que ameritan sustitución)")
    else:
        print("VEREDICTO: ❌ RECHAZADO (Presenta infracciones mecánicas formales)")
    print("-" * 75)

    print("\n1. FALLOS MECÁNICOS (HARD GATES):")
    if mechanical_failures:
        for f in mechanical_failures:
            print(f"   ❌ [{f['check']}] {f['message']}")
    else:
        print("   ✅ Ningún fallo mecánico detectado.")

    print("\n2. ADVERTENCIAS HEURÍSTICAS (OBSERVACIONES DE REVISIÓN):")
    if heuristic_warnings:
        for w in heuristic_warnings:
            quote_tag = " (en cita)" if w.get("in_quote") else ""
            print(f"   ⚠️ [{w['check']}]{quote_tag} {w['message']}")
    else:
        print("   ✅ Ninguna advertencia heurística registrada.")

    print("\n3. PREGUNTAS DE REVISIÓN SUSTANTIVA (EVALUACIÓN HUMANA/EDITORIAL):")
    for q in substantive_questions:
        print(f"   🔍 {q}")

    print("=" * 75)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auditor determinístico para columnas y ensayos de economía política.")
    parser.add_argument("file", help="Ruta al archivo Markdown de la columna")
    parser.add_argument("--venue", default="jacobin", choices=["jacobin", "generic", "jacobin-lat"],
                        help="Perfil de medio a aplicar (default: jacobin)")
    parser.add_argument("--require-latam-comparisons", action="store_true",
                        help="Encargo específico: exigir mención/comparación de >= 3 países de AL")
    parser.add_argument("--require-weber", action="store_true",
                        help="Encargo específico: exigir mención a Isabella Weber / sellers' inflation")
    parser.add_argument("--json", action="store_true", help="Emitir reporte en formato JSON")

    args = parser.parse_args()
    res = auditar_columna(
        args.file,
        venue=args.venue,
        require_latam_comparisons=args.require_latam_comparisons,
        require_weber=args.require_weber,
        as_json=args.json
    )
    if res["verdict"] == "FAIL":
        sys.exit(1)
    sys.exit(0)
