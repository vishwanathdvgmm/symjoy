# src/symjoy/core/search.py

from symjoy.core.registry import _REGISTRY

def search(query: str):
    """
    Search for symbols by name across all categories.
    Case-insensitive substring match.

    Ordering:
    1. Exact match
    2. Prefix match
    3. Substring match
    4. Category (deterministic)
    5. Name (deterministic)
    """
    if not query:
        return []

    query = query.lower()
    results = []

    for symbol in _REGISTRY.values():
        name = symbol.name.lower()
        if query in name:
            if name == query:
                rank = 0
            elif name.startswith(query):
                rank = 1
            else:
                rank = 2

            results.append(
                {
                    "name": symbol.name,
                    "char": symbol.char,
                    "category": symbol.category,
                    "unicode": symbol.unicode,
                    "_rank": rank,  # internal only
                }
            )

    # Deterministic + relevance ordering
    results.sort(
        key=lambda x: (x["_rank"], x["category"], x["name"])
    )

    # Remove internal rank before returning
    for r in results:
        r.pop("_rank", None)

    return results
