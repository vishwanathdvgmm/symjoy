from symjoy import emoji

def test_grouping():
    results = emoji.by_group("emotion")

    assert isinstance(results, list)
    assert len(results) > 0