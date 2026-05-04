#!/usr/bin/env python3
"""
badge_generator.py — Glitch Badge Generator
============================================
Generates all 133 animated glitch badges derived programmatically from the
badge-glitch.svg DNA.  Three usage modes:

  python badge_generator.py all    --out ./profile/assets/badges
  python badge_generator.py repo   --out ./assets
  python badge_generator.py custom "POST QUANTUM" --accent "#a78bfa" --tag "Security" --width 260
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Badge specification types
# ---------------------------------------------------------------------------

class BadgeSpec(NamedTuple):
    tag:    str          # left-side label  (e.g. "TWITTER")
    value:  str          # right-side value  (e.g. "FOLLOW")
    accent: str          # hex accent colour (e.g. "#1da1f2")
    slug:   str          # filename stem     (e.g. "twitter")
    widths: list[int]    # sizes to render   (e.g. [200, 280])


# ---------------------------------------------------------------------------
# Collections
# ---------------------------------------------------------------------------

SOCIAL_BADGES: list[BadgeSpec] = [
    BadgeSpec("TWITTER",   "FOLLOW",    "#1da1f2", "twitter",   [200, 280]),
    BadgeSpec("INSTAGRAM", "FOLLOW",    "#e1306c", "instagram", [200, 280]),
    BadgeSpec("YOUTUBE",   "SUBSCRIBE", "#ff0000", "youtube",   [200, 280]),
    BadgeSpec("LINKEDIN",  "CONNECT",   "#0a66c2", "linkedin",  [200, 280]),
    BadgeSpec("GITHUB",    "FOLLOW",    "#f0f6fc", "github",    [200, 280]),
    BadgeSpec("TIKTOK",    "FOLLOW",    "#fe2c55", "tiktok",    [200, 280]),
    BadgeSpec("FACEBOOK",  "LIKE",      "#1877f2", "facebook",  [200, 280]),
    BadgeSpec("REDDIT",    "JOIN",      "#ff4500", "reddit",    [200, 280]),
    BadgeSpec("TWITCH",    "FOLLOW",    "#9146ff", "twitch",    [200, 280]),
    BadgeSpec("PINTEREST", "FOLLOW",    "#e60023", "pinterest", [200, 280]),
    BadgeSpec("MASTODON",  "FOLLOW",    "#6364ff", "mastodon",  [200, 280]),
    BadgeSpec("BLUESKY",   "FOLLOW",    "#0085ff", "bluesky",   [200, 280]),
]

COMMS_BADGES: list[BadgeSpec] = [
    BadgeSpec("DISCORD",   "JOIN",      "#5865f2", "discord",   [220, 310]),
    BadgeSpec("TELEGRAM",  "CHAT",      "#2aabee", "telegram",  [220, 310]),
    BadgeSpec("MATRIX",    "JOIN",      "#0dbd8b", "matrix",    [220, 310]),
    BadgeSpec("SLACK",     "WORKSPACE", "#4a154b", "slack",     [220, 310]),
    BadgeSpec("SIGNAL",    "MESSAGE",   "#2592e9", "signal",    [220, 310]),
    BadgeSpec("WHATSAPP",  "CHAT",      "#25d366", "whatsapp",  [220, 310]),
    BadgeSpec("EMAIL",     "CONTACT",   "#ea4335", "email",     [220, 310]),
    BadgeSpec("PHONE",     "CALL",      "#34a853", "phone",     [220, 310]),
    BadgeSpec("RSS",       "SUBSCRIBE", "#f26522", "rss",       [220, 310]),
    BadgeSpec("IRC",       "CONNECT",   "#00aeef", "irc",       [220, 310]),
    BadgeSpec("XMPP",      "CHAT",      "#0a6096", "xmpp",      [220, 310]),
    BadgeSpec("KEYBASE",   "VERIFY",    "#ff6f21", "keybase",   [220, 310]),
    BadgeSpec("WIRE",      "MESSAGE",   "#00b0ff", "wire",      [220, 310]),
    BadgeSpec("ELEMENT",   "JOIN",      "#0dbd8b", "element",   [220, 310]),
]

REPO_BADGES: list[BadgeSpec] = [
    # Status
    BadgeSpec("STATUS", "ACTIVE",       "#39ff14", "status-active",       [220, 290]),
    BadgeSpec("STATUS", "MAINTENANCE",  "#f0c040", "status-maintenance",  [220, 290]),
    BadgeSpec("STATUS", "DEPRECATED",   "#ff4444", "status-deprecated",   [220, 290]),
    BadgeSpec("STATUS", "WIP",          "#ff9900", "status-wip",          [220, 290]),
    BadgeSpec("STATUS", "STABLE",       "#39ff14", "status-stable",       [220, 290]),
    BadgeSpec("STATUS", "BETA",         "#f0c040", "status-beta",         [220, 290]),
    # License
    BadgeSpec("LICENSE", "MIT",         "#a0c040", "license-mit",         [220, 290]),
    BadgeSpec("LICENSE", "GPL-3",       "#cc4444", "license-gpl",         [220, 290]),
    BadgeSpec("LICENSE", "APACHE-2",    "#d07020", "license-apache",      [220, 290]),
    BadgeSpec("LICENSE", "BSD-3",       "#4080c0", "license-bsd",         [220, 290]),
    BadgeSpec("LICENSE", "CC0",         "#888888", "license-cc0",         [220, 290]),
    BadgeSpec("LICENSE", "PROPRIETARY", "#ff4444", "license-proprietary", [220, 290]),
    # Build
    BadgeSpec("BUILD",  "PASSING",      "#39ff14", "build-passing",       [220, 290]),
    BadgeSpec("BUILD",  "FAILING",      "#ff4444", "build-failing",       [220, 290]),
    BadgeSpec("BUILD",  "UNKNOWN",      "#888888", "build-unknown",       [220, 290]),
    # Security
    BadgeSpec("SECURITY", "POST-QUANTUM", "#a78bfa", "security-pq",       [220, 290]),
    BadgeSpec("SECURITY", "E2E-ENC",      "#34d399", "security-e2e",      [220, 290]),
    BadgeSpec("SECURITY", "HARDENED",     "#f59e0b", "security-hardened", [220, 290]),
    BadgeSpec("SECURITY", "AUDITED",      "#60a5fa", "security-audited",  [220, 290]),
    # Contrib
    BadgeSpec("CONTRIB", "PRs WELCOME",  "#39ff14", "contrib-prs",        [220, 290]),
    BadgeSpec("CONTRIB", "CONTRIBUTORS", "#60a5fa", "contrib-all",        [220, 290]),
    BadgeSpec("CONTRIB", "HELP WANTED",  "#ff6b6b", "contrib-help",       [220, 290]),
    # Version
    BadgeSpec("VERSION", "LATEST",       "#39ff14", "version-latest",     [220, 290]),
    BadgeSpec("VERSION", "SEMVER",       "#60a5fa", "version-semver",     [220, 290]),
    BadgeSpec("VERSION", "SNAPSHOT",     "#f0c040", "version-snapshot",   [220, 290]),
    # Language
    BadgeSpec("LANG", "PYTHON",         "#3572a5", "lang-python",         [220, 290]),
    BadgeSpec("LANG", "JAVASCRIPT",     "#f1e05a", "lang-js",             [220, 290]),
    BadgeSpec("LANG", "GO",             "#00add8", "lang-go",             [220, 290]),
    BadgeSpec("LANG", "RUST",           "#dea584", "lang-rust",           [220, 290]),
    BadgeSpec("LANG", "TYPESCRIPT",     "#2b7489", "lang-ts",             [220, 290]),
    # Platform
    BadgeSpec("PLATFORM", "LINUX",      "#fcc624", "platform-linux",      [220, 290]),
    BadgeSpec("PLATFORM", "MACOS",      "#999999", "platform-macos",      [220, 290]),
    BadgeSpec("PLATFORM", "WINDOWS",    "#0078d4", "platform-windows",    [220, 290]),
    BadgeSpec("PLATFORM", "DOCKER",     "#2496ed", "platform-docker",     [220, 290]),
    BadgeSpec("PLATFORM", "CLOUD",      "#00adef", "platform-cloud",      [220, 290]),
]

COLLECTIONS: dict[str, list[BadgeSpec]] = {
    "social": SOCIAL_BADGES,
    "comms":  COMMS_BADGES,
    "repo":   REPO_BADGES,
}


# ---------------------------------------------------------------------------
# SVG generation
# ---------------------------------------------------------------------------

def _slug_id(text: str) -> str:
    """Produce a safe XML id fragment from arbitrary text."""
    return re.sub(r"[^a-z0-9]", "-", text.lower())


def make_badge(
    tag:    str,
    value:  str,
    accent: str,
    width:  int = 220,
    height: int = 34,
) -> str:
    """Return a standalone animated glitch badge SVG string."""

    w  = width
    h  = height
    # Left (tag) side width — proportional to tag string length, min 35 %
    raw_split = max(int(w * 0.36), len(tag) * 8 + 20)
    split     = min(raw_split, w - 60)          # ensure value area ≥ 60 px
    tag_cx    = split // 2
    val_cx    = split + (w - split) // 2

    uid = _slug_id(f"{tag}-{value}-{width}")    # unique per badge×size

    # 7-frame chromatic-aberration keyframe tables (steps(1) timing)
    # red  shifts LEFT,  cyan shifts RIGHT across 7 frames + rest
    red_x_tag  = ";".join([
        str(tag_cx - 2), str(tag_cx), str(tag_cx + 2),
        str(tag_cx - 1), str(tag_cx + 1), str(tag_cx - 2),
        str(tag_cx), str(tag_cx),
    ])
    cyn_x_tag  = ";".join([
        str(tag_cx + 2), str(tag_cx), str(tag_cx - 2),
        str(tag_cx + 1), str(tag_cx - 1), str(tag_cx + 2),
        str(tag_cx), str(tag_cx),
    ])
    red_x_val  = ";".join([
        str(val_cx - 2), str(val_cx), str(val_cx + 2),
        str(val_cx - 1), str(val_cx + 1), str(val_cx - 2),
        str(val_cx), str(val_cx),
    ])
    cyn_x_val  = ";".join([
        str(val_cx + 2), str(val_cx), str(val_cx - 2),
        str(val_cx + 1), str(val_cx - 1), str(val_cx + 2),
        str(val_cx), str(val_cx),
    ])
    ca_op      = "0.45;0.10;0.45;0.40;0.20;0.45;0;0.45"
    flick_op   = "0;0;0;0;0;0.08;0;0"
    dur        = "3.7s"

    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg"
     width="{w}" height="{h}"
     role="img" aria-label="{tag}: {value}">
  <title>{tag}: {value}</title>
  <defs>
    <!-- CRT phosphor scanline grid (4 px repeat) -->
    <pattern id="sl-{uid}" x="0" y="0" width="{w}" height="4"
             patternUnits="userSpaceOnUse">
      <rect width="{w}" height="2" fill="#000" opacity="0.14"/>
    </pattern>
    <!-- Top-edge gradient pulse accent seam -->
    <linearGradient id="tg-{uid}" x1="0" y1="0" x2="1" y2="0"
                    gradientUnits="objectBoundingBox">
      <stop offset="0"   stop-color="{accent}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{accent}" stop-opacity="1"/>
      <stop offset="1"   stop-color="{accent}" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        values="-0.4 0;0.4 0;-0.4 0" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    <clipPath id="cb-{uid}">
      <rect width="{w}" height="{h}"/>
    </clipPath>
  </defs>

  <g clip-path="url(#cb-{uid})">
    <!-- ── Void background ── -->
    <rect width="{w}" height="{h}" fill="#0b0c0b"/>
    <!-- Subtle tag-side tint -->
    <rect width="{split}" height="{h}" fill="#0e120e"/>

    <!-- ── Border ── -->
    <rect width="{w - 2}" height="{h - 2}" x="1" y="1"
          fill="none" stroke="#1a2a24" stroke-width="1"/>

    <!-- ── Top-edge gradient pulse ── -->
    <rect width="{w}" height="1" fill="url(#tg-{uid})"/>

    <!-- ── Divider seam ── -->
    <rect x="{split}" y="0" width="1" height="{h}"
          fill="{accent}" opacity="0.30"/>

    <!-- ── Corner bracket decorators (border-width trick via path) ── -->
    <path d="M4,4 L4,10 M4,4 L10,4"
          stroke="#1a2a24" stroke-width="1" fill="none"/>
    <path d="M{w - 4},4 L{w - 4},10 M{w - 4},4 L{w - 10},4"
          stroke="#1a2a24" stroke-width="1" fill="none"/>
    <path d="M4,{h - 4} L4,{h - 10} M4,{h - 4} L10,{h - 4}"
          stroke="#1a2a24" stroke-width="1" fill="none"/>
    <path d="M{w - 4},{h - 4} L{w - 4},{h - 10} M{w - 4},{h - 4} L{w - 10},{h - 4}"
          stroke="#1a2a24" stroke-width="1" fill="none"/>

    <!-- ═══════════════════════════════════════════════════════════
         TAG text — chromatic aberration glitch (7-frame steps(1))
         Red channel shifts LEFT, Cyan channel shifts RIGHT
    ═══════════════════════════════════════════════════════════════ -->
    <!-- red channel -->
    <text font-family="'Courier New',Courier,monospace"
          font-size="11" font-weight="700" letter-spacing="0.5"
          fill="#ff3030" text-anchor="middle" x="{tag_cx}" y="22">
      <animate attributeName="x"
               values="{red_x_tag}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      <animate attributeName="fill-opacity"
               values="{ca_op}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      {tag.upper()}
    </text>
    <!-- cyan channel -->
    <text font-family="'Courier New',Courier,monospace"
          font-size="11" font-weight="700" letter-spacing="0.5"
          fill="#00e5ff" text-anchor="middle" x="{tag_cx}" y="22">
      <animate attributeName="x"
               values="{cyn_x_tag}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      <animate attributeName="fill-opacity"
               values="{ca_op}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      {tag.upper()}
    </text>
    <!-- primary layer -->
    <text font-family="'Courier New',Courier,monospace"
          font-size="11" font-weight="700" letter-spacing="0.5"
          fill="#b8d4b8" text-anchor="middle" x="{tag_cx}" y="22">
      <animate attributeName="x"
               values="{tag_cx};{tag_cx};{tag_cx};{tag_cx};{tag_cx - 1};{tag_cx};{tag_cx};{tag_cx}"
               dur="{dur}" repeatCount="indefinite" calcMode="discrete"/>
      {tag.upper()}
    </text>

    <!-- ═══════════════════════════════════════════════════════════
         VALUE text — same glitch pattern, accent colour primary
    ═══════════════════════════════════════════════════════════════ -->
    <!-- red channel -->
    <text font-family="'Courier New',Courier,monospace"
          font-size="11" font-weight="700" letter-spacing="0.5"
          fill="#ff3030" text-anchor="middle" x="{val_cx}" y="22">
      <animate attributeName="x"
               values="{red_x_val}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      <animate attributeName="fill-opacity"
               values="{ca_op}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      {value.upper()}
    </text>
    <!-- cyan channel -->
    <text font-family="'Courier New',Courier,monospace"
          font-size="11" font-weight="700" letter-spacing="0.5"
          fill="#00e5ff" text-anchor="middle" x="{val_cx}" y="22">
      <animate attributeName="x"
               values="{cyn_x_val}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      <animate attributeName="fill-opacity"
               values="{ca_op}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
      {value.upper()}
    </text>
    <!-- primary layer (accent colour) -->
    <text font-family="'Courier New',Courier,monospace"
          font-size="11" font-weight="700" letter-spacing="0.5"
          fill="{accent}" text-anchor="middle" x="{val_cx}" y="22">
      <animate attributeName="x"
               values="{val_cx};{val_cx};{val_cx};{val_cx};{val_cx - 1};{val_cx};{val_cx};{val_cx}"
               dur="{dur}" repeatCount="indefinite" calcMode="discrete"/>
      <animate attributeName="fill-opacity"
               values="1;0.70;1;0.90;1;0.80;1;1"
               dur="{dur}" repeatCount="indefinite" calcMode="discrete"/>
      {value.upper()}
    </text>

    <!-- ── CRT scanline overlay ── -->
    <rect width="{w}" height="{h}" fill="url(#sl-{uid})"/>

    <!-- ── Synchronized screen-flicker pulse ── -->
    <rect width="{w}" height="{h}" fill="#0b0c0b">
      <animate attributeName="opacity"
               values="{flick_op}" dur="{dur}"
               repeatCount="indefinite" calcMode="discrete"/>
    </rect>
  </g>
</svg>
"""
    return svg


# ---------------------------------------------------------------------------
# File I/O helpers
# ---------------------------------------------------------------------------

def write_badge(path: Path, svg: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg, encoding="utf-8")
    print(f"  wrote  {path}")


def generate_collection(
    specs:   list[BadgeSpec],
    out_dir: Path,
    subdir:  str,
) -> int:
    """Generate both size variants for every spec in *specs*.

    Returns the number of SVG files written.
    """
    count = 0
    for spec in specs:
        for w in spec.widths:
            suffix = "-sm" if w == min(spec.widths) else "-lg"
            fname  = f"{spec.slug}{suffix}.svg"
            svg    = make_badge(spec.tag, spec.value, spec.accent, width=w)
            write_badge(out_dir / subdir / fname, svg)
            count += 1
    return count


# ---------------------------------------------------------------------------
# Catalog SVG
# ---------------------------------------------------------------------------

def make_catalog(
    all_specs: dict[str, list[BadgeSpec]],
    out_dir:   Path,
) -> None:
    """Write a single catalog SVG that lists every badge slug and accent."""
    rows: list[str] = []
    y = 30
    for collection, specs in all_specs.items():
        rows.append(
            f'  <text x="10" y="{y}" font-family="monospace" font-size="11"'
            f' fill="#1a2a24" font-weight="700">{collection.upper()}</text>'
        )
        y += 16
        for spec in specs:
            rows.append(
                f'  <text x="20" y="{y}" font-family="monospace" font-size="10"'
                f' fill="{spec.accent}">{spec.slug}  {spec.tag}:{spec.value}</text>'
            )
            y += 14

    total_h = y + 20
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="420" height="{total_h}">\n'
        f'  <rect width="420" height="{total_h}" fill="#0b0c0b"/>\n'
        f'  <text x="10" y="16" font-family="monospace" font-size="12"'
        f' fill="#39ff14" font-weight="700">GLITCH BADGE CATALOG</text>\n'
    )
    footer = "</svg>\n"
    catalog_svg = header + "\n".join(rows) + "\n" + footer
    write_badge(out_dir / "catalog.svg", catalog_svg)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="command", required=True)

    # ── all ──────────────────────────────────────────────────────────────────
    all_p = sub.add_parser("all", help="Regenerate every badge across all collections")
    all_p.add_argument("--out", default=".", metavar="DIR",
                       help="Root output directory (default: .)")

    # ── per-collection ───────────────────────────────────────────────────────
    for name in COLLECTIONS:
        cp = sub.add_parser(name, help=f"Generate the '{name}' collection only")
        cp.add_argument("--out", default=".", metavar="DIR")

    # ── custom ───────────────────────────────────────────────────────────────
    cust = sub.add_parser("custom", help="One-off custom badge (any label, any accent)")
    cust.add_argument("value",          metavar="VALUE",
                      help='Right-side value text, e.g. "POST QUANTUM"')
    cust.add_argument("--tag",    default="BADGE", metavar="TAG",
                      help="Left-side tag text (default: BADGE)")
    cust.add_argument("--accent", default="#39ff14", metavar="HEX",
                      help="Accent colour (default: #39ff14)")
    cust.add_argument("--width",  type=int, default=220, metavar="PX",
                      help="Badge width in px (default: 220)")
    cust.add_argument("--out",    default=".", metavar="DIR")
    cust.add_argument("--name",   default=None, metavar="SLUG",
                      help="Output filename stem (default: derived from VALUE)")

    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args    = parse_args(argv)
    out_dir = Path(args.out).expanduser()
    total   = 0

    if args.command == "all":
        print(f"Generating all badges → {out_dir}")
        for collection, specs in COLLECTIONS.items():
            n = generate_collection(specs, out_dir, collection)
            total += n
            print(f"  {collection}: {n} SVGs")
        make_catalog(COLLECTIONS, out_dir)
        total += 1
        print(f"\n✓  {total} files written to {out_dir}")

    elif args.command in COLLECTIONS:
        specs = COLLECTIONS[args.command]
        print(f"Generating '{args.command}' collection → {out_dir}")
        n = generate_collection(specs, out_dir, args.command)
        print(f"\n✓  {n} SVGs written to {out_dir}/{args.command}")

    elif args.command == "custom":
        slug   = args.name or re.sub(r"[^a-z0-9]+", "-", args.value.lower()).strip("-")
        fname  = f"{slug}.svg"
        svg    = make_badge(args.tag, args.value, args.accent, width=args.width)
        out_dir.mkdir(parents=True, exist_ok=True)
        dest   = out_dir / fname
        dest.write_text(svg, encoding="utf-8")
        print(f"✓  custom badge written to {dest}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
