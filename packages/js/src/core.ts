/**
 * glitch-badges — core SVG generator
 *
 * Pure TypeScript, zero dependencies. Produces the same animated glitch SVG
 * as the Python badge_generator.py, using foreignObject + CSS for maximum
 * fidelity in GitHub README contexts.
 */

// ── Brand tokens ────────────────────────────────────────────────────────────
export const DARK_BG     = "#0b0c0b" as const;
export const DARK_BORDER = "#1a2a24" as const;
export const DARK_ACCENT = "#1fe8a8" as const;
export const DARK_MUTED  = "#4a7060" as const;
export const GLITCH_RED  = "#ff3366" as const;
export const GLITCH_CYAN = "#33ffee" as const;
export const SCAN_COLOR  = "rgba(31,232,168,0.025)" as const;

// ── Types ────────────────────────────────────────────────────────────────────
export interface BadgeOptions {
  /** Right-side label text */
  text: string;
  /** Hex accent colour (default: VRIL seafoam #1fe8a8) */
  accent?: string;
  /** Badge width in px (default: 220) */
  width?: number;
  /** Badge height in px (default: 36) */
  height?: number;
  /** Optional left-side tag label */
  tag?: string;
  /** Colour for the tag section (defaults to accent) */
  tagColor?: string;
  /** Glitch animation duration in seconds (default: 5) */
  duration?: number;
}

export interface BadgePreset {
  slug:      string;
  text:      string;
  accent:    string;
  tag:       string | null;
  tagColor:  string | null;
}

// ── Sanitization helpers ─────────────────────────────────────────────────────
/**
 * Escape a string for safe insertion into HTML content (text nodes, attributes).
 * Prevents XSS when user-supplied strings are embedded in the SVG's foreignObject HTML.
 */
function escapeHtml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#x27;");
}

/**
 * Escape a string for safe insertion as a CSS `content:'...'` value.
 * Escapes backslashes first, then single-quotes, newlines, and `<` to
 * prevent `</style>` injection that could break out of the style block.
 */
function escapeCssContent(str: string): string {
  return str
    .replace(/\\/g, "\\\\")  // backslash first
    .replace(/'/g, "\\'")        // single-quote
    .replace(/\n/g, "\\A ")     // newline
    .replace(/</g, "\\3C ");     // prevent </style> injection
}

/**
 * Validate that a value is a safe hex colour (e.g. "#1fe8a8" or "#fff").
 * Falls back to the default accent if the value looks unsafe.
 */
function safeColor(value: string, fallback: string): string {
  return /^#[0-9a-fA-F]{3,8}$/.test(value.trim()) ? value.trim() : fallback;
}

// ── Core generator ───────────────────────────────────────────────────────────
/**
 * Generate a standalone animated glitch badge SVG string.
 *
 * @example
 * const svg = makeBadge({ text: "POST QUANTUM", accent: "#a78bfa", tag: "Security" });
 * fs.writeFileSync("security-pq.svg", svg);
 */
export function makeBadge(options: BadgeOptions): string {
  const {
    text,
    accent    = DARK_ACCENT,
    width     = 220,
    height    = 36,
    tag       = null,
    tagColor  = null,
    duration  = 5,
  } = options;

  // Sanitize user-supplied inputs
  const safeText    = escapeHtml(text);
  const safeAccent  = safeColor(accent, DARK_ACCENT);
  const safeTagClr  = tagColor ? safeColor(tagColor, DARK_ACCENT) : safeAccent;
  const safeTag     = tag ? escapeHtml(tag) : null;
  const cssEsc      = escapeCssContent(text);

  const tc  = safeTagClr;
  const fs  = Math.max(9, Math.min(15, Math.round(width * 0.056)));

  const tagCss = safeTag
    ? `.tag{background:${tc}18;border-right:1px solid ${tc}40;` +
      `padding:0 10px;font-size:${Math.max(8, fs - 2)}px;letter-spacing:.15em;` +
      `text-transform:uppercase;color:${tc};height:100%;` +
      `display:flex;align-items:center;flex-shrink:0;white-space:nowrap;}`
    : "";

  const tagHtml = safeTag ? `<div class="tag">${safeTag}</div>` : "";
  const jc      = safeTag ? "" : "justify-content:center;";

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
<foreignObject width="100%" height="100%">
<div xmlns="http://www.w3.org/1999/xhtml">
<style>
*{margin:0;padding:0;box-sizing:border-box}
.badge{width:${width}px;height:${height}px;background:${DARK_BG};border:1px solid ${DARK_BORDER};
  border-radius:4px;display:flex;align-items:center;${jc}
  position:relative;overflow:hidden;
  font-family:ui-monospace,'SF Mono','Fira Mono',Consolas,monospace;}
.badge::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,${safeAccent},transparent);}${tagCss}
.inner{display:flex;align-items:center;${safeTag ? "flex:1;justify-content:center;" : ""}padding:0 12px;height:100%;}
.lbl{font-size:${fs}px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:${safeAccent};position:relative;user-select:none;white-space:nowrap;}
.lbl::before,.lbl::after{content:'${cssEsc}';position:absolute;top:0;left:0;width:100%;height:100%;opacity:0;}
.lbl::before{color:${GLITCH_RED};mix-blend-mode:screen;}
.lbl::after{color:${GLITCH_CYAN};mix-blend-mode:screen;}
.lbl{animation:gm ${duration}s steps(1) infinite;}
.lbl::before{animation:gr ${duration}s steps(1) infinite;}
.lbl::after{animation:gc ${duration}s steps(1) infinite;}
@keyframes gm{0%,89%,100%{transform:none;opacity:1}
  90%{transform:skewX(-1deg) translateX(2px);opacity:.9}91%{transform:none;opacity:1}
  93%{transform:skewX(.5deg) translateX(-1px);opacity:.95}94%{transform:none;opacity:1}
  96%{transform:skewX(-.5deg) translateX(1px);opacity:.9}97%{transform:none;opacity:1}}
@keyframes gr{0%,89%,100%{transform:translateX(0);opacity:0}
  90%{transform:translateX(-3px);opacity:.7}91%{opacity:0}
  93%{transform:translateX(2px);opacity:.5}94%{opacity:0}
  96%{transform:translateX(-2px);opacity:.6}97%{opacity:0}}
@keyframes gc{0%,89%,100%{transform:translateX(0);opacity:0}
  90%{transform:translateX(3px);opacity:.6}91%{opacity:0}
  93%{transform:translateX(-2px);opacity:.5}94%{opacity:0}
  96%{transform:translateX(2px);opacity:.55}97%{opacity:0}}
.scan{position:absolute;inset:0;pointer-events:none;
  background:repeating-linear-gradient(0deg,transparent,transparent 3px,${SCAN_COLOR} 3px,${SCAN_COLOR} 4px);
  animation:fl ${duration}s steps(1) infinite;}
@keyframes fl{0%,89%,100%{opacity:1}90%{opacity:.55}91%{opacity:1}93%{opacity:.7}94%{opacity:1}}
.br{position:absolute;width:7px;height:7px;border-color:${safeAccent};border-style:solid;opacity:.35;}
.br-tl{top:4px;left:4px;border-width:1px 0 0 1px;}.br-tr{top:4px;right:4px;border-width:1px 1px 0 0;}
.br-bl{bottom:4px;left:4px;border-width:0 0 1px 1px;}.br-br{bottom:4px;right:4px;border-width:0 1px 1px 0;}
</style>
<div class="badge">
  <div class="scan"></div>
  <div class="br br-tl"></div><div class="br br-tr"></div>
  <div class="br br-bl"></div><div class="br br-br"></div>
  ${tagHtml}<div class="inner"><div class="lbl">${safeText}</div></div>
</div></div></foreignObject></svg>`;
}

// ── URL helper ───────────────────────────────────────────────────────────────
const BADGE_BASE =
  "https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges";

/**
 * Return the raw GitHub URL for a pre-built badge SVG.
 *
 * @param collection  "social" | "comms" | "repo" | "status"
 * @param slug        Badge filename without extension, e.g. "twitter" or "security-pq"
 * @param wide        Use the wider variant (default: false)
 *
 * @example
 * badgeUrl("repo", "security-pq", true)
 * // → https://raw.githubusercontent.com/.../repo/security-pq-wide.svg
 */
export function badgeUrl(
  collection: "social" | "comms" | "repo" | "status",
  slug: string,
  wide = false,
): string {
  const suffix = wide ? "-wide" : "";
  return `${BADGE_BASE}/${collection}/${slug}${suffix}.svg`;
}

/**
 * Return an HTML `<img>` tag pointing to a pre-built badge.
 */
export function badgeImg(
  collection: "social" | "comms" | "repo" | "status",
  slug: string,
  alt: string,
  wide = false,
): string {
  const url = badgeUrl(collection, slug, wide);
  const w   = wide ? 290 : 220;
  return `<img src="${url}" width="${w}" height="34" alt="${alt}"/>`;
}
