from dataclasses import dataclass
import warnings
import os
import json
from pathlib import Path

from symjoy.categories import (
    emoji as emoji_legacy,
    symbols,
    arrows,
    math,
    currency,
    misc,
)

_DEBUG = os.environ.get("SYMJOY_DEBUG", "").lower() in {"1", "true", "yes"}

# -------------------------------
# New Metadata-Aware SymbolNode
# -------------------------------

@dataclass(frozen=True)
class SymbolNode:
    name: str
    char: str
    category: str
    unicode: str
    keywords: tuple[str, ...] = ()
    aliases: dict[str, tuple[str, ...]] = None
    related: tuple[str, ...] = ()

# -------------------------------
# Internal State
# -------------------------------

_REGISTRY: dict[str, SymbolNode] = {}
_BY_CATEGORY: dict[str, set[str]] = {}

_INITIALIZED = False

_STOPWORDS = {"with", "of", "and", "the", "a", "an", "face"}

# -------------------------------
# Utility
# -------------------------------

def _unicode_codepoint(char: str) -> str:
    return " ".join(f"U+{ord(c):04X}" for c in char)

def _register_symbol(node: SymbolNode):
    if node.name in _REGISTRY:
        if _DEBUG:
            warnings.warn(
                f"Duplicate symbol key detected: '{node.name}'",
                RuntimeWarning,
            )
        return

    _REGISTRY[node.name] = node
    _BY_CATEGORY.setdefault(node.category, set()).add(node.name)

# -------------------------------
# JSON Loader (emoji only for now)
# -------------------------------

def _load_category_from_json(category_name: str) -> bool:
    data_path = Path(__file__).parent.parent / "data" / f"{category_name}.json"

    if not data_path.exists():
        return False

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            items = json.load(f)

        for item in items:
            # Auto keyword generation
            raw_keywords = item.get("keywords", [])
            if not raw_keywords:
                raw_keywords = item["name"].split("_")
            keywords = tuple(raw_keywords)

            # Auto alias generation
            raw_aliases = item.get("aliases", {})
            if not raw_aliases:
                raw_aliases = {"en": [item["name"]]}
            aliases = {
                lang: tuple(vals)
                for lang, vals in raw_aliases.items()
            }

            node = SymbolNode(
                name=item["name"],
                char=item["char"],
                category=category_name,
                unicode=_unicode_codepoint(item["char"]),
                keywords=keywords,
                aliases=aliases,
                related=tuple(item.get("related", [])),
            )

            _register_symbol(node)

        return True

    except Exception as e:
        if _DEBUG:
            warnings.warn(f"Failed to load {category_name}.json: {e}")
        return False


def _enrich_metadata():
    """
    Automatically enrich nodes with:
    - Generated keywords (if empty)
    - Generated aliases (if empty)
    - Token-based relationships
    """

    # Step 1 — Fill missing keywords & aliases
    for name, node in list(_REGISTRY.items()):

        # Generate keywords if empty
        if not node.keywords:
            tokens = tuple(
                t for t in name.split("_")
                if t.lower() not in _STOPWORDS
            )
        else:
            tokens = node.keywords

        # Generate alias if empty
        if not node.aliases:
            aliases = {"en": (name.replace("_", " "),)}
        else:
            aliases = node.aliases

        # Replace node (dataclass is frozen)
        _REGISTRY[name] = SymbolNode(
            name=node.name,
            char=node.char,
            category=node.category,
            unicode=node.unicode,
            keywords=tokens,
            aliases=aliases,
            related=node.related,
        )

    # Step 2 — Auto-generate relationships
    for name, node in list(_REGISTRY.items()):

        base_tokens = {
            t.lower()
            for t in node.keywords
            if t.lower() not in _STOPWORDS
        }

        auto_related = set(node.related)

        for other in _REGISTRY.values():
            if other.name == name:
                continue

            other_tokens = {
                t.lower()
                for t in other.keywords
                if t.lower() not in _STOPWORDS
            }

            if base_tokens.intersection(other_tokens):
                auto_related.add(other.name)

        _REGISTRY[name] = SymbolNode(
            name=node.name,
            char=node.char,
            category=node.category,
            unicode=node.unicode,
            keywords=node.keywords,
            aliases=node.aliases,
            related=tuple(sorted(auto_related)),
        )

# -------------------------------
# Legacy Fallback Loader
# -------------------------------

def _register_legacy_category(category_name: str, data: dict):
    for name, char in data.items():
        node = SymbolNode(
            name=name,
            char=char,
            category=category_name,
            unicode=_unicode_codepoint(char),
        )
        _register_symbol(node)

# -------------------------------
# Lazy Registry Builder
# -------------------------------

def _ensure_initialized():
    global _INITIALIZED

    if _INITIALIZED:
        return

    # Load JSON categories
    for category in ["emoji", "symbols", "arrows", "math", "currency", "misc"]:
        _load_category_from_json(category)
    
    _enrich_metadata()

    _INITIALIZED = True

# -------------------------------
# Public API
# -------------------------------

def get_symbol(name: str) -> SymbolNode | None:
    _ensure_initialized()
    return _REGISTRY.get(name)

def list_categories() -> list[str]:
    _ensure_initialized()
    return sorted(_BY_CATEGORY.keys())

def list_by_category(category: str) -> list[SymbolNode]:
    _ensure_initialized()
    return [
        _REGISTRY[name]
        for name in sorted(_BY_CATEGORY.get(category, []))
    ]

def get_related(name: str) -> list[SymbolNode]:
    _ensure_initialized()

    node = _REGISTRY.get(name)
    if not node:
        return []

    related_set = set(node.related)

    if node.keywords:
        node_keywords = {
            k.lower()
            for k in node.keywords
            if k.lower() not in _STOPWORDS
        }

        for other in _REGISTRY.values():
            if other.name == name:
                continue

            if not other.keywords:
                continue

            other_keywords = {
                k.lower()
                for k in other.keywords
                if k.lower() not in _STOPWORDS
            }

            if node_keywords.intersection(other_keywords):
                related_set.add(other.name)

    # Unique + deterministic ordering
    unique_nodes = [
        _REGISTRY[n]
        for n in sorted(related_set)
        if n in _REGISTRY
    ]

    return unique_nodes