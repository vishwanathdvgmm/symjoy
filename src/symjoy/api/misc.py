# src/symjoy/api/misc.py

import random as _random
from symjoy.core.registry import get_symbol, list_by_category

_CATEGORY = "misc"

def get(name: str):
    if not name:
        return None

    symbol = get_symbol(name.lower())
    if symbol and symbol.category == _CATEGORY:
        return symbol.char
    return None

def random():
    symbols = list_by_category(_CATEGORY)
    if not symbols:
        return None
    return _random.choice(symbols).char

def list():
    return [s.name for s in list_by_category(_CATEGORY)]

def items():
    return {s.name: s.char for s in list_by_category(_CATEGORY)}

# ---- v2.1.0 helper APIs ----

def exists(name: str) -> bool:
    if not name:
        return False

    symbol = get_symbol(name.lower())
    return bool(symbol and symbol.category == _CATEGORY)

def info(name: str) -> dict | None:
    if not name:
        return None

    symbol = get_symbol(name.lower())
    if symbol and symbol.category == _CATEGORY:
        return {
            "name": symbol.name,
            "char": symbol.char,
            "category": symbol.category,
            "unicode": symbol.unicode,
        }
    return None
