from collections import defaultdict
from symjoy.core.registry import _REGISTRY

_NAME_INDEX = {}
_KEYWORD_INDEX = defaultdict(set)
_ALIAS_INDEX = defaultdict(set)
_TOKEN_INDEX = defaultdict(set)

_INDEX_BUILT = False

def build_index():
    global _INDEX_BUILT

    if _INDEX_BUILT:
        return

    for node in _REGISTRY.values():

        # Name index
        _NAME_INDEX[node.name] = node

        # Keyword index
        if node.keywords:
            for kw in node.keywords:
                _KEYWORD_INDEX[kw.lower()].add(node.name)

        # Alias index
        if node.aliases:
            for lang_aliases in node.aliases.values():
                for alias in lang_aliases:
                    _ALIAS_INDEX[alias.lower()].add(node.name)

        # Token index
        for token in node.name.split("_"):
            _TOKEN_INDEX[token.lower()].add(node.name)

    _INDEX_BUILT = True

def search_keyword(keyword: str):
    return _KEYWORD_INDEX.get(keyword.lower(), set())

def search_alias(alias: str):
    return _ALIAS_INDEX.get(alias.lower(), set())

def search_token(token: str):
    return _TOKEN_INDEX.get(token.lower(), set())