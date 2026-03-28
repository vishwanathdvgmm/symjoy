# Symjoy Architecture

## Overview

symjoy is a metadata-driven Unicode symbol engine built around a layered architecture designed for:

- extensibility.
- performance.
- deterministic behavior.
- clean API boundaries.

# Architecture Layers

symjoy is organized into **six logical layers**:

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

- `emoji.json`
- `symbols.json`
- `arrows.json`
- `math.json`
- `currency.json`
- `misc.json`

These files contain the **raw symbol definitions + metadata**.

Example:

```json
{
	"name": "heart",
	"char": "❤️",
	"keywords": ["heart", "love"],
	"aliases": { "en": ["red heart"] },
	"group": "symbolic"
}
```

### Responsibilities

- Source of truth for all symbols.
- No logic - Pure data layer.
- Easily extensible without code changes.

---

## Layer 2 — Registry Layer

Location:

`src/symjoy/core/registry.py`

### Responsibilities

- Lazy initialization.
- Load JSON categories.
- Register symbols into a unified registry.
- Provide lookup APIs.

### Core Structure

Each symbol is represented as:

```Plain text
SymbolNode
```

Fields:

- name
- char
- category
- unicode
- keywords
- aliases
- related
- group

The registry is the **central in-memory representation** of all symbols.

---

## Layer 3 — Metadata Enrichment Layer

Runs immediatetly after registry load.

### Responsibilities:

- Generate missing keywords.
- Normalize aliases.
- Build sematic relationships.
- Preserve grouping metadata.

### Behavior

Example:

```python
face_with_tears_of_joy
→ keywords: ["tears", "joy"]
```

Relationships are computed via **shared keyword tokens**.

---

## Layer 4 — Index Engine (v2.6)

Location:

`src/symjoy/core/index.py`

The index engine builds internal lookup structures to accelerate search queries.

Indexes created:

| Index         | Purpose               |
| ------------- | --------------------- |
| Name index    | direct lookup         |
| Keyword index | keyword → symbols     |
| Alias index   | alias → symbols       |
| Token index   | tokenized name lookup |

Example:

```python
keyword_index["heart"] → ["heart", "red_heart"]
```

### Purpose

- Avoid full registry scans.
- Enable scalable search performance.

---

## Layer 5 — Search Engine

Location:
`src/symjoy/core/search.py`

### Responsibilities:

- Query index engine.
- Merge candidate sets.
- Rank results deterministically.

### Ranking priority (v2.7):

1. Exact name match
2. Keyword match
3. Alias match
4. Token match
5. Fallback

### Behavior

- Uses **indexed lookups only**
- Supports **multi-token queries**
- Deterministic ordering:

```python
(key_rank, category, name)
```

---

## Layer 6 — API Layer

Location:

`src/symjoy/api/`

Provides category-specific interfaces.

### Categories:

- emoji
- symbols
- arrows
- math
- currency
- misc

### API Surface:

```python
get()
random()
list()
items()
related()
exists()
info()
by_group()
```

Example:

```python
from symjoy import emoji

emoji.get("smile")
emoji.by_group("emotion")
```

### Role

- Thin abstraction over registry.
- Category isolation.
- Consistent developer experience.

---

## Design Principles

**Data-driven architecture**

All symbol originate from JSON.

**Separation of concerns**

Each layer has a specific responsibility.

**Lazy Initialization**

Registry loads only when required.

**Deterministic behavior**

Search and outputs are stable.

**Performance-Oriented**

Index engine prevents O(n) scans.

**Backward compatibility**

Legacy dictionary access supported until v3.0.

---

## Future Directions (v3.x)

Planned enhancements:

- Plugin system (external symbol packs).
- Unicode database ingestion.
- Language packs for aliases.
- CLI interface (symjoy search).
- Fuzzy search (Levenshtein distance).
- Advanced Ranking models.
