"""Piccola libreria per comporre figure SVG con stile editoriale coerente."""
from xml.sax.saxutils import escape

# Palette del volume
BURG = "#900C3F"
BURG_L = "#f6e1ea"
BURG_M = "#d98aa8"
BLU = "#1F3A5F"
BLU_L = "#e3ebf5"
BLU_M = "#7f9cc0"
ANT = "#2E2E33"
GRI = "#6b6b73"
GRI_L = "#eeeef0"
GRI_M = "#c4c4ca"
OCRA = "#b07d00"
OCRA_L = "#fbf1d6"
VERDE = "#2f6b4f"
VERDE_L = "#e2f0e8"
VIOLA = "#5b3c8f"
VIOLA_L = "#ece6f6"
FONT = "'Source Sans 3', 'Inter', sans-serif"


class SVG:
    def __init__(self, w, h, pref):
        self.w, self.h, self.pref = w, h, pref
        self.el = []
        self.defs = []
        self._marker(BURG, "b")
        self._marker(BLU, "u")
        self._marker(ANT, "a")
        self._marker(GRI, "g")
        self._marker(VERDE, "v")
        self._marker(OCRA, "o")

    # ---------------- infrastruttura ----------------
    def _marker(self, colore, nome):
        self.defs.append(
            f'<marker id="{self.pref}-m{nome}" viewBox="0 0 10 10" refX="8.5" refY="5" '
            f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{colore}"/></marker>')

    def mid(self, colore):
        return {BURG: "b", BLU: "u", ANT: "a", GRI: "g", VERDE: "v", OCRA: "o"}.get(colore, "a")

    def add(self, s):
        self.el.append(s)

    def render(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="100%" font-family="{FONT}" role="img">'
                f'<defs>{"".join(self.defs)}</defs>' + "".join(self.el) + "</svg>")

    # ---------------- primitive ----------------
    def rect(self, x, y, w, h, fill="none", stroke="none", sw=1, rx=0, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')

    def circle(self, cx, cy, r, fill="none", stroke="none", sw=1, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{sw}"{d} opacity="{op}"/>')

    def ellipse(self, cx, cy, rx, ry, fill="none", stroke="none", sw=1, op=1, rot=0):
        self.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}" opacity="{op}" '
                 f'transform="rotate({rot} {cx:.1f} {cy:.1f})"/>')

    def path(self, d, fill="none", stroke=ANT, sw=1, dash=None, op=1, extra=""):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds} '
                 f'opacity="{op}" stroke-linejoin="round" stroke-linecap="round" {extra}/>')

    def line(self, x1, y1, x2, y2, stroke=ANT, sw=1, dash=None, op=1):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
                 f'stroke-width="{sw}"{ds} opacity="{op}"/>')

    def polyline(self, pts, stroke=ANT, sw=1.2, fill="none"):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.add(f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
                 f'stroke-linejoin="round" stroke-linecap="round"/>')

    def text(self, x, y, s, size=13, weight=400, fill=ANT, anchor="start", italic=False, lh=1.18, ls=None):
        righe = s if isinstance(s, (list, tuple)) else [s]
        st = ' font-style="italic"' if italic else ""
        lsp = f' letter-spacing="{ls}"' if ls else ""
        out = [f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
               f'text-anchor="{anchor}"{st}{lsp}>']
        for i, r in enumerate(righe):
            dy = 0 if i == 0 else size * lh
            out.append(f'<tspan x="{x:.1f}" dy="{dy:.1f}">{fmt(r)}</tspan>')
        out.append("</text>")
        self.add("".join(out))

    def arrow(self, x1, y1, x2, y2, colore=ANT, sw=1.6, dash=None, testa=True, coda=False, curva=None):
        m = f"url(#{self.pref}-m{self.mid(colore)})"
        me = f' marker-end="{m}"' if testa else ""
        ms = f' marker-start="{m}"' if coda else ""
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        if curva is None:
            d = f"M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}"
        else:
            cx, cy = curva
            d = f"M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"
        self.add(f'<path d="{d}" fill="none" stroke="{colore}" stroke-width="{sw}"{ds}{me}{ms}/>')

    def arrowpath(self, d, colore=ANT, sw=1.6, dash=None):
        m = f"url(#{self.pref}-m{self.mid(colore)})"
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="none" stroke="{colore}" stroke-width="{sw}"{ds} marker-end="{m}"/>')

    # ---------------- elementi composti ----------------
    def box(self, x, y, w, h, righe, fill=BLU_L, stroke=BLU, size=12.5, weight=400, colore=ANT,
            rx=6, sw=1.2, titolo=None, tcol=None, align="middle", lh=1.2, dash=None):
        self.rect(x, y, w, h, fill=fill, stroke=stroke, sw=sw, rx=rx, dash=dash)
        righe = righe if isinstance(righe, (list, tuple)) else [righe]
        n = len(righe) + (1 if titolo else 0)
        tot = n * size * lh
        yy = y + h / 2 - tot / 2 + size * 0.85
        xx = x + w / 2 if align == "middle" else x + 8
        if titolo:
            self.text(xx, yy, titolo, size=size, weight=700, fill=tcol or stroke, anchor=align)
            yy += size * lh
        if righe:
            self.text(xx, yy, list(righe), size=size, weight=weight, fill=colore, anchor=align, lh=lh)

    def pill(self, x, y, s, fill=BURG, colore="#fff", size=11, pad=6, h=None):
        w = larghezza(s, size) + 2 * pad
        h = h or size * 1.55
        self.rect(x, y, w, h, fill=fill, rx=h / 2)
        self.text(x + w / 2, y + h / 2 + size * 0.36, s, size=size, weight=700, fill=colore, anchor="middle")
        return w

    def etichetta_pannello(self, x, y, s, size=15):
        self.text(x, y, s, size=size, weight=700, fill=BURG)


def larghezza(s, size):
    """Stima della larghezza di un testo in Source Sans (unità SVG)."""
    import re
    s = re.sub(r"<[^>]+>", "", s)
    return len(s) * size * 0.5


def fmt(s):
    """Escape XML, poi converte marcature minime: ^{..} apice, _{..} pedice, **..** grassetto, *..* corsivo."""
    import re
    s = escape(s)
    s = re.sub(r"\^\{([^}]*)\}", r'<tspan baseline-shift="super" font-size="70%">\1</tspan>', s)
    s = re.sub(r"_\{([^}]*)\}", r'<tspan baseline-shift="sub" font-size="70%">\1</tspan>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r'<tspan font-weight="700">\1</tspan>', s)
    s = re.sub(r"\*([^*]+)\*", r'<tspan font-style="italic">\1</tspan>', s)
    return s
