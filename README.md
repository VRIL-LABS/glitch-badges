<div align="center">
<img src=".github/profile/assets/header.svg" width="900" alt="glitch-badges by VRIL LABS"/>
</div>

<div align="center">

[![CI](https://github.com/dubzrn/glitch-badges/actions/workflows/ci.yml/badge.svg)](https://github.com/dubzrn/glitch-badges/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/glitch-badges?color=%231fe8a8&label=npm)](https://www.npmjs.com/package/glitch-badges)
[![PyPI](https://img.shields.io/pypi/v/glitch-badges?color=%231fe8a8&label=pypi)](https://pypi.org/p/glitch-badges)
[![Crates.io](https://img.shields.io/crates/v/glitch-badges?color=%231fe8a8&label=crates.io)](https://crates.io/crates/glitch-badges)
[![License: MIT](https://img.shields.io/badge/license-MIT-1fe8a8.svg)](LICENSE)

</div>

> **133 animated glitch badges** across 4 collections — VRIL LABS phosphor-seafoam palette, chromatic-aberration glitch animation, CRT scanlines, corner bracket decorators.  
> All derived programmatically from a single `badge-glitch.svg` DNA.

---

## Badge Architecture

Every badge inherits the exact same DNA:

| Property | Value |
|---|---|
| Background | `#0b0c0b` void |
| Border | `#1a2a24` |
| Glitch | Chromatic aberration — red channel shifts left, cyan shifts right, `steps(1)` animation |
| Scanlines | 4 px repeating phosphor grid, synchronized flicker |
| Corners | CSS `border-width` bracket decorators |
| Accent seam | Top-edge `linear-gradient` pulse |

---

## The Collections

| Collection | Badges | Sizes | Notes |
|---|---|---|---|
| **Social** (`/social`) | 12 platforms + extras | 200 px + 280 px | Twitter, Instagram, YouTube, LinkedIn, GitHub, TikTok, Mastodon, Bluesky… |
| **Comms** (`/comms`) | 14 platforms + extras | 220 px + 310 px | Discord, Telegram, Matrix, Slack, Signal, WhatsApp, Keybase… |
| **Repo** (`/repo`) | 33 types | 220 px + 290 px | Status, License, Build, Security, Contrib, Version, Lang, Platform |
| **Status** (`/status`) | 24 standalone | 220 px | PQ-ready, passing, failing, coverage, downloads… |

---

## Quick-Start: Drop a Badge into any README

```markdown
<!-- Standard size -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq.svg" width="220" height="34" alt="Post-Quantum"/>

<!-- Wide variant -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq-wide.svg" width="290" height="34" alt="Post-Quantum"/>

<!-- Wrap in a link -->
[![Post-Quantum](https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq.svg)](https://github.com/dubzrn/glitch-badges)
```

---

## Badge Gallery

> Live preview — every badge rendered from `raw.githubusercontent.com`. Click any badge to copy its URL from the [catalog](#badge-catalog) below.

<p align="center"><b>Social Media</b></p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/twitter.svg" width="200" height="34" alt="Twitter"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/instagram.svg" width="190" height="52" alt="Instagram"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/youtube.svg" width="180" height="52" alt="YouTube"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/linkedin.svg" width="180" height="52" alt="LinkedIn"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/bluesky.svg" width="170" height="52" alt="Bluesky"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/mastodon.svg" width="180" height="52" alt="Mastodon"/>
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/twitter-wide.svg" width="280" height="38" alt="Twitter Wide"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/bluesky-wide.svg" width="280" height="38" alt="Bluesky Wide"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/sponsor-wide.svg" width="280" height="38" alt="Sponsor Wide"/>
</p>

<p align="center"><b>Communications</b></p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/discord.svg" width="180" height="52" alt="Discord"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/telegram.svg" width="185" height="52" alt="Telegram"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/signal.svg" width="220" height="34" alt="Signal"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/slack.svg" width="195" height="52" alt="Slack"/>
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/matrix.svg" width="180" height="52" alt="Matrix"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/email.svg" width="160" height="52" alt="Email"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/comms/discord-wide.svg" width="310" height="38" alt="Discord Wide"/>
</p>

<p align="center"><b>Repository Status</b></p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/status-stable.svg" width="220" height="34" alt="Stable"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/status-wip.svg" width="220" height="34" alt="WIP"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/build-passing.svg" width="220" height="34" alt="Build Passing"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/build-failing.svg" width="220" height="34" alt="Build Failing"/>
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq.svg" width="220" height="34" alt="Post-Quantum"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-encrypted.svg" width="220" height="34" alt="Encrypted"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/license-mit.svg" width="220" height="34" alt="MIT"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/contrib-welcome.svg" width="220" height="34" alt="PRs Welcome"/>
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/lang-python.svg" width="220" height="34" alt="Python"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/lang-rust.svg" width="220" height="34" alt="Rust"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/lang-nodejs.svg" width="220" height="34" alt="Node.js"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/lang-go.svg" width="220" height="34" alt="Go"/>
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq-wide.svg" width="290" height="34" alt="Post-Quantum Wide"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/status-stable-wide.svg" width="290" height="34" alt="Stable Wide"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/build-passing-wide.svg" width="290" height="34" alt="Build Passing Wide"/>
</p>

<p align="center"><b>Standalone Status</b></p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/pq-ready.svg" width="188" height="38" alt="PQ Ready"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/status-passing.svg" width="155" height="38" alt="Passing"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/status-stable.svg" width="148" height="38" alt="Stable"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/open-source.svg" width="172" height="38" alt="Open Source"/>
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/contributing.svg" width="182" height="38" alt="Contributing"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/security.svg" width="158" height="38" alt="Security"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/downloads.svg" width="155" height="38" alt="Downloads"/>&#160;
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/coverage.svg" width="178" height="38" alt="Coverage"/>
</p>

---

## SDK Integrations

### TypeScript / React / Node.js

[![npm](https://img.shields.io/npm/v/glitch-badges?color=%231fe8a8)](https://www.npmjs.com/package/glitch-badges)

```bash
npm install glitch-badges
```

**Generate a badge SVG (Node.js / server-side)**

```typescript
import { makeBadge, badgeUrl } from "glitch-badges";

// Generate SVG string
const svg = makeBadge({
  text:   "POST QUANTUM",
  accent: "#a78bfa",
  tag:    "Security",
  width:  260,
});
fs.writeFileSync("security-pq.svg", svg);

// Get CDN URL for pre-built badge
const url = badgeUrl("repo", "security-pq", /* wide */ true);
```

**React component**

```tsx
import { GlitchBadge, GlitchBadgeImg } from "glitch-badges/react";

// Inline SVG (no network request)
<GlitchBadge text="POST QUANTUM" accent="#a78bfa" tag="Security" width={260} />

// Pre-built badge from CDN
<GlitchBadgeImg collection="repo" slug="security-pq" alt="Post-Quantum" wide />
```

**CLI**

```bash
# One-off custom badge
npx glitch-badges custom "POST QUANTUM" --accent "#a78bfa" --tag "Security" --width 260

# Get CDN URL
npx glitch-badges url repo security-pq --wide

# List all slugs
npx glitch-badges list
npx glitch-badges list repo
```

---

### Python

```bash
pip install glitch-badges
```

```python
from glitch_badges import make_badge, badge_url, get_preset

# Generate SVG
svg = make_badge("POST QUANTUM", accent="#a78bfa", tag="Security", width=260)
open("security-pq.svg", "w").write(svg)

# CDN URL
url = badge_url("repo", "security-pq", wide=True)

# Lookup preset
p = get_preset("twitter")   # → Preset(slug='twitter', accent='#1DA1F2', ...)
```

**CLI**

```bash
glitch-badges custom "POST QUANTUM" --accent "#a78bfa" --tag "Security"
glitch-badges url repo security-pq --wide
glitch-badges list
```

**Or use the self-contained root-level generator** (no install required):

```bash
# Regenerate all 133 badges
python badge_generator.py all --out .github/profile/assets/badges

# One collection only
python badge_generator.py repo --out ./assets

# One-off custom badge
python badge_generator.py custom "POST QUANTUM" --accent "#a78bfa" --tag "Security" --width 260
```

---

### Rust

[![crates.io](https://img.shields.io/crates/v/glitch-badges?color=%231fe8a8)](https://crates.io/crates/glitch-badges)

```toml
# Cargo.toml
[dependencies]
glitch-badges = "1"
```

```rust
use glitch_badges::{BadgeOptions, make_badge, badge_url};

// Generate SVG
let svg = make_badge(BadgeOptions {
    text:   "POST QUANTUM".into(),
    accent: "#a78bfa".into(),
    tag:    Some("Security".into()),
    width:  260,
    ..Default::default()
});
std::fs::write("security-pq.svg", svg).unwrap();

// CDN URL
let url = badge_url("repo", "security-pq", true);
```

**CLI binary**

```bash
glitch-badges custom "POST QUANTUM" --accent "#a78bfa" --tag Security
glitch-badges url repo security-pq --wide
```

---

## Badge Catalog

> Two size variants per badge: standard (no suffix) and wide (`-wide`).  
> All URLs point to this repository's raw SVGs on GitHub.

**Base URL:** `https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/`

---

### 1 · Social Media Badges

Path: `.github/profile/assets/badges/social/`

| Badge | Standard `<img>` | Wide `<img>` |
|---|---|---|
| Twitter | `<img src="...social/twitter.svg" width="200" height="34" alt="Twitter"/>` | `<img src="...social/twitter-wide.svg" width="280" height="38" alt="Twitter"/>` |
| X | `<img src="...social/x.svg" width="200" height="34" alt="X"/>` | `<img src="...social/x-wide.svg" width="280" height="38" alt="X"/>` |
| Instagram | `<img src="...social/instagram.svg" width="200" height="34" alt="Instagram"/>` | `<img src="...social/instagram-wide.svg" width="280" height="38" alt="Instagram"/>` |
| LinkedIn | `<img src="...social/linkedin.svg" width="200" height="34" alt="LinkedIn"/>` | `<img src="...social/linkedin-wide.svg" width="280" height="38" alt="LinkedIn"/>` |
| YouTube | `<img src="...social/youtube.svg" width="200" height="34" alt="YouTube"/>` | `<img src="...social/youtube-wide.svg" width="280" height="38" alt="YouTube"/>` |
| TikTok | `<img src="...social/tiktok.svg" width="200" height="34" alt="TikTok"/>` | `<img src="...social/tiktok-wide.svg" width="280" height="38" alt="TikTok"/>` |
| Mastodon | `<img src="...social/mastodon.svg" width="200" height="34" alt="Mastodon"/>` | `<img src="...social/mastodon-wide.svg" width="280" height="38" alt="Mastodon"/>` |
| Bluesky | `<img src="...social/bluesky.svg" width="200" height="34" alt="Bluesky"/>` | `<img src="...social/bluesky-wide.svg" width="280" height="38" alt="Bluesky"/>` |
| Share | `<img src="...social/share.svg" width="200" height="34" alt="Share"/>` | `<img src="...social/share-wide.svg" width="280" height="38" alt="Share"/>` |
| Star | `<img src="...social/star.svg" width="200" height="34" alt="Star"/>` | `<img src="...social/star-wide.svg" width="280" height="38" alt="Star"/>` |
| Sponsor | `<img src="...social/sponsor.svg" width="200" height="34" alt="Sponsor"/>` | `<img src="...social/sponsor-wide.svg" width="280" height="38" alt="Sponsor"/>` |
| Newsletter | `<img src="...social/newsletter.svg" width="200" height="34" alt="Newsletter"/>` | `<img src="...social/newsletter-wide.svg" width="280" height="38" alt="Newsletter"/>` |

<details><summary>Expand full-URL copy-paste snippets</summary>

```markdown
<!-- Twitter -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/twitter.svg" width="200" height="34" alt="Twitter"/>
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/twitter-wide.svg" width="280" height="38" alt="Twitter"/>

<!-- Instagram -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/instagram.svg" width="200" height="34" alt="Instagram"/>

<!-- LinkedIn -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/linkedin.svg" width="200" height="34" alt="LinkedIn"/>

<!-- YouTube -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/youtube.svg" width="200" height="34" alt="YouTube"/>

<!-- GitHub (social) -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/github.svg" width="200" height="34" alt="GitHub"/>

<!-- Mastodon -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/mastodon.svg" width="200" height="34" alt="Mastodon"/>

<!-- Bluesky -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/bluesky.svg" width="200" height="34" alt="Bluesky"/>

<!-- Sponsor -->
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/sponsor.svg" width="200" height="34" alt="Sponsor"/>
```

</details>

**Wrap in a link:**
```markdown
[![Twitter](https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/twitter.svg)](https://twitter.com/yourhandle)
[![Bluesky](https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/social/bluesky-wide.svg)](https://bsky.app/profile/yourhandle)
```

---

### 2 · Communication Platform Badges

Path: `.github/profile/assets/badges/comms/`

| Badge | Standard `<img>` | Wide `<img>` |
|---|---|---|
| Discord | `<img src="...comms/discord.svg" width="220" height="34" alt="Discord"/>` | `<img src="...comms/discord-wide.svg" width="310" height="38" alt="Discord"/>` |
| GitHub | `<img src="...comms/github.svg" width="220" height="34" alt="GitHub"/>` | `<img src="...comms/github-wide.svg" width="310" height="38" alt="GitHub"/>` |
| Telegram | `<img src="...comms/telegram.svg" width="220" height="34" alt="Telegram"/>` | `<img src="...comms/telegram-wide.svg" width="310" height="38" alt="Telegram"/>` |
| Slack | `<img src="...comms/slack.svg" width="220" height="34" alt="Slack"/>` | `<img src="...comms/slack-wide.svg" width="310" height="38" alt="Slack"/>` |
| Matrix | `<img src="...comms/matrix.svg" width="220" height="34" alt="Matrix"/>` | `<img src="...comms/matrix-wide.svg" width="310" height="38" alt="Matrix"/>` |
| Signal | `<img src="...comms/signal.svg" width="220" height="34" alt="Signal"/>` | `<img src="...comms/signal-wide.svg" width="310" height="38" alt="Signal"/>` |
| WhatsApp | `<img src="...comms/whatsapp.svg" width="220" height="34" alt="WhatsApp"/>` | `<img src="...comms/whatsapp-wide.svg" width="310" height="38" alt="WhatsApp"/>` |
| Keybase | `<img src="...comms/keybase.svg" width="220" height="34" alt="Keybase"/>` | `<img src="...comms/keybase-wide.svg" width="310" height="38" alt="Keybase"/>` |
| Chat | `<img src="...comms/chat.svg" width="220" height="34" alt="Chat"/>` | `<img src="...comms/chat-wide.svg" width="310" height="38" alt="Chat"/>` |
| Forum | `<img src="...comms/forum.svg" width="220" height="34" alt="Forum"/>` | `<img src="...comms/forum-wide.svg" width="310" height="38" alt="Forum"/>` |
| Docs | `<img src="...comms/docs.svg" width="220" height="34" alt="Docs"/>` | `<img src="...comms/docs-wide.svg" width="310" height="38" alt="Docs"/>` |
| Support | `<img src="...comms/support.svg" width="220" height="34" alt="Support"/>` | `<img src="...comms/support-wide.svg" width="310" height="38" alt="Support"/>` |
| Email | `<img src="...comms/email.svg" width="220" height="34" alt="Email"/>` | `<img src="...comms/email-wide.svg" width="310" height="38" alt="Email"/>` |
| Secure Channel | `<img src="...comms/secure_channel.svg" width="220" height="34" alt="Secure Channel"/>` | `<img src="...comms/secure_channel-wide.svg" width="310" height="38" alt="Secure Channel"/>` |

---

### 3 · Repository Status Badges

Path: `.github/profile/assets/badges/repo/`

#### Status

| Badge | Standard `<img>` | Wide `<img>` |
|---|---|---|
| Stable | `<img src="...repo/status-stable.svg" width="220" height="34" alt="Stable"/>` | `<img src="...repo/status-stable-wide.svg" width="290" height="34" alt="Stable"/>` |
| In Progress | `<img src="...repo/status-wip.svg" width="220" height="34" alt="In Progress"/>` | `<img src="...repo/status-wip-wide.svg" width="290" height="34" alt="In Progress"/>` |
| Experimental | `<img src="...repo/status-experimental.svg" width="220" height="34" alt="Experimental"/>` | `<img src="...repo/status-experimental-wide.svg" width="290" height="34" alt="Experimental"/>` |
| Maintained | `<img src="...repo/status-maintained.svg" width="220" height="34" alt="Maintained"/>` | `<img src="...repo/status-maintained-wide.svg" width="290" height="34" alt="Maintained"/>` |
| Deprecated | `<img src="...repo/status-deprecated.svg" width="220" height="34" alt="Deprecated"/>` | `<img src="...repo/status-deprecated-wide.svg" width="290" height="34" alt="Deprecated"/>` |
| Archived | `<img src="...repo/status-archived.svg" width="220" height="34" alt="Archived"/>` | `<img src="...repo/status-archived-wide.svg" width="290" height="34" alt="Archived"/>` |

#### License

| Badge | Standard | Wide |
|---|---|---|
| MIT | `<img src="...repo/license-mit.svg" width="220" height="34" alt="MIT"/>` | `<img src="...repo/license-mit-wide.svg" width="290" height="34" alt="MIT"/>` |
| Apache 2.0 | `<img src="...repo/license-apache2.svg" width="220" height="34" alt="Apache 2.0"/>` | `<img src="...repo/license-apache2-wide.svg" width="290" height="34" alt="Apache 2.0"/>` |
| GPL 3.0 | `<img src="...repo/license-gpl3.svg" width="220" height="34" alt="GPL 3.0"/>` | `<img src="...repo/license-gpl3-wide.svg" width="290" height="34" alt="GPL 3.0"/>` |
| BSL 1.1 | `<img src="...repo/license-bsl.svg" width="220" height="34" alt="BSL 1.1"/>` | `<img src="...repo/license-bsl-wide.svg" width="290" height="34" alt="BSL 1.1"/>` |
| Proprietary | `<img src="...repo/license-proprietary.svg" width="220" height="34" alt="Proprietary"/>` | `<img src="...repo/license-proprietary-wide.svg" width="290" height="34" alt="Proprietary"/>` |

#### Build

| Badge | Standard | Wide |
|---|---|---|
| Passing | `<img src="...repo/build-passing.svg" width="220" height="34" alt="Build Passing"/>` | `<img src="...repo/build-passing-wide.svg" width="290" height="34" alt="Build Passing"/>` |
| Failing | `<img src="...repo/build-failing.svg" width="220" height="34" alt="Build Failing"/>` | `<img src="...repo/build-failing-wide.svg" width="290" height="34" alt="Build Failing"/>` |
| Pending | `<img src="...repo/build-pending.svg" width="220" height="34" alt="Build Pending"/>` | `<img src="...repo/build-pending-wide.svg" width="290" height="34" alt="Build Pending"/>` |

#### Security

| Badge | Standard | Wide |
|---|---|---|
| Post-Quantum | `<img src="...repo/security-pq.svg" width="220" height="34" alt="Post-Quantum"/>` | `<img src="...repo/security-pq-wide.svg" width="290" height="34" alt="Post-Quantum"/>` |
| E2E Encrypted | `<img src="...repo/security-encrypted.svg" width="220" height="34" alt="Encrypted"/>` | `<img src="...repo/security-encrypted-wide.svg" width="290" height="34" alt="Encrypted"/>` |
| Audited | `<img src="...repo/security-audited.svg" width="220" height="34" alt="Audited"/>` | `<img src="...repo/security-audited-wide.svg" width="290" height="34" alt="Audited"/>` |
| CVE Free | `<img src="...repo/security-cve-free.svg" width="220" height="34" alt="CVE Free"/>` | `<img src="...repo/security-cve-free-wide.svg" width="290" height="34" alt="CVE Free"/>` |

#### Contributions

| Badge | Standard | Wide |
|---|---|---|
| PRs Welcome | `<img src="...repo/contrib-welcome.svg" width="220" height="34" alt="PRs Welcome"/>` | `<img src="...repo/contrib-welcome-wide.svg" width="290" height="34" alt="PRs Welcome"/>` |
| Seeking Contribs | `<img src="...repo/contrib-seeking.svg" width="220" height="34" alt="Seeking Contributors"/>` | `<img src="...repo/contrib-seeking-wide.svg" width="290" height="34" alt="Seeking Contributors"/>` |
| Closed | `<img src="...repo/contrib-closed.svg" width="220" height="34" alt="Closed"/>` | `<img src="...repo/contrib-closed-wide.svg" width="290" height="34" alt="Closed"/>` |

#### Version

| Badge | Standard | Wide |
|---|---|---|
| Alpha | `<img src="...repo/version-alpha.svg" width="220" height="34" alt="Alpha"/>` | `<img src="...repo/version-alpha-wide.svg" width="290" height="34" alt="Alpha"/>` |
| Beta | `<img src="...repo/version-beta.svg" width="220" height="34" alt="Beta"/>` | `<img src="...repo/version-beta-wide.svg" width="290" height="34" alt="Beta"/>` |
| Release Candidate | `<img src="...repo/version-rc.svg" width="220" height="34" alt="RC"/>` | `<img src="...repo/version-rc-wide.svg" width="290" height="34" alt="RC"/>` |
| Stable | `<img src="...repo/version-stable.svg" width="220" height="34" alt="Stable"/>` | `<img src="...repo/version-stable-wide.svg" width="290" height="34" alt="Stable"/>` |

#### Language / Platform

| Badge | Standard | Wide |
|---|---|---|
| Python | `<img src="...repo/lang-python.svg" width="220" height="34" alt="Python"/>` | `<img src="...repo/lang-python-wide.svg" width="290" height="34" alt="Python"/>` |
| Go | `<img src="...repo/lang-go.svg" width="220" height="34" alt="Go"/>` | `<img src="...repo/lang-go-wide.svg" width="290" height="34" alt="Go"/>` |
| Rust | `<img src="...repo/lang-rust.svg" width="220" height="34" alt="Rust"/>` | `<img src="...repo/lang-rust-wide.svg" width="290" height="34" alt="Rust"/>` |
| Node.js | `<img src="...repo/lang-nodejs.svg" width="220" height="34" alt="Node.js"/>` | `<img src="...repo/lang-nodejs-wide.svg" width="290" height="34" alt="Node.js"/>` |
| C / C++ | `<img src="...repo/lang-c.svg" width="220" height="34" alt="C/C++"/>` | `<img src="...repo/lang-c-wide.svg" width="290" height="34" alt="C/C++"/>` |
| Linux | `<img src="...repo/platform-linux.svg" width="220" height="34" alt="Linux"/>` | `<img src="...repo/platform-linux-wide.svg" width="290" height="34" alt="Linux"/>` |
| WebAssembly | `<img src="...repo/platform-wasm.svg" width="220" height="34" alt="WebAssembly"/>` | `<img src="...repo/platform-wasm-wide.svg" width="290" height="34" alt="WebAssembly"/>` |
| FPGA / ASIC | `<img src="...repo/platform-fpga.svg" width="220" height="34" alt="FPGA/ASIC"/>` | `<img src="...repo/platform-fpga-wide.svg" width="290" height="34" alt="FPGA/ASIC"/>` |

---

### 4 · Standalone Status Badges

Path: `.github/profile/assets/badges/status/`

| Slug | Use Case |
|---|---|
| `status-passing` | CI / test passing |
| `status-failing` | CI / test failing |
| `status-pending` | CI pending / queued |
| `status-building` | Currently building |
| `status-alpha` / `status-beta` / `status-stable` | Release maturity |
| `status-deprecated` / `status-archived` | End-of-life |
| `status-maintained` / `status-wip` | Maintenance state |
| `pq-ready` | Post-quantum crypto |
| `security` | General security notice |
| `open-source` | OSS badge |
| `license-mit` / `license-apache` / `license-prop` | License short-form |
| `sponsor` | Sponsorship CTA |
| `docs` | Docs available |
| `contributing` | Contributions open |
| `downloads` / `coverage` | Metrics |
| `version-release` / `version-prerelease` | Release channel |

```markdown
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/status/pq-ready.svg" width="220" height="34" alt="PQ Ready"/>
```

---

## Quick Copy — Full Repo Badge Row

```markdown
<div align="center">

<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/status-stable.svg" width="220" height="34" alt="Stable"/>
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/license-mit.svg" width="220" height="34" alt="MIT"/>
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq.svg" width="220" height="34" alt="Post-Quantum"/>
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-encrypted.svg" width="220" height="34" alt="Encrypted"/>
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/build-passing.svg" width="220" height="34" alt="Build Passing"/>
<img src="https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/contrib-welcome.svg" width="220" height="34" alt="PRs Welcome"/>

</div>
```

---

## Deployment Layout

```
.github/profile/assets/badges/
├── social/    ← 31 SVGs  (standard + -wide variants)
├── comms/     ← 36 SVGs  (standard + -wide variants)
├── repo/      ← 66 SVGs  (standard + -wide variants)
└── status/    ← 24 SVGs  (standalone, no wide variant)
```

---

## Publishing / Registry Status

| Registry | Package | Status |
|---|---|---|
| npm | [`glitch-badges`](https://www.npmjs.com/package/glitch-badges) | [![npm](https://img.shields.io/npm/v/glitch-badges?color=%231fe8a8)](https://www.npmjs.com/package/glitch-badges) |
| PyPI | [`glitch-badges`](https://pypi.org/project/glitch-badges/) | Published on tag push via `publish-pypi.yml` |
| crates.io | [`glitch-badges`](https://crates.io/crates/glitch-badges) | Published on tag push via `publish-crates.yml` |

To release a new version:
1. Bump `version` in `packages/js/package.json`, `packages/py/pyproject.toml`, `packages/rs/Cargo.toml`
2. Update `CHANGELOG.md`
3. Push a `v<semver>` tag — CI handles the rest

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

*Copyright (c) 2026 VLABS, LLC. All rights reserved.* <br>
*[VRIL LABS Open Source License v1.0](https://github.com/VrilLabs/vril-js/blob/main/LICENSE) — [vril.li/license](https://vril.li/license)*.

---

<div align="center">
<strong>133 Badges · 4 Collections · Animated SVGs · 0 Dependencies · GitHub-ready</strong><br>
  <sub>Built by <strong>VRIL LABS</strong> · Encrypting the future</sub>
</div>
