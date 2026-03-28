from symjoy import emoji, symbols, arrows, math, currency, misc

def test_emoji_get():
    assert emoji.get("face_with_tears_of_joy") is not None

def test_symbol_get():
    assert symbols.get("heart") is not None

def test_arrow_get():
    assert arrows.get("left") is not None

def test_math_get():
    assert math.get("pi") is not None

def test_currency_get():
    assert currency.get("rupee") is not None

def test_misc_get():
    assert misc.get("sun") is not None

def test_random_emoji():
    assert emoji.random() is not None

def test_related():
    related = emoji.related("heart")
    assert isinstance(related, list)