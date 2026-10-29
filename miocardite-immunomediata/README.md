# Miocardite immunomediata — Vademecum Omnia Medicinae 2026–27

Capitolo monografico: *Dall'immunologia molecolare alla diagnosi clinico-strumentale e alla terapia*.

| File | Contenuto |
|---|---|
| `Miocardite_immunomediata_VOM_2026-27.pdf` | PDF finale, A4, 40 pagine |
| `sorgente/` | Sorgente modificabile: capitoli HTML, `stile.css`, font, generatori delle figure (`figure/*.py`) |
| `figure/` | Le 12 figure originali (SVG vettoriale + PNG) |
| `bibliografia.md` | Bibliografia verificata (37 voci) |
| `prompt_figure_chatgpt.md` | Prompt tecnici per eventuali versioni illustrative delle figure |
| `FASE1_progettazione.md` | Indice e piano iniziale |

## Ricostruire il PDF
```
cd sorgente
python3 build.py          # rigenera figure, HTML e PDF (serve Node + Playwright/Chromium)
python3 build.py --png    # anche le anteprime delle pagine in sorgente/_anteprime/
```
Per modificare il testo si interviene sui file `sorgente/capitoli/*.html`, assemblati in ordine alfabetico; per le figure, sui moduli `sorgente/figure/fig_*.py`.
