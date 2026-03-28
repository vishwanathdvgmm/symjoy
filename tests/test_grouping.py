from symjoy import emoji

def test_grouping():
    results = emoji.by_group("emotion")

    assert isinstance(results, list)
    assert len(results) > 0
    assert all("name" in r and "char" in r for r in results)