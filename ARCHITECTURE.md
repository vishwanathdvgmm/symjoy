# Symjoy Architecture

## Overview

symjoy is a metadata-driven Unicode symbol engine built around a layered architecture.

---

## Layer 1 — Data Layer

Location:

`src/symjoy/data/\*.json`

Each category is stored as JSON:

- emoji.json
- symbols.json
- arrows.json
- math.json
- currency.json
- misc.json

These contain raw symbol definitions.

---

## Layer 2 — Core Engine

Location:

`src/symjoy/core/`

### Registry

- Lazy initialization
- Loads JSON categories
- Builds internal registry
- Applies runtime enrichment
- Resolves duplicates deterministically

### Metadata Enrichment

- Auto-generates keywords from names
- Auto-generates default aliases
- Builds semantic relationship graph

---

## Layer 3 — API Layer

Location:

`src/symjoy/api/`

Each category exposes:

- get()
- list()
- items()
- random()
- related()

API isolates categories while leveraging the shared registry.

---

## Design Principles

- Data-driven architecture
- Separation of concerns
- Lazy loading
- Deterministic behavior
- Backward compatibility
- Future-ready extensibility

---

## Future Directions (v3.x)

- Multi-category membership
- Indexed search engine
- Plugin system
- Unicode database ingestion
- Language packs
