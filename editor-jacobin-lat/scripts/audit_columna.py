#!/usr/bin/env python3
"""
audit_columna.py — Auditor Determinístico Editorial para Jacobin América Latina
Calibrado según los criterios de Martín Arboleda y la rúbrica de 100 puntos.
Refinado para exigir prosa pública, asertiva y rigurosa, libre de clichés panfletarios.

Uso:
    python audit_columna.py ruta/a/tu_columna.md
"""

import sys
import re
import os
from pathlib import Path

# Países de América Latina para verificar latinoamericanización
PAISES_LATAM = [
    "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Costa Rica",
    "Cuba", "Ecuador", "El Salvador", "Guatemala", "Honduras", "México",
    "Nicaragua", "Panamá", "Paraguay", "Perú", "Puerto Rico",
    "República Dominicana", "Uruguay", "Venezuela"
]

# Términos de jerga académica a des-especializar
JERGA_ACADEMICA = [
    ("historiografía", "relato oficial de la derecha / historia oficial"),
    ("populismo macroeconómico", "el mito del derroche fiscal popular"),
    ("veto estructural", "huelga patronal de inversiones / boicot de crédito"),
    ("estudio de evento", "seguimiento diario de la reacción del mercado"),
    ("señoreaje", "creación de dinero / emisión"),
    ("emisión inorgánica", "el cliché de la 'maquinita de billetes'"),
    ("rigideces estructurales", "atraso productivo / límites físicos de la oferta"),
    ("choques exógenos", "agresiones externas deliberadas / asfixia financiera"),
    ("admisibilidad", "solidez empírica / coherencia material de los datos"),
    ("balance de pagos", "asfixia de divisas / falta estructural de dólares")
]

# Clichés panfletarios / agitprop a erradicar
CLICHES_PANFLETARIOS = [
    "burguesía rapaz", "pueblo heroico", "lacayos", "la lucha continúa",
    "a las calles", "odio de clase", "planes siniestros", "salvaje capitalismo",
    "vilmente", "parasitaria oligarquía"
]

# Palabras clave de contemporaneización
KEYWORDS_CONTEMPORANEO = [
    "2020", "2021", "2022", "2023", "2024", "2025", "2026",
    "post-pandemia", "pospandemia", "pandemia", "hoy", "actual",
    "reciente", "contemporáneo", "isabella weber", "sellers' inflation",
    "inflación de vendedores", "márgenes empresariales", "márgenes de ganancia"
]

# Clichés académicos prohibidos en apertura o cierre
CLICHES_ACADEMICOS = [
    "la historiografía ha establecido",
    "la literatura económica ha debatido",
    "este trabajo analiza",
    "en este artículo sostengo",
    "es necesario seguir investigando",
    "futuras investigaciones deberán",
    "queda por estudiar"
]


def strip_markdown(text: str) -> str:
    """Remueve formato markdown pesado para conteo limpio de palabras."""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\|.*?\|', '', text)
    return text


def auditar_columna(filepath: str):
    path = Path(filepath)
    if not path.exists():
        print(f"❌ Error: El archivo '{filepath}' no existe.")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    lines = raw_text.splitlines()
    clean_text = strip_markdown(raw_text)
    words = clean_text.split()
    total_words = len(words)

    # 1. TÍTULO
    title = ""
    for line in lines:
        if line.strip().startswith("# "):
            title = line.strip()[2:].strip()
            break

    title_words = len(title.split()) if title else 0
    has_subtitle = (":" in title) or ("—" in title) or (" - " in title)

    # 2. PÁRRAFOS Y APERTURA
    paragraphs = [p.strip() for p in raw_text.split("\n\n") if len(p.strip().split()) > 15]
    opening_text = " ".join(paragraphs[:2]) if len(paragraphs) >= 2 else (paragraphs[0] if paragraphs else "")
    closing_text = " ".join(paragraphs[-2:]) if len(paragraphs) >= 2 else (paragraphs[-1] if paragraphs else "")

    # Contemporaneización en apertura
    has_contemporary_opening = any(kw in opening_text.lower() for kw in KEYWORDS_CONTEMPORANEO)
    has_academic_opening = any(cliche in opening_text.lower() for cliche in [
        "historiografía", "la literatura", "este artículo", "este ensayo"
    ])

    # 3. LATINOAMERICANIZACIÓN (Países detectados)
    paises_detectados = []
    for pais in PAISES_LATAM:
        if re.search(r'\b' + re.escape(pais) + r'\b', raw_text, re.IGNORECASE):
            paises_detectados.append(pais)

    # 4. REFERENCIAS CONTEMPORÁNEAS (Weber, post-2020)
    has_weber = bool(re.search(r'\bweber\b', raw_text, re.IGNORECASE))
    has_post_2020 = any(year in raw_text for year in ["2020", "2021", "2022", "2023", "2024", "2025", "2026"])

    # 5. DETECCIÓN DE JERGA ACADÉMICA
    jerga_encontrada = []
    for termino, sugerencia in JERGA_ACADEMICA:
        matches = len(re.findall(r'\b' + re.escape(termino) + r'\b', raw_text, re.IGNORECASE))
        if matches > 0:
            jerga_encontrada.append((termino, matches, sugerencia))

    # 6. DETECCIÓN DE CLICHÉS PANFLETARIOS
    cliches_detectados = []
    for panfleto in CLICHES_PANFLETARIOS:
        matches = len(re.findall(r'\b' + re.escape(panfleto) + r'\b', raw_text, re.IGNORECASE))
        if matches > 0:
            cliches_detectados.append((panfleto, matches))

    # 7. CIERRE
    has_academic_closing = any(cliche in closing_text.lower() for cliche in [
        "seguir investigando", "futuras investigaciones", "queda por estudiar", "más investigaciones"
    ])

    # CÁLCULO DE SCORE
    score = 0

    # Dimensión 1: Contemporaneización (20 pts)
    p_contemp = 0
    if has_contemporary_opening:
        p_contemp += 12
    if has_post_2020 or has_weber:
        p_contemp += 8
    score += p_contemp

    # Dimensión 2: Des-especialización y Registro Público (20 pts)
    p_desesp = 20 - min(15, len(jerga_encontrada) * 3)
    if cliches_detectados:
        p_desesp -= min(10, len(cliches_detectados) * 5)
    score += max(0, p_desesp)

    # Dimensión 3: Latinoamericanización (15 pts)
    p_latam = 0
    if len(paises_detectados) >= 3:
        p_latam = 15
    elif len(paises_detectados) == 2:
        p_latam = 10
    elif len(paises_detectados) == 1:
        p_latam = 4
    score += p_latam

    # Dimensión 4: Titular Afirmativo (15 pts)
    p_title = 0
    if title:
        if not has_subtitle:
            p_title += 8
        if title_words <= 12:
            p_title += 7
        elif title_words <= 16:
            p_title += 4
    score += p_title

    # Dimensión 5: Extensión (15 pts)
    p_ext = 0
    if 1700 <= total_words <= 2200:
        p_ext = 15
    elif 1500 <= total_words <= 2500:
        p_ext = 11
    elif 1300 <= total_words < 1500:
        p_ext = 6
    else:
        p_ext = 2
    score += p_ext

    # Dimensión 6: Cierre y Fuerza Analítica (15 pts)
    p_close = 15
    if has_academic_closing:
        p_close -= 10
    score += max(0, p_close)

    # Penalizaciones automáticas
    if has_subtitle:
        score -= 5
    if has_academic_opening:
        score -= 10
    if cliches_detectados:
        score -= 10
    score = max(0, min(100, score))

    # INFORME
    print("=" * 70)
    print("📋 REPORTE DE AUDITORÍA EDITORIAL — JACOBIN AMÉRICA LATINA")
    print(f"Archivo auditado: {path.name}")
    print("=" * 70)
    print(f"PUNTAJE GLOBAL: {score} / 100")
    if score >= 80:
        print("ESTADO: ✅ APROBADO PARA ENVÍO EDITORIAL")
    elif score >= 60:
        print("ESTADO: ⚠️ REQUIERE REVISIÓN Y EDICIÓN PREVIA")
    else:
        print("ESTADO: ❌ RECHAZADO (Requiere reescritura sustancial)")
    print("-" * 70)

    print("\n1. EXTENSIÓN Y PALABRAS:")
    print(f"   • Total palabras: {total_words} (Meta: 1.800 – 2.000 palabras | Rango: 1.500–2.500)")
    if total_words < 1500:
        print(f"   ⚠️ Alerta: Faltan aproximadamente {1800 - total_words} palabras.")
    elif total_words > 2500:
        print(f"   ⚠️ Alerta: Excede por {total_words - 2500} palabras el límite superior.")
    else:
        print("   ✅ Extensión en rango adecuado.")

    print("\n2. TITULAR DE TESIS PÚBLICA:")
    if title:
        print(f"   • Texto: \"{title}\"")
        print(f"   • Palabras: {title_words} (Máximo recomendado: 12)")
        if has_subtitle:
            print("   ❌ Alerta: Contiene dos puntos (':') o estructura de subtítulo.")
            print("      Jacobin NO usa subtítulos. Debe ser una tesis declarativa asertiva.")
        else:
            print("   ✅ Título sin subtítulo.")
    else:
        print("   ❌ No se detectó encabezado principal H1 (# Título)")

    print("\n3. APERTURA Y GANCHO CONTEMPORÁNEO:")
    if has_academic_opening:
        print("   ❌ Alerta: La apertura contiene fórmulas académicas/historiográficas.")
    if has_contemporary_opening:
        print("   ✅ Apertura con anclaje contemporáneo detectado.")
    else:
        print("   ⚠️ Alerta: Los primeros párrafos no mencionan coyunturas recientes (2022-2026, inflación reciente).")

    print("\n4. LATINOAMERICANIZACIÓN:")
    print(f"   • Países detectados ({len(paises_detectados)}): {', '.join(paises_detectados) if paises_detectados else 'Ninguno'}")
    if len(paises_detectados) < 3:
        print("   ⚠️ Alerta: Se debe conectar con al menos otros 2 países de la región.")
    else:
        print("   ✅ Perspectiva regional amplia confirmada.")

    print("\n5. CITACIÓN CONTEMPORÁNEA (Weber / post-2020):")
    print(f"   • Cita a Isabella Weber / sellers' inflation: {'✅ Detectada' if has_weber else '❌ No encontrada'}")
    print(f"   • Referencias post-2020: {'✅ Detectadas' if has_post_2020 else '❌ No encontradas'}")

    print("\n6. DES-ESPECIALIZACIÓN Y CONTROL TONAL:")
    if jerga_encontrada:
        print("   🔍 Jerga de paper detectada para traducir a prosa pública:")
        for term, count, sug in jerga_encontrada:
            print(f"      • '{term}' ({count}x) ➔ Sugerencia: '{sug}'")
    else:
        print("   ✅ Prosa libre de tecnicismos endogámicos.")

    if cliches_detectados:
        print("   ❌ Clichés panfletarios / moralistas detectados (¡Purgar!):")
        for panf, count in cliches_detectados:
            print(f"      • '{panf}' ({count}x)")
    else:
        print("   ✅ Tono sobrio y analítico: libre de eslóganes panfletarios.")

    print("\n" + "=" * 70)
    print("SUGERENCIAS PRIORITARIAS:")
    step = 1
    if has_subtitle:
        print(f"  {step}. Formular un titular de tesis afirmativo, sobrio y sin subtítulo (máx. 12 palabras).")
        step += 1
    if not has_contemporary_opening:
        print(f"  {step}. Abrir en el presente: anclar los primeros 2 párrafos a la inflación y presiones distributivas recientes en América Latina.")
        step += 1
    if len(paises_detectados) < 3:
        print(f"  {step}. Extender la perspectiva material hacia al menos 2 países de la región (ej. Argentina, Brasil).")
        step += 1
    if not has_weber:
        print(f"  {step}. Introducir a Isabella Weber (sellers' inflation / márgenes empresariales) para conectar con el debate vivo.")
        step += 1
    if cliches_detectados:
        print(f"  {step}. Reemplazar los calificativos moralistas por la explicación forense del mecanismo material de boicot.")
        step += 1
    print("=" * 70)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audit_columna.py ruta/a/tu_columna.md")
        sys.exit(1)
    auditar_columna(sys.argv[1])
