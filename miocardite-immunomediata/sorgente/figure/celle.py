"""Icone cellulari schematiche riutilizzabili."""
import math
from svglib import BURG, BURG_L, BLU, BLU_L, ANT, GRI, GRI_L, OCRA, OCRA_L, VERDE, VERDE_L, VIOLA, VIOLA_L


def cardiomiocita(s, x, y, w=120, h=42, fill="#f7e6ec", stroke=BURG, nucleo=True, danno=False):
    s.rect(x, y, w, h, fill=fill, stroke=stroke, sw=1.3, rx=10)
    for i in range(1, int(w / 9)):
        xx = x + i * 9
        if nucleo and abs(xx - (x + w / 2)) < 16:
            continue
        s.line(xx, y + 5, xx, y + h - 5, stroke=stroke, sw=0.6, op=0.45)
    if nucleo:
        s.ellipse(x + w / 2, y + h / 2, 13, 7, fill="#e9c3d1", stroke=stroke, sw=1)
    if danno:
        s.path(f"M{x + w * 0.72},{y} l6,9 l-7,7 l8,9 l-6,9 l5,8", stroke="#fff", sw=3)
        s.path(f"M{x + w * 0.72},{y} l6,9 l-7,7 l8,9 l-6,9 l5,8", stroke=BURG, sw=1.1)


def macrofago(s, cx, cy, r=20, fill="#f3dfc8", stroke=OCRA, etichetta=None, size=11):
    pts = []
    for k in range(14):
        a = 2 * math.pi * k / 14
        rr = r * (1 + 0.22 * math.sin(3 * a) + 0.12 * math.cos(5 * a))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = "M" + " ".join(f"{px:.1f},{py:.1f}" for px, py in pts) + "Z"
    s.path(d, fill=fill, stroke=stroke, sw=1.2)
    s.path(f"M{cx - r * 0.35},{cy - r * 0.1} q{r * 0.3},{-r * 0.5} {r * 0.6},0 q{r * 0.1},{r * 0.45} -{r * 0.3},{r * 0.4} q-{r * 0.35},0 -{r * 0.3},-{r * 0.4}z",
           fill="#d9b48f", stroke=stroke, sw=0.8)
    if etichetta:
        s.text(cx, cy + r + size + 2, etichetta, size=size, weight=600, anchor="middle", fill=ANT)


def linfocita(s, cx, cy, r=13, fill=BLU_L, stroke=BLU, nucleo="#9fb6d6", etichetta=None, size=11, dentro=None):
    s.circle(cx, cy, r, fill=fill, stroke=stroke, sw=1.2)
    s.circle(cx, cy, r * 0.72, fill=nucleo, stroke="none")
    if dentro:
        s.text(cx, cy + 4, dentro, size=r * 0.75, weight=700, anchor="middle", fill=ANT)
    if etichetta:
        s.text(cx, cy + r + size + 1, etichetta, size=size, weight=600, anchor="middle", fill=ANT)


def neutrofilo(s, cx, cy, r=13, etichetta=None, size=11):
    s.circle(cx, cy, r, fill="#f1eef6", stroke=VIOLA, sw=1.2)
    for dx, dy in ((-5, -3), (1, -5), (5, 1), (-1, 5)):
        s.circle(cx + dx, cy + dy, 3.6, fill="#b8a6d6")
    if etichetta:
        s.text(cx, cy + r + size + 1, etichetta, size=size, weight=600, anchor="middle")


def eosinofilo(s, cx, cy, r=13, etichetta=None, size=11):
    s.circle(cx, cy, r, fill="#fde3d6", stroke="#c0532b", sw=1.2)
    s.circle(cx - 4, cy, 4.5, fill="#8f7fb5")
    s.circle(cx + 4, cy, 4.5, fill="#8f7fb5")
    for dx, dy in ((-8, -6), (6, -8), (8, 6), (-6, 8), (0, -10), (0, 10), (10, -1)):
        s.circle(cx + dx, cy + dy, 1.6, fill="#e26a3a")
    if etichetta:
        s.text(cx, cy + r + size + 1, etichetta, size=size, weight=600, anchor="middle")


def mastocita(s, cx, cy, r=14, etichetta=None, size=11):
    s.circle(cx, cy, r, fill="#efe7f6", stroke=VIOLA, sw=1.2)
    s.circle(cx, cy, 5, fill="#b8a6d6")
    for k in range(10):
        a = 2 * math.pi * k / 10
        s.circle(cx + 9 * math.cos(a), cy + 9 * math.sin(a), 1.8, fill=VIOLA)
    if etichetta:
        s.text(cx, cy + r + size + 1, etichetta, size=size, weight=600, anchor="middle")


def dendritica(s, cx, cy, r=14, etichetta=None, size=11, fill="#e2f0e8", stroke=VERDE):
    pts = []
    for k in range(16):
        a = 2 * math.pi * k / 16
        rr = r * (1.9 if k % 2 == 0 else 0.85)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = "M" + " ".join(f"{px:.1f},{py:.1f}" for px, py in pts) + "Z"
    s.path(d, fill=fill, stroke=stroke, sw=1.2)
    s.circle(cx, cy, r * 0.5, fill="#a9cdb9")
    if etichetta:
        s.text(cx, cy + r * 1.9 + size, etichetta, size=size, weight=600, anchor="middle")


def plasmacellula(s, cx, cy, r=14, etichetta=None, size=11):
    s.ellipse(cx, cy, r * 1.15, r * 0.9, fill="#e3ebf5", stroke=BLU, sw=1.2)
    s.circle(cx - r * 0.45, cy, r * 0.45, fill="#9fb6d6")
    for k in range(4):
        s.path(f"M{cx + 1},{cy - 7 + k * 4.5} q4,-2 8,0", stroke=BLU, sw=0.8)
    if etichetta:
        s.text(cx, cy + r + size + 1, etichetta, size=size, weight=600, anchor="middle")


def fibroblasto(s, cx, cy, l=46, etichetta=None, size=11):
    s.path(f"M{cx - l / 2},{cy} Q{cx},{cy - 11} {cx + l / 2},{cy} Q{cx},{cy + 11} {cx - l / 2},{cy}Z",
           fill="#eef3e3", stroke="#6c7f3a", sw=1.1)
    s.ellipse(cx, cy, 7, 3.5, fill="#c4d19e")
    if etichetta:
        s.text(cx, cy + 22, etichetta, size=size, weight=600, anchor="middle")


def anticorpo(s, x, y, sc=1.0, colore=BLU, rot=0):
    s.add(f'<g transform="translate({x},{y}) rotate({rot}) scale({sc})">'
          f'<path d="M0,0 L0,14 M0,0 L-8,-10 M0,0 L8,-10" stroke="{colore}" stroke-width="2.4" fill="none" stroke-linecap="round"/></g>')
