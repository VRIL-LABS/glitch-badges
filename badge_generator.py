#!/usr/bin/env python3
"""
badge_generator.py — VRIL LABS animated glitch badge factory
Derived from badge-glitch.svg. Generates GitHub README-compatible SVGs.

Usage:
  python badge_generator.py                    # regenerates all 3 collections
  python badge_generator.py custom "MY LABEL" --accent "#ff6b6b" --tag "Status"
"""

import os, sys, argparse

# ── VRIL LABS brand tokens ────────────────────────────────────────────────────
DARK_BG     = "#0b0c0b"
DARK_BORDER = "#1a2a24"
DARK_ACCENT = "#1fe8a8"
DARK_MUTED  = "#4a7060"
GLITCH_RED  = "#ff3366"
GLITCH_CYAN = "#33ffee"
SCAN_COLOR  = "rgba(31,232,168,0.025)"

def make_badge(txt, accent=DARK_ACCENT, w=220, h=36,
               tag=None, tag_color=None, dur=5):
    tc  = tag_color or DARK_MUTED
    fs  = max(9, min(15, int(w * 0.056)))
    esc = txt.replace("'", "\\'")

    tag_css  = (f".tag{{background:{tc}18;border-right:1px solid {tc}40;"
                f"padding:0 10px;font-size:{max(8,fs-2)}px;letter-spacing:0.15em;"
                f"text-transform:uppercase;color:{tc};height:100%;"
                f"display:flex;align-items:center;flex-shrink:0;white-space:nowrap;}}"
                if tag else "")
    tag_html  = f'<div class="tag">{tag}</div>' if tag else ""
    jc        = "" if tag else "justify-content:center;"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<foreignObject width="100%" height="100%">
<div xmlns="http://www.w3.org/1999/xhtml">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
.badge{{width:{w}px;height:{h}px;background:{DARK_BG};border:1px solid {DARK_BORDER};
  border-radius:4px;display:flex;align-items:center;{jc}
  position:relative;overflow:hidden;
  font-family:ui-monospace,'SF Mono','Fira Mono',Consolas,monospace;}}
.badge::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,{accent},transparent);}}{tag_css}
.inner{{display:flex;align-items:center;{"flex:1;justify-content:center;" if tag else ""}padding:0 12px;height:100%;}}
.lbl{{font-size:{fs}px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;
  color:{accent};position:relative;user-select:none;white-space:nowrap;}}
.lbl::before,.lbl::after{{content:'{esc}';position:absolute;top:0;left:0;width:100%;height:100%;opacity:0;}}
.lbl::before{{color:{GLITCH_RED};mix-blend-mode:screen;}}
.lbl::after{{color:{GLITCH_CYAN};mix-blend-mode:screen;}}
.lbl{{animation:gm {dur}s steps(1) infinite;}}
.lbl::before{{animation:gr {dur}s steps(1) infinite;}}
.lbl::after{{animation:gc {dur}s steps(1) infinite;}}
@keyframes gm{{0%,89%,100%{{transform:none;opacity:1}}
  90%{{transform:skewX(-1deg) translateX(2px);opacity:.9}}91%{{transform:none;opacity:1}}
  93%{{transform:skewX(.5deg) translateX(-1px);opacity:.95}}94%{{transform:none;opacity:1}}
  96%{{transform:skewX(-.5deg) translateX(1px);opacity:.9}}97%{{transform:none;opacity:1}}}}
@keyframes gr{{0%,89%,100%{{transform:translateX(0);opacity:0}}
  90%{{transform:translateX(-3px);opacity:.7}}91%{{opacity:0}}
  93%{{transform:translateX(2px);opacity:.5}}94%{{opacity:0}}
  96%{{transform:translateX(-2px);opacity:.6}}97%{{opacity:0}}}}
@keyframes gc{{0%,89%,100%{{transform:translateX(0);opacity:0}}
  90%{{transform:translateX(3px);opacity:.6}}91%{{opacity:0}}
  93%{{transform:translateX(-2px);opacity:.5}}94%{{opacity:0}}
  96%{{transform:translateX(2px);opacity:.55}}97%{{opacity:0}}}}
.scan{{position:absolute;inset:0;pointer-events:none;
  background:repeating-linear-gradient(0deg,transparent,transparent 3px,{SCAN_COLOR} 3px,{SCAN_COLOR} 4px);
  animation:fl {dur}s steps(1) infinite;}}
@keyframes fl{{0%,89%,100%{{opacity:1}}90%{{opacity:.55}}91%{{opacity:1}}93%{{opacity:.7}}94%{{opacity:1}}}}
.br{{position:absolute;width:7px;height:7px;border-color:{accent};border-style:solid;opacity:.35;}}
.br-tl{{top:4px;left:4px;border-width:1px 0 0 1px;}}.br-tr{{top:4px;right:4px;border-width:1px 1px 0 0;}}
.br-bl{{bottom:4px;left:4px;border-width:0 0 1px 1px;}}.br-br{{bottom:4px;right:4px;border-width:0 1px 1px 0;}}
</style>
<div class="badge">
  <div class="scan"></div>
  <div class="br br-tl"></div><div class="br br-tr"></div>
  <div class="br br-bl"></div><div class="br br-br"></div>
  {tag_html}<div class="inner"><div class="lbl">{txt}</div></div>
</div></div></foreignObject></svg>"""


# ── Batch definitions (edit to add/remove badges) ─────────────────────────────
PA = {
    "twitter":"#1DA1F2","x":"#e7e7e7","instagram":"#E1306C",
    "linkedin":"#0A66C2","youtube":"#FF0000","tiktok":"#69C9D0",
    "mastodon":"#6364FF","bluesky":"#0085ff",
    "discord":"#5865F2","github":"#c8ccca","telegram":"#26A5E4",
    "slack":"#E01E5A","matrix":"#0DBD8B","signal":"#3A76F0",
    "whatsapp":"#25D366","keybase":"#FF6F21",
}

SOCIAL = [
    ("twitter","Twitter","Follow",PA["twitter"]),
    ("x","X","Follow",PA["x"]),
    ("instagram","Instagram","Follow",PA["instagram"]),
    ("linkedin","LinkedIn","Connect",PA["linkedin"]),
    ("youtube","YouTube","Subscribe",PA["youtube"]),
    ("tiktok","TikTok","Follow",PA["tiktok"]),
    ("mastodon","Mastodon","Follow",PA["mastodon"]),
    ("bluesky","Bluesky","Follow",PA["bluesky"]),
    ("share",None,"Share",DARK_ACCENT),
    ("star",None,"Star",DARK_ACCENT),
    ("sponsor",None,"Sponsor","#ff6b8b"),
    ("newsletter",None,"Newsletter",DARK_ACCENT),
]

COMMS = [
    ("discord","Discord","Join Server",PA["discord"]),
    ("github","GitHub","Star Repo",PA["github"]),
    ("telegram","Telegram","Join Channel",PA["telegram"]),
    ("slack","Slack","Join Workspace",PA["slack"]),
    ("matrix","Matrix","Join Room",PA["matrix"]),
    ("signal","Signal","Message Us",PA["signal"]),
    ("whatsapp","WhatsApp","Chat",PA["whatsapp"]),
    ("keybase","Keybase","Encrypted Chat",PA["keybase"]),
    ("chat",None,"Open Chat",DARK_ACCENT),
    ("forum",None,"Discuss",DARK_ACCENT),
    ("docs",None,"Docs",DARK_ACCENT),
    ("support",None,"Support","#ffd166"),
    ("email",None,"Email Us",DARK_ACCENT),
    ("secure_channel",None,"Secure Channel",DARK_ACCENT),
]

REPO = [
    ("status-stable","Status","Stable","#1fe8a8"),
    ("status-experimental","Status","Experimental","#ff9f1c"),
    ("status-deprecated","Status","Deprecated","#888888"),
    ("status-archived","Status","Archived","#aaaaaa"),
    ("status-wip","Status","In Progress","#ffd166"),
    ("status-maintained","Status","Maintained","#1fe8a8"),
    ("license-mit","License","MIT","#1fe8a8"),
    ("license-apache2","License","Apache 2.0","#1fe8a8"),
    ("license-gpl3","License","GPL 3.0","#1fe8a8"),
    ("license-proprietary","License","Proprietary","#ff6b6b"),
    ("license-bsl","License","BSL 1.1","#a78bfa"),
    ("build-passing","Build","Passing","#1fe8a8"),
    ("build-failing","Build","Failing","#ff6b6b"),
    ("build-pending","Build","Pending","#ffd166"),
    ("security-pq","Security","Post-Quantum","#1fe8a8"),
    ("security-encrypted","Security","E2E Encrypted","#1fe8a8"),
    ("security-audited","Security","Audited","#1fe8a8"),
    ("security-cve-free","Security","CVE Free","#1fe8a8"),
    ("contrib-welcome","Contrib","PRs Welcome","#a78bfa"),
    ("contrib-seeking","Contrib","Seeking Contribs","#a78bfa"),
    ("contrib-closed","Contrib","Closed","#888888"),
    ("version-alpha","Version","Alpha","#ff9f1c"),
    ("version-beta","Version","Beta","#ffd166"),
    ("version-stable","Version","Stable","#1fe8a8"),
    ("version-rc","Version","Release Candidate","#69C9D0"),
    ("lang-python","Lang","Python","#3776AB"),
    ("lang-go","Lang","Go","#00ADD8"),
    ("lang-rust","Lang","Rust","#CE422B"),
    ("lang-nodejs","Lang","Node.js","#539E43"),
    ("lang-c","Lang","C / C++","#6295CB"),
    ("platform-linux","Platform","Linux","#1fe8a8"),
    ("platform-wasm","Platform","WebAssembly","#654FF0"),
    ("platform-fpga","Platform","FPGA / ASIC","#1fe8a8"),
]


def run_batch(name, definitions, out_dir, sizes):
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for entry in definitions:
        stem, tag, txt, accent = entry
        for sfx, w, h in sizes:
            svg = make_badge(txt, accent=accent, w=w, h=h,
                             tag=tag, tag_color=accent,
                             dur=5 + abs(hash(stem)) % 4)
            path = os.path.join(out_dir, f"{stem}{sfx}.svg")
            with open(path, "w") as f:
                f.write(svg)
            n += 1
    print(f"  {name}: {n} badges → {out_dir}")
    return n


def main():
    parser = argparse.ArgumentParser(description="VRIL LABS badge generator")
    parser.add_argument("mode", nargs="?", default="all",
                        help='all | social | comms | repo | custom')
    parser.add_argument("label", nargs="?", help="Label text (custom mode)")
    parser.add_argument("--accent", default=DARK_ACCENT)
    parser.add_argument("--tag", default=None)
    parser.add_argument("--tag-color", default=None)
    parser.add_argument("--width", type=int, default=220)
    parser.add_argument("--height", type=int, default=34)
    parser.add_argument("--dur", type=int, default=5)
    parser.add_argument("--out", default=".")
    args = parser.parse_args()

    base = args.out

    if args.mode == "custom":
        if not args.label:
            print("ERROR: provide a label text for custom mode"); sys.exit(1)
        svg = make_badge(args.label, accent=args.accent,
                         w=args.width, h=args.height,
                         tag=args.tag, tag_color=args.tag_color,
                         dur=args.dur)
        fname = args.label.lower().replace(" ", "-") + ".svg"
        path = os.path.join(args.out, fname)
        with open(path, "w") as f:
            f.write(svg)
        print(f"Custom badge → {path}")
        return

    batches = {
        "social": (SOCIAL, os.path.join(base, "social"),
                   [("", 200, 34), ("-wide", 280, 38)]),
        "comms":  (COMMS,  os.path.join(base, "comms"),
                   [("", 220, 34), ("-wide", 310, 38)]),
        "repo":   (REPO,   os.path.join(base, "repo"),
                   [("", 220, 34), ("-wide", 290, 38)]),
    }

    total = 0
    selected = batches.keys() if args.mode == "all" else [args.mode]
    for key in selected:
        defs, out, sizes = batches[key]
        total += run_batch(key, defs, out, sizes)
    print(f"Done — {total} total SVGs generated.")


if __name__ == "__main__":
    main()
