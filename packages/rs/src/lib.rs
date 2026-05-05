//! glitch-badges — Rust library
//!
//! Generate animated VRIL LABS glitch badge SVGs with zero runtime dependencies.
//!
//! # Examples
//!
//! ```rust
//! use glitch_badges::{BadgeOptions, make_badge, badge_url};
//!
//! // Generate a custom badge SVG
//! let svg = make_badge(BadgeOptions {
//!     text: "POST QUANTUM".into(),
//!     accent: "#a78bfa".into(),
//!     tag: Some("Security".into()),
//!     width: 260,
//!     ..Default::default()
//! });
//! std::fs::write("security-pq.svg", svg).unwrap();
//!
//! // Get the CDN URL for a pre-built badge
//! let url = badge_url("repo", "security-pq", true);
//! ```

// ── Brand tokens ─────────────────────────────────────────────────────────────
pub const DARK_BG: &str     = "#0b0c0b";
pub const DARK_BORDER: &str = "#1a2a24";
pub const DARK_ACCENT: &str = "#1fe8a8";
pub const DARK_MUTED: &str  = "#4a7060";
pub const GLITCH_RED: &str  = "#ff3366";
pub const GLITCH_CYAN: &str = "#33ffee";
pub const SCAN_COLOR: &str  = "rgba(31,232,168,0.025)";

const BADGE_BASE: &str =
    "https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges";

// ── Types ─────────────────────────────────────────────────────────────────────
/// Configuration for badge generation.
#[derive(Debug, Clone)]
pub struct BadgeOptions {
    /// Right-side label text (e.g. `"POST QUANTUM"`).
    pub text: String,
    /// Hex accent colour (default: `"#1fe8a8"`).
    pub accent: String,
    /// Badge width in pixels (default: `220`).
    pub width: u32,
    /// Badge height in pixels (default: `36`).
    pub height: u32,
    /// Optional left-side tag label (e.g. `Some("Security")`).
    pub tag: Option<String>,
    /// Colour for the tag section (defaults to `accent`).
    pub tag_color: Option<String>,
    /// Glitch animation cycle in seconds (default: `5`).
    pub duration: u32,
}

impl Default for BadgeOptions {
    fn default() -> Self {
        Self {
            text:      String::new(),
            accent:    DARK_ACCENT.into(),
            width:     220,
            height:    36,
            tag:       None,
            tag_color: None,
            duration:  5,
        }
    }
}

// ── Core generator ────────────────────────────────────────────────────────────
/// Generate a standalone animated glitch badge SVG string.
pub fn make_badge(opts: BadgeOptions) -> String {
    let tc  = opts.tag_color.as_deref().unwrap_or(&opts.accent).to_string();
    let fs  = (opts.width as f64 * 0.056).round().clamp(9.0, 15.0) as u32;
    let esc = opts.text.replace('\'', "\\'");
    let dur = opts.duration;
    let w   = opts.width;
    let h   = opts.height;

    let tag_css = if opts.tag.is_some() {
        format!(
            ".tag{{background:{tc}18;border-right:1px solid {tc}40;\
             padding:0 10px;font-size:{tag_fs}px;letter-spacing:.15em;\
             text-transform:uppercase;color:{tc};height:100%;\
             display:flex;align-items:center;flex-shrink:0;white-space:nowrap;}}",
            tag_fs = fs.saturating_sub(2).max(8)
        )
    } else {
        String::new()
    };

    let tag_html = opts.tag.as_deref()
        .map(|t| format!(r#"<div class="tag">{t}</div>"#))
        .unwrap_or_default();

    let jc = if opts.tag.is_some() { "" } else { "justify-content:center;" };
    let inner_extra = if opts.tag.is_some() { "flex:1;justify-content:center;" } else { "" };
    let accent = &opts.accent;

    format!(
        r#"<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<foreignObject width="100%" height="100%">
<div xmlns="http://www.w3.org/1999/xhtml">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
.badge{{width:{w}px;height:{h}px;background:{bg};border:1px solid {border};
  border-radius:4px;display:flex;align-items:center;{jc}
  position:relative;overflow:hidden;
  font-family:ui-monospace,'SF Mono','Fira Mono',Consolas,monospace;}}
.badge::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,{accent},transparent);}}{tag_css}
.inner{{display:flex;align-items:center;{inner_extra}padding:0 12px;height:100%;}}
.lbl{{font-size:{fs}px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:{accent};position:relative;user-select:none;white-space:nowrap;}}
.lbl::before,.lbl::after{{content:'{esc}';position:absolute;top:0;left:0;width:100%;height:100%;opacity:0;}}
.lbl::before{{color:{red};mix-blend-mode:screen;}}
.lbl::after{{color:{cyan};mix-blend-mode:screen;}}
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
  background:repeating-linear-gradient(0deg,transparent,transparent 3px,{scan} 3px,{scan} 4px);
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
  {tag_html}<div class="inner"><div class="lbl">{text}</div></div>
</div></div></foreignObject></svg>"#,
        bg     = DARK_BG,
        border = DARK_BORDER,
        red    = GLITCH_RED,
        cyan   = GLITCH_CYAN,
        scan   = SCAN_COLOR,
        text   = opts.text,
    )
}

/// Return the raw GitHub CDN URL for a pre-built badge SVG.
///
/// # Arguments
/// * `collection` — `"social"`, `"comms"`, `"repo"`, or `"status"`
/// * `slug`       — badge filename without extension, e.g. `"security-pq"`
/// * `wide`       — whether to use the wider variant
pub fn badge_url(collection: &str, slug: &str, wide: bool) -> String {
    let suffix = if wide { "-wide" } else { "" };
    format!("{BADGE_BASE}/{collection}/{slug}{suffix}.svg")
}

/// Return an HTML `<img>` tag for a pre-built badge.
pub fn badge_img(collection: &str, slug: &str, alt: &str, wide: bool) -> String {
    let url = badge_url(collection, slug, wide);
    let w   = if wide { 290 } else { 220 };
    format!(r#"<img src="{url}" width="{w}" height="34" alt="{alt}"/>"#)
}

// ── Tests ─────────────────────────────────────────────────────────────────────
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn make_badge_contains_text() {
        let svg = make_badge(BadgeOptions {
            text: "HELLO".into(),
            ..Default::default()
        });
        assert!(svg.contains("HELLO"));
        assert!(svg.contains("<svg"));
        assert!(svg.contains("</svg>"));
    }

    #[test]
    fn make_badge_with_tag() {
        let svg = make_badge(BadgeOptions {
            text:   "PASSING".into(),
            accent: "#1fe8a8".into(),
            tag:    Some("Build".into()),
            width:  220,
            height: 36,
            ..Default::default()
        });
        assert!(svg.contains("PASSING"));
        assert!(svg.contains("Build"));
    }

    #[test]
    fn badge_url_standard() {
        let url = badge_url("repo", "security-pq", false);
        assert_eq!(
            url,
            "https://raw.githubusercontent.com/dubzrn/glitch-badges/main/.github/profile/assets/badges/repo/security-pq.svg"
        );
    }

    #[test]
    fn badge_url_wide() {
        let url = badge_url("social", "twitter", true);
        assert!(url.ends_with("twitter-wide.svg"));
    }
}
