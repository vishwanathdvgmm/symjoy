from symjoy import search

def test_keywords_index():
    results = search("joy")
    assert len(results) > 0

def test_aliases_index():
    results = search("heart")
    assert len(results) > 0

def test_tokens_index():
    results = search("face_with_tears_of_joy")
    assert len(results) > 0