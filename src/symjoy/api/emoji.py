# src/symjoy/api/emoji.py

import random as _random
from symjoy.core.registry import get_symbol, list_by_category

_CATEGORY = "emoji"

def get(name: str):
    """
    Get an emoji by name.
    Returns the unicode character or None if not found.
    """
    if not name:
        return None

    symbol = get_symbol(name.lower())
    if symbol and symbol.category == _CATEGORY:
        return symbol.char
    return None

def random():
    """
    Return a random emoji character.
    """
    symbols = list_by_category(_CATEGORY)
    if not symbols:
        return None
    return _random.choice(symbols).char

def list():
    """
    List all emoji names (sorted).
    """
    return [s.name for s in list_by_category(_CATEGORY)]

def items():
    """
    Return a dict of {name: char} for emojis.
    """
    return {s.name: s.char for s in list_by_category(_CATEGORY)}

# ---- v2.1.0 helper APIs ----

def exists(name: str) -> bool:
    """
    Check if an emoji exists by name.
    """
    if not name:
        return False

    symbol = get_symbol(name.lower())
    return bool(symbol and symbol.category == _CATEGORY)

def info(name: str) -> dict | None:
    """
    Return metadata for an emoji.

    {
        "name": str,
        "char": str,
        "category": str,
        "unicode": str
    }
    """
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
