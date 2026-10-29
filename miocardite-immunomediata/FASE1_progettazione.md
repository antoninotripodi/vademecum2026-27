# MIOCARDITE IMMUNOMEDIATA
### Dall'immunologia molecolare alla diagnosi clinico-strumentale e alla terapia
*Vademecum Omnia Medicinae 2026–27 — FASE 1: progettazione*

---

## 0. Decisioni di impianto

| Aspetto | Proposta | Motivazione |
|---|---|---|
| **Lunghezza** | **38–40 pagine A4** (obiettivo minimo 30) | Il budget analitico (§2) mostra che l'indice obbligatorio, con il metodo "richiamo di base → meccanismo → applicazione" e le 5 domande per ogni reperto ECG/eco, richiede ~39 pagine. Sotto 30 si dovrebbero comprimere proprio Cap. II, III, VI e IX. Vedi §2.2 per la variante a 30 pagine. |
| **Perimetro** | "Miocardite immunomediata" = tutte le forme in cui il danno è prodotto dalla risposta immunitaria dell'ospite: post-infettiva/autoimmune linfocitaria, ICI, cellule giganti, eosinofila, da malattie autoimmuni sistemiche, da farmaci (ipersensibilità); sarcoidosi come diagnosi differenziale/forma granulomatosa. La miocardite con replicazione virale attiva è trattata come *contrasto* necessario. | Il discrimine terapeutico (immunosoppressione sì/no) dipende proprio dalla distinzione tra danno da patogeno e danno da risposta dell'ospite. |
| **Toolchain** | HTML + CSS di stampa → PDF via Chromium (come il file già presente in `esame-obiettivo-cmi/`) | Doppia colonna, tabelle booktabs, box tematici e figure vettoriali; il sorgente HTML resta modificabile. LaTeX non è installato nell'ambiente. |
| **Figure** | **Vettoriali SVG originali prodotte da me** (vedi §4) + prompt tecnici per ChatGPT per le figure "illustrative" | In questa sessione **non è disponibile alcuna integrazione ChatGPT** tra i miei strumenti. Per ECG, curve, schemi CMR e algoritmi, un SVG costruito geometricamente è più controllabile e verificabile di un'immagine generativa (derivazioni, intervalli, pattern LGE corretti). |
| **Classi di evidenza** | Ogni affermazione patogenetica marcata con etichetta: **[Fisiologia]**, **[Uomo]**, **[Modello animale]**, **[Ipotesi]**; per la terapia: **[LG ESC 2025]**, **[ACC 2024]**, **[Consenso]**, **[Osservazionale]** | Richiesto dal prompt (§2, §6). |

---

## 1. Indice dettagliato

> Legenda box: **KP** Key Points · **RI** Richiamo di immunologia · **MM** Meccanismo molecolare · **CCF** Correlazione clinico-fisiopatologica · **CI** Come interpretare il reperto · **AD** Attenzione diagnostica

### Frontespizio, abstract strutturato, mappa del capitolo (1 p.)
- Titolo, sottotitolo, collocazione nel volume
- Abstract in 5 punti; "Come usare il capitolo" (percorsi di lettura: immunologico / clinico / ripasso rapido)
- Elenco abbreviazioni (in nota marginale, oltre alla definizione alla prima comparsa)

### CAPITOLO I — Definizione, classificazione ed eziologia (2,5 pp.)
1.1 Definizione istopatologica (Dallas; criteri immunoistochimici ≥14 leucociti/mm² con ≥4 monociti/mm² e CD3+ ≥7/mm²) e definizione clinica (sospetto clinico, diagnosi CMR-based, diagnosi bioptica) — confronto ESC 2025 vs ACC 2024
1.2 Miocardite vs miocardiopatia infiammatoria vs cardiomiopatia dilatativa (DCM): un continuum temporale e fenotipico
1.3 Decorso: acuta, fulminante, persistente/subacuta, cronica (miocardiopatia infiammatoria)
1.4 Eziologia: infettiva (virale con replicazione vs genoma virale latente), immunomediata, autoimmune, post-infettiva, malattie autoimmuni sistemiche, farmaci (ipersensibilità vs tossicità), ICI, eosinofila, cellule giganti, sarcoidosi
1.5 Miocardite, miopericardite, perimiocardite: criteri distintivi (sindromi infiammatorie miopericardiche, concetto unificante ESC 2025)
1.6 Classificazioni cliniche e prognostiche moderne: presentazioni ad alto/basso rischio; stadiazione ACC 2024 (stadi A–D); "complicated vs uncomplicated"
1.7 Perché fenotipi simili hanno meccanismi e terapie diverse (quadro sinottico)
- **Tabella 1** — Classificazione eziopatogenetica: trigger | effettore immunitario dominante | istologia | terapia di principio
- **Box AD** — "Miocardite" non è una diagnosi eziologica
- **Box KP**

### CAPITOLO II — Richiami di immunologia fondamentale (5 pp.)
2.1 **Immunità innata**
- Barriere; logica del riconoscimento del non-self e del danno ("modello del pericolo")
- PRR: TLR (superficie vs endosomiali; TLR3/7/8 per RNA virale — rilevante per coxsackievirus B3), NLR, RLR (RIG-I, MDA5 → MAVS → IRF3/7 → IFN tipo I)
- PAMP vs DAMP (HMGB1, HSP, ATP extracellulare, DNA mitocondriale, frammenti di matrice)
- Cascata TLR: via **MyD88-dipendente** (MyD88 → IRAK4/IRAK1 → TRAF6 → TAK1 → complesso IKK → degradazione IκBα → traslocazione NF-κB p65/p50; MAPK → AP-1) e **TRIF-dipendente** (TLR3, TLR4 endosomiale → TRIF → TBK1/IKKε → IRF3 → IFN-β)
- Cellule: dendritiche (convenzionali vs plasmacitoidi), monociti (classici Ly6C^hi/CD14++ vs non classici), macrofagi (residenti cardiaci di origine embrionale CCR2⁻ vs derivati da monociti CCR2⁺; superamento della dicotomia M1/M2), neutrofili (NET), mastociti, NK (recettori attivatori/inibitori, "missing self"), complemento (vie classica/lectinica/alternativa, C3 convertasi, C5a, MAC)
2.2 **Inflammasoma**
- NLRP3 (domini PYD–NACHT–LRR), ASC, procaspasi-1 → caspasi-1
- Segnale 1 (priming NF-κB: trascrizione di NLRP3 e pro-IL-1β) e segnale 2 (efflusso di K⁺, ROS mitocondriali, rottura lisosomiale; NEK7)
- Maturazione di IL-1β e IL-18; taglio di gasdermina D → pori N-terminali → piroptosi e rilascio di citochine
- **Box MM** — perché il doppio segnale è un dispositivo di sicurezza
- Collegamento al cardiomiocita e ai fibroblasti cardiaci
2.3 **Immunità adattativa**
- Maturazione timica (doppio negativo → doppio positivo → selezione positiva/negativa → CD4 o CD8 singolo positivo)
- TCR αβ e complesso CD3 (ITAM); MHC-I (via citosolica: proteasoma → TAP → ER) e MHC-II (via endosomiale, catena invariante, CLIP, HLA-DM); cross-presentazione
- Costimolazione CD28–CD80/CD86; modello a tre segnali (antigene, costimolazione, citochine)
- Segnalazione del TCR: **Lck** → fosforilazione ITAM → **ZAP-70** → **LAT**/SLP-76 → **PLCγ1** → IP₃ (Ca²⁺ → calcineurina → **NFAT**) e DAG (PKCθ → CARMA1-BCL10-MALT1 → **NF-κB**; RasGRP → Ras-MAPK → **AP-1**) → IL-2/CD25 → proliferazione (mTOR)
- Differenziazione: Th1 (IL-12, STAT4, T-bet, IFN-γ), Th2 (IL-4, STAT6, GATA3), Th17 (IL-6 + TGF-β, IL-23, STAT3, RORγt, IL-17A), Treg (TGF-β, IL-2, STAT5, FOXP3)
- CD8⁺ citotossici: sinapsi immunologica, perforina, granzima B (caspasi-3, BID), Fas/FasL (caspasi-8); IFN-γ e TNF
- Linfociti B, centro germinativo, plasmacellule, isotipi; anticorpi e complemento come effettori
- **Box RI** — Dove agiscono i farmaci immunosoppressori (mappa anticipata dei bersagli: calcineurina, IMPDH, sintesi purine, GR)
2.4 **Tolleranza immunologica**
- Centrale (AIRE, espressione ectopica di antigeni tissutali: perché la miosina cardiaca α è scarsamente espressa nel timo → difetto di tolleranza centrale [Uomo/Modello animale])
- Periferica: anergia, delezione clonale, ignoranza, Treg (CTLA-4 transendocitosi di CD80/86, IL-10, TGF-β, consumo di IL-2)
- **CTLA-4** (fase di priming, linfonodo) vs **PD-1/PD-L1** (fase effettrice, tessuto; SHP-2 → defosforilazione di CD28/TCR)
- Perdita di tolleranza e autoimmunità → **anticipazione ICI**
- **Figure 1, 2, 3, 4**

### CAPITOLO III — Fisiopatologia molecolare della miocardite (7 pp.) — *nucleo del capitolo*
3.1 **Innesco**: danno iniziale (citolisi virale, ischemia microvascolare, tossicità), DAMP, attivazione dei PRR nel cardiomiocita/fibroblasta/endotelio, chemochine, cascata di adesione (selectine → integrine LFA-1/VLA-4 ↔ ICAM-1/VCAM-1 → diapedesi), infiltrazione. Il caso paradigmatico CVB3: recettore CAR, proteasi 2A che taglia la distrofina [Modello animale + Uomo]
3.2 **Attivazione immunitaria**: macrofagi residenti vs reclutati (CCR2/CCL2), DC e trasporto dell'antigene al linfonodo mediastinico, attivazione T, espansione clonale, polarizzazione Th1/Th17, insufficienza relativa delle Treg, citotossicità CD8⁺, autoanticorpi
- **Tabella 2** — Mediatori: IL-1β, IL-6, TNF-α, IFN-γ, IL-17A, TGF-β, CXCL9, CXCL10, CCL2 × origine | recettore | trasduzione (IL-1R1/MyD88; gp130/JAK1-STAT3; TNFR1 → NF-κB vs caspasi-8; IFNGR/JAK1-JAK2/STAT1; IL-17RA/RC-Act1-TRAF6; TβRI/II-SMAD2/3; CXCR3; CCR2) | effetto sul miocardio
3.3 **Autoimmunità miocardica**: mimicry molecolare, epitope spreading, bystander activation, esposizione di antigeni criptici; autoantigeni (catena pesante della miosina α, troponina I, recettore β1-adrenergico, ANT); modello EAM (miosina + adiuvante; ruolo di IL-17 e GM-CSF) [Modello animale]; persistenza dopo clearance virale; autoanticorpi anti-cuore nell'uomo come marcatori di rischio familiare [Uomo] — distinzione rigorosa tra livelli di evidenza
3.4 **Danno diretto del cardiomiocita**: apoptosi (estrinseca/intrinseca), necrosi e necroptosi (RIPK1/RIPK3/MLKL), piroptosi, ROS/RNS (NADPH ossidasi, iNOS → perossinitrito), disfunzione mitocondriale e mPTP, switch metabolico, Ca²⁺: SERCA2a ↓, fosfolambano, RyR2 ossidato/iperfosforilato (perdita diastolica), NCX; danno sarcolemmale; alterazioni di troponine/titina; effetto inotropo negativo acuto di TNF/IL-1/IL-6 (NO, desensibilizzazione β-adrenergica) — ciascuno collegato alla perdita di contrattilità
- **Box CCF** — perché la disfunzione può essere *reversibile* (stunning infiammatorio) oppure *irreversibile* (perdita di miociti)
3.5 **Infiammazione e disfunzione elettrica**: edema e infiltrato (aumento della resistenza di accoppiamento, rimodellamento della connessina-43), riduzione di I_to e I_K (prolungamento del PA, QT), I_Na ridotta (conduzione lenta), Ca²⁺ e DAD → attività triggerata, eterogeneità della ripolarizzazione, rientro attorno a cicatrice, coinvolgimento del sistema di conduzione (BAV: cellule giganti, sarcoidosi, Lyme) — **fase acuta vs fase cicatriziale**
3.6 **Riparazione e rimodellamento**: segnali di risoluzione (lipossine, resolvine), efferocitosi (MerTK), macrofagi riparativi, fibroblasti → miofibroblasti (TGF-β/SMAD2/3, α-SMA, tensione meccanica), collagene I/III, fibrosi sostitutiva vs interstiziale, rimodellamento ventricolare e geometria (legge di Laplace), evoluzione verso DCM; fibrosi come substrato di rientro
3.7 **Forme immunomediate specifiche** — ciascuna con lo schema *Trigger → meccanismo → istologia → fenotipo → terapia*:
1. Cellule giganti (T CD8/CD4, macrofagi fusi, necrosi estesa; BAV/TV; immunosoppressione combinata)
2. Eosinofila (ipersensibilità/DRESS, EGPA, sindrome ipereosinofila; proteine granulari MBP/ECP/EPO; tre fasi: necrotica → trombotica → fibrotica)
3. ICI (perdita di PD-1/CTLA-4; espansione clonale T CD8⁺ anti-α-miosina [Uomo, Axelrod 2022]; miosite/miastenia overlap; steroidi ad alte dosi, abatacept)
4. LES e altre malattie autoimmuni sistemiche (immunocomplessi, complemento, vasculite; anti-Ro e cuore; sclerosi sistemica; miosite)
5. Post-infettiva (dalla fase virale alla fase autoimmune; ruolo della PCR virale tissutale)
- **Tabella 3** — Confronto sinottico delle cinque forme
- **Figure 5, 6, 7**

### CAPITOLO IV — Anatomia patologica (1,5 pp.)
Macroscopia; infiltrato linfocitario/linfo-istiocitario, eosinofilo, granulomatoso (sarcoidosi vs cellule giganti: granulomi ben formati vs necrosi diffusa); necrosi dei miociti; fibrosi; criteri di Dallas (miocardite attiva/borderline) e loro limiti; immunoistochimica (CD3, CD68, HLA-DR); PCR/RT-PCR per genomi virali (parvovirus B19: problema della bassa carica come reperto spesso non patogenetico); diagnosi differenziale istologica
- **Tabella 4** — Istologia → terapia (come il reperto bioptico modifica la decisione)

### CAPITOLO V — Semeiotica clinica ed esame obiettivo (2 pp.)
5.1 Anamnesi: per ciascun sintomo, meccanismo (dolore: pericardio vs danno miocardico/vasospasmo; dispnea: ↑ pressione telediastolica; palpitazioni/sincope: aritmie/BAV; prodromi; ICI: timing tipico nelle prime settimane-mesi; farmaci; familiarità → cardiomiopatie genetiche "a fenotipo miocarditico")
5.2 Esame obiettivo: ogni reperto con *meccanismo — significato — limiti* (tachicardia sproporzionata alla febbre, polso alternante, PA differenziale ridotta, riempimento capillare, turgore giugulare, itto spostato, S3, S4, IM funzionale, sfregamento, rantoli, edemi, epatomegalia, segni di shock e classificazione SCAI)
- **Tabella 5** — Reperto → meccanismo → significato

### CAPITOLO VI — Elettrocardiogramma: guida all'interpretazione (3,5 pp.)
6.1 Richiami: PA di lavoro (fasi 0–4, correnti) vs PA pacemaker (I_f, I_Ca,L); sistema di conduzione; significato di P, PR, QRS, ST, T, QT/QTc
6.2–6.3 Reperti, **ciascuno con le cinque domande** (Cos'è? — Dove? — Come lo riconosco? — Perché nella miocardite? — Significato diagnostico/prognostico):
sopraslivellamento ST, sottoslivellamento ST (e del PR), inversione T, alterazioni aspecifiche, onde Q, bassi voltaggi, QRS allargato/blocchi di branca, BAV I–III grado, BESV/BEV, TV non sostenuta/sostenuta, FA, QTc lungo
- **Tabella 6** — Confronto: miocardite vs STEMI vs pericardite acuta vs ripolarizzazione precoce (morfologia ST, distribuzione, reciprocità, PR, evoluzione T, Q, Spodick, rapporto ST/T in V6)
- **Box AD** — ECG normale non esclude; QRS ≥120 ms come marcatore prognostico negativo
- **Figura 8** (8a–8f)

### CAPITOLO VII — Esami di laboratorio (1,5 pp.)
hs-cTnI/hs-cTnT (cinetica, 99° percentile, cTnT e muscolo scheletrico → rilevante in ICI con miosite), BNP/NT-proBNP, PCR, VES, emocromo, eosinofilia, funzione renale/epatica, CK (miosite), autoanticorpi selezionati, sierologie virali (scarsa utilità), anti-AChR/anti-striati nell'ICI
- **Tabella 7** — Esame | cosa misura | perché si altera | limite | "non esclude se…"
- **Box CI** — Danno ≠ eziologia

### CAPITOLO VIII — Ecocardiografia (2 pp.)
Principi fisici essenziali (impedenza acustica, risoluzione, Doppler, speckle tracking); per ciascun parametro le 5 domande (FE, cinetica segmentaria, GLS e pattern regionale, volumi, spessore/edema nelle forme fulminanti, VD, diastole, IM/IT funzionale, versamento, complicanze); perché un eco normale non esclude
- **Figura 9**

### CAPITOLO IX — Risonanza magnetica cardiaca (3,5 pp.)
9.1 Fisica: spin, B₀, RF, T1 e T2, T1/T2 mapping (MOLLI/ShMOLLI, valori dipendenti dal sito/scanner), ECV (formula con ematocrito), gadolinio (agente extracellulare)
9.2 LGE: distribuzione del gadolinio, inversion recovery e "annullamento" del miocardio sano, perché necrosi e fibrosi trattengono il contrasto, riconoscimento e quantificazione; pattern subepicardico, mesocardico (es. settale), subendocardico, transmurale; ischemico vs non ischemico, eccezioni (MINOCA, sarcoidosi, miocardite con pattern atipico); LGE ≠ infiammazione attiva
9.3 Criteri di Lake Louise 2018: criterio T2-based + criterio T1-based ("2 su 2" per alta specificità), criteri di supporto (versamento/LGE pericardico, disfunzione sistolica), prestazioni, timing (ottimale entro 2–3 settimane dall'esordio), limiti
9.4 Prognosi: LGE mesoparietale settale, LGE persistente senza edema a 6 mesi (ITAMY), FE, follow-up CMR entro 6 mesi
- **Figure 10, 11**

### CAPITOLO X — Altre tecniche diagnostiche (1,5 pp.)
Coronarografia e TC coronarica (esclusione di SCA, MINOCA), PET ¹⁸F-FDG (soppressione del consumo fisiologico; sarcoidosi), Holter/monitoraggio, test genetici (DSP, FLNC, LMNA, PKP2: la "miocardite ricorrente" come fenotipo di cardiomiopatia genetica), **biopsia endomiocardica**: tecnica, sedi (setto VD; biventricolare/guidata da imaging), indicazioni (ESC 2025/ACC 2024), rischi, sampling error, istologia + IHC + PCR, impatto terapeutico
- **Tabella 8** — Indicazioni alla BEM

### CAPITOLO XI — Diagnosi e diagnosi differenziale (3 pp.)
Algoritmo in 10 passi (stabilità → … → eziologia); differenziale con SCA, pericardite, Takotsubo, DCM, cardiomiopatie genetiche (incl. ARVC/ALVC), sarcoidosi, altri danni miocardici (sepsi, tossici, miosite)
**Casi clinici ragionati** (ogni esame scelto/escluso con motivazione):
- Caso A — 22 anni, dolore toracico post-virale, ST diffuso, hs-cTn elevata
- Caso B — 45 anni, dispnea, FE 30%, TV non sostenuta, BAV di II grado → sospetto cellule giganti/sarcoidosi → BEM
- Caso C — 68 anni, melanoma in nivolumab + ipilimumab, ptosi e mialgie, hs-cTnT ↑, CK ↑, ECG con QRS allargato
- **Figura 12**

### CAPITOLO XII — Terapia (4 pp.)
12.1 Gestione generale: criteri di ricovero e di rischio, monitoraggio, restrizione dell'attività (≥3–6 mesi), FANS/colchicina solo per la componente pericardica, follow-up
12.2 Disfunzione VS: terapia dello scompenso (GDMT), cautele farmacologiche, shock cardiogeno, MCS (Impella, VA-ECMO, LV unloading), trasferimento in centro hub
12.3 **Immunosoppressione** — per corticosteroidi, azatioprina, micofenolato, ciclosporina/tacrolimus, globuline anti-timocita, abatacept, IVIG, anakinra (contesti specifici): meccanismo molecolare, bersaglio, razionale, indicazioni, evidenze (TIMIC, Myocarditis Treatment Trial, IMAC…), limiti/effetti avversi
- **Tabella 9** — Quando l'immunosoppressione è indicata / considerata / non raccomandata (replicazione virale attiva)
12.4 Forme speciali: cellule giganti, eosinofila, ICI (algoritmo cardio-oncologico ESC 2022 + ESC 2025), malattie autoimmuni sistemiche
12.5 Aritmie e morte improvvisa: trattamento acuto, defibrillatore indossabile, pacemaker temporaneo/definitivo, ICD (timing: evitare decisioni definitive in fase acuta salvo forme specifiche)
12.6 Prognosi e follow-up: recupero, infiammazione persistente, fibrosi residua, DCM, recidive, ritorno allo sport (criteri ESC), schema di rivalutazione
- **Box KP finale** e "Dieci errori da non commettere"

### Bibliografia (1,5 pp.) · Indice delle figure e delle tabelle

---

## 2. Distribuzione delle pagine

### 2.1 Versione raccomandata (~39 pp.)

| Sezione | Pagine | Figure | Tabelle |
|---|---:|---|---|
| Frontespizio, abstract, abbreviazioni | 1 | — | — |
| I — Definizione, classificazione | 2,5 | — | T1 |
| II — Immunologia fondamentale | 5 | F1, F2, F3, F4 | — |
| III — Fisiopatologia molecolare | 7 | F5, F6, F7 | T2, T3 |
| IV — Anatomia patologica | 1,5 | — | T4 |
| V — Semeiotica | 2 | — | T5 |
| VI — ECG | 3,5 | F8 (pagina intera) | T6 |
| VII — Laboratorio | 1,5 | — | T7 |
| VIII — Ecocardiografia | 2 | F9 | — |
| IX — CMR | 3,5 | F10, F11 | — |
| X — Altre tecniche, BEM | 1,5 | — | T8 |
| XI — Diagnosi, casi clinici | 3 | F12 | — |
| XII — Terapia | 4 | — | T9 |
| Bibliografia, indici | 1,5 | — | — |
| **Totale** | **≈39** | **12** | **9** |

### 2.2 Variante compressa a 30 pagine (se preferisci il limite originario)
Cosa si perderebbe, in ordine: Cap. II ridotto a 3,5 pp. (via RLR e complemento in tabella), Cap. III a 5,5 pp. (forme specifiche solo in Tabella 3), ECG 2,5 pp. (cinque domande in forma tabellare), CMR 2,5 pp., un solo caso clinico esteso + due sintetici, Cap. V in sola tabella. **Non la raccomando**: comprime esattamente i passaggi causali che sono l'obiettivo del capitolo.

---

## 3. Elenco definitivo delle figure

Stile comune: vettoriale, palette burgundy `#900C3F` (processi patologici/danno), blu accademico `#1F3A5F` (immunità/strutture), antracite `#333333` (testo, contorni), grigio chiaro per sfondi; carattere sans per le etichette; etichette in italiano; larghezza colonna (≈85 mm) o pagina (≈178 mm).

| # | Titolo | Formato | Contenuto obbligatorio | Rischi da verificare |
|---|---|---|---|---|
| 1 | Architettura della risposta immunitaria cardiaca | pagina | Miocardio con cellule residenti (macrofagi CCR2⁻, fibroblasti, endotelio, mastociti); braccio innato (monociti CCR2⁺, neutrofili, NK, DC) e adattativo (CD4 Th1/Th17, Treg, CD8, B/plasmacellule); linfonodo mediastinico; mediatori principali | Non attribuire produzioni citochiniche errate |
| 2 | Attivazione dell'immunità innata | colonna | PAMP/DAMP → TLR (membrana ed endosoma) → MyD88 (IRAK4/1-TRAF6-TAK1-IKK-IκBα-NF-κB) e TRIF (TBK1-IRF3) → geni proinfiammatori → chemochine → adesione/diapedesi | Topologia corretta di TLR3/7/9 (endosoma) e TLR2/4 |
| 3 | Inflammasoma NLRP3 | colonna | Segnale 1 (NF-κB) e 2 (K⁺, ROS, NEK7), assemblaggio NLRP3–ASC–procaspasi-1 (PYD–PYD, CARD–CARD), caspasi-1 → IL-1β/IL-18 maturi; gasdermina D → poro → piroptosi | Domini PYD/CARD collocati correttamente |
| 4 | Attivazione del linfocita T | pagina | Sinapsi APC–T: MHC-II/peptide–TCR/CD3/CD4; CD80/86–CD28 vs CTLA-4; PD-L1–PD-1/SHP-2; Lck → ZAP-70 → LAT/SLP-76 → PLCγ1 → IP₃/Ca²⁺/calcineurina/NFAT, DAG/PKCθ/NF-κB, Ras/MAPK/AP-1; bersagli di ciclosporina, MMF, steroidi, abatacept, anti-PD-1 | Bersagli farmacologici esatti |
| 5 | Patogenesi immunomediata della miocardite | pagina | Tre fasi (danno iniziale → espansione immunitaria/autoimmunità → risoluzione o cronicizzazione) con mimicry, epitope spreading, bystander; etichette di livello di evidenza | Non presentare il modello EAM come dimostrato nell'uomo |
| 6 | Danno del cardiomiocita | colonna | Sarcolemma, RyR2, SERCA2a/PLN, NCX, mitocondrio (ROS, mPTP, citocromo c), sarcomero; apoptosi/necrosi/piroptosi; frecce verso ↓ contrattilità | Direzione dei flussi di Ca²⁺ |
| 7 | Evoluzione della malattia | colonna | Asse temporale: giorni (innata) → settimane (adattativa) → mesi (fibrosi); bivio: guarigione / infiammazione persistente / DCM | — |
| 8 | ECG nella miocardite | pagina | **Tracciati schematici, dichiarati come tali**: 8a ST concavo diffuso + sottoslivellamento PR; 8b STEMI inferiore con reciprocità in aVL (confronto); 8c inversione T diffusa; 8d BBS/QRS allargato; 8e BAV II grado Mobitz II e III grado; 8f TV monomorfa. Griglia standard 25 mm/s, 10 mm/mV, annotazioni | Ampiezze e intervalli in scala; reciprocità corretta |
| 9 | Ecocardiografia | colonna | Schemi apicale 4 camere e asse corto: ipocinesia globale vs segmentaria; bull's-eye GLS con pattern non coronarico; versamento; ispessimento edematoso nella fulminante | Segmentazione AHA a 17 segmenti corretta |
| 10 | CMR e LGE | pagina | Asse corto e 4 camere schematici: subendocardico/transmurale in territorio coronarico vs subepicardico infero-laterale e mesoparietale settale (miocardite), patchy (sarcoidosi); curva di inversion recovery con TI di annullamento | Territori coronarici coerenti con i 17 segmenti |
| 11 | Criteri di Lake Louise 2018 | colonna | Due blocchi (T2-based: T2 mapping/T2W; T1-based: T1 mapping, ECV, LGE), regola "≥1 + ≥1", criteri di supporto; mini-istogrammi T1/T2 normale vs patologico | Usare valori relativi (z-score/locali), non cut-off assoluti universali |
| 12 | Algoritmo diagnostico-terapeutico | pagina | Flowchart dal sospetto alla terapia eziologica, con rami: instabile → hub/MCS/BEM precoce; stabile → ECG/troponina/eco → esclusione SCA → CMR → BEM se criteri → terapia | Coerenza con ESC 2025 / ACC 2024 |

**Prompt tecnici per ChatGPT**: verranno forniti in FASE 3 in un file separato (`prompt_figure_chatgpt.md`) per tutte le 12 figure, nel caso tu voglia versioni illustrative alternative. Nel PDF entreranno solo figure effettivamente prodotte e verificate; nessun segnaposto sarà dichiarato come figura completata.

---

## 4. Tabelle e box (riepilogo)
- **9 tabelle** booktabs (T1–T9, vedi indice).
- **Box previsti**: KP (uno per capitolo, 12), RI (≈5, Cap. II–III), MM (≈6), CCF (≈6), CI (≈8, Cap. VI–IX), AD (≈6).
- Regola: i box contengono sintesi o approfondimenti, **mai** contenuti assenti dal testo principale.

---

## 5. Fonti — nucleo bibliografico (stato di verifica)

Verificati in FASE 1 (esistenza, anno, rivista):
1. Schulz-Menger J, Imazio M, et al. *2025 ESC Guidelines for the management of myocarditis and pericarditis.* Eur Heart J 2025;46:3952–4041. doi:10.1093/eurheartj/ehaf192 — ✔ verificato
2. Drazner MH, Bozkurt B, Cooper LT, et al. *2024 ACC Expert Consensus Decision Pathway on Strategies and Criteria for the Diagnosis and Management of Myocarditis.* J Am Coll Cardiol, pubbl. online 10/12/2024. doi:10.1016/j.jacc.2024.10.080 — ✔ verificato (volume/pagine da confermare in FASE 5)

Da verificare puntualmente in FASE 5 (riferimenti noti, di cui controllerò anno, pagine e DOI prima di inserirli):
- Caforio ALP et al. ESC WG position statement, Eur Heart J 2013
- Ferreira VM et al. Lake Louise Criteria aggiornati, J Am Coll Cardiol 2018
- Messroghli DR et al. SCMR consensus su T1/T2/ECV mapping, J Cardiovasc Magn Reson 2017
- Tschöpe C et al. Myocarditis and inflammatory cardiomyopathy, Nat Rev Cardiol 2021
- Ammirati E et al. Circulation 2018 (registro lombardo); J Am Coll Cardiol 2019 (fulminante); Circ Heart Fail 2020 (consenso gestione)
- Kociol RD et al. AHA Scientific Statement sulla miocardite fulminante, Circulation 2020
- Aretz HT. Dallas criteria, Hum Pathol 1987; Leone O et al. consensus AECVP/SCVP sulla BEM, Cardiovasc Pathol 2012; Cooper LT et al. ruolo della BEM, Circulation 2007
- Cooper LT et al. Giant-cell myocarditis, N Engl J Med 1997
- Brambatti M et al. Eosinophilic myocarditis, J Am Coll Cardiol 2017
- Johnson DB et al. N Engl J Med 2016; Mahmood SS et al. J Am Coll Cardiol 2018; Moslehi JJ et al. Lancet 2018; Salem JE et al. (abatacept) N Engl J Med 2019; Axelrod ML et al. Nature 2022 (T cell anti-α-miosina nell'ICI)
- Lyon AR et al. 2022 ESC Guidelines on cardio-oncology, Eur Heart J 2022
- Frustaci A et al. TIMIC, Eur Heart J 2009; Mason JW et al. Myocarditis Treatment Trial, N Engl J Med 1995; McNamara DM et al. IMAC, Circulation 2001
- Kindermann I et al. Circulation 2008; Grün S et al. J Am Coll Cardiol 2012; Aquaro GD et al. ITAMY, J Am Coll Cardiol 2019
- Neu N et al. (miosina e miocardite autoimmune sperimentale), J Immunol 1987
- Swanson KV, Deng M, Ting JP. NLRP3 inflammasome, Nat Rev Immunol 2019
- Pelliccia A et al. 2020 ESC Guidelines on sports cardiology, Eur Heart J 2021
- Thygesen K et al. Fourth Universal Definition of MI, Eur Heart J 2019

Regola: un riferimento entra in bibliografia solo dopo verifica; i DOI non verificati non vengono riportati. Le linee guida verranno parafrasate e rielaborate, senza riprodurne testi o figure.

---

## 6. Piano delle fasi successive
| Fase | Prodotto | Note |
|---|---|---|
| 2 — Redazione | Testo completo Cap. I–XII in HTML sorgente | Procederò per blocchi (I–III, IV–VIII, IX–XII) con commit intermedi |
| 3 — Iconografia | 12 SVG originali + `prompt_figure_chatgpt.md` | ECG generati da forme d'onda parametriche in scala reale |
| 4 — Impaginazione | PDF A4 doppia colonna via Chromium | Stile coerente con il volume |
| 5 — Revisione | Controllo scientifico, verifica bibliografica, render pagina per pagina | Correzione di overflow e spazi vuoti |
| 6 — Consegna | PDF, HTML sorgente, cartella `figure/`, `bibliografia.md` | Tutto nella cartella `miocardite-immunomediata/` del repository |

## 7. Decisioni che ti chiedo di confermare
1. **Lunghezza**: ~39 pagine (raccomandata) o variante compressa a 30.
2. **Figure**: SVG vettoriali originali prodotti da me (raccomandato, integrazione ChatGPT non disponibile in questa sessione) + prompt ChatGPT come materiale accessorio.
3. **Impostazione dei casi clinici**: età e scenari del §1 (Cap. XI) vanno bene o preferisci altri contesti (es. miocardite post-vaccino mRNA come quarto caso)?
