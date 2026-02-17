![PyPI](https://img.shields.io/pypi/v/symjoy)
![Python](https://img.shields.io/pypi/pyversions/symjoy)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

# Symjoy

A structured, metadata-driven Unicode symbol engine for Python.

**symjoy** provides clean, consistent, and intelligent access to Unicode characters including:

- Emojis 😄
- Symbols ♥
- Arrows →
- Mathematical symbols π
- Currency signs ₹
- Miscellaneous icons ☀

It is designed for chat applications, games, educational tools, financial apps, and any Python project requiring Unicode characters.

---

## ✨ Key Features

- JSON-backed data architecture
- Lazy-loaded registry
- Automatic keyword enrichment
- Semantic relationship graph
- Multilingual alias support
- Deterministic search ordering
- Category-isolated APIs
- Backward compatible with v2.x

---

## 📦 Installation

```bash
pip install symjoy
```

## 🚀 Basic Usage

```Python
from symjoy import emoji, symbols, arrows, math, currency, misc, search

print(emoji.get("smile"))      # 😄
print(symbols.get("heart"))    # ♥
print(arrows.get("right"))     # →
print(math.get("pi"))          # π
print(currency.get("rupee"))   # ₹
print(misc.get("sun"))         # ☀

print(emoji.random())          # Random emoji
```

## 📚 Category API

Each category exposes a consistent interface:

```python
get(name) -> str | None
random() -> str
list() -> list[str]
items() -> dict[str, str]
related(name) -> list[dict]
```

Example:

```python
from symjoy import emoji

print(emoji.list())
print(emoji.related("broken_heart"))
```

## 🔎 Intelligent Search

Search across all categories:

```python
from symjoy import search

results = search("heart")
```

Search is ranked by:

1. Exact match
2. Prefix match
3. Substring match
4. Deterministic category ordering

## 🧠 Metadata Engine (v2.5.0)

v2.5.0 introduces a major internal upgrade:

- JSON-driven data storage
- Runtime metadata enrichment
- Automatic keyword generation
- Token-based semantic relationship graph
- Fully category-agnostic registry

Example:

```python
emoji.related("heart")
search("joy")
```

## Backward Compatibility (v1.x)

Version 2.x still supports legacy v1-style access:

```python
from symjoy import emojis
print(emojis["smile"])
```

⚠️ This usage is deprecated and will be removed in symjoy v3.0.0.

## 📖 Documentation

[📜 Changelog](CHANGELOG.md)

[🔄 Migration Guide](MIGRATION.md)

[🏗 Architecture Overview](ARCHITECTURE.md)

## Project Links

**If any issue with the package you can contact here:**

- **Email:** vishwanathdvgmm@gmail.com

**The source code is available on GitHub**

- **Github:** https://github.com/vishwanathdvgmm/symjoy
- **Github issues:** https://github.com/vishwanathdvgmm/symjoy/issues

**The link for the package in pypi.org is:**

- **Pypi:** https://pypi.org/project/symjoy/

**License: MIT**
