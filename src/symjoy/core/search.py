from symjoy.core.registry import _REGISTRY, _ensure_initialized
from symjoy.core.index import search_keyword, search_alias, search_token

def search(query: str, language: str = "en"):
    if not query:
        return []

    _ensure_initialized()

    query = query.lower()

    candidates = set()

    # exact name
    if query in _REGISTRY:
        candidates.add(query)

    # keyword index
    candidates |= search_keyword(query)

    # alias index
    candidates |= search_alias(query)

    # token index
    candidates |= search_token(query)

    results = []

    for name in candidates:
        symbol = _REGISTRY.get(name)
        if not symbol:
            continue

        results.append(
            {
                "name": symbol.name,
                "char": symbol.char,
                "category": symbol.category,
                "unicode": symbol.unicode,
            }
        )

    results.sort(key=lambda x: (x["category"], x["name"]))

    return results