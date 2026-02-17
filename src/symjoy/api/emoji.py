# src/symjoy/api/emoji.py

import random as _random
from symjoy.core.registry import get_symbol, list_by_category

_CATEGORY = "emoji"

def get(name: str):
    """
    Get an emoji by name.
    Returns the unicode character or None if not found.
    """
    symbol = get_symbol(name)
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
