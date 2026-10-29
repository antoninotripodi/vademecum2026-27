"""Figure 5–7: patogenesi, danno del cardiomiocita, evoluzione."""
import math
from svglib import (SVG, BURG, BURG_L, BURG_M, BLU, BLU_L, BLU_M, ANT, GRI, GRI_L, GRI_M,
                    OCRA, OCRA_L, VERDE, VERDE_L, VIOLA, VIOLA_L)
from celle import linfocita, macrofago


EV = {"Uomo": (BLU_L, BLU), "Modello animale": (OCRA_L, OCRA), "Ipotesi": (VIOLA_L, VIOLA)}


def tag(s, x, y, t):
    f, c = EV[t]
    w = len(t) * 5.6 + 12
    s.rect(x, y, w, 15, fill=f, stroke=c, rx=3, sw=0.8)
    s.text(x + w / 2, y + 11, t.upper(), size=8.6, weight=700, fill=c, anchor="middle", ls=0.3)
    return w


# ------------------------------------------------------------------ Figura 5
def fig05():
    s = SVG(1000, 560, "f5")
    cols = [(10, "FASE 1 · DANNO E IMMUNITÀ INNATA", "giorni", BURG),
            (345, "FASE 2 · RISPOSTA ADATTATIVA E AUTOIMMUNITÀ", "settimane", BLU),
            (680, "FASE 3 · RISOLUZIONE O CRONICIZZAZIONE", "mesi", VERDE)]
    for x, t, d, c in cols:
        s.rect(x, 8, 310, 30, fill=c, rx=5)
        s.text(x + 155, 28, t, size=12, weight=700, fill="#fff", anchor="middle", ls=0.4)
        s.text(x + 155, 54, d, size=11, weight=600, fill=c, anchor="middle", italic=True)

    def colonna(x, voci, c, f):
        y = 64
        pos = []
        for righe, h in voci:
            s.box(x, y, 310, h, righe, fill=f, stroke=c, size=11.3, lh=1.22)
            pos.append((y, h))
            y += h + 22
        for (y1, h1), (y2, _) in zip(pos, pos[1:]):
            s.arrow(x + 155, y1 + h1 + 2, x + 155, y2 - 2, colore=c, sw=1.6)
        return pos

    p1 = colonna(10, [
        (["**Trigger**: virus cardiotropo (CVB3 → CAR/CD55;", "proteasi 2A taglia la distrofina), farmaco, ICI"], 46),
        (["**Danno del cardiomiocita**: citolisi, necrosi", "→ rilascio di DAMP (HMGB1, ATP, DNA mt)"], 46),
        (["**Riconoscimento**: TLR3/7/8, RIG-I/MDA5, NLRP3", "→ NF-κB, IRF3/7, caspasi-1"], 46),
        (["**Mediatori**: IFN-α/β (antivirale) · TNF-α, IL-1β,", "IL-6 · chemochine CCL2, CXCL1/8, CXCL10"], 46),
        (["**Infiltrato innato**: monociti CCR2⁺, neutrofili, NK", "edema interstiziale (↑T2) · troponina ↑"], 46),
    ], BURG, "#fdf3f6")
    p2 = colonna(345, [
        (["**Cellule dendritiche** trasportano antigeni virali", "e cardiaci al linfonodo (CCR7)"], 46),
        (["**Attivazione T**: TCR + CD28–CD80/86 + IL-12,", "IL-6, IL-23 → espansione clonale"], 46),
        (["**Effettori**: Th1 (IFN-γ), Th17 (IL-17A, GM-CSF),", "CD8⁺ (perforina, granzimi, FasL); Treg insufficienti"], 46),
        (["**Perdita della tolleranza**: mimetismo molecolare,", "attivazione bystander, antigeni criptici, epitope spreading"], 46),
        (["**Autoanticorpi**: α-miosina, troponina I,", "recettore β1-adrenergico, ANT"], 46),
    ], BLU, "#f3f6fb")
    # fase 3 con biforcazione
    x = 680
    s.box(x, 64, 310, 46, ["**Clearance del virus** (CD8⁺, NK, IFN)", "e calo del segnale di pericolo"], fill="#f2f8f4", stroke=VERDE, size=11.3)
    s.arrow(x + 80, 112, x + 80, 136, colore=VERDE, sw=1.6)
    s.arrow(x + 230, 112, x + 230, 136, colore=BURG, sw=1.6)
    s.box(x, 138, 150, 120, ["**Risoluzione**", "efferocitosi (MerTK)", "macrofagi riparativi", "IL-10, TGF-β, Treg", "→ guarigione con", "cicatrice minima"],
          fill="#f2f8f4", stroke=VERDE, size=11, lh=1.2)
    s.box(x + 160, 138, 150, 120, ["**Persistenza**", "necrosi → DAMP →", "autoantigeni →", "T effettori → nuova", "necrosi (circuito", "autoalimentato)"],
          fill="#fdf3f6", stroke=BURG, size=11, lh=1.2)
    s.arrow(x + 235, 260, x + 235, 284, colore=BURG, sw=1.6)
    s.box(x, 286, 310, 64, ["**Fibrosi** (TGF-β → SMAD2/3, miofibroblasti)", "**Rimodellamento** (Laplace, neuro-ormoni)", "→ miocardiopatia infiammatoria cronica / DCM"],
          fill="#fdf3f6", stroke=BURG, size=11.3, lh=1.22)
    s.arrow(x + 155, 352, x + 155, 376, colore=BURG, sw=1.6)
    s.box(x, 378, 310, 46, ["**Substrato aritmico**: cicatrice, conduzione lenta,", "rientro → TV, morte improvvisa"], fill="#fdf3f6", stroke=BURG, size=11.3)
    s.box(x, 446, 310, 46, ["Predittori nell'uomo: infiammazione IHC persistente,", "LGE esteso, LGE senza edema a 6 mesi"], fill="#fff", stroke=GRI, size=11, dash="4 3")
    # frecce tra colonne
    s.arrow(322, 150, 343, 110, colore=ANT, sw=1.8)
    s.arrow(657, 240, 678, 100, colore=ANT, sw=1.8, curva=(672, 170))
    # tag di evidenza
    yb = 506
    s.text(10, yb + 14, "Livello di evidenza:", size=10.5, weight=700, fill=GRI)
    xx = 112
    for t in ("Uomo", "Modello animale", "Ipotesi"):
        xx += tag(s, xx, yb + 3, t) + 8
    # tag puntuali
    s.text(370, yb + 14, ["Uomo: infiltrati T e macrofagici, linfociti T anti-α-MyHC, valore prognostico di infiammazione e LGE.",
           "Modello animale: sequenza a tre fasi, proteasi 2A–distrofina, ruolo di IL-17/GM-CSF. Ipotesi: contributo di epitopi virali mimetici."],
           size=10.3, fill=GRI, italic=True, lh=1.3)
    s.h = yb + 38
    return s.render()


# ------------------------------------------------------------------ Figura 6
def fig06():
    s = SVG(500, 640, "f6")
    # cellula
    s.rect(20, 60, 460, 400, fill="#fdf6f8", stroke=BURG, sw=2.2, rx=26)
    s.text(470, 52, "sarcolemma", size=10.5, fill=BURG, anchor="end", italic=True)
    # esterno: CD8, citochine
    linfocita(s, 55, 30, r=15, fill=BURG_L, stroke=BURG, nucleo="#fff", dentro="CD8")
    s.text(78, 20, ["perforina + granzimi,", "FasL → apoptosi"], size=10, fill=BURG, lh=1.15)
    s.arrow(60, 46, 75, 72, colore=BURG, sw=1.5)
    s.text(300, 22, ["TNF-α, IL-1β, IL-6 → iNOS → NO,", "perossinitrito; ↓ risposta β-adrenergica"], size=10, fill=OCRA, anchor="middle", lh=1.15)
    s.arrow(300, 40, 300, 74, colore=OCRA, sw=1.5)
    # canale L e NCX
    s.rect(140, 54, 22, 14, fill=BLU_L, stroke=BLU, rx=3)
    s.text(151, 50, "canale L", size=10, weight=700, fill=BLU, anchor="middle")
    s.arrow(151, 70, 151, 120, colore=BLU, sw=1.6)
    s.text(158, 100, "Ca²⁺", size=10, fill=BLU)
    s.rect(466, 250, 14, 32, fill=OCRA_L, stroke=OCRA, rx=3)
    s.text(473, 314, "NCX", size=10, weight=700, fill=OCRA, anchor="middle")
    s.arrow(455, 258, 492, 258, colore=BLU, sw=1.3)
    s.arrow(492, 276, 455, 276, colore=BURG, sw=1.3)
    s.text(452, 254, "Ca²⁺", size=9.5, fill=BLU, anchor="end")
    s.text(452, 292, "3 Na⁺ → DAD", size=9.5, fill=BURG, anchor="end", weight=700)
    # reticolo sarcoplasmatico
    s.path("M80,150 C140,128 330,128 400,150 C420,158 420,178 400,184 C330,204 140,204 80,184 C62,178 62,158 80,150 Z",
           fill="#eaf0f8", stroke=BLU, sw=1.3)
    s.text(240, 172, "reticolo sarcoplasmatico (Ca²⁺)", size=11, weight=700, fill=BLU, anchor="middle")
    s.rect(140, 128, 26, 16, fill="#fff", stroke=BLU, rx=3)
    s.text(153, 140, "RyR2", size=9.5, weight=700, fill=BLU, anchor="middle")
    s.arrow(160, 146, 200, 230, colore=BLU, sw=1.4)
    s.arrow(150, 146, 105, 228, colore=BURG, sw=1.4, dash="4 3")
    s.text(32, 240, ["leak diastolico", "(RyR2 ossidato)"], size=10, fill=BURG, weight=700, lh=1.15)
    s.rect(330, 190, 34, 16, fill="#fff", stroke=VERDE, rx=3)
    s.text(347, 202, "SERCA", size=9, weight=700, fill=VERDE, anchor="middle")
    s.ellipse(374, 208, 10, 6, fill=OCRA_L, stroke=OCRA)
    s.text(392, 224, "PLN", size=9.5, weight=700, fill=OCRA)
    s.arrow(350, 240, 347, 208, colore=VERDE, sw=1.4)
    s.text(300, 255, ["↓ SERCA2a, PLN ipofosforilato", "→ rilasciamento lento, ↓ carico"], size=10, fill=BURG, weight=700, anchor="middle", lh=1.15)
    # sarcomero
    ys = 300
    s.rect(60, ys, 300, 70, fill="#fff", stroke=GRI, rx=6)
    s.line(70, ys + 10, 70, ys + 60, stroke=ANT, sw=2.5)
    s.line(350, ys + 10, 350, ys + 60, stroke=ANT, sw=2.5)
    for k in range(4):
        yy = ys + 16 + k * 12
        s.line(70, yy, 190, yy, stroke=BLU_M, sw=1.6)
        s.line(230, yy, 350, yy, stroke=BLU_M, sw=1.6)
        s.line(150, yy + 6, 270, yy + 6, stroke=BURG_M, sw=3)
    s.text(210, ys + 86, "sarcomero: actina (blu), miosina (bordeaux), dischi Z", size=10, fill=GRI, anchor="middle", italic=True)
    s.text(380, ys + 20, ["calpaine → taglio di", "troponina I, titina", "distrofina tagliata", "(proteasi 2A virale)"], size=10, fill=BURG, weight=600, lh=1.2)
    # mitocondrio
    s.ellipse(400, 410, 60, 28, fill="#fff3e3", stroke=OCRA, sw=1.3)
    s.path("M352,410 q8,-16 16,0 t16,0 t16,0 t16,0 t16,0 t12,0", stroke=OCRA, sw=1)
    s.text(400, 448, "mitocondrio", size=10, fill=OCRA, anchor="middle", italic=True)
    s.text(150, 405, ["ROS, mPTP aperto, ↓ ATP,", "citocromo c → apoptosoma"], size=10.3, fill=BURG, weight=700, anchor="middle", lh=1.15)
    s.arrow(250, 410, 336, 410, colore=BURG, sw=1.3, coda=True, testa=False)
    # effetto
    s.arrow(250, 462, 250, 486, colore=BURG, sw=2)
    s.box(80, 488, 340, 30, ["↓ forza contrattile · ↓ rilasciamento · instabilità elettrica"], fill=BURG, stroke=BURG,
          colore="#fff", size=11.5, weight=700)
    # morte cellulare
    yy = 536
    s.text(250, yy, "MODALITÀ DI MORTE CELLULARE", size=10.5, weight=700, fill=ANT, anchor="middle", ls=0.8)
    vv = [("Apoptosi", ["caspasi-8 (Fas, TNFR1)", "caspasi-9 (mitocondrio)", "→ caspasi-3"]),
          ("Necrosi / necroptosi", ["ATP ↓, Ca²⁺ ↑;", "RIPK1 → RIPK3 → MLKL", "→ DAMP, troponina"]),
          ("Piroptosi", ["caspasi-1 →", "gasdermina D", "→ IL-1β, IL-18"])]
    for i, (t, r) in enumerate(vv):
        s.box(12 + i * 162, yy + 8, 152, 74, r, titolo=t, fill="#fff", stroke=BURG, size=10.3, lh=1.18)
    s.h = yy + 88
    return s.render()


# ------------------------------------------------------------------ Figura 7
def fig07():
    s = SVG(500, 560, "f7")
    # bande temporali
    x0, x1 = 40, 485
    fasi = [(40, 160, "GIORNI", "innata", BURG_L, BURG), (160, 300, "SETTIMANE", "adattativa", BLU_L, BLU),
            (300, 485, "MESI", "riparazione", VERDE_L, VERDE)]
    for a, b, t, n, f, c in fasi:
        s.rect(a, 10, b - a, 40, fill=f, stroke=c, sw=0.8)
        s.text((a + b) / 2, 27, t, size=11, weight=700, fill=c, anchor="middle", ls=0.8)
        s.text((a + b) / 2, 43, n, size=10.5, fill=c, anchor="middle", italic=True)
    # catena
    s.box(40, 66, 130, 46, ["Infiammazione", "(edema, infiltrato)"], fill="#fdf3f6", stroke=BURG, size=11)
    s.box(185, 66, 120, 46, ["Danno", "(necrosi, troponina)"], fill="#fdf3f6", stroke=BURG, size=11)
    s.box(320, 66, 165, 46, ["Riparazione", "(efferocitosi, miofibroblasti)"], fill="#f2f8f4", stroke=VERDE, size=11)
    s.arrow(172, 89, 183, 89, colore=ANT)
    s.arrow(307, 89, 318, 89, colore=ANT)
    # biforcazione
    s.arrow(400, 114, 110, 146, colore=VERDE, sw=1.6)
    s.arrow(402, 114, 260, 146, colore=OCRA, sw=1.6)
    s.arrow(404, 114, 410, 146, colore=BURG, sw=1.6)
    s.box(20, 148, 150, 70, ["**Guarigione**", "cicatrice minima,", "funzione normale"], fill="#f2f8f4", stroke=VERDE, size=10.8)
    s.box(180, 148, 150, 70, ["**Infiammazione**", "**persistente**", "miocardiopatia", "infiammatoria"], fill=OCRA_L, stroke=OCRA, size=10.8, lh=1.12)
    s.box(340, 148, 150, 70, ["**Fibrosi estesa**", "rimodellamento →", "DCM, aritmie"], fill="#fdf3f6", stroke=BURG, size=10.8)
    s.text(95, 234, "forme non complicate", size=10, fill=VERDE, anchor="middle", italic=True)
    s.text(415, 234, "forme complicate / fulminanti", size=10, fill=BURG, anchor="middle", italic=True)
    # grafico
    gy0, gy1 = 270, 470
    s.line(x0, gy1, x1, gy1, stroke=ANT, sw=1.2)
    s.line(x0, gy0, x0, gy1, stroke=ANT, sw=1.2)
    yc = (gy0 + gy1) / 2
    s.add(f'<text x="24" y="{yc}" font-size="10" fill="{GRI}" font-style="italic" text-anchor="middle" '
          f'transform="rotate(-90 24 {yc})">intensità relativa</text>')
    for xx, t in [(40, "0"), (100, "3 g"), (160, "1 sett"), (230, "3 sett"), (300, "1 mese"), (390, "3–6 mesi"), (480, "12 mesi")]:
        s.line(xx, gy1, xx, gy1 + 5, stroke=ANT)
        s.text(xx, gy1 + 18, t, size=10, anchor="middle", fill=ANT)

    def curva(f, colore, dash=None):
        pts = []
        for i in range(0, 446):
            x = x0 + i
            u = i / 445.0
            pts.append((x, gy1 - f(u) * (gy1 - gy0 - 10)))
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        s.path(d, stroke=colore, sw=2.4, dash=dash)

    curva(lambda u: 0.95 * math.exp(-((u - 0.1) / 0.09) ** 2) if u > 0.1 else 0.95 * math.exp(-((u - 0.1) / 0.05) ** 2), BURG)
    curva(lambda u: 0.85 * math.exp(-((u - 0.22) / 0.2) ** 2), BLU)
    curva(lambda u: 0.62 / (1 + math.exp(-(u - 0.45) / 0.07)) + 0.05, VERDE)
    curva(lambda u: 0.9 / (1 + math.exp(-(u - 0.5) / 0.08)) * 1.0 + 0.05, VERDE, dash="5 4")
    s.text(92, 282, "troponina", size=10.5, weight=700, fill=BURG)
    s.text(195, 312, "edema (T2)", size=10.5, weight=700, fill=BLU)
    s.text(470, 312, ["fibrosi (LGE, ECV)", "estesa"], size=10.5, weight=700, fill=VERDE, anchor="end")
    s.text(470, 372, "limitata", size=10.5, weight=700, fill=VERDE, anchor="end")
    s.text(260, 505, "Andamento indicativo, non in scala; asse dei tempi compresso.", size=10, fill=GRI, anchor="middle", italic=True)
    s.h = 515
    return s.render()
