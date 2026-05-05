/**
 * glitch-badges — main entry point
 * Re-exports everything needed to generate, lookup, and embed glitch badges.
 */
export {
  makeBadge,
  badgeUrl,
  badgeImg,
  // Brand tokens
  DARK_BG,
  DARK_BORDER,
  DARK_ACCENT,
  DARK_MUTED,
  GLITCH_RED,
  GLITCH_CYAN,
  SCAN_COLOR,
} from "./core.js";

export type { BadgeOptions } from "./core.js";

export {
  ALL_PRESETS,
  SOCIAL_PRESETS,
  COMMS_PRESETS,
  REPO_PRESETS,
  STATUS_PRESETS,
  getPreset,
} from "./presets.js";

export type { Preset } from "./presets.js";
