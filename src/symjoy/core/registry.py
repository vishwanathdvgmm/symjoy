# src/symjoy/core/registry.py

from dataclasses import dataclass
import warnings, os

from symjoy.categories import (
    emoji,
    symbols,
    arrows,
    math,
    currency,
    misc,
)

_DEBUG = os.environ.get("SYMJOY_DEBUG", "").lower() in {"1", "true", "yes"}

@dataclass(frozen=True)
class Symbol:
    name: str
    char: str
    category: str
    unicode: str

_REGISTRY = {}
_BY_CATEGORY = {}

def _unicode_codepoint(char: str) -> str:
    return " ".join(f"U+{ord(c):04X}" for c in char)

def _register_category(category_name: str, data: dict):
    if category_name not in _BY_CATEGORY:
        _BY_CATEGORY[category_name] = set()

    for name, char in data.items():
        if name in _REGISTRY:
            if _DEBUG:
                warnings.warn(
                    f"Duplicate symbol key detected: '{name}' "
                    f"(existing category: {_REGISTRY[name].category}, "
                    f"new category: {category_name})",
                    RuntimeWarning,
                )

        symbol = Symbol(
            name=name,
            char=char,
            category=category_name,
            unicode=_unicode_codepoint(char),
        )

        _REGISTRY[name] = symbol
        _BY_CATEGORY[category_name].add(name)

def _build_registry():
    _register_category("emoji", emoji.emojis)
    _register_category("symbols", symbols.symbols)
    _register_category("arrows", arrows.arrows)
    _register_category("math", math.math_symbols)
    _register_category("currency", currency.currency)
    _register_category("misc", misc.misc)

_build_registry()

def get_symbol(name: str) -> Symbol | None:
    return _REGISTRY.get(name)

def list_categories() -> list[str]:
    return sorted(_BY_CATEGORY.keys())

def list_by_category(category: str) -> list[Symbol]:
    return [ _REGISTRY[name] for name in sorted(_BY_CATEGORY.get(category, [])) ]
