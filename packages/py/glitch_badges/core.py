"""
glitch_badges.core
Generates animated glitch badge SVGs — same visual output as badge_generator.py
but exposed as a importable library function.
"""
from __future__ import annotations

# ── Brand tokens ─────────────────────────────────────────────────────────────
DARK_BG     = "#0b0c0b"
DARK_BORDER = "#1a2a24"
DARK_ACCENT = "#1fe8a8"
DARK_MUTED  = "#4a7060"
GLITCH_RED  = "#ff3366"
GLITCH_CYAN = "#33ffee"
SCAN_COLOR  = "rgba(31,232,168,0.025)"

_BADGE_BASE = (
    "https://raw.githubusercontent.com/dubzrn/glitch-badges"
    "/main/.github/profile/assets/badges"
)


def make_badge(
    text:      str,
    accent:    str  = DARK_ACCENT,
    width:     int  = 220,
    height:    int  = 36,
    tag:       str | None = None,
    tag_color: str | None = None,
    duration:  int  = 5,
) -> str:
    """Return a standalone animated glitch badge SVG string.

    Parameters
    ----------
    text:      Right-side label text (e.g. "POST QUANTUM").
    accent:    Hex accent colour.
    width:     Badge width in pixels.
    height:    Badge height in pixels.
    tag:       Optional left-side tag label (e.g. "Security").
    tag_color: Colour for the tag section (defaults to *accent*).
    duration:  Glitch animation cycle in seconds.

    Returns
    -------
    str — A self-contained SVG string ready to write to a .svg file.

    Examples
    --------
    >>> svg = make_badge("POST QUANTUM", accent="#a78bfa", tag="Security", width=260)
    >>> open("security-pq.svg", "w").write(svg)
    """
    tc = tag_color or accent
    fs = max(9, min(15, int(width * 0.056)))
    esc = text.replace("'", "\\'")

    tag_css = (
        f".tag{{background:{tc}18;border-right:1px solid {tc}40;"
        f"padding:0 10px;font-size:{max(8, fs - 2)}px;letter-spacing:.15em;"
        f"text-transform:uppercase;color:{tc};height:100%;"
        f"display:flex;align-items:center;flex-shrink:0;white-space:nowrap;}}"
    ) if tag else ""

    tag_html = f'<div class="tag">{tag}</div>' if tag else ""
    jc = "" if tag else "justify-content:center;"

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"'
        f' viewBox="0 0 {width} {height}">\n'
        f'<foreignObject width="100%" height="100%">\n'
        f'<div xmlns="http://www.w3.org/1999/xhtml">\n'
        f"<style>\n"
        f"*{{margin:0;padding:0;box-sizing:border-box}}\n"
        f".badge{{width:{width}px;height:{height}px;background:{DARK_BG};border:1px solid {DARK_BORDER};"
        f"border-radius:4px;display:flex;align-items:center;{jc}"
        f"position:relative;overflow:hidden;"
        f"font-family:ui-monospace,'SF Mono','Fira Mono',Consolas,monospace;}}\n"
        f".badge::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;"
        f"background:linear-gradient(90deg,transparent,{accent},transparent);}}{tag_css}\n"
        f".inner{{display:flex;align-items:center;{'flex:1;justify-content:center;' if tag else ''}padding:0 12px;height:100%;}}\n"
        f".lbl{{font-size:{fs}px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;"
        f"color:{accent};position:relative;user-select:none;white-space:nowrap;}}\n"
        f".lbl::before,.lbl::after{{content:'{esc}';position:absolute;top:0;left:0;width:100%;height:100%;opacity:0;}}\n"
        f".lbl::before{{color:{GLITCH_RED};mix-blend-mode:screen;}}\n"
        f".lbl::after{{color:{GLITCH_CYAN};mix-blend-mode:screen;}}\n"
        f".lbl{{animation:gm {duration}s steps(1) infinite;}}\n"
        f".lbl::before{{animation:gr {duration}s steps(1) infinite;}}\n"
        f".lbl::after{{animation:gc {duration}s steps(1) infinite;}}\n"
        f"@keyframes gm{{0%,89%,100%{{transform:none;opacity:1}}\n"
        f"  90%{{transform:skewX(-1deg) translateX(2px);opacity:.9}}91%{{transform:none;opacity:1}}\n"
        f"  93%{{transform:skewX(.5deg) translateX(-1px);opacity:.95}}94%{{transform:none;opacity:1}}\n"
        f"  96%{{transform:skewX(-.5deg) translateX(1px);opacity:.9}}97%{{transform:none;opacity:1}}}}\n"
        f"@keyframes gr{{0%,89%,100%{{transform:translateX(0);opacity:0}}\n"
        f"  90%{{transform:translateX(-3px);opacity:.7}}91%{{opacity:0}}\n"
        f"  93%{{transform:translateX(2px);opacity:.5}}94%{{opacity:0}}\n"
        f"  96%{{transform:translateX(-2px);opacity:.6}}97%{{opacity:0}}}}\n"
        f"@keyframes gc{{0%,89%,100%{{transform:translateX(0);opacity:0}}\n"
        f"  90%{{transform:translateX(3px);opacity:.6}}91%{{opacity:0}}\n"
        f"  93%{{transform:translateX(-2px);opacity:.5}}94%{{opacity:0}}\n"
        f"  96%{{transform:translateX(2px);opacity:.55}}97%{{opacity:0}}}}\n"
        f".scan{{position:absolute;inset:0;pointer-events:none;"
        f"background:repeating-linear-gradient(0deg,transparent,transparent 3px,{SCAN_COLOR} 3px,{SCAN_COLOR} 4px);"
        f"animation:fl {duration}s steps(1) infinite;}}\n"
        f"@keyframes fl{{0%,89%,100%{{opacity:1}}90%{{opacity:.55}}91%{{opacity:1}}93%{{opacity:.7}}94%{{opacity:1}}}}\n"
        f".br{{position:absolute;width:7px;height:7px;border-color:{accent};border-style:solid;opacity:.35;}}\n"
        f".br-tl{{top:4px;left:4px;border-width:1px 0 0 1px;}}.br-tr{{top:4px;right:4px;border-width:1px 1px 0 0;}}\n"
        f".br-bl{{bottom:4px;left:4px;border-width:0 0 1px 1px;}}.br-br{{bottom:4px;right:4px;border-width:0 1px 1px 0;}}\n"
        f"</style>\n"
        f'<div class="badge">\n'
        f'  <div class="scan"></div>\n'
        f'  <div class="br br-tl"></div><div class="br br-tr"></div>\n'
        f'  <div class="br br-bl"></div><div class="br br-br"></div>\n'
        f'  {tag_html}<div class="inner"><div class="lbl">{text}</div></div>\n'
        f"</div></div></foreignObject></svg>"
    )


def badge_url(
    collection: str,
    slug:       str,
    wide:       bool = False,
) -> str:
    """Return the raw GitHub CDN URL for a pre-built badge SVG.

    Parameters
    ----------
    collection: "social" | "comms" | "repo" | "status"
    slug:       Badge filename without extension, e.g. "security-pq"
    wide:       Use the wider variant (default: False)

    Examples
    --------
    >>> badge_url("repo", "security-pq", wide=True)
    'https://raw.githubusercontent.com/.../repo/security-pq-wide.svg'
    """
    suffix = "-wide" if wide else ""
    return f"{_BADGE_BASE}/{collection}/{slug}{suffix}.svg"


def badge_img(
    collection: str,
    slug:       str,
    alt:        str,
    wide:       bool = False,
) -> str:
    """Return an HTML ``<img>`` tag for a pre-built badge.

    Examples
    --------
    >>> print(badge_img("repo", "security-pq", "Post-Quantum", wide=True))
    <img src="..." width="290" height="34" alt="Post-Quantum"/>
    """
    url = badge_url(collection, slug, wide)
    w   = 290 if wide else 220
    return f'<img src="{url}" width="{w}" height="34" alt="{alt}"/>'
