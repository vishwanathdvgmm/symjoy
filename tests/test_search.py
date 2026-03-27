from symjoy import search

def test_exact_search():
    results = search("smile")

    assert len(results) > 0
    assert results[0]["name"] == "smile"

def test_keyword_search():
    results = search("joy")

    assert any(r["name"] == "face_with_tears_of_joy" for r in results)

def test_alias_search():
    results = search("heart")

    assert len(results) > 0

def test_empty_query():
    results = search("")

    assert results == []