# Changelog

All notable changes to this project are documented in this file.

The format follows principles from **Keep a Changelog** and adheres to **Semantic Versioning**.

---

## [2.7.0] - 2026-03-28

### Added

- Semantic grouping system (`group` field in data layer).
- `by_group()` API across all categories.
- Multi-token search support.
- Improved test coverage for grouping and search.
- CI automation via GitHub Actions.

### Changed

- Search engine upgraded to use indexed keyword, alias, and token matching.
- Deterministic ranking refined:
    - exact → keyword → alias → token.
- Registry enrichment pipeline updated to preserve `group` metadata.
- API consistency improvements across all category modules.

### Fixed

- Incorrect `by_group()` implementation in category APIs.
- `emoji.related()` returning empty results due to logic error.
- Case normalization issues in search and indexing.

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

- Legacy dictionary access (`emojis["name"]`).
- Direct category dict usage.

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

- Introduced structured v2 API.
- Global search support.
- Backward compatibility with v1 (deprecated layer added).

---

## [1.0.0] - 2025-09-11

### Added

- Initial release.
