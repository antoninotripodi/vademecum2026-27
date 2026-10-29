"""Figura 8 — Tracciati ECG schematici generati da forme d'onda parametriche.

Scala reale sulla pagina stampata: la figura occupa 180 mm di larghezza (viewBox 1000),
quindi 1 mm = 1000/180 unità. Carta standard: 25 mm/s, 10 mm/mV.
"""
import math
from svglib import SVG, BURG, BLU, ANT, GRI, OCRA

MM = 1000 / 180.0          # unità SVG per millimetro stampato
PX_S = 25 * MM             # unità per secondo
PX_MV = 10 * MM            # unità per millivolt


def g(t, c, s):
    return math.exp(-0.5 * ((t - c) / s) ** 2)


def ga(t, c, s1, s2):
    s = s1 if t < c else s2
    return math.exp(-0.5 * ((t - c) / s) ** 2)


def sig(x):
    x = max(-60, min(60, x))
    return 1 / (1 + math.exp(-x))


def onda_p(t, amp=0.15, pr_dep=0.0, pr=0.16):
    """Onda P centrata a 0.05 s dall'inizio; pr_dep = spostamento del segmento PR (mV)."""
    v = amp * g(t, 0.05, 0.022)
    if pr_dep:
        v += pr_dep * sig((t - 0.095) / 0.006) * (1 - sig((t - pr) / 0.004))
    return v


def qrst(t, comp, j, st=0.0, t_amp=0.3, t_c=0.2, t_s=(0.055, 0.04), dome=0.0, t_end=0.32):
    """comp: lista (centro, sigma, ampiezza) del QRS (tempi relativi all'inizio del QRS)."""
    v = sum(a * g(t, c, s) for c, s, a in comp)
    if st:
        v += st * sig((t - j) / 0.004) * (1 - sig((t - (j + t_end)) / 0.03))
    if dome:
        v += dome * ga(t, j + 0.07, 0.035, 0.09) * sig((t - j + 0.01) / 0.004)
    v += t_amp * ga(t, j + t_c, t_s[0], t_s[1])
    return v


def segnale(t, p_list, q_list):
    v = 0.0
    for tp, kw in p_list:
        if -0.05 < t - tp < 0.5:
            v += onda_p(t - tp, **kw)
    for tq, kw in q_list:
        if -0.05 < t - tq < 0.75:
            v += qrst(t - tq, **kw)
    return v


def griglia(s, x, y, w, h):
    s.rect(x, y, w, h, fill="#fdf6f8")
    n = int(w / MM) + 1
    for i in range(n):
        xx = x + i * MM
        if xx > x + w + 0.1:
            break
        grosso = i % 5 == 0
        s.line(xx, y, xx, y + h, stroke="#e6a9be" if grosso else "#f3d6e0", sw=0.7 if grosso else 0.35)
    m = int(h / MM) + 1
    for j in range(m):
        yy = y + j * MM
        if yy > y + h + 0.1:
            break
        grosso = j % 5 == 0
        s.line(x, yy, x + w, yy, stroke="#e6a9be" if grosso else "#f3d6e0", sw=0.7 if grosso else 0.35)
    s.rect(x, y, w, h, stroke="#d98aa8", sw=0.8)


def striscia(s, x, y, w, h, base, nome, p_list, q_list, durata=None, sw=1.5):
    """Disegna griglia + tracciato. base = distanza della linea isoelettrica dal bordo superiore (mm)."""
    griglia(s, x, y, w, h)
    y0 = y + base * MM
    dur = durata or w / PX_S
    pts = []
    k = 0
    while True:
        t = k * 0.002
        if t > dur:
            break
        pts.append((x + t * PX_S, y0 - segnale(t, p_list, q_list) * PX_MV))
        k += 1
    s.polyline(pts, stroke=ANT, sw=sw)
    s.rect(x + 3, y + 3, len(nome) * 7.2 + 8, 16, fill="#fff", rx=2, op=0.9)
    s.text(x + 7, y + 15.5, nome, size=12.5, weight=700, fill=BLU)
    return y0


def tx(x, t):
    return x + t * PX_S


def ty(y0, mv):
    return y0 - mv * PX_MV


def nota(s, x, y, testo, xa, ya, colore=BURG, anchor="start", size=11.5):
    s.text(x, y, testo, size=size, weight=600, fill=colore, anchor=anchor)
    s.arrow(x + (0 if anchor == "start" else 0), y + 3, xa, ya, colore=colore, sw=1.1)


def costruisci():
    W = 1000
    s = SVG(W, 1150, "f8")
    # componenti QRS tipici (centro s, sigma s, ampiezza mV), tempi dall'inizio del QRS
    norm = [(0.012, 0.006, -0.08), (0.038, 0.009, 1.1), (0.062, 0.008, -0.25)]
    v5 = [(0.012, 0.006, -0.1), (0.04, 0.01, 1.4), (0.066, 0.008, -0.2)]
    avr = [(0.02, 0.008, 0.12), (0.045, 0.011, -0.95), (0.07, 0.008, 0.1)]
    piccolo = [(0.02, 0.008, 0.25), (0.045, 0.01, -0.45), (0.07, 0.008, 0.15)]
    rr, pr = 0.80, 0.16

    def battiti(n, t0=0.12, **kw):
        ps = [(t0 + i * rr, dict(pr=pr, **kw.get("p", {}))) for i in range(n)]
        qs = [(t0 + i * rr + pr, kw["q"]) for i in range(n)]
        return ps, qs

    xs = [20, 350, 680]
    lw, h = 300, 26 * MM

    # ---------------- (a) miopericardite ----------------
    y = 40
    s.etichetta_pannello(20, y - 14, "a  Miopericardite: ST sopraslivellato diffuso e concavo, PR sottoslivellato")
    peri = [(0.012, 0.006, -0.05), (0.038, 0.009, 1.1), (0.062, 0.008, -0.08)]
    p, q = battiti(3, p={"amp": 0.15, "pr_dep": -0.1}, q=dict(comp=peri, j=0.08, st=0.26, t_amp=0.3, t_c=0.2))
    y0 = striscia(s, xs[0], y, lw, h, 16, "II", p, q)
    t1 = 0.12 + rr + pr
    nota(s, xs[0] + 170, y + 18, "ST ↑ concavo", tx(xs[0], t1 + 0.13), ty(y0, 0.3))
    nota(s, xs[0] + 75, y + h - 8, "PR ↓", tx(xs[0], 0.12 + rr + 0.125), ty(y0, -0.13))
    v5p = [(0.012, 0.006, -0.06), (0.04, 0.01, 1.35), (0.066, 0.008, -0.08)]
    p, q = battiti(3, p={"amp": 0.12, "pr_dep": -0.09}, q=dict(comp=v5p, j=0.085, st=0.28, t_amp=0.32, t_c=0.2))
    striscia(s, xs[1], y, lw, h, 17, "V5", p, q)
    p, q = battiti(3, p={"amp": -0.12, "pr_dep": 0.09}, q=dict(comp=avr, j=0.088, st=-0.14, t_amp=-0.3, t_c=0.19))
    y0 = striscia(s, xs[2], y, lw, h, 11, "aVR", p, q)
    nota(s, xs[2] + 150, y + h - 8, "ST ↓ e PR ↑ in aVR", tx(xs[2], t1 + 0.13), ty(y0, -0.2))

    # ---------------- (b) STEMI inferiore ----------------
    y = 40 + h + 46
    s.etichetta_pannello(20, y - 14, "b  Confronto: STEMI inferiore — ST convesso territoriale con immagine speculare in aVL")
    p, q = battiti(3, q=dict(comp=norm, j=0.085, dome=0.32, t_amp=0.38, t_c=0.17, t_s=(0.06, 0.045)))
    y0 = striscia(s, xs[0], y, lw, h, 17, "II", p, q)
    p, q = battiti(3, q=dict(comp=[(0.012, 0.006, -0.15), (0.038, 0.009, 0.7), (0.062, 0.008, -0.2)],
                             j=0.085, dome=0.42, t_amp=0.42, t_c=0.17, t_s=(0.06, 0.045)))
    y0 = striscia(s, xs[1], y, lw, h, 17, "III", p, q)
    nota(s, xs[1] + 155, y + 14, "ST ↑ convesso", tx(xs[1], t1 + 0.11), ty(y0, 0.5))
    p, q = battiti(3, p={"amp": 0.08}, q=dict(comp=piccolo, j=0.085, st=-0.2, t_amp=-0.15, t_c=0.17))
    y0 = striscia(s, xs[2], y, lw, h, 12, "aVL", p, q)
    nota(s, xs[2] + 140, y + h - 8, "ST ↓ speculare", tx(xs[2], t1 + 0.11), ty(y0, -0.22))

    # ---------------- (c) T invertite e (d) BBS ----------------
    y = 40 + 2 * (h + 46)
    lw2 = 225
    xs2 = [20, 265, 520, 765]
    s.etichetta_pannello(20, y - 14, "c  Inversione simmetrica dell'onda T")
    s.etichetta_pannello(520, y - 14, "d  Blocco di branca sinistra (QRS 150 ms)")
    tinv = dict(comp=[(0.012, 0.006, -0.05), (0.038, 0.009, 0.9), (0.064, 0.009, -0.5)], j=0.085,
                t_amp=-0.42, t_c=0.2, t_s=(0.05, 0.05))
    p, q = battiti(2, q=tinv)
    y0 = striscia(s, xs2[0], y, lw2, h, 14, "V3", p, q)
    nota(s, xs2[0] + 120, y + h - 8, "T negativa", tx(xs2[0], 0.12 + pr + 0.29), ty(y0, -0.38))
    p, q = battiti(2, q=dict(tinv, comp=v5, t_amp=-0.45))
    striscia(s, xs2[1], y, lw2, h, 15, "V4", p, q)
    lbbb_v1 = dict(comp=[(0.015, 0.008, 0.1), (0.075, 0.03, -1.35)], j=0.15, st=0.18, t_amp=0.32, t_c=0.17)
    lbbb_v6 = dict(comp=[(0.045, 0.024, 0.85), (0.105, 0.024, 0.95)], j=0.15, st=-0.12, t_amp=-0.32, t_c=0.17)
    p, q = battiti(2, q=lbbb_v1)
    y0 = striscia(s, xs2[2], y, lw2, h, 9, "V1", p, q)
    nota(s, xs2[2] + 115, y + h - 6, "QS largo", tx(xs2[2], 0.12 + pr + 0.08), ty(y0, -1.2))
    p, q = battiti(2, q=lbbb_v6)
    y0 = striscia(s, xs2[3], y, lw2, h, 18, "V6", p, q)
    nota(s, xs2[3] + 120, y + 14, "R larga «a M»", tx(xs2[3], 0.12 + pr + 0.08), ty(y0, 1.05))

    # ---------------- (e) BAV ----------------
    y = 40 + 3 * (h + 46)
    lw3 = 960
    s.etichetta_pannello(20, y - 14, "e  BAV II grado Mobitz II (PR costante, P non condotta)  ·  BAV completo (P dissociate, scappamento a QRS largo)")
    # Mobitz II 3:2
    ps, qs = [], []
    for i in range(9):
        tp = 0.15 + i * 0.78
        ps.append((tp, dict(amp=0.15)))
        if i % 3 != 2:
            qs.append((tp + 0.18, dict(comp=norm, j=0.085, t_amp=0.3, t_c=0.19)))
    y0 = striscia(s, 20, y, lw3, 22 * MM, 15, "II", ps, qs)
    for i in range(9):
        tp = 0.15 + i * 0.78
        if i % 3 == 2:
            xx = tx(20, tp + 0.05)
            s.text(xx, y + 22 * MM - 6, "P bloccata", size=10.5, weight=700, fill=BURG, anchor="middle")
            s.arrow(xx, y + 22 * MM - 18, xx, ty(y0, 0.2) + 2, colore=BURG, sw=1.0)
    for k in (1, 3):
        s.text(tx(20, 0.15 + k * 0.78 + 0.11), y + 18, "PR 180 ms", size=10.5, weight=600, fill=BLU, anchor="middle")
    # BAV completo
    y2 = y + 22 * MM + 12
    ps = [(0.1 + i * 0.62, dict(amp=0.16)) for i in range(12)]
    esc = dict(comp=[(0.04, 0.03, 0.9), (0.11, 0.025, -0.35)], j=0.16, t_amp=-0.35, t_c=0.2, t_s=(0.06, 0.06))
    qs = [(0.45 + i * 1.6, esc) for i in range(5)]
    y0 = striscia(s, 20, y2, lw3, 24 * MM, 14, "II", ps, qs)
    for i in range(12):
        xx = tx(20, 0.1 + i * 0.62 + 0.05)
        if xx < 20 + lw3 - 8:
            s.text(xx, y2 + 24 * MM - 5, "P", size=10.5, weight=700, fill=BURG, anchor="middle")
    s.text(tx(20, 0.45 + 1.6 + 0.05), y2 + 16, "scappamento ventricolare ≈ 38/min", size=10.5, weight=600, fill=BLU, anchor="middle")
    s.text(lw3 + 10, y2 + 16, "P ≈ 97/min", size=10.5, weight=700, fill=BURG, anchor="end")

    # ---------------- (f) TV ----------------
    y = y2 + 24 * MM + 46
    s.etichetta_pannello(20, y - 14, "f  Tachicardia ventricolare monomorfa (≈170/min) con dissociazione atrio-ventricolare")
    ps = [(0.25 + i * 0.82, dict(amp=0.18)) for i in range(9)]
    tv = dict(comp=[(0.045, 0.028, 1.25), (0.115, 0.022, -0.45)], j=0.15, t_amp=-0.42, t_c=0.11, t_s=(0.04, 0.045))
    qs = [(0.1 + i * 0.353, tv) for i in range(20)]
    y0 = striscia(s, 20, y, lw3, 30 * MM, 15, "II", ps, qs)
    for i in range(9):
        xx = tx(20, 0.25 + i * 0.82 + 0.05)
        s.text(xx, y + 30 * MM - 5, "▲", size=9, weight=700, fill=BURG, anchor="middle")
    s.text(560, y + 30 * MM + 14, "▲ attività atriale dissociata (P a ≈ 73/min, indipendenti dai QRS)", size=11, weight=600, fill=BURG, anchor="middle")
    s.text(lw3 + 20, y - 14, "QRS ≈ 160 ms", size=12, weight=700, fill=BLU, anchor="end")

    # calibrazione e legenda
    s.text(980, 1146, "Carta: 25 mm/s · 10 mm/mV · quadretto piccolo 1 mm = 40 ms × 0,1 mV · TRACCIATI SCHEMATICI, NON REGISTRAZIONI REALI",
           size=10.5, weight=600, fill=GRI, anchor="end")
    s.h = y + 30 * MM + 30
    s.text(980, s.h - 2, "", size=1)
    return s


def svg():
    s = costruisci()
    # sposta la nota finale in fondo alla figura
    s.el = [e for e in s.el if "TRACCIATI SCHEMATICI" not in e]
    s.h += 16
    s.text(980, s.h - 4, "Carta: 25 mm/s · 10 mm/mV · quadretto piccolo 1 mm = 40 ms × 0,1 mV · tracciati schematici, non registrazioni reali",
           size=10.5, weight=600, fill=GRI, anchor="end")
    return s.render()
