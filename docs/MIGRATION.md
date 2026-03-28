# Migration Guide

This document explains how to migrate between major and minor versions of **symjoy**.

---

## Migrating from symjoy 1.0.0 to 2.1.0

symjoy 2.x introduced a structured category-based API while preserving backward compatibility.

### What Changed

- Raw dictionaries replaced by category APIs.
- Global search introduced.
- Metadata (category, unicode) exposed.

### Deprecated Usage

Old style:

```python
from symjoy import emojis
emojis["smile"]
```

New style:

```python
from symjoy import emoji
emoji.get("smile")
```

Deprecated dictionary access will be removed in symjoy v3.0.0.

## Migrating from 2.1.0 to 2.5.0

v2.5.0 introduces a major internal architecture upgrade.

**What Changed Internally**

- All categories are now JSON-backed
- Registry is fully data-driven
- Runtime metadata enrichment added
- Automatic keyword generation
- Token-based semantic relationship graph

**What Did NOT Change**

- Public API remains stable
- No breaking changes
- Existing v2.x code continues to work

## Migrating from 2.5.0 to 2.6.0

v2.6.0 introduces an **indexed search engine** to improve performance.

**What Changed Internally**

- Symbol index engine added.
- Keyword, alias and token indexes created at initialization.
- Search now uses indexed lookups instead of scanning the registry.

**What Did NOT Change**

- The `search()` API remains unchanged.
- All categories APIs remain identical.
- No breaking changes were introduced.

**Performance Impact**

Search operations are now significantly faster because symbol metadata is indexed during initialization rather than scanned during every query.

Example (unchanged usage):

```python
from symjoy import search

search("heart")
search("joy")
```

## Migrating from 2.6.0 to 2.7.0

v2.7.0 introduces **semantic grouping and improved search behavior**.

### New Features

1. **Grouping API**

Symbols are now categorized into semantic groups.

```python
from symjoy import emoji

emoji.by_group("emotion")
```

Available groups include:

- emotion
- gesture
- nature
- object
- activity
- symbolic

2. **Improved Search**

Search now supports:

- multi-token queries
- keyword + alias + token matching
- refined ranking

```python
search("smile face")
search("red heart")
```

### What Changed

- Search results may appear in a different order due to improved ranking.
- Internal grouping metadata (`group`) added to all symbols.

### What Did NOT Change

- Existing APIs (`get`, `list`, `items`, `related`) remain unchanged.
- No breaking changes introduced.
- Existing code continues to work without modification.

### Optional Adoption

You can optionally use the new grouping feature:

```python
emoji.by_group("emotion")
```

No migration is required if you don’t use it.
