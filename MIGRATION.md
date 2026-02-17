# Migration Guide

## Migrating from symjoy 1.0.0 to 2.1.0

symjoy 2.x introduced a structured category-based API while preserving backward compatibility.

### What Changed

- Raw dictionaries replaced by category APIs
- Global search introduced
- Metadata (category, unicode) exposed

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

Deprecated dict access will be removed in v3.0.0.

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
