from symjoy import search

def test_exact_search():
    results = search("smile")

    assert isinstance(results, list)
    assert len(results) > 0

def test_keyword_search():
    results = search("joy")

    assert any("joy" in r["name"] for r in results)

def test_alias_search():
    results = search("heart")

    assert len(results) > 0

def test_empty_query():
    results = search("")

    assert results == []