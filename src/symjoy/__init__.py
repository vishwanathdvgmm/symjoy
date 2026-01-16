# src/symjoy/__init__.py

import warnings

from symjoy.categories.emoji import emojis as _emojis
from symjoy.categories.symbols import symbols as _symbols
from symjoy.categories.arrows import arrows as _arrows
from symjoy.categories.math import math_symbols as _math_symbols
from symjoy.categories.currency import currency as _currency
from symjoy.categories.misc import misc as _misc

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

emojis = _DeprecatedDict(_emojis, "emojis", "symjoy.emoji.get()")
symbols = _DeprecatedDict(_symbols, "symbols", "symjoy.symbols.get()")
arrows = _DeprecatedDict(_arrows, "arrows", "symjoy.arrows.get()")
math_symbols = _DeprecatedDict(_math_symbols, "math_symbols", "symjoy.math.get()")
currency = _DeprecatedDict(_currency, "currency", "symjoy.currency.get()")
misc = _DeprecatedDict(_misc, "misc", "symjoy.misc.get()")

from symjoy.api import emoji, symbols, arrows, math, currency, misc
from symjoy.core.search import search

__all__ = [
    "search",
    "emojis",
    "symbols",
    "arrows",
    "math_symbols",
    "currency",
    "misc",
]

__version__ = "2.1.0"

__license__ = "MIT"

__author__ = "Vishwanath M M"
