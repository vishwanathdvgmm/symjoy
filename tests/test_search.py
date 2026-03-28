from symjoy import search

def test_exact_search():
    results = search("grinning_face")

    assert len(results) > 0
    assert results[0]["name"] == "grinning_face"

def test_multi_token_search():
    results = search("smile face")

    assert len(results) > 0

def test_case_insensitive():
    from symjoy import emoji

    assert emoji.get("GRINNING_FACE") == emoji.get("grinning_face")

def test_keyword_search():
    results = search("joy")

    assert any("joy" in r["name"] for r in results)

def test_alias_search():
    results = search("heart")

    assert len(results) > 0

def test_empty_query():
    results = search("")

    assert results == []

def test_related_invalid():
    from symjoy import emoji

    assert emoji.related("") == []