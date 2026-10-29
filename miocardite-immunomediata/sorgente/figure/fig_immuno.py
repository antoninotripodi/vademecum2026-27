"""Figure 1–4: immunologia fondamentale."""
from svglib import (SVG, BURG, BURG_L, BURG_M, BLU, BLU_L, BLU_M, ANT, GRI, GRI_L, GRI_M,
                    OCRA, OCRA_L, VERDE, VERDE_L, VIOLA, VIOLA_L)
from celle import (cardiomiocita, macrofago, linfocita, neutrofilo, mastocita, dendritica,
                   plasmacellula, fibroblasto, anticorpo, eosinofilo)


# ------------------------------------------------------------------ Figura 1
def fig01():
    s = SVG(1000, 560, "f1")
    # tre zone
    s.rect(10, 30, 395, 395, fill="#fbf3f6", stroke=BURG_M, rx=14)
    s.rect(420, 30, 210, 395, fill="#f3f5f9", stroke=BLU_M, rx=14)
    s.rect(645, 30, 345, 395, fill="#f1f7f3", stroke="#8fbfa4", rx=14)
    s.text(207, 22, "MIOCARDIO: CELLULE RESIDENTI", size=13, weight=700, fill=BURG, anchor="middle", ls=1)
    s.text(525, 22, "CIRCOLO: RECLUTAMENTO", size=13, weight=700, fill=BLU, anchor="middle", ls=1)
    s.text(817, 22, "LINFONODO MEDIASTINICO", size=13, weight=700, fill=VERDE, anchor="middle", ls=1)

    # --- miocardio
    for i, (x, y) in enumerate([(30, 55), (165, 55), (30, 115), (165, 115), (95, 175), (230, 175)]):
        cardiomiocita(s, x, y, w=125, h=44, danno=(i == 3))
    s.text(298, 128, ["cardiomiocita", "danneggiato"], size=11, weight=600, fill=BURG, anchor="start")
    s.text(130, 245, "cardiomiociti", size=11.5, weight=600, anchor="middle")
    # capillare
    s.rect(30, 262, 355, 30, fill="#fde9ec", stroke="#c55", rx=15)
    s.text(207, 282, "capillare: endotelio (selectine, ICAM-1, VCAM-1, MHC-II indotto)", size=11, weight=600, fill="#a33", anchor="middle")
    fibroblasto(s, 80, 320, etichetta="fibroblasto")
    macrofago(s, 180, 325, r=18, etichetta="macrofago residente CCR2⁻")
    mastocita(s, 320, 322, etichetta="mastocita")
    s.text(207, 392, ["Sorveglianza, sostegno della conduzione,", "angiogenesi e riparazione"], size=11, fill=GRI, anchor="middle", italic=True)
    s.text(207, 410, "", size=1)

    # --- circolo
    s.rect(440, 55, 170, 170, fill="#fde9ec", stroke="#c55", rx=85, op=0.6)
    macrofago(s, 485, 110, r=15, fill="#f6e3cf")
    s.text(485, 140, ["monocita", "CCR2⁺"], size=11, weight=600, anchor="middle")
    neutrofilo(s, 565, 100)
    s.text(565, 128, "neutrofilo", size=11, weight=600, anchor="middle")
    linfocita(s, 525, 185, r=13, fill="#efe9f7", stroke=VIOLA, nucleo="#c7b6e3")
    s.text(560, 190, "NK", size=11, weight=700, fill=VIOLA)
    s.arrow(450, 240, 395, 240, colore=BURG, sw=2)
    s.text(525, 250, ["chemochine", "CCL2 → CCR2 (monociti)", "CXCL1/8 → neutrofili", "CXCL9/10 → CXCR3 (Th1, CD8⁺, NK)"],
           size=11, anchor="middle", lh=1.25)
    s.text(525, 335, ["adesione: selectine → integrine", "LFA-1/ICAM-1, VLA-4/VCAM-1", "→ diapedesi"], size=11, anchor="middle", fill=BLU, lh=1.25)
    s.text(525, 400, ["innata: minuti–giorni"], size=11, weight=700, anchor="middle", fill=GRI, italic=True)

    # --- linfonodo
    s.ellipse(817, 175, 150, 120, fill="#e2f0e8", stroke="#8fbfa4", sw=1.2)
    dendritica(s, 735, 165, r=14)
    s.text(735, 205, ["cellula", "dendritica"], size=11, weight=600, anchor="middle")
    s.arrow(762, 160, 800, 140, colore=VERDE, sw=1.6)
    linfocita(s, 818, 132, r=13, dentro="T")
    s.text(818, 112, "T naïve", size=11, weight=600, anchor="middle")
    s.text(840, 168, ["MHC-peptide + CD80/86", "→ attivazione"], size=10.5, fill=VERDE, anchor="start", lh=1.2)
    # popolazioni effettrici
    eff = [(700, 300, "Th1", BLU_L, BLU, "IFN-γ"), (765, 300, "Th17", "#fde9d6", "#c0532b", "IL-17A"),
           (830, 300, "CD8⁺", BURG_L, BURG, "perforina"), (895, 300, "Treg", VERDE_L, VERDE, "IL-10, TGF-β")]
    for x, y, t, f, c, m in eff:
        linfocita(s, x, y, r=17, fill=f, stroke=c, nucleo="#ffffff", dentro=t)
        s.text(x, y + 32, m, size=10.5, weight=600, anchor="middle", fill=c)
    plasmacellula(s, 950, 250)
    s.text(950, 228, "plasmacellula", size=10.5, weight=600, anchor="middle")
    anticorpo(s, 955, 275, sc=0.8)
    s.arrow(818, 150, 800, 270, colore=VERDE, sw=1.4, dash="4 3")
    s.text(817, 375, ["espansione clonale e polarizzazione", "adattativa: giorni–settimane"], size=11, anchor="middle", fill=GRI, italic=True)
    # ritorno al cuore
    s.arrow(660, 410, 395, 410, colore=BURG, sw=2.2, curva=(530, 445))
    s.text(530, 445, "ritorno al miocardio dei linfociti effettori e degli anticorpi", size=11.5, weight=700, fill=BURG, anchor="middle")
    s.arrow(395, 70, 690, 140, colore=VERDE, sw=1.6, dash="5 3", curva=(560, 40))
    s.text(560, 52, "trasporto di antigeni (CCR7)", size=11, weight=600, fill=VERDE, anchor="middle")

    # --- mediatori
    y = 470
    s.text(10, y, "MEDIATORI PRINCIPALI E CELLULA DI ORIGINE", size=12.5, weight=700, fill=ANT, ls=0.8)
    voci = [("IFN-α/β", "cardiomiociti infetti, DC plasmacitoidi", VERDE),
            ("TNF-α, IL-1β, IL-6", "macrofagi, mastociti, fibroblasti", OCRA),
            ("IL-18, IL-1β maturi", "inflammasoma NLRP3", OCRA),
            ("IFN-γ", "Th1, CD8⁺, NK", BLU),
            ("IL-17A, GM-CSF", "Th17", "#c0532b"),
            ("IL-10, TGF-β", "Treg, macrofagi riparativi", VERDE),
            ("autoanticorpi", "plasmacellule", BLU)]
    x = 10
    for i, (a, b, c) in enumerate(voci):
        col = i % 4
        row = i // 4
        xx = 10 + col * 247
        yy = y + 14 + row * 40
        s.rect(xx, yy, 238, 34, fill="#fff", stroke=c, rx=5)
        s.text(xx + 8, yy + 15, a, size=12, weight=700, fill=c)
        s.text(xx + 8, yy + 29, b, size=10.5, fill=ANT)
    return s.render()


# ------------------------------------------------------------------ Figura 2
def fig02():
    s = SVG(500, 640, "f2")
    # ligandi
    s.text(250, 18, "PAMP virali e DAMP dal cardiomiocita necrotico", size=12.5, weight=700, fill=BURG, anchor="middle")
    s.path("M40,38 q8,-8 16,0 t16,0 t16,0 t16,0", stroke=BURG, sw=2)
    s.text(72, 58, "RNA virale", size=10.5, anchor="middle", fill=BURG)
    for i, (x, t) in enumerate([(170, "HMGB1"), (240, "HSP"), (300, "ATP"), (370, "DNA mt")]):
        s.circle(x, 36, 7, fill=BURG_L, stroke=BURG)
        s.text(x, 58, t, size=10.5, anchor="middle", fill=BURG)
    # membrana
    s.rect(10, 70, 480, 12, fill="#f0e3c8", stroke=OCRA, rx=4)
    s.text(490, 66, "membrana plasmatica", size=10, anchor="end", fill=OCRA, italic=True)
    # TLR4/2 dimeri
    for x, t in [(120, "TLR4"), (200, "TLR2")]:
        s.rect(x - 14, 50, 10, 46, fill=BLU_L, stroke=BLU, rx=4)
        s.rect(x + 4, 50, 10, 46, fill=BLU_L, stroke=BLU, rx=4)
        s.text(x, 112, t, size=11, weight=700, anchor="middle", fill=BLU)
    s.arrow(178, 42, 205, 52, colore=BURG, sw=1.2)
    # endosoma
    s.ellipse(380, 140, 95, 42, fill="#f5f0fa", stroke=VIOLA)
    s.text(380, 118, "endosoma", size=10.5, anchor="middle", italic=True, fill=VIOLA)
    for x, t in [(330, "TLR3"), (380, "TLR7/8"), (432, "TLR9")]:
        s.rect(x - 9, 128, 7, 30, fill=BLU_L, stroke=BLU, rx=3)
        s.rect(x + 2, 128, 7, 30, fill=BLU_L, stroke=BLU, rx=3)
        s.text(x, 173, t, size=10.5, weight=700, anchor="middle", fill=BLU)
    # adattatori
    s.box(95, 130, 120, 34, ["MyD88"], fill=BLU_L, stroke=BLU, size=13, weight=700)
    s.arrow(150, 98, 150, 128, colore=BLU)
    s.box(300, 205, 110, 32, ["TRIF"], fill=VERDE_L, stroke=VERDE, size=13, weight=700)
    s.arrow(330, 178, 345, 203, colore=VERDE)
    s.arrow(128, 98, 340, 205, colore=VERDE, dash="4 3", curva=(240, 170))
    s.text(416, 226, ["da TLR3 e", "TLR4 endosomiale"], size=9.5, fill=VERDE, italic=True, lh=1.15)
    # cascata MyD88
    passi = [("IRAK4 → IRAK1", "myddosoma"), ("TRAF6", "ubiquitina K63"), ("TAK1 / TAB2-3", ""),
             ("IKKα · IKKβ · NEMO", "")]
    y = 185
    for t, n in passi:
        s.arrow(155, y - 19, 155, y - 2, colore=BLU)
        s.box(80, y, 150, 30, [t], fill="#fff", stroke=BLU, size=12, weight=700)
        if n:
            s.text(236, y + 19, n, size=10, fill=GRI, italic=True)
        y += 50
    # IkB
    y += 0
    s.arrow(155, y - 19, 155, y + 2, colore=BLU)
    s.box(40, y + 4, 230, 50, [], fill=GRI_L, stroke=GRI)
    s.rect(55, y + 14, 50, 28, fill="#fff", stroke=GRI, rx=6)
    s.text(80, y + 33, "IκBα", size=11.5, weight=700, anchor="middle")
    s.text(80, y + 12, "P", size=10, weight=700, fill=BURG, anchor="middle")
    s.circle(140, y + 28, 15, fill=BLU_L, stroke=BLU)
    s.circle(165, y + 28, 15, fill=BLU_L, stroke=BLU)
    s.text(140, y + 32, "p65", size=10, weight=700, anchor="middle", fill=BLU)
    s.text(165, y + 32, "p50", size=10, weight=700, anchor="middle", fill=BLU)
    s.text(218, y + 25, ["degradazione", "proteasomica"], size=10, anchor="middle", fill=GRI, italic=True)
    # MAPK
    s.text(245, 335, ["p38 / JNK", "→ AP-1"], size=11, weight=700, fill=OCRA)
    s.arrow(232, 330, 244, 330, colore=OCRA, sw=1.2)
    # TRIF branch
    s.arrow(355, 239, 355, 262, colore=VERDE)
    s.box(295, 264, 120, 30, ["TBK1 / IKKε"], fill="#fff", stroke=VERDE, size=12, weight=700)
    s.arrow(355, 296, 355, 318, colore=VERDE)
    s.box(310, 320, 90, 30, ["IRF3"], fill="#fff", stroke=VERDE, size=12, weight=700)
    # nucleo
    yn = 455
    s.ellipse(250, yn + 70, 235, 72, fill="#f4f1fa", stroke=VIOLA, sw=1.3)
    s.text(250, yn + 22, "NUCLEO", size=11, weight=700, fill=VIOLA, anchor="middle", ls=1)
    s.arrow(152, y + 56, 152, yn + 30, colore=BLU, sw=2)
    s.arrow(355, 352, 355, yn + 30, colore=VERDE, sw=2)
    s.text(150, yn + 50, ["**NF-κB + AP-1:**", "TNF-α, IL-6, pro-IL-1β,", "NLRP3, CCL2, CXCL8,", "E-selectina, ICAM-1, VCAM-1"],
           size=11, anchor="middle", lh=1.2)
    s.text(365, yn + 50, ["**IRF3:**", "IFN-β", "(stato antivirale", "via IFNAR)"], size=11, anchor="middle", lh=1.2)
    s.arrow(250, yn + 144, 250, yn + 168, colore=BURG, sw=2)
    s.text(250, yn + 182, "Citochine, chemochine e molecole di adesione → reclutamento leucocitario", size=11.5,
           weight=700, fill=BURG, anchor="middle")
    s.h = yn + 190
    return s.render()


# ------------------------------------------------------------------ Figura 3
def fig03():
    s = SVG(500, 600, "f3")
    # segnale 1
    s.box(10, 10, 230, 108, [], fill=BLU_L, stroke=BLU)
    s.text(125, 30, "SEGNALE 1 · innesco", size=12.5, weight=700, fill=BLU, anchor="middle")
    s.text(125, 50, ["PAMP/DAMP → TLR · TNF · IL-1", "→ NF-κB", "↑ trascrizione di NLRP3", "e di pro-IL-1β, pro-IL-18"],
           size=11, anchor="middle", lh=1.22)
    # segnale 2
    s.box(260, 10, 230, 108, [], fill=BURG_L, stroke=BURG)
    s.text(375, 30, "SEGNALE 2 · attivazione", size=12.5, weight=700, fill=BURG, anchor="middle")
    s.text(375, 50, ["ATP → P2X7 → efflusso di K⁺", "ROS e DNA mitocondriale", "danno lisosomiale (catepsina B)",
                     "flussi di Ca²⁺"], size=11, anchor="middle", lh=1.22)
    s.arrow(125, 120, 190, 158, colore=BLU, sw=1.8)
    s.arrow(375, 120, 310, 158, colore=BURG, sw=1.8)
    # assemblaggio: domini
    y = 165
    s.text(250, y + 2, "Assemblaggio dell'inflammasoma", size=12, weight=700, fill=ANT, anchor="middle")
    # NLRP3
    x0 = 40
    s.text(x0, y + 30, "NLRP3", size=11.5, weight=700, fill=ANT)
    s.rect(x0 + 55, y + 16, 50, 22, fill="#c9b6e6", stroke=VIOLA, rx=4)
    s.text(x0 + 80, y + 31, "PYD", size=10.5, weight=700, anchor="middle")
    s.rect(x0 + 105, y + 16, 110, 22, fill="#e6dff3", stroke=VIOLA, rx=4)
    s.text(x0 + 160, y + 31, "NACHT (ATPasi)", size=10.5, weight=700, anchor="middle")
    s.rect(x0 + 215, y + 16, 70, 22, fill="#f3eefa", stroke=VIOLA, rx=4)
    s.text(x0 + 250, y + 31, "LRR", size=10.5, weight=700, anchor="middle")
    s.ellipse(x0 + 312, y + 27, 22, 12, fill=OCRA_L, stroke=OCRA)
    s.text(x0 + 312, y + 31, "NEK7", size=9.5, weight=700, anchor="middle", fill=OCRA)
    # ASC
    s.text(x0, y + 72, "ASC", size=11.5, weight=700, fill=ANT)
    s.rect(x0 + 55, y + 58, 50, 22, fill="#c9b6e6", stroke=VIOLA, rx=4)
    s.text(x0 + 80, y + 73, "PYD", size=10.5, weight=700, anchor="middle")
    s.rect(x0 + 105, y + 58, 50, 22, fill="#f7d8a6", stroke=OCRA, rx=4)
    s.text(x0 + 130, y + 73, "CARD", size=10.5, weight=700, anchor="middle")
    # procaspasi-1
    s.text(x0, y + 114, ["procaspasi-1"], size=11.5, weight=700, fill=ANT)
    s.rect(x0 + 105, y + 100, 50, 22, fill="#f7d8a6", stroke=OCRA, rx=4)
    s.text(x0 + 130, y + 115, "CARD", size=10.5, weight=700, anchor="middle")
    s.rect(x0 + 155, y + 100, 60, 22, fill=BURG_L, stroke=BURG, rx=4)
    s.text(x0 + 185, y + 115, "p20", size=10.5, weight=700, anchor="middle")
    s.rect(x0 + 215, y + 100, 50, 22, fill=BURG_L, stroke=BURG, rx=4)
    s.text(x0 + 240, y + 115, "p10", size=10.5, weight=700, anchor="middle")
    # interazioni omotipiche
    s.line(x0 + 80, y + 38, x0 + 80, y + 58, stroke=VIOLA, sw=2, dash="3 2")
    s.text(x0 + 30, y + 52, "PYD–PYD", size=9.5, fill=VIOLA, anchor="middle", italic=True)
    s.line(x0 + 130, y + 80, x0 + 130, y + 100, stroke=OCRA, sw=2, dash="3 2")
    s.text(x0 + 182, y + 94, "CARD–CARD", size=9.5, fill=OCRA, anchor="middle", italic=True)
    s.text(x0 + 330, y + 70, ["polimerizzazione di ASC", "(«speck»): prossimità", "→ autoproteolisi"], size=10.5, anchor="middle",
           fill=GRI, italic=True, lh=1.2)
    # caspasi-1
    y2 = y + 145
    s.arrow(250, y2, 250, y2 + 20, colore=BURG, sw=2)
    s.box(170, y2 + 22, 160, 32, ["caspasi-1 attiva"], fill=BURG, stroke=BURG, size=13, weight=700, colore="#fff")
    # prodotti
    y3 = y2 + 80
    s.arrow(200, y2 + 56, 95, y3, colore=BURG)
    s.arrow(300, y2 + 56, 400, y3, colore=BURG)
    s.box(15, y3 + 2, 170, 58, ["pro-IL-1β (31 kDa) → IL-1β", "pro-IL-18 → IL-18"], fill="#fff", stroke=BURG, size=11.5)
    s.box(315, y3 + 2, 170, 58, ["gasdermina D", "→ frammento N-terminale"], fill="#fff", stroke=BURG, size=11.5)
    # membrana con pori
    ym = y3 + 105
    s.rect(10, ym, 480, 14, fill="#f0e3c8", stroke=OCRA, rx=4)
    for x in (300, 360, 420):
        s.rect(x - 10, ym - 3, 20, 20, fill="#fff", stroke=BURG, sw=1.5, rx=3)
        s.line(x - 10, ym + 7, x - 10, ym + 7)
    s.arrow(400, y3 + 62, 360, ym - 4, colore=BURG)
    s.text(470, ym - 8, "pori di GSDMD-N", size=10.5, fill=BURG, anchor="end", weight=600)
    s.arrow(100, y3 + 62, 300, ym - 4, colore=BURG, dash="4 3")
    s.text(250, ym + 40, ["uscita di IL-1β e IL-18 · ingresso di acqua e ioni", "→ rigonfiamento, rottura (NINJ1): **piroptosi** e nuovi DAMP"],
           size=11.5, anchor="middle", lh=1.25)
    s.h = ym + 80
    return s.render()


# ------------------------------------------------------------------ Figura 4
def fig04():
    s = SVG(1000, 600, "f4")
    # APC e cellula T
    s.path("M14,40 Q6,300 14,560 L230,560 Q270,300 230,40 Z", fill=VERDE_L, stroke=VERDE, sw=1.4)
    s.text(130, 30, "CELLULA PRESENTANTE L'ANTIGENE", size=11.5, weight=700, fill=VERDE, anchor="middle", ls=0.5)
    s.path("M330,40 Q300,300 330,560 L990,560 L990,40 Z", fill="#f2f5fa", stroke=BLU, sw=1.4)
    s.text(660, 30, "LINFOCITA T CD4⁺", size=12, weight=700, fill=BLU, anchor="middle", ls=0.8)
    s.circle(820, 470, 0.1)
    # coppie recettoriali
    coppie = [
        (90, "MHC-II + peptide", "TCR / CD3 + CD4", "SEGNALE 1", BLU),
        (210, "CD80 / CD86", "CD28", "SEGNALE 2 (costimolazione)", VERDE),
        (320, "CD80 / CD86", "CTLA-4", "freno (fase di innesco)", BURG),
        (430, "PD-L1 / PD-L2", "PD-1 → SHP-2", "freno (fase effettrice)", BURG),
    ]
    for y, a, b, nota, c in coppie:
        s.rect(165, y - 14, 95, 28, fill="#fff", stroke=VERDE, rx=5)
        s.text(212, y + 4, a, size=10.5, weight=700, anchor="middle", fill=VERDE)
        s.rect(318, y - 14, 112, 28, fill="#fff", stroke=c, rx=5)
        s.text(374, y + 4, b, size=10.5, weight=700, anchor="middle", fill=c)
        s.line(260, y, 318, y, stroke=c, sw=2.4)
        s.text(290, y - 18, nota, size=9.5, weight=600, anchor="middle", fill=c)
    # citochine
    s.text(110, 520, ["**SEGNALE 3:** citochine", "IL-12 → Th1 · IL-6/IL-23 → Th17", "IL-4 → Th2 · TGF-β + IL-2 → Treg"],
           size=10.5, anchor="middle", lh=1.25)
    # farmaci sulla sinapsi
    s.pill(30, 228, "abatacept ⊣ CD80/86", fill=BURG, size=10.5)
    s.pill(30, 360, "anti-CTLA-4 (ipilimumab)", fill="#5b1e35", size=10.5)
    s.pill(30, 466, "anti-PD-1 / anti-PD-L1", fill="#5b1e35", size=10.5)
    s.text(30, 404, ["gli ICI bloccano i freni:", "il linfocita resta attivo"], size=10, fill=BURG, italic=True, lh=1.2)
    # cascata intracellulare
    def nodo(x, y, w, t, c=BLU, f="#fff", sz=11.5):
        s.box(x, y, w, 28, [t], fill=f, stroke=c, size=sz, weight=700)
    nodo(455, 76, 80, "Lck")
    nodo(560, 76, 90, "ZAP-70")
    s.arrow(535, 90, 558, 90, colore=BLU)
    nodo(675, 76, 120, "LAT · SLP-76")
    s.arrow(650, 90, 673, 90, colore=BLU)
    nodo(675, 130, 120, "PLCγ1")
    s.arrow(735, 104, 735, 128, colore=BLU)
    s.text(440, 128, ["fosforilazione degli ITAM", "di CD3 e ζ"], size=10, fill=GRI, italic=True, lh=1.2)
    # IP3 / DAG
    s.text(735, 178, "PIP₂ → IP₃ + DAG", size=11, weight=700, anchor="middle", fill=ANT)
    s.arrow(700, 184, 560, 214, colore=BLU)
    s.arrow(735, 184, 735, 214, colore=BLU)
    s.arrow(770, 184, 900, 214, colore=BLU)
    nodo(470, 216, 170, "IP₃ → Ca²⁺ (RE, STIM1/ORAI1)")
    nodo(670, 216, 130, "DAG → PKCθ")
    nodo(830, 216, 140, "DAG → RasGRP → Ras")
    nodo(490, 270, 130, "calcineurina", c=BURG)
    s.arrow(555, 246, 555, 268, colore=BLU)
    nodo(670, 270, 130, "CARMA1-BCL10-MALT1")
    s.arrow(735, 246, 735, 268, colore=BLU)
    nodo(830, 270, 140, "Raf → MEK → ERK; JNK")
    s.arrow(900, 246, 900, 268, colore=BLU)
    nodo(490, 324, 130, "NFAT (defosforilato)")
    s.arrow(555, 300, 555, 322, colore=BLU)
    nodo(670, 324, 130, "IKK → NF-κB")
    s.arrow(735, 300, 735, 322, colore=BLU)
    nodo(830, 324, 140, "AP-1 (Fos/Jun)")
    s.arrow(900, 300, 900, 322, colore=BLU)
    # CD28 -> PI3K
    s.arrow(430, 210, 455, 374, colore=VERDE, curva=(460, 300))
    nodo(440, 376, 150, "PI3K → Akt → mTOR", c=VERDE)
    # nucleo
    s.ellipse(735, 470, 220, 62, fill="#f4f1fa", stroke=VIOLA, sw=1.3)
    s.text(735, 448, "NUCLEO", size=10.5, weight=700, fill=VIOLA, anchor="middle", ls=1)
    for x in (555, 735, 900):
        s.arrow(x, 354, x if x != 555 else 620, 418 if x != 735 else 412, colore=BLU, sw=1.8)
    s.text(735, 474, "trascrizione di IL-2 e CD25 (IL-2Rα), IFN-γ, IL-17…", size=12, weight=700, anchor="middle")
    s.text(735, 494, "IL-2 → IL-2R → JAK1/JAK3 → STAT5 → espansione clonale", size=11, anchor="middle", fill=ANT)
    # farmaci intracellulari
    s.pill(445, 408, "sirolimus ⊣ mTOR", size=10.5)
    x = 345
    w1 = s.pill(x, 545, "ciclosporina, tacrolimus ⊣ calcineurina", size=10.5)
    s.line(x + 60, 545, 520, 302, stroke=BURG, sw=1, dash="3 3")
    x += w1 + 10
    w2 = s.pill(x, 545, "corticosteroidi ⊣ NF-κB, AP-1", size=10.5)
    s.line(x + w2 / 2, 545, 735, 354, stroke=BURG, sw=1, dash="3 3")
    x += w2 + 10
    w3 = s.pill(x, 545, "MMF, azatioprina ⊣ sintesi delle purine", size=10.5)
    s.line(x + w3 / 2, 545, 860, 502, stroke=BURG, sw=1, dash="3 3")
    s.h = 575
    return s.render()
