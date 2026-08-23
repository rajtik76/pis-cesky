#!/usr/bin/env python3
"""Určí adresář s jazykovými daty pro nástroje pis-cesky.

Pořadí hledání pro každý datový soubor:
1. $PIS_CESKY_DATA - explicitní přepis
2. data/ vedle kořene pluginu - lokálně postavená kopie (třeba v klonu repa)
3. ~/.cache/pis-cesky (respektuje $XDG_CACHE_HOME) - sdílený výchozí
   adresář; přežije aktualizace pluginu, na rozdíl od verzované cache
   Claude pluginů.

Spuštěno přímo vypíše adresář, do kterého se mají stavět nová data.
"""
import os
from pathlib import Path

LOCAL = Path(__file__).resolve().parent.parent / "data"


def build_dir():
    """Where new data gets built: $PIS_CESKY_DATA or the shared cache dir."""
    env = os.environ.get("PIS_CESKY_DATA")
    if env:
        return Path(env).expanduser()
    xdg = os.environ.get("XDG_CACHE_HOME")
    base = Path(xdg).expanduser() if xdg else Path.home() / ".cache"
    return base / "pis-cesky"


def data_file(name):
    """Existing copy of `name`, or its build-dir path when none exists yet."""
    if os.environ.get("PIS_CESKY_DATA"):
        return build_dir() / name
    local = LOCAL / name
    if local.exists():
        return local
    return build_dir() / name


if __name__ == "__main__":
    print(build_dir())
