# Symjoy

**symjoy** is a comprehensive Python package providing easy access to Unicode characters, including **emojis, symbols, arrows, mathematical symbols, currency signs, and miscellaneous icons**. Perfect for chat apps, games, educational tools, financial apps, or any Python project requiring Unicode characters.

Version 2.x introduces a clean, discoverable API while maintaining backward compatibility
with version 1.x.

## Installation

Install from PyPI:

```bash
pip install symjoy
```

## Usage

#### 1. Quick Start (v2 API)

```
from symjoy import emoji, symbols, arrows, math, currency, misc, search

print(emoji.get("smile"))      # 😄
print(symbols.get("heart"))    # ♥
print(arrows.get("right"))     # →
print(math.get("pi"))          # π
print(currency.get("rupee"))   # ₹
print(misc.get("sun"))         # ☀

print(emoji.random())          # random emoji
```

#### 2. Category APIs

Each category exposes the same interface:

```
get(name)      -> str | None
random()       -> str
list()         -> list[str]
items()        -> dict[str, str]
```

##### **Example**

```
from symjoy import emoji

emoji.list()
emoji.items()
```

#### 3. Global Search

Search across all categories:

```
from symjoy import search

results = search("heart")
```

Expected results:

```
[
  {
    "name": "heart",
    "char": "♥",
    "category": "symbols",
    "unicode": "U+2665"
  }
]
```

#### 4. Backward Compatibility (v1.x)

Version 2.x still supports v1-style access:

```
from symjoy import emojis
print(emojis["smile"])
```

⚠️ This usage is deprecated and will be removed in symjoy 3.0.0.

## Github Link

**If any issue with the package you can contact here:**

-   **Email:** vishwanathdvgmm@gmail.com

**The source code is available on GitHub**

-   **Github:** https://github.com/vishwanathdvgmm/symjoy
