from __future__ import annotations
import random as _random
from symjoy.core.registry import get_symbol, list_by_category
from symjoy.core.registry import get_related as _get_related

_CATEGORY = "emoji"

def get(name: str) -> str | None:
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

def random() -> str | None:
    """
    Return a random emoji character.
    """
    symbols = list_by_category(_CATEGORY)
    if not symbols:
        return None
    return _random.choice(symbols).char

def list() -> list[str]:
    """
    List all emoji names (sorted).
    """
    return [s.name for s in list_by_category(_CATEGORY)]

def items() -> dict[str, str]:
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

def related(name: str) -> list[dict]:
    """
    Return related emoji characters.
    """
    if not None:
        return []

    nodes = _get_related(name.lower())
    return [
        {"name": n.name, "char": n.char}
        for n in nodes
        if n.category == _CATEGORY
    ]