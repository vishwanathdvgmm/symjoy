from symjoy import emoji, symbols, arrows, math, currency, misc

def test_emoji_get():
    assert emoji.get("smile") == "😄"

def test_symbol_get():
    assert symbols.get("heart") == "♥"

def test_arrow_get():
    assert arrows.get("left") == "←"

def test_math_get():
    assert math.get("pi") == "π"

def test_currency_get():
    assert currency.get("rupee") == "₹"

def test_misc_get():
    assert misc.get("sun") == "☀"

def test_random_emoji():
    assert emoji.random() is not None

def test_related():
    related = emoji.related("heart")

    assert isinstance(related, list)