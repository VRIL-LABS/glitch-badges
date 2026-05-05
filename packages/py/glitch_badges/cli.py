"""glitch_badges.cli — command-line interface."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .core import make_badge, badge_url
from .presets import ALL_PRESETS, get_preset


def _list_cmd(args: argparse.Namespace) -> int:
    col = args.collection
    presets = [p for p in ALL_PRESETS if not col or p.collection == col]
    if not presets:
        print(f"Unknown collection: {col}", file=sys.stderr)
        return 1
    for p in presets:
        tag = f"[{p.tag}]" if p.tag else ""
        print(f"  {p.collection:<8}  {p.slug:<30} {tag:<12} {p.text}")
    return 0


def _url_cmd(args: argparse.Namespace) -> int:
    preset = get_preset(args.slug)
    col = preset.collection if preset else args.collection
    if not col:
        print("Provide --collection <social|comms|repo|status>", file=sys.stderr)
        return 1
    print(badge_url(col, args.slug, wide=args.wide))
    return 0


def _custom_cmd(args: argparse.Namespace) -> int:
    svg = make_badge(
        text=args.value,
        accent=args.accent,
        width=args.width,
        height=args.height,
        tag=args.tag or None,
        duration=args.duration,
    )
    slug = args.name or re.sub(r"[^a-z0-9]+", "-", args.value.lower()).strip("-")
    dest = Path(args.out) / f"{slug}.svg"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(svg, encoding="utf-8")
    print(f"✓  {dest}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="glitch-badges",
        description="VRIL LABS animated glitch badge generator",
    )
    sub = p.add_subparsers(dest="command", required=True)

    # ── list ──────────────────────────────────────────────────────────────────
    lp = sub.add_parser("list", help="List available badge slugs")
    lp.add_argument("collection", nargs="?", help="Filter by collection")

    # ── url ───────────────────────────────────────────────────────────────────
    up = sub.add_parser("url", help="Print CDN URL for a pre-built badge")
    up.add_argument("slug", help="Badge slug, e.g. security-pq")
    up.add_argument("--collection", "-c", default=None,
                    help="Collection override if slug is ambiguous")
    up.add_argument("--wide", action="store_true", help="Use wide variant")

    # ── custom ────────────────────────────────────────────────────────────────
    cp = sub.add_parser("custom", help="Generate a one-off custom badge")
    cp.add_argument("value",             help='Right-side label, e.g. "POST QUANTUM"')
    cp.add_argument("--tag",    default=None,      help="Left-side tag label")
    cp.add_argument("--accent", default="#1fe8a8", help="Hex accent colour")
    cp.add_argument("--width",  type=int, default=220, help="Width in px")
    cp.add_argument("--height", type=int, default=36,  help="Height in px")
    cp.add_argument("--duration", type=int, default=5, help="Animation duration (s)")
    cp.add_argument("--out",    default=".",       help="Output directory")
    cp.add_argument("--name",   default=None,      help="Output filename stem")

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args   = parser.parse_args(argv)
    dispatch = {"list": _list_cmd, "url": _url_cmd, "custom": _custom_cmd}
    return dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
