# Symjoy Architecture

## Overview

symjoy is a metadata-driven Unicode symbol engine built around a layered architecture designed for ease of use and extensibility, performance and deterministic behavior.

# Architecture Layers

symjoy is organized into sux logical layers:

1. Data Layer
2. Registry Layer
3. Metadata Enrichment Layer
4. Index Engine Layer
5. Search Engine Layer
6. API Layer

---

## Layer 1 — Data Layer

Location:

`src/symjoy/data/*.json`

Each category is stored as JSON:

- emoji.json
- symbols.json
- arrows.json
- math.json
- currency.json
- misc.json

These files contain the **raw symbol definitions**.

Example entry:

```json
{
	"name": "heart",
	"char": "❤️"
}
```

This design allows new symbols to be added without modifying the codebase.

---

## Layer 2 — Registry Layer

Location:

`src/symjoy/core/registry.py`

### Responsibilities

- Lazy initialization.
- Loads categories JSON files.
- Register symbols internally.
- Build the unified symbol registry.
- Provide lookup APIs for symbols.

Registry output:

```text
SymbolNode
```

Each node conatins:

- name
- char
- category
- unicode
- keywords
- aliases
- related symbols

---

## Layer 3 — Metadata Enrichment Layer

After symbols are registerd, metadata enrichment runs.

Responsibilities:

- Auto-generate keywords from symbol names.
- Generate default aliases.
- Build sematic relationships between symbols.

Example:

```python
face_with_tears_of_joy
→ keywords: ["tears", "joy"]
```

Relationships are built by matching shared keyword tokens.

---

## Layer 4 — Index Engine (v2.6)

Location:

`src/symjoy/core/index.py`

The index engine builds internal lookup structures to accelerate search queries.

Indexes created:

| Index         | Purpose               |
| ------------- | --------------------- |
| Name index    | direct symbol lookup  |
| Keyword index | keyword → symbols     |
| Alias index   | alias → symbols       |
| Token index   | tokenized name lookup |

Example:

```python
keyword_index["heart"] → ["heart", "red_heart", "black_heart"]
```

This allows the search engine to avoid scanning the entire registry.

## Layer 5 — Search Engine

Location:
`src/symjoy/core/search.py`

Responsibilities:

- Query the index engine
- Rank search results
- Return deterministic symbol results

Search ranking priority:

1. Exact name match
2. Prefix name match
3. Keyword match
4. Alias match
5. Substring fallback

Example:

```python
from symjoy import search

search("heart")
search("joy")
```

## Layer 6 — API Layer

Location:

`src/symjoy/api/`

The API layer provides category-specific interfaces.

Categories:

- emoji
- symbols
- arrows
- math
- currency
- misc

Each category exposes:

```python
get()
random()
list()
items()
related()
exists()
info()
```

The API layer isolates categories while using the shared registry.

## Design Principles

symjoy follows several key architectural principles:

**Data-driven architecture**

All symbol definitions come from JSON data.

**Separation of concerns**

Each layer handles a specific responsibility.

**Lazy loading**

Registry initialization occurs only when needed.

**Deterministic behavior**

Search results are consistently ordered.

**Performance-aware design**

The index engine ensures search remains fast as the dataset grows.

**Backward compatibility**

Legacy dictionary access remains available until v3.0.

---

## Future Directions (v3.x)

Planned architectural expansions include:

- Plugin system for external symbol packs
- Unicode database ingestion
- Language packs for multilingual aliases
- CLI interface (symjoy search)
- Advanced fuzzy search
