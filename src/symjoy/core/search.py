# src/symjoy/core/search.py

from symjoy.core.registry import _REGISTRY

def search(query: str):
    """
    Search for symbols by name across all categories.
    Case-insensitive substring match.
    """
    if not query:
        return []

    query = query.lower()
    results = []

    for symbol in _REGISTRY.values():
        if query in symbol.name.lower():
            results.append(
                {
                    "name": symbol.name,
                    "char": symbol.char,
                    "category": symbol.category,
                    "unicode": symbol.unicode,
                }
            )

    # Deterministic ordering
    results.sort(key=lambda x: (x["category"], x["name"]))
    return results
