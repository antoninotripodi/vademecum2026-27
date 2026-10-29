#!/usr/bin/env python3
"""Assembla i capitoli HTML, incorpora le figure SVG e genera il PDF.

Uso:  python3 build.py            -> HTML + PDF
      python3 build.py --png      -> anche anteprime PNG delle pagine (controllo visivo)
"""
import pathlib, re, subprocess, sys

QUI = pathlib.Path(__file__).resolve().parent
RADICE = QUI.parent
HTML_OUT = QUI / "miocardite_immunomediata.html"
PDF_OUT = RADICE / "Miocardite_immunomediata_VOM_2026-27.pdf"

TESTA = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Miocardite immunomediata — Vademecum Omnia Medicinae 2026–27</title>
<link rel="stylesheet" href="fonts.css">
<link rel="stylesheet" href="stile.css">
</head>
<body>
"""
CODA = "\n</body>\n</html>\n"


def incorpora_svg(html: str) -> str:
    """Sostituisce <img src="figure/xxx.svg"> con l'SVG inline (così usa i font della pagina)."""
    def sost(m):
        svg = (QUI / m.group(1)).read_text(encoding="utf-8")
        svg = re.sub(r"<\?xml[^>]*>\s*", "", svg)
        return svg
    return re.sub(r'<img src="(figure/[^"]+\.svg)"[^>]*>', sost, html)


def main():
    # le figure vengono rigenerate a ogni build
    subprocess.run([sys.executable, str(QUI / "figure" / "genera_figure.py")], check=True)
    capitoli = sorted((QUI / "capitoli").glob("*.html"))
    corpo = "\n".join(c.read_text(encoding="utf-8") for c in capitoli)
    HTML_OUT.write_text(TESTA + incorpora_svg(corpo) + CODA, encoding="utf-8")
    subprocess.run(["node", str(QUI / "render.js"), str(HTML_OUT), str(PDF_OUT)], check=True)
    print("PDF:", PDF_OUT)
    if "--png" in sys.argv:
        anteprime = QUI / "_anteprime"
        anteprime.mkdir(exist_ok=True)
        for f in anteprime.glob("*.png"):
            f.unlink()
        subprocess.run(["pdftoppm", "-r", "70", "-png", str(PDF_OUT), str(anteprime / "p")], check=True)


if __name__ == "__main__":
    main()
