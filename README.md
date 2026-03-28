![PyPI](https://img.shields.io/pypi/v/symjoy)
![Python](https://img.shields.io/pypi/pyversions/symjoy)
![License](https://img.shields.io/badge/license-MIT-blue.svg)<br>
![Downloads](https://img.shields.io/pypi/dm/symjoy)
![Status](https://img.shields.io/badge/status-active-success)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

# ✨Symjoy - Unicode Engine for Python

| Version | Highlights                              |
| ------- | --------------------------------------- |
| v2.7.0  | Grouping API + search improvements + CI |
| v2.6.0  | Indexed search engine                   |
| v2.5.0  | Metadata-driven architecture            |
| v2.1.0  | Helper APIs & improved search           |
| v2.0.0  | Structured category API                 |

A **metadata-driven Unicode symbol engine** for Python.

**Symjoy** provides clean, structured, and intelligent access to Unicode characters including:

- Emojis 😄
- Symbols ❤️
- Arrows →
- Mathematical symbols π
- Currency signs ₹
- Miscellaneous icons ☀️

Designed for:

- 💬Chat applications
- 🎮 Games
- 📚Educational tools
- 💰 Financial systems
- ⚙️ Developer utilities

---

## ✨ Key Features

- JSON-backed data architecture.
- Lazy-loaded registry.
- Automatic keyword enrichment.
- Semantic relationship graph.
- Multilingual alias support.
- ⚡**Indexed search engine**.
- Deterministic search ordering.
- Category-isolated APIs.
- Backward compatible with v2.x.

---

## 📦 Installation

```bash
pip install symjoy
```

Required Python version: **3.12+**

## 🚀 Basic Usage

```Python
from symjoy import emoji, symbols, arrows, math, currency, misc, search

print(emoji.get("smile"))      # 😄
print(symbols.get("heart"))    # ❤️
print(arrows.get("right"))     # →
print(math.get("pi"))          # π
print(currency.get("rupee"))   # ₹
print(misc.get("sun"))         # ☀️

print(emoji.random())          # Random emoji
```

## 📚 Category API

Each category exposes a consistent interface:

```python
get(name) -> str | None
exists(name) -> bool
info(name) -> dict | None
random() -> str | None
list() -> list[str]
items() -> dict[str, str]
related(name) -> list[dict]
by_group(group) -> list[dict]
```

Example:

```python
from symjoy import emoji

print(emoji.list())
print(emoji.related("heart"))
print(emoji.by_group("emotion"))
```

## 🔎 Intelligent Search

Search across all categories:

```python
from symjoy import search

results = search("heart")
```

### Ranking Strategy

Search is ranked by:

1. Exact match.
2. Keyword match.
3. Alias match.
4. Token match.

### Multi-token Support

```python
search("smile face")
search("red heart")
```

## 🧠 Metadata Engine (v2.5.0)

Introduced a fully data-driven system::

- JSON-driven data storage
- Runtime metadata enrichment
- Automatic keyword generation
- Token-based relationship graph
- Category-agnostic registry

```python
emoji.related("heart")
search("joy")
```

## ⚡ Indexed Search Engine (v2.6.0)

Introduces internal indexing for high-performance queries.

### Indexed Fields

- Names.
- Keywords.
- Aliases.
- Tokens.

### Benefits:

- Faster lookups.
- Scalable architecture.
- Reduced full-registry scans.
- Improved query precision.

## 🚀 Grouping & Search Improvements (v2.7.0)

v2.7.0 introduces **semantic grouping and enhanced search capabilities**.

### 🧩 Grouping API

Symbols are now organized into semantic groups:

- emotion
- gesture
- nature
- object
- activity
- symbolic

```python
from symjoy import emoji

emoji.by_group("emotion")
```

### 🔍 Improved Search Engine

Search now supports:

- multi-token queries
- keyword + alias + token indexing
- deterministic ranking

```python
search("smile face")
search("red heart")
```

### ⚙️ Developer Improvements

- CI automation (GitHub Actions)
- Improved test coverage
- Stabilized registry + index pipeline

## 🔁 Backward Compatibility (v1.x)

Version 2.x still supports legacy v1-style access:

```python
from symjoy import emojis
print(emojis["smile"])
```

⚠️ This usage is deprecated and will be removed in symjoy v3.0.0.

## 📖 Documentation

[📜 Changelog](https://github.com/vishwanathdvgmm/symjoy/blob/main/docs/CHANGELOG.md)

[🔄 Migration Guide](https://github.com/vishwanathdvgmm/symjoy/blob/main/docs/MIGRATION.md)

[🏗 Architecture Overview](https://github.com/vishwanathdvgmm/symjoy/blob/main/docs/ARCHITECTURE.md)

[📁 File Structure](https://github.com/vishwanathdvgmm/symjoy/blob/main/docs/STRUCTURE.md)

## Project Links

- **Pypi:** https://pypi.org/project/symjoy/
- **Github:** https://github.com/vishwanathdvgmm/symjoy
- **Github issues:** https://github.com/vishwanathdvgmm/symjoy/issues
- **Email:** vishwanathdvgmm@gmail.com

## License

**MIT License**
