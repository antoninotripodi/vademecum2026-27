"""Figure 9–11: ecocardiografia, LGE, criteri di Lake Louise."""
import math
from svglib import (SVG, BURG, BURG_L, BURG_M, BLU, BLU_L, BLU_M, ANT, GRI, GRI_L, GRI_M,
                    OCRA, OCRA_L, VERDE, VERDE_L, VIOLA, VIOLA_L)


def settore_anulare(cx, cy, r1, r2, a1, a2):
    """Settore di corona circolare tra raggi r1<r2 e angoli a1<a2 (gradi, antiorario da +x; y verso l'alto)."""
    def p(r, a):
        t = math.radians(a)
        return cx + r * math.cos(t), cy - r * math.sin(t)
    large = 1 if (a2 - a1) % 360 > 180 else 0
    x1, y1 = p(r2, a1)
    x2, y2 = p(r2, a2)
    x3, y3 = p(r1, a2)
    x4, y4 = p(r1, a1)
    return (f"M{x1:.1f},{y1:.1f} A{r2},{r2} 0 {large} 0 {x2:.1f},{y2:.1f} "
            f"L{x3:.1f},{y3:.1f} A{r1},{r1} 0 {large} 1 {x4:.1f},{y4:.1f} Z")


# ------------------------------------------------------------------ Figura 9
def a4c(s, cx, top, sc, spessore, dil, versamento=False, titolo=""):
    """Schema apicale 4 camere: apice in alto, VS a destra dell'osservatore."""
    # settore ecografico
    s.path(f"M{cx},{top} L{cx - 150 * sc},{top + 250 * sc} A{290 * sc},{290 * sc} 0 0 0 {cx + 150 * sc},{top + 250 * sc} Z",
           fill="#1d1d22", stroke="none")
    ap = top + 30 * sc
    base = top + 175 * sc
    lw = (38 + 14 * dil) * sc          # semiasse trasversale del VS
    # pericardio / versamento
    # VS (destra) e VD (sinistra) come archi
    vs_c = cx + 34 * sc
    s.path(f"M{vs_c - lw},{base} C{vs_c - lw},{ap + 40 * sc} {vs_c - 10 * sc},{ap - 4 * sc} {vs_c},{ap - 4 * sc} "
           f"C{vs_c + 10 * sc},{ap - 4 * sc} {vs_c + lw},{ap + 40 * sc} {vs_c + lw},{base}",
           fill="#3a3a40", stroke="#cfcfd4", sw=spessore * sc)
    if versamento:
        e = spessore * sc / 2 + 9 * sc
        s.path(f"M{vs_c - lw - e * 0.4},{base - 40 * sc} C{vs_c - lw},{ap + 40 * sc - e} {vs_c - 10 * sc},{ap - 4 * sc - e} {vs_c},{ap - 4 * sc - e} "
               f"C{vs_c + 10 * sc},{ap - 4 * sc - e} {vs_c + lw + e},{ap + 40 * sc} {vs_c + lw + e},{base}",
               fill="none", stroke="#f0f0f2", sw=2.4)
    vd_c = cx - 52 * sc
    s.path(f"M{vd_c - 30 * sc},{base} C{vd_c - 32 * sc},{ap + 90 * sc} {vd_c + 8 * sc},{ap + 34 * sc} {vs_c - lw + 4},{ap + 52 * sc}",
           fill="none", stroke="#bcbcc2", sw=4 * sc)
    # atri
    s.ellipse(vs_c, base + 38 * sc, 36 * sc, 34 * sc, fill="#2b2b30", stroke="#bcbcc2", sw=3 * sc)
    s.ellipse(vd_c, base + 36 * sc, 30 * sc, 32 * sc, fill="#2b2b30", stroke="#bcbcc2", sw=3 * sc)
    # valvole
    s.line(vs_c - 30 * sc, base + 2, vs_c - 8 * sc, base - 14 * sc, stroke="#f0f0f2", sw=2)
    s.line(vs_c + 30 * sc, base + 2, vs_c + 8 * sc, base - 14 * sc, stroke="#f0f0f2", sw=2)
    s.line(vd_c - 26 * sc, base + 2, vd_c - 6 * sc, base - 12 * sc, stroke="#f0f0f2", sw=2)
    s.line(vd_c + 22 * sc, base + 2, vd_c + 4 * sc, base - 12 * sc, stroke="#f0f0f2", sw=2)
    s.text(vs_c, ap + 80 * sc, "VS", size=12, weight=700, fill="#fff", anchor="middle")
    s.text(vd_c - 4 * sc, ap + 100 * sc, "VD", size=11, weight=700, fill="#fff", anchor="middle")
    s.text(vs_c, base + 44 * sc, "AS", size=10.5, weight=700, fill="#ddd", anchor="middle")
    s.text(vd_c, base + 42 * sc, "AD", size=10.5, weight=700, fill="#ddd", anchor="middle")
    s.text(cx, top + 310 * sc, titolo, size=11.5, weight=700, fill=ANT, anchor="middle")


def fig09():
    s = SVG(500, 690, "f9")
    s.etichetta_pannello(8, 18, "a  Apicale 4 camere")
    a4c(s, 125, 34, 0.78, 26, 0.0, versamento=True, titolo="fase acuta (forma fulminante)")
    a4c(s, 375, 34, 0.78, 8, 1.0, titolo="fase cronica (evoluzione a DCM)")
    s.text(125, 294, ["VS non dilatato, pareti ispessite", "(edema), FEVS ridotta, versamento"], size=10.3, fill=GRI, anchor="middle", lh=1.2)
    s.text(375, 294, ["VS dilatato e sferico, pareti", "assottigliate, IM funzionale"], size=10.3, fill=GRI, anchor="middle", lh=1.2)
    s.text(232, 60, "versamento", size=9.5, fill=BURG, weight=700, anchor="end")
    s.arrow(200, 64, 186, 84, colore=BURG, sw=1)

    # bull's-eye
    s.etichetta_pannello(8, 342, "b  Global longitudinal strain (bull's-eye, 17 segmenti)")
    cx, cy = 170, 512
    R = [0, 26, 62, 98, 132]
    valori = {1: -20, 2: -19, 3: -18, 4: -15, 5: -8, 6: -17, 7: -21, 8: -20, 9: -19, 10: -17, 11: -10, 12: -14,
              13: -22, 14: -21, 15: -20, 16: -18, 17: -21}

    def colore(v):
        # più negativo = deformazione migliore = bordeaux intenso; vicino a 0 = chiaro/azzurro
        u = max(0.0, min(1.0, (-v - 6) / 16))
        if u < 0.35:
            return "#c9d8ea"
        r1, g1, b1 = (0xf6, 0xd5, 0xe1)
        r2, g2, b2 = (0x90, 0x0c, 0x3f)
        k = (u - 0.35) / 0.65
        return f"#{int(r1 + (r2 - r1) * k):02x}{int(g1 + (g2 - g1) * k):02x}{int(b1 + (b2 - b1) * k):02x}"

    nomi_base = [(1, 60, 120), (2, 120, 180), (3, 180, 240), (4, 240, 300), (5, 300, 360), (6, 0, 60)]
    for seg, a1, a2 in nomi_base:
        s.path(settore_anulare(cx, cy, R[3], R[4], a1, a2), fill=colore(valori[seg]), stroke="#fff", sw=1.5)
        s.path(settore_anulare(cx, cy, R[2], R[3], a1, a2), fill=colore(valori[seg + 6]), stroke="#fff", sw=1.5)
        for rr, sg in ((R[3] + 17, seg), (R[2] + 18, seg + 6)):
            am = math.radians((a1 + a2) / 2)
            v = valori[sg]
            s.text(cx + rr * math.cos(am), cy - rr * math.sin(am) + 4, str(v), size=10.5, weight=700,
                   fill="#fff" if v <= -15 else ANT, anchor="middle")
    for seg, a1, a2 in [(13, 45, 135), (14, 135, 225), (15, 225, 315), (16, 315, 405)]:
        s.path(settore_anulare(cx, cy, R[1], R[2], a1, a2 if a2 <= 360 else a2 - 0.01), fill=colore(valori[seg]), stroke="#fff", sw=1.5)
        am = math.radians((a1 + a2) / 2)
        s.text(cx + 44 * math.cos(am), cy - 44 * math.sin(am) + 4, str(valori[seg]), size=10, weight=700, fill="#fff", anchor="middle")
    s.circle(cx, cy, R[1], fill=colore(valori[17]), stroke="#fff", sw=1.5)
    s.text(cx, cy + 4, str(valori[17]), size=10, weight=700, fill="#fff", anchor="middle")
    # orientamento
    s.text(cx, cy - R[4] - 6, "anteriore", size=10, fill=GRI, anchor="middle", italic=True)
    s.text(cx, cy + R[4] + 14, "inferiore", size=10, fill=GRI, anchor="middle", italic=True)
    s.text(cx - R[4] - 4, cy + 4, "setto", size=10, fill=GRI, anchor="end", italic=True)
    s.text(cx + R[4] + 4, cy + 4, "laterale", size=10, fill=GRI, anchor="start", italic=True)
    # legenda e lettura
    lx = 345
    s.text(lx, 410, "strain (%)", size=10.5, weight=700, fill=ANT)
    for i, v in enumerate([-22, -18, -14, -10, -6]):
        s.rect(lx, 418 + i * 18, 22, 16, fill=colore(v), stroke="#fff")
        s.text(lx + 28, 430 + i * 18, str(v), size=10, fill=ANT)
    s.text(lx, 540, ["GLS globale ≈ −17%", "(lievemente ridotto)", "FEVS 57% (conservata)"], size=10.5, weight=700, fill=BURG, lh=1.25)
    s.text(lx, 598, ["Riduzione infero-laterale", "basale e media: pattern", "non coronarico, coerente", "con LGE subepicardico"], size=10, fill=ANT, lh=1.2)
    s.text(250, 682, "Valori illustrativi; i valori normali dipendono dal software.", size=9.8, fill=GRI, anchor="middle", italic=True)
    s.h = 688
    return s.render()


# ------------------------------------------------------------------ Figura 10
def asse_corto(s, cx, cy, lge, titolo, sottotitolo, R=56, r=34):
    """lge: lista di (r_in_frazione, r_out_frazione, a1, a2) — frazioni dello spessore 0=endo, 1=epi."""
    s.rect(cx - 82, cy - 74, 164, 148, fill="#141418", rx=6)
    # VD (a sinistra dell'osservatore, adiacente al setto)
    s.path(f"M{cx - R * 0.55},{cy - R * 0.86} C{cx - R * 1.55},{cy - R * 0.9} {cx - R * 1.55},{cy + R * 0.9} {cx - R * 0.55},{cy + R * 0.86}",
           fill="#8a8a92", stroke="#2c2c31", sw=6)
    s.circle(cx, cy, R, fill="#2c2c31")
    s.circle(cx, cy, r, fill="#8a8a92")
    for f1, f2, a1, a2 in lge:
        s.path(settore_anulare(cx, cy, r + (R - r) * f1, r + (R - r) * f2, a1, a2), fill="#f4f4f6", stroke="none")
    s.text(cx, cy + 92, titolo, size=12, weight=700, fill=ANT, anchor="middle")
    s.text(cx, cy + 108, sottotitolo, size=10.5, fill=GRI, anchor="middle", lh=1.15)


def fig10():
    s = SVG(1000, 560, "f10")
    y = 92
    xs = [92, 282, 472, 662, 852]
    asse_corto(s, xs[0], y, [(0, 0.5, 45, 160)], "a  Infarto subendocardico", ["territorio DA"])
    asse_corto(s, xs[1], y, [(0, 1, 290, 345)], "b  Infarto transmurale", ["territorio Cx (infero-laterale)"])
    asse_corto(s, xs[2], y, [(0.65, 1, 280, 350), (0.75, 1, 350, 365)], "c  Miocardite", ["subepicardico infero-laterale"])
    asse_corto(s, xs[3], y, [(0.35, 0.68, 140, 220)], "d  Miocardite", ["mesoparietale settale"])
    asse_corto(s, xs[4], y, [(0.2, 0.75, 150, 185), (0, 0.45, 200, 222), (0.5, 1, 20, 45), (0, 1, 238, 250)],
               "e  Sarcoidosi", ["a chiazze, multifocale"])
    # etichette orientamento nel primo
    s.text(xs[0], 12, "anteriore", size=9.5, fill=GRI, anchor="middle", italic=True)
    s.text(xs[0] - 80, y - 62, "VD", size=10, weight=700, fill="#ddd")
    s.text(xs[0] + 66, y + 4, "lat.", size=9.5, fill="#ddd")
    # legenda colori
    s.text(20, 238, "Legenda (immagine LGE):", size=10.5, weight=700, fill=ANT)
    for i, (c, t) in enumerate([("#2c2c31", "miocardio sano «annullato» (nero)"), ("#f4f4f6", "LGE: necrosi o fibrosi (bianco)"),
                                ("#8a8a92", "sangue in cavità (grigio)")]):
        s.rect(170 + i * 250, 227, 16, 14, fill=c, stroke=GRI)
        s.text(192 + i * 250, 238, t, size=10.5, fill=ANT)
    # distinzione
    s.rect(20, 252, 960, 40, fill=GRI_L, rx=5)
    s.text(500, 268, "Ischemico: coinvolge sempre il subendocardio e segue un territorio coronarico (fronte d'onda dal subendocardio all'epicardio).",
           size=11, anchor="middle", fill=ANT)
    s.text(500, 284, "Non ischemico: subepicardico o mesoparietale, risparmia il subendocardio, non segue i territori. Eccezioni: eosinofila, cellule giganti, sarcoidosi.",
           size=11, anchor="middle", fill=ANT)

    # curve di inversione-recupero
    gx0, gx1, gy0, gy1 = 90, 640, 320, 530
    ymid = (gy0 + gy1) / 2
    s.etichetta_pannello(20, 318, "Principio dell'acquisizione LGE")
    s.line(gx0, ymid, gx1, ymid, stroke=ANT, sw=1)
    s.line(gx0, gy0 + 6, gx0, gy1 - 6, stroke=ANT, sw=1)
    s.text(gx1, ymid + 16, "tempo dopo l'impulso di 180° (ms)", size=10, fill=GRI, anchor="end", italic=True)
    s.text(gx0 - 6, gy0 + 16, "+M₀", size=10, fill=GRI, anchor="end")
    s.text(gx0 - 6, gy1 - 6, "−M₀", size=10, fill=GRI, anchor="end")
    s.text(gx0 - 6, ymid + 4, "0", size=10, fill=GRI, anchor="end")
    tmax = 1000.0

    def X(t):
        return gx0 + (gx1 - gx0) * t / tmax

    def Y(m):
        return ymid - m * (gy1 - gy0 - 20) / 2

    curve = [(450, "#4a4a52", "miocardio sano (T1 ≈ 450 ms)"), (250, BURG, "miocardio con LGE (T1 ≈ 250 ms)"),
             (330, BLU, "sangue (T1 ≈ 330 ms)")]
    for T1, c, nome in curve:
        pts = [(X(t), Y(1 - 2 * math.exp(-t / T1))) for t in range(0, 1001, 5)]
        s.polyline(pts, stroke=c, sw=2.4)
    TI = 450 * math.log(2)
    s.line(X(TI), gy0, X(TI), gy1, stroke=OCRA, sw=1.4, dash="5 4")
    s.text(X(TI) + 6, gy0 + 12, f"TI ≈ {TI:.0f} ms: il miocardio sano passa per lo zero", size=10.5, weight=700, fill=OCRA)
    for T1, c, nome in curve:
        m = 1 - 2 * math.exp(-TI / T1)
        s.circle(X(TI), Y(m), 4, fill=c)
    # legenda curve
    lx = 670
    for i, (T1, c, nome) in enumerate(curve):
        s.line(lx, 352 + i * 22, lx + 26, 352 + i * 22, stroke=c, sw=2.6)
        s.text(lx + 34, 356 + i * 22, nome, size=10.5, fill=ANT)
    s.text(lx, 436, ["Al TI scelto il segnale (|M_{z}|) del miocardio sano è", "nullo → nero; il tessuto con più gadolinio ha",
                     "T1 più breve, ha già recuperato → bianco.", "Valori di T1 post-contrasto illustrativi."],
           size=10.5, fill=ANT, lh=1.3)
    s.h = 545
    return s.render()


# ------------------------------------------------------------------ Figura 11
def fig11():
    s = SVG(500, 560, "f11")
    s.box(10, 10, 230, 34, ["CRITERIO T2-BASED · edema"], fill=BLU, stroke=BLU, colore="#fff", size=12, weight=700)
    s.box(260, 10, 230, 34, ["CRITERIO T1-BASED · danno"], fill=BURG, stroke=BURG, colore="#fff", size=12, weight=700)
    s.box(10, 50, 230, 54, ["**T2 mapping**: aumento", "regionale o globale del T2"], fill=BLU_L, stroke=BLU, size=11)
    s.box(10, 110, 230, 66, ["**Immagini T2-pesate**: iperintensità", "regionale o globale (es. rapporto", "miocardio/muscolo scheletrico ≥2)"],
          fill=BLU_L, stroke=BLU, size=11)
    s.box(260, 50, 230, 38, ["**T1 nativo** aumentato"], fill=BURG_L, stroke=BURG, size=11)
    s.box(260, 94, 230, 38, ["**ECV** aumentato"], fill=BURG_L, stroke=BURG, size=11)
    s.box(260, 138, 230, 38, ["**LGE** a distribuzione non ischemica"], fill=BURG_L, stroke=BURG, size=11)
    s.text(125, 194, "almeno 1", size=11.5, weight=700, fill=BLU, anchor="middle")
    s.text(375, 194, "almeno 1", size=11.5, weight=700, fill=BURG, anchor="middle")
    s.arrow(125, 200, 225, 226, colore=BLU, sw=2)
    s.arrow(375, 200, 275, 226, colore=BURG, sw=2)
    s.text(250, 216, "+", size=20, weight=700, fill=ANT, anchor="middle")
    s.box(60, 228, 380, 46, ["Infiammazione miocardica acuta", "con elevata specificità"], fill=ANT, stroke=ANT, colore="#fff", size=12.5, weight=700)
    s.text(250, 292, ["Un solo tipo di marcatore: può supportare la diagnosi in un contesto clinico", "appropriato, ma con specificità minore."],
           size=10.5, fill=GRI, anchor="middle", italic=True, lh=1.25)
    s.box(10, 320, 480, 48, ["**Criteri di supporto**: versamento o enhancement/edema pericardico (pericardite);", "disfunzione sistolica del VS regionale o globale"],
          fill=GRI_L, stroke=GRI, size=10.8)

    # mini-grafici
    def mini(x0, y0, w, h, titolo, c, spost, nota):
        s.text(x0, y0 - 6, titolo, size=11, weight=700, fill=c)
        s.rect(x0 + w * 0.28, y0, w * 0.22, h, fill=GRI_L)
        s.text(x0 + w * 0.39, y0 + h + 14, "riferimento locale", size=9, fill=GRI, anchor="middle", italic=True)
        s.line(x0, y0 + h, x0 + w, y0 + h, stroke=ANT, sw=1)
        for mu, col, op in ((0.39, GRI, 1), (0.39 + spost, c, 1)):
            pts = [(x0 + w * u / 100, y0 + h - (h - 6) * math.exp(-0.5 * ((u / 100 - mu) / 0.07) ** 2)) for u in range(0, 101)]
            s.polyline(pts, stroke=col, sw=2)
        s.text(x0 + w, y0 + h + 14, "ms →", size=9, fill=GRI, anchor="end")
        s.text(x0 + w * (0.39 + spost), y0 + 8, nota, size=9.5, fill=c, anchor="middle", weight=700)

    mini(30, 404, 190, 70, "T2 (ms)", BLU, 0.3, "edema")
    mini(280, 404, 190, 70, "T1 nativo / ECV", BURG, 0.33, "danno")
    s.text(250, 520, ["Curve grigie: miocardio sano; colorate: miocardio infiammato. I valori normali", "dipendono da scanner, campo e sequenza: si usano intervalli di riferimento locali."],
           size=10, fill=GRI, anchor="middle", italic=True, lh=1.25)
    s.h = 548
    return s.render()
