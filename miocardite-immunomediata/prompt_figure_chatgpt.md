# Prompt tecnici per versioni illustrative delle figure (ChatGPT / generatori di immagini)

In questa sessione l'integrazione ChatGPT **non era disponibile**. Le 12 figure del PDF sono state quindi disegnate come grafica vettoriale originale (cartella `figure/`, file SVG e PNG). I prompt seguenti servono **solo** se vuoi produrre versioni illustrative alternative con ChatGPT. Ogni immagine generata va confrontata con la figura vettoriale e con il testo, perché i generatori di immagini sbagliano spesso etichette, tracciati ECG e anatomia.

**Indicazioni comuni** (da aggiungere a ogni prompt): stile editoriale da rivista scientifica (Nature Reviews Cardiology), sfondo bianco; palette: bordeaux #900C3F per i processi patologici, blu scuro #1F3A5F per le strutture immunitarie, antracite #2E2E33 per testo e contorni; accenti moderati; etichette in italiano, in sans-serif, leggibili in formato A4; nessun logo; nessun testo inventato.

---

### Figura 1: Architettura della risposta immunitaria cardiaca
Schema orizzontale in tre pannelli. (1) Miocardio: cardiomiociti striati, fibroblasti, capillare con endotelio, macrofagi residenti CCR2⁻, mastociti. (2) Circolo: monociti CCR2⁺, neutrofili e cellule NK che attraversano l'endotelio (selectine, ICAM-1, VCAM-1) richiamati dalle chemochine CCL2, CXCL1/8, CXCL9/10. (3) Linfonodo mediastinico: una cellula dendritica presenta l'antigene a un linfocita T naïve; ne derivano Th1 (IFN-γ), Th17 (IL-17A), CD8⁺ (perforina), Treg (IL-10, TGF-β) e plasmacellule con anticorpi. Una freccia di ritorno mostra gli effettori che tornano al cuore. In basso, una legenda dei mediatori con la cellula che li produce.

### Figura 2: Attivazione dell'immunità innata
Cascata verticale. In alto, PAMP (RNA virale) e DAMP (HMGB1, HSP, ATP, DNA mitocondriale). Al centro, una membrana con TLR4/TLR2 e un endosoma con TLR3, TLR7/8 e TLR9. Ramo sinistro: MyD88 → IRAK4/IRAK1 → TRAF6 (ubiquitina K63) → TAK1/TAB2-3 → IKKα/IKKβ/NEMO → fosforilazione e degradazione di IκBα → NF-κB (p65/p50) nel nucleo; ramo laterale p38/JNK → AP-1. Ramo destro: TRIF → TBK1/IKKε → IRF3 → IFN-β. Nel nucleo: TNF-α, IL-6, pro-IL-1β, NLRP3, CCL2, ICAM-1/VCAM-1. Rispetta la topologia: TLR3, TLR7/8 e TLR9 sono endosomiali.

### Figura 3: Inflammasoma NLRP3
Segnale 1 (TLR/IL-1R → NF-κB → trascrizione di NLRP3 e pro-IL-1β) e segnale 2 (ATP → P2X7 → efflusso di K⁺, ROS mitocondriali, danno lisosomiale). Assemblaggio con i domini disegnati come blocchi: NLRP3 (PYD–NACHT–LRR, con NEK7 legata al dominio LRR), ASC (PYD–CARD), procaspasi-1 (CARD–p20–p10); le interazioni omotipiche sono PYD–PYD e CARD–CARD. La caspasi-1 attiva matura IL-1β e IL-18 e taglia la gasdermina D, il cui frammento N-terminale forma pori nella membrana: rilascio delle citochine e piroptosi.

### Figura 4: Attivazione del linfocita T
Sinapsi immunologica tra APC e linfocita T CD4⁺. Coppie recettoriali: MHC-II/peptide–TCR/CD3 con CD4 e Lck; CD80/86–CD28; CD80/86–CTLA-4; PD-L1–PD-1 con SHP-2. Via intracellulare: Lck → ZAP-70 → LAT/SLP-76 → PLCγ1 → IP₃ (Ca²⁺ → calcineurina → NFAT) e DAG (PKCθ → CARMA1-BCL10-MALT1 → NF-κB; RasGRP → Ras → MAPK → AP-1); CD28 → PI3K → Akt → mTOR; nel nucleo, IL-2 e CD25. Bersagli farmacologici indicati con il simbolo ⊣: ciclosporina e tacrolimus sulla calcineurina, corticosteroidi su NF-κB/AP-1, sirolimus su mTOR, micofenolato e azatioprina sulla sintesi delle purine, abatacept su CD80/86, anticorpi anti-PD-1 e anti-CTLA-4 sui recettori inibitori.

### Figura 5: Patogenesi immunomediata della miocardite
Tre colonne temporali (giorni, settimane, mesi). Fase 1: trigger (virus, farmaco, ICI), danno del cardiomiocita, DAMP, PRR, mediatori, infiltrato innato. Fase 2: cellule dendritiche → linfonodo, attivazione T, Th1/Th17/CD8⁺, perdita della tolleranza (mimetismo, bystander, antigeni criptici, epitope spreading), autoanticorpi. Fase 3: biforcazione tra risoluzione (efferocitosi, Treg) e persistenza, con fibrosi, rimodellamento e substrato aritmico. Badge colorati per il livello di evidenza (Uomo, Modello animale, Ipotesi).

### Figura 6: Danno del cardiomiocita
Sezione di un cardiomiocita: canale del Ca²⁺ di tipo L, reticolo sarcoplasmatico con RyR2 (perdita diastolica di Ca²⁺) e SERCA2a con fosfolambano, NCX (3 Na⁺ in entrata, corrente depolarizzante), mitocondrio (ROS, mPTP, citocromo c), sarcomero (calpaine, troponina I, titina) e sarcolemma danneggiato da perforina e complemento. All'esterno: CD8⁺, TNF-α/IL-1β → iNOS. In basso: apoptosi, necrosi/necroptosi e piroptosi.

### Figura 7: Evoluzione della malattia
Linea del tempo (giorni → settimane → mesi): infiammazione → danno → riparazione, poi tre esiti (guarigione, infiammazione persistente, fibrosi estesa/DCM). Grafico con andamento indicativo di troponina, edema (T2) e fibrosi (LGE/ECV), dichiarato «non in scala».

### Figura 8: ECG nella miocardite (usare con estrema cautela)
**Sconsigliato generarla con un modello di immagini**: i tracciati prodotti in questo modo sono quasi sempre elettrofisiologicamente sbagliati. Se la generi comunque, richiedi carta millimetrata 25 mm/s e 10 mm/mV, scritta «tracciato schematico» e pannelli: (a) ST sopraslivellato concavo in II e V5 con PR sottoslivellato e immagine opposta in aVR; (b) STEMI inferiore con ST convesso in II/III e sottoslivellamento speculare in aVL; (c) onde T negative simmetriche; (d) BBS (QS largo in V1, R larga a M in V6, QRS 150 ms); (e) BAV Mobitz II e BAV completo; (f) TV monomorfa con dissociazione atrio-ventricolare. Verifica ogni pannello confrontandolo con la Figura 8 vettoriale.

### Figura 9: Ecocardiografia
(a) Due schemi apicali 4 camere (apice in alto, VS a destra dell'osservatore): forma fulminante (VS non dilatato, pareti ispessite, versamento lieve) e fase cronica (VS dilatato e sferico, pareti sottili). (b) Bull's-eye a 17 segmenti con orientamento standard (anteriore in alto, setto a sinistra), con riduzione dello strain nei segmenti infero-laterali basali e medi.

### Figura 10: CMR e LGE
Cinque sezioni in asse corto in stile immagine LGE (miocardio sano nero, LGE bianco, sangue grigio, VD a sinistra dell'osservatore): (a) infarto subendocardico nel territorio della discendente anteriore; (b) infarto transmurale infero-laterale; (c) miocardite con LGE subepicardico infero-laterale; (d) miocardite con LGE mesoparietale settale; (e) sarcoidosi con LGE a chiazze multifocale. Sotto, le curve di inversion recovery con il tempo di inversione che annulla il miocardio sano.

### Figura 11: Criteri di Lake Louise 2018
Due colonne: marcatori T2-based (T2 mapping, immagini T2-pesate) e marcatori T1-based (T1 nativo, ECV, LGE non ischemico). Regola «≥1 + ≥1» → infiammazione miocardica acuta ad alta specificità; con un solo marcatore la specificità è minore. In basso i criteri di supporto (pericardio, disfunzione sistolica). Non inserire valori soglia assoluti.

### Figura 12: Algoritmo diagnostico-terapeutico
Flowchart: sospetta miocardite → stabilità emodinamica ed elettrica? Ramo instabile: stabilizzazione → centro hub con supporto meccanico (MCS) → coronarografia + BEM precoce → istotipo → terapia eziologica. Ramo stabile: ECG, biomarcatori, ecocardiogramma → esclusione della SCA → CMR (Lake Louise) → BEM se indicata → stratificazione del rischio → eziologia. In basso: terapia guidata dal meccanismo e follow-up (CMR entro 6 mesi, decisione sull'ICD a 3–6 mesi).
