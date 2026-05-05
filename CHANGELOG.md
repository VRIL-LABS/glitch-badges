# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] — 2026

### Added

- **README.md**: PyPI and Crates.io package badges, each linked to the respective registry package page.
- **LICENSE**: Added `LICENSE` file to `packages/rs/` (Rust crate) and `packages/js/` (npm package) so all three registry releases include the license.

### Changed

- All three registry packages (`npm`, `pypi`, `crates.io`) bumped to `1.0.1` to stay in sync.

---

## [1.0.0] — 2024

### Added

- **133 animated glitch badges** across 4 collections: `social` (31 SVGs), `comms` (36 SVGs), `repo` (66 SVGs), `status` (24 SVGs).
- `badge_generator.py` — standalone Python factory script (all / per-collection / custom modes).
- **TypeScript/React/Node SDK** — `packages/js/` → published to npm as `glitch-badges`.
  - Core SVG generator (`makeBadge`, `badgeUrl`, `badgeImg`)
  - React components (`GlitchBadge`, `GlitchBadgeImg`, `GlitchBadgeFromPreset`)
  - Full preset library for all badge slugs
  - CLI: `npx glitch-badges custom|url|list`
- **Python SDK** — `packages/py/` → `glitch-badges` on PyPI.
  - Library API (`make_badge`, `badge_url`, `badge_img`, presets)
  - CLI: `glitch-badges custom|url|list`
- **Rust crate** — `packages/rs/` → `glitch-badges` on crates.io.
  - Library API (`make_badge`, `badge_url`, `badge_img`)
  - CLI binary
- CI/CD workflows: `ci.yml` (test all SDKs), `publish-npm.yml`, `publish-pypi.yml`, `publish-crates.yml`.
- `LICENSE` (MIT), `CONTRIBUTING.md`, `CHANGELOG.md`.
