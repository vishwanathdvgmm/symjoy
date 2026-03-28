from symjoy.core.registry import (
    get_symbol,
    list_categories,
    list_by_category,
    get_related,
)

def test_symbol_lookup():
    node = get_symbol("heart")

    assert node is not None
    assert node.char == "♥"
    assert node.category == "symbols"

def test_categories_exist():
    categories = list_categories()

    assert isinstance(categories, list)
    assert len(categories) > 0

def test_list_by_category():
    emojis = list_by_category("emoji")

    assert isinstance(emojis, list)
    assert len(emojis) > 0

def test_related_symbols():
    related = get_related("heart")

    assert isinstance(related, list)