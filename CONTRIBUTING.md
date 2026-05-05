# Contributing to glitch-badges

Thank you for considering a contribution! This document explains the conventions and workflow.

## Repository layout

```
glitch-badges/
├── badge_generator.py              ← Python generator (root, self-contained)
├── .github/profile/assets/badges/ ← 157 pre-built SVGs (auto-generated)
│   ├── social/    (31 SVGs)
│   ├── comms/     (36 SVGs)
│   ├── repo/      (66 SVGs)
│   └── status/    (24 SVGs)
├── packages/
│   ├── js/        ← TypeScript / React / Node SDK  → npm: glitch-badges
│   ├── py/        ← Python SDK                     → PyPI: glitch-badges
│   └── rs/        ← Rust crate                     → crates.io: glitch-badges
└── .github/workflows/
    ├── ci.yml            ← runs on every push/PR
    ├── publish-npm.yml   ← triggers on v* tag
    ├── publish-pypi.yml  ← triggers on v* tag
    └── publish-crates.yml← triggers on v* tag
```

## Development setup

### JavaScript / TypeScript

```bash
cd packages/js
npm install
npm run build    # or: npm run dev  (watch mode)
```

### Python

```bash
cd packages/py
pip install -e .
glitch-badges --help
```

### Rust

```bash
cd packages/rs
cargo build
cargo test
```

## Adding a badge

1. Open `badge_generator.py` and add an entry to the relevant `SOCIAL`, `COMMS`, or `REPO` list.
2. Run the generator to produce the SVGs:
   ```bash
   python badge_generator.py all --out .github/profile/assets/badges
   ```
3. Mirror the new preset in **all three SDKs**:
   - `packages/js/src/presets.ts`
   - `packages/py/glitch_badges/presets.py`
   - (optional but appreciated) `packages/rs/src/lib.rs` — the Rust crate currently contains the generator only
4. Update `README.md` — add a row to the appropriate catalog table.
5. Open a PR.

## Releasing a new version

1. Bump `version` in `packages/js/package.json`, `packages/py/pyproject.toml`, `packages/rs/Cargo.toml`.
2. Update `CHANGELOG.md`.
3. Push a `v<semver>` tag (e.g. `v1.1.0`).  
   CI will automatically publish to npm, PyPI, and crates.io.

## Code style

| Stack      | Formatter        | Linter       |
|------------|------------------|--------------|
| TypeScript | (none enforced)  | tsc --strict |
| Python     | (none enforced)  | PEP 8        |
| Rust       | `cargo fmt`      | `cargo clippy` |

## License

By contributing you agree that your work will be released under the [MIT License](LICENSE).
