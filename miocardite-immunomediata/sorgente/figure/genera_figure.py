#!/usr/bin/env python3
"""Genera tutte le figure SVG del capitolo (sorgente/figure/*.svg)."""
import importlib, pathlib, sys

QUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))

FIGURE = {
    "fig01_architettura.svg": ("fig_immuno", "fig01"),
    "fig02_innata.svg": ("fig_immuno", "fig02"),
    "fig03_inflammasoma.svg": ("fig_immuno", "fig03"),
    "fig04_linfocitaT.svg": ("fig_immuno", "fig04"),
    "fig05_patogenesi.svg": ("fig_pato", "fig05"),
    "fig06_cardiomiocita.svg": ("fig_pato", "fig06"),
    "fig07_evoluzione.svg": ("fig_pato", "fig07"),
    "fig08_ecg.svg": ("fig_ecg", "svg"),
    "fig09_eco.svg": ("fig_imaging", "fig09"),
    "fig10_lge.svg": ("fig_imaging", "fig10"),
    "fig11_lakelouise.svg": ("fig_imaging", "fig11"),
    "fig12_algoritmo.svg": ("fig_algoritmo", "fig12"),
}


def segnaposto(nome):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="100%">'
            f'<rect x="1" y="1" width="498" height="198" fill="#f4f4f6" stroke="#900C3F" stroke-dasharray="6 4"/>'
            f'<text x="250" y="105" text-anchor="middle" font-size="16" fill="#900C3F">SEGNAPOSTO {nome}</text></svg>')


def main():
    solo = sys.argv[1:]
    fatte = 0
    for nome, (mod, fun) in FIGURE.items():
        if solo and not any(x in nome for x in solo):
            continue
        try:
            m = importlib.import_module(mod)
            contenuto = getattr(m, fun)()
            fatte += 1
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"  {nome}: non ancora disponibile ({e}) -> segnaposto")
            contenuto = segnaposto(nome)
        (QUI / nome).write_text(contenuto, encoding="utf-8")
    print(f"figure generate: {fatte}/{len(FIGURE)}")


if __name__ == "__main__":
    main()
