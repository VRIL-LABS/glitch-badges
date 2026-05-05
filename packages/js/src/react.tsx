/**
 * glitch-badges/react
 *
 * Drop-in React component that renders a glitch badge SVG inline (no network
 * request) or as an <img> pointing to the pre-built raw GitHub URL.
 */
import React from "react";
import { makeBadge, badgeUrl, type BadgeOptions } from "./core.js";
import type { Preset } from "./presets.js";

// ── Inline SVG component ─────────────────────────────────────────────────────
export interface GlitchBadgeProps extends BadgeOptions {
  /** Accessible alt text (defaults to "text" or "tag: text") */
  alt?: string;
  /** Additional CSS class name */
  className?: string;
  /** Inline style override */
  style?: React.CSSProperties;
}

/**
 * Renders a glitch badge as an inline `<span>` containing a raw SVG string.
 * Works in any React environment that renders HTML (not RN).
 *
 * @example
 * <GlitchBadge text="POST QUANTUM" accent="#a78bfa" tag="Security" width={260} />
 */
export const GlitchBadge: React.FC<GlitchBadgeProps> = ({
  alt,
  className,
  style,
  ...opts
}) => {
  const svg = makeBadge(opts);
  const label = alt ?? (opts.tag ? `${opts.tag}: ${opts.text}` : opts.text);
  return (
    <span
      role="img"
      aria-label={label}
      className={className}
      style={{ display: "inline-block", lineHeight: 0, ...style }}
      dangerouslySetInnerHTML={{ __html: svg }}
    />
  );
};

// ── Image URL component ──────────────────────────────────────────────────────
export interface GlitchBadgeImgProps {
  /** Preset slug, e.g. "security-pq" or "twitter" */
  slug: string;
  /** Collection the badge lives in */
  collection?: "social" | "comms" | "repo" | "status";
  /** Use the wide variant */
  wide?: boolean;
  /** Accessible alt text */
  alt?: string;
  /** Override width (px) */
  width?: number;
  /** Override height (px) */
  height?: number;
  /** Additional class name */
  className?: string;
  /** Inline style override */
  style?: React.CSSProperties;
}

/**
 * Renders a `<img>` pointing to the pre-built SVG on GitHub raw CDN.
 *
 * @example
 * <GlitchBadgeImg collection="repo" slug="security-pq" wide alt="Post-Quantum" />
 */
export const GlitchBadgeImg: React.FC<GlitchBadgeImgProps> = ({
  slug,
  collection = "repo",
  wide = false,
  alt = slug,
  width,
  height = 34,
  className,
  style,
}) => {
  const src  = badgeUrl(collection, slug, wide);
  const w    = width ?? (wide ? 290 : 220);
  return (
    <img
      src={src}
      width={w}
      height={height}
      alt={alt}
      className={className}
      style={style}
    />
  );
};

// ── Preset-based component ───────────────────────────────────────────────────
export interface GlitchBadgePresetProps {
  preset: Preset;
  wide?: boolean;
  /** "inline" renders the SVG directly; "img" uses the CDN URL (default: "img") */
  mode?: "inline" | "img";
  className?: string;
  style?: React.CSSProperties;
}

/**
 * Render a badge from a preset object (from `SOCIAL_PRESETS`, `REPO_PRESETS`, etc.)
 */
export const GlitchBadgeFromPreset: React.FC<GlitchBadgePresetProps> = ({
  preset,
  wide = false,
  mode = "img",
  ...rest
}) => {
  if (mode === "inline") {
    return (
      <GlitchBadge
        text={preset.text}
        tag={preset.tag ?? undefined}
        accent={preset.accent}
        width={wide ? 290 : 220}
        {...rest}
      />
    );
  }
  return (
    <GlitchBadgeImg
      slug={preset.slug}
      collection={preset.collection}
      wide={wide}
      alt={preset.tag ? `${preset.tag}: ${preset.text}` : preset.text}
      {...rest}
    />
  );
};
