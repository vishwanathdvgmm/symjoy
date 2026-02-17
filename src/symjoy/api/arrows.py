# src/symjoy/api/arrows.py

import random as _random
from symjoy.core.registry import get_symbol, list_by_category

_CATEGORY = "arrows"

def get(name: str):
    symbol = get_symbol(name)
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
