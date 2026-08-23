#!/usr/bin/env python3
"""Vypíše valenční rámce českého slovesa z VALLEX 4.5.

Použití: vazby.py <sloveso> [další slovesa...]
Data:    vallex-verbs-4.5.xml (staví se skriptem stahni-data.sh; kde se
         hledá, říká datadir.py)

U každého významu vypíše pozice rámce (funktor, povinnost, tvary),
význam a jeden příklad. Pády se značí zkratkami nom, gen, dat, aku,
vok, lok, ins.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from datadir import data_file

NS = {"v": "http://ufal.mff.cuni.cz/vallex-2.0"}
DATA = data_file("vallex-verbs-4.5.xml")

CASES = {"1": "nom", "2": "gen", "3": "dat", "4": "aku", "5": "vok", "6": "lok", "7": "ins"}


def form_str(form):
    t = form.get("type", "")
    if t == "direct_case":
        return CASES.get(form.get("case", ""), form.get("case", "?"))
    if t == "prepos_case":
        return f"{form.get('prepos_lemma', '?')}+{CASES.get(form.get('case', ''), '?')}"
    if t == "subord_conj":
        return f"spojka {form.get('subord_conj_lemma', '?')}"
    if t == "infinitive":
        return "inf"
    if t == "adverb":
        return "adv"
    lemma = form.get("lemma")
    return f"{t}{':' + lemma if lemma else ''}"


def text_of(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if not DATA.exists():
        script = Path(__file__).resolve().parent / "stahni-data.sh"
        sys.exit(f"Chybí {DATA} - spusť: bash {script}")

    wanted = set(sys.argv[1:])
    root = ET.parse(DATA).getroot()
    found = set()

    for lexeme in root.iter(f"{{{NS['v']}}}lexeme"):
        lemmas = [text_of(m) for m in lexeme.findall(".//v:mlemma", NS)]
        # mlemma may hold variants like "dívat (se)" - match on the bare verb too
        keys = set()
        for lm in lemmas:
            keys.add(lm)
            keys.add(lm.replace(" (se)", "").replace(" (si)", "").strip())
        hit = wanted & keys
        if not hit:
            continue
        found |= hit
        aspects = {m.get("aspect") for m in lexeme.findall(".//v:mlemma", NS)}
        print(f"== {' / '.join(lemmas)}  (vid: {', '.join(sorted(a for a in aspects if a))})")
        for blu in lexeme.findall(".//v:blu", NS):
            slots = []
            for slot in blu.findall("./v:frame/v:slot", NS):
                forms = [form_str(f) for f in slot.findall("./v:form", NS)]
                opt = "" if slot.get("type") == "obl" else "?"
                slots.append(f"{slot.get('functor')}{opt}({','.join(forms) or '-'})")
            gloss = text_of(blu.find("./v:gloss", NS))
            example = text_of(blu.find("./v:example", NS))
            print(f"  {' '.join(slots)}")
            if gloss:
                print(f"    = {gloss}")
            if example:
                print(f"    např.: {example}")
        print()

    for miss in wanted - found:
        print(f"'{miss}' ve VALLEX není - zkus základní tvar, nebo je to podezřelé sloveso.")


if __name__ == "__main__":
    main()
