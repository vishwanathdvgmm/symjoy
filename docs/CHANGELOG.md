# Changelog

All notable changes to this project are documented in this file.

The format follows principles from **Keep a Changelog** and adheres to **Semantic Versioning**.

---

## [2.6.0] - 2026-03-07

### Added

- Symbol search index engine.
- Keyword, alias and token indexes for faster lookup.
- Indexed search infrastructure for metadata queries.

### Improved

- Search performance through indexed lookups.
- Registry initialization pipeline.
- Metadata-aware search ranking.

## [2.5.0] - 2026-02-17

### Added

- JSON-driven category architecture.
- Runtime metadata enrichment engine.
- Automatic keyword generation.
- Token-based semantic relationship graph.
- Unified `related()` API across all categories.
- Category-agnostic JSON loader.

### Changed

- Registry fully data-driven.
- All categories migrated to JSON.
- Improved search ranking logic.

### Deprecated

- Legacy dictionary access (`emojis["name"]`)
- Direct category dict usage

---

## [2.1.0] - 2026-01-16

### Added

- Expanded emoji, math, arrows, currency, misc, and symbols datasets.
- Added helper APIs: `exists()` and `info()`.
- Improved search relevance (exact matches first).
- Deterministic API tests.

---

## [2.0.0] - 2026-01-13

### Changed

- Introduced structured v2 API
- Global search support
- Backward compatibility with v1 (deprecated layer added)

---

## [1.0.0] - 2025-09-11

### Added

- Initial release
