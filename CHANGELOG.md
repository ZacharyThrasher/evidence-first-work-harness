# Changelog

## Unreleased

### Fixed
- Made `docs/` the exclusive GitHub Pages web root with pre-rendered `index.html`, `quickstart.html`, and `reasoning.html`.
- Moved editable reasoning/design Markdown outside the Pages root so site navigation cannot fall through to raw Markdown.
- Added `docs/.nojekyll` for deterministic static hosting.

## 2.1.0 — 2026-09-14

Company-ready distribution release.

### Changed
- Made `.claude/skills/efwh/` the single canonical protocol/distribution copy.
- Made `/efwh` explicitly user-invocable only with `disable-model-invocation: true`.
- Added zero-edit personal installers and organization rollout guidance.
- Updated the visual guide for GitHub distribution and retained minimal creator attribution.

### Added
- Company rollout runbook.
- Security, support, contribution, ownership, PR, issue, and release-checklist guidance.
- Structural CI validation with no third-party Python dependencies.
- Repository-level architecture and release documentation.

## 2.0.0 — 2026-09-14

Introduced the zero-edit `/efwh` Agent Skill UX, adaptive autonomy/rigor, visual guide, and self-initializing per-problem `.efwh/` state.
