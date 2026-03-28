from symjoy.core.registry import _REGISTRY, _ensure_initialized
from symjoy.core.index import search_keyword, search_alias, search_token

def search(query: str, language: str = "en"):
    if not query:
        return []

    _ensure_initialized()

    query = query.lower().strip()
    tokens = query.split()

    candidates = set()
    rank_map = {}

    def set_rank(name, rank):
        if name not in rank_map or rank < rank_map[name]:
            rank_map[name] = rank

    # exact name
    if query in _REGISTRY:
        candidates.add(query)
        set_rank(query, 0)

    # keyword index
    for token in tokens:
        for name in search_keyword(token):
            candidates.add(name)
            set_rank(name, 2)

    # alias index
    for token in tokens:    
        for name in search_alias(token):
            candidates.add(name)
            set_rank(name, 3)

    # token index
    for token in tokens:
        for name in search_token(token):
            candidates.add(name)
            set_rank(name, 4)

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
                "_rank": rank_map.get(name, 5),
            }
        )

    results.sort(key=lambda x: (x["name"] != query, x["_rank"], x["category"], x["name"]))

    for r in results:
        r.pop("_rank", None)

    return results
