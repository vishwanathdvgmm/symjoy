from symjoy.core.registry import _REGISTRY, _ensure_initialized

def search(query: str, language: str = "en"):
    """
    Metadata-aware search.

    Ordering priority:
    0 - Exact name match
    1 - Prefix name match
    2 - Keyword match
    3 - Alias match
    4 - Substring name match
    5 - Deterministic fallback
    """
    if not query:
        return []

    _ensure_initialized()

    query = query.lower()
    results = []

    for symbol in _REGISTRY.values():
        name = symbol.name.lower()
        rank = None

        # Exact name
        if name == query:
            rank = 0

        # Prefix name
        elif name.startswith(query):
            rank = 1

        # Keyword match
        elif symbol.keywords and query in [k.lower() for k in symbol.keywords]:
            rank = 2

        # Alias match
        elif (
            symbol.aliases
            and language in symbol.aliases
            and query in [a.lower() for a in symbol.aliases[language]]
        ):
            rank = 3

        # Substring fallback
        elif query in name:
            rank = 4

        if rank is not None:
            results.append(
                {
                    "name": symbol.name,
                    "char": symbol.char,
                    "category": symbol.category,
                    "unicode": symbol.unicode,
                    "_rank": rank,
                }
            )

    results.sort(key=lambda x: (x["_rank"], x["category"], x["name"]))

    for r in results:
        r.pop("_rank", None)

    return results