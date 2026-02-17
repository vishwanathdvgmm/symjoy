import warnings

# --- Modern API modules ---
from symjoy.api import (
    emoji,
    symbols,
    arrows,
    math,
    currency,
    misc,
)

from symjoy.core.search import search

# --- Legacy category data (for v1 compatibility only) ---
from symjoy.categories.emoji import emoji as _legacy_emojis
from symjoy.categories.symbols import symbols as _legacy_symbols
from symjoy.categories.arrows import arrows as _legacy_arrows
from symjoy.categories.math import math_symbols as _legacy_math_symbols
from symjoy.categories.currency import currency as _legacy_currency
from symjoy.categories.misc import misc as _legacy_misc

class _DeprecatedDict(dict):
    def __init__(self, data, name, replacement):
        super().__init__(data)
        self._name = name
        self._replacement = replacement

    def __getitem__(self, key):
        warnings.warn(
            f"'{self._name}' is deprecated and will be removed in symjoy 3.0.0. "
            f"Use {self._replacement} instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return super().__getitem__(key)

# --- Deprecated exports (plural) ---
emojis = _DeprecatedDict(_legacy_emojis, "emojis", "symjoy.emoji.get()")
legacy_symbols = _DeprecatedDict(_legacy_symbols, "symbols", "symjoy.symbols.get()")
legacy_arrows = _DeprecatedDict(_legacy_arrows, "arrows", "symjoy.arrows.get()")
legacy_math_symbols = _DeprecatedDict(_legacy_math_symbols, "math_symbols", "symjoy.math.get()")
legacy_currency = _DeprecatedDict(_legacy_currency, "currency", "symjoy.currency.get()")
legacy_misc = _DeprecatedDict(_legacy_misc, "misc", "symjoy.misc.get()")

__all__ = [
    "search",
    "emoji",
    "symbols",
    "arrows",
    "math",
    "currency",
    "misc",
    "emojis",  # deprecated
]

__version__ = "2.5.0-dev"

__license__ = "MIT"

__author__ = "Vishwanath M M"
