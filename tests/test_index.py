from symjoy import search

def test_keywords_index():
    results = search("joy")
    assert any(r["name"] == "joy" for r in results)

def test_aliases_index():
    results = search("heart")
    assert any("heart" in r["name"] for r in results)

def test_tokens_index():
    results = search("smile")
    assert any(r["name"] == "smile" for r in results)