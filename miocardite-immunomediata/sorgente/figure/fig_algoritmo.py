"""Figura 12 — Algoritmo diagnostico-terapeutico."""
from svglib import (SVG, BURG, BURG_L, BURG_M, BLU, BLU_L, BLU_M, ANT, GRI, GRI_L, GRI_M,
                    OCRA, OCRA_L, VERDE, VERDE_L, VIOLA, VIOLA_L)


def fig12():
    s = SVG(1000, 720, "f12")
    # ingresso
    s.box(300, 8, 400, 54, ["**SOSPETTA MIOCARDITE**", "dolore toracico · scompenso/shock · aritmie, sincope"],
          fill=ANT, stroke=ANT, colore="#fff", size=12.5)
    s.text(500, 80, "contesto: prodromi virali, farmaci, vaccini, ICI, malattie autoimmuni, familiarità", size=11, fill=GRI, anchor="middle", italic=True)
    s.arrow(500, 86, 500, 104, colore=ANT, sw=2)
    # rombo stabilità
    s.path("M500,106 L640,140 L500,174 L360,140 Z", fill="#fff", stroke=ANT, sw=1.6)
    s.text(500, 136, ["1 · Stabilità emodinamica", "ed elettrica?"], size=11.5, weight=700, anchor="middle", lh=1.15)
    s.arrow(360, 140, 200, 140, colore=BURG, sw=2)
    s.arrow(200, 140, 200, 196, colore=BURG, sw=2)
    s.text(270, 132, "NO", size=12, weight=700, fill=BURG, anchor="middle")
    s.arrow(640, 140, 760, 140, colore=BLU, sw=2)
    s.arrow(760, 140, 760, 196, colore=BLU, sw=2)
    s.text(700, 132, "SÌ", size=12, weight=700, fill=BLU, anchor="middle")

    # ramo instabile
    s.rect(20, 190, 360, 430, fill="#fdf3f6", stroke=BURG_M, rx=10)
    s.text(200, 214, "ALTO RISCHIO · STADIO D (ACC)", size=12, weight=700, fill=BURG, anchor="middle", ls=0.5)
    s.text(200, 230, "shock, bassa portata, TV sostenuta, BAV avanzato", size=10.5, fill=BURG, anchor="middle", italic=True)
    passi_i = [
        (["**Stabilizzazione**: inotropi/vasopressori,", "cardioversione, pacing temporaneo"], 46),
        (["**Centro hub**: supporto circolatorio meccanico", "(Impella, VA-ECMO), terapia intensiva"], 46),
        (["**Coronarografia + BEM precoce**", "(istologia, immunoistochimica, PCR virale)"], 46),
        (["**Istotipo** → GCM · eosinofila · linfocitaria", "(virus ±) · ICI · sarcoidosi"], 46),
        (["**Terapia eziologica** + supporto", "→ ponte al recupero, alla decisione o al trapianto"], 46),
    ]
    y = 244
    prev = None
    for righe, h in passi_i:
        if prev:
            s.arrow(200, prev + 2, 200, y - 2, colore=BURG, sw=1.6)
        s.box(40, y, 320, h, righe, fill="#fff", stroke=BURG, size=11.2)
        prev = y + h
        y += h + 26
    # CMR quando stabile
    s.text(200, 608, "CMR appena le condizioni lo consentono", size=10.5, fill=BURG, anchor="middle", italic=True)

    # ramo stabile
    s.rect(400, 190, 580, 430, fill="#f3f6fb", stroke=BLU_M, rx=10)
    s.text(690, 214, "PAZIENTE STABILE", size=12, weight=700, fill=BLU, anchor="middle", ls=0.5)
    passi_s = [
        (["**2–5 · Anamnesi, esame obiettivo, ECG, biomarcatori, ecocardiogramma**",
          "hs-cTn (dinamica), NT-proBNP, PCR, emocromo (eosinofili), CK; FEVS, GLS, versamento"], 46),
        (["**6 · Escludere la sindrome coronarica acuta**",
          "coronarografia (STEMI-like, rischio alto) · TC coronarica (rischio basso-intermedio)"], 46),
        (["**7 · CMR (Lake Louise 2018)**: ≥1 criterio T2 + ≥1 criterio T1 → miocardite definita",
          "negativa o dubbia → rivalutare timing e diagnosi alternative (Takotsubo, genetica…)"], 46),
        (["**8 · BEM** se rischio alto, mancata risposta, sospetto di forme specifiche,",
          "BAV/TV con disfunzione, prima di un'immunosoppressione"], 46),
        (["**9 · Stratificazione del rischio**: FEVS, aritmie, estensione e sede dell'LGE",
          "**10 · Eziologia**: virale attiva, post-infettiva/autoimmune, ICI, eosinofila, GCM, genetica"], 46),
    ]
    y = 230
    prev = None
    for righe, h in passi_s:
        if prev:
            s.arrow(690, prev + 2, 690, y - 2, colore=BLU, sw=1.6)
        s.box(420, y, 540, h, righe, fill="#fff", stroke=BLU, size=11.2)
        prev = y + h
        y += h + 26
    s.arrow(690, prev + 2, 690, 640, colore=BLU, sw=1.6)
    s.arrow(200, 620, 200, 640, colore=BURG, sw=1.6)

    # terapia
    s.text(500, 660, "TERAPIA GUIDATA DAL MECCANISMO", size=12, weight=700, fill=ANT, anchor="middle", ls=0.6)
    voci = [("Tutti", "scompenso, aritmie, restrizione attività", GRI_L, ANT),
            ("Virale attiva", "supporto; evitare immunosoppressione", "#fff", BURG),
            ("Virus-negativa progressiva", "considerare prednisone + azatioprina", "#fff", BLU),
            ("ICI", "stop ICI + metilprednisolone; abatacept", "#fff", BLU),
            ("Eosinofila / GCM", "corticosteroidi / IS combinata", "#fff", BLU)]
    x = 10
    for t, d, f, c in voci:
        s.box(x, 668, 192, 46, [d], titolo=t, fill=f, stroke=c, tcol=c, size=10.3, lh=1.15)
        x += 198
    s.h = 720
    # follow-up
    s.text(500, 734, "", size=1)
    return s.render() .replace('viewBox="0 0 1000 720"', 'viewBox="0 0 1000 770"').replace(
        "</svg>",
        f'<rect x="10" y="724" width="980" height="40" rx="6" fill="{VERDE_L}" stroke="{VERDE}"/>'
        f'<text x="500" y="740" font-size="11.3" text-anchor="middle" fill="{ANT}"><tspan font-weight="700" fill="{VERDE}">FOLLOW-UP</tspan>'
        f' · restrizione dell\'esercizio personalizzata · ECG, Holter, ecocardiogramma, biomarcatori · <tspan font-weight="700">CMR entro 6 mesi</tspan></text>'
        f'<text x="500" y="756" font-size="11.3" text-anchor="middle" fill="{ANT}">defibrillatore indossabile come ponte · decisione sull\'ICD a 3–6 mesi · test genetici se forme ricorrenti o familiari</text>'
        "</svg>")
