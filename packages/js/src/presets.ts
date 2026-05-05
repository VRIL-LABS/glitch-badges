/**
 * glitch-badges/presets
 * Pre-defined badge specs for all three collections.
 */
import type { BadgeOptions } from "./core.js";

export interface Preset extends BadgeOptions {
  slug: string;
  collection: "social" | "comms" | "repo" | "status";
}

// ── Social ───────────────────────────────────────────────────────────────────
export const SOCIAL_PRESETS: Preset[] = [
  { slug: "twitter",    collection: "social", text: "Follow",     tag: "Twitter",    accent: "#1DA1F2" },
  { slug: "x",          collection: "social", text: "Follow",     tag: "X",          accent: "#e7e7e7" },
  { slug: "instagram",  collection: "social", text: "Follow",     tag: "Instagram",  accent: "#E1306C" },
  { slug: "linkedin",   collection: "social", text: "Connect",    tag: "LinkedIn",   accent: "#0A66C2" },
  { slug: "youtube",    collection: "social", text: "Subscribe",  tag: "YouTube",    accent: "#FF0000" },
  { slug: "tiktok",     collection: "social", text: "Follow",     tag: "TikTok",     accent: "#69C9D0" },
  { slug: "mastodon",   collection: "social", text: "Follow",     tag: "Mastodon",   accent: "#6364FF" },
  { slug: "bluesky",    collection: "social", text: "Follow",     tag: "Bluesky",    accent: "#0085FF" },
  { slug: "share",      collection: "social", text: "Share",      tag: undefined,         accent: "#1fe8a8" },
  { slug: "star",       collection: "social", text: "Star",       tag: undefined,         accent: "#1fe8a8" },
  { slug: "sponsor",    collection: "social", text: "Sponsor",    tag: undefined,         accent: "#ff6b8b" },
  { slug: "newsletter", collection: "social", text: "Newsletter", tag: undefined,         accent: "#1fe8a8" },
];

// ── Comms ────────────────────────────────────────────────────────────────────
export const COMMS_PRESETS: Preset[] = [
  { slug: "discord",     collection: "comms", text: "Join Server",      tag: "Discord",  accent: "#5865F2" },
  { slug: "github",      collection: "comms", text: "Star Repo",        tag: "GitHub",   accent: "#c8ccca" },
  { slug: "telegram",    collection: "comms", text: "Join Channel",     tag: "Telegram", accent: "#26A5E4" },
  { slug: "slack",       collection: "comms", text: "Join Workspace",   tag: "Slack",    accent: "#E01E5A" },
  { slug: "matrix",      collection: "comms", text: "Join Room",        tag: "Matrix",   accent: "#0DBD8B" },
  { slug: "signal",      collection: "comms", text: "Message Us",       tag: "Signal",   accent: "#3A76F0" },
  { slug: "whatsapp",    collection: "comms", text: "Chat",             tag: "WhatsApp", accent: "#25D366" },
  { slug: "keybase",     collection: "comms", text: "Encrypted Chat",   tag: "Keybase",  accent: "#FF6F21" },
  { slug: "chat",        collection: "comms", text: "Open Chat",        tag: undefined,       accent: "#1fe8a8" },
  { slug: "forum",       collection: "comms", text: "Discuss",          tag: undefined,       accent: "#1fe8a8" },
  { slug: "docs",        collection: "comms", text: "Docs",             tag: undefined,       accent: "#1fe8a8" },
  { slug: "support",     collection: "comms", text: "Support",          tag: undefined,       accent: "#ffd166" },
  { slug: "email",       collection: "comms", text: "Email Us",         tag: undefined,       accent: "#1fe8a8" },
  { slug: "secure_channel", collection: "comms", text: "Secure Channel", tag: undefined,      accent: "#1fe8a8" },
];

// ── Repo ─────────────────────────────────────────────────────────────────────
export const REPO_PRESETS: Preset[] = [
  // Status
  { slug: "status-stable",       collection: "repo", text: "Stable",        tag: "Status",   accent: "#1fe8a8" },
  { slug: "status-experimental", collection: "repo", text: "Experimental",  tag: "Status",   accent: "#ff9f1c" },
  { slug: "status-deprecated",   collection: "repo", text: "Deprecated",    tag: "Status",   accent: "#888888" },
  { slug: "status-archived",     collection: "repo", text: "Archived",      tag: "Status",   accent: "#aaaaaa" },
  { slug: "status-wip",          collection: "repo", text: "In Progress",   tag: "Status",   accent: "#ffd166" },
  { slug: "status-maintained",   collection: "repo", text: "Maintained",    tag: "Status",   accent: "#1fe8a8" },
  // License
  { slug: "license-mit",         collection: "repo", text: "MIT",           tag: "License",  accent: "#1fe8a8" },
  { slug: "license-apache2",     collection: "repo", text: "Apache 2.0",    tag: "License",  accent: "#1fe8a8" },
  { slug: "license-gpl3",        collection: "repo", text: "GPL 3.0",       tag: "License",  accent: "#1fe8a8" },
  { slug: "license-proprietary", collection: "repo", text: "Proprietary",   tag: "License",  accent: "#ff6b6b" },
  { slug: "license-bsl",         collection: "repo", text: "BSL 1.1",       tag: "License",  accent: "#a78bfa" },
  // Build
  { slug: "build-passing",       collection: "repo", text: "Passing",       tag: "Build",    accent: "#1fe8a8" },
  { slug: "build-failing",       collection: "repo", text: "Failing",       tag: "Build",    accent: "#ff6b6b" },
  { slug: "build-pending",       collection: "repo", text: "Pending",       tag: "Build",    accent: "#ffd166" },
  // Security
  { slug: "security-pq",         collection: "repo", text: "Post-Quantum",  tag: "Security", accent: "#1fe8a8" },
  { slug: "security-encrypted",  collection: "repo", text: "E2E Encrypted", tag: "Security", accent: "#1fe8a8" },
  { slug: "security-audited",    collection: "repo", text: "Audited",       tag: "Security", accent: "#1fe8a8" },
  { slug: "security-cve-free",   collection: "repo", text: "CVE Free",      tag: "Security", accent: "#1fe8a8" },
  // Contrib
  { slug: "contrib-welcome",     collection: "repo", text: "PRs Welcome",   tag: "Contrib",  accent: "#a78bfa" },
  { slug: "contrib-seeking",     collection: "repo", text: "Seeking Contribs", tag: "Contrib", accent: "#a78bfa" },
  { slug: "contrib-closed",      collection: "repo", text: "Closed",        tag: "Contrib",  accent: "#888888" },
  // Version
  { slug: "version-alpha",       collection: "repo", text: "Alpha",         tag: "Version",  accent: "#ff9f1c" },
  { slug: "version-beta",        collection: "repo", text: "Beta",          tag: "Version",  accent: "#ffd166" },
  { slug: "version-stable",      collection: "repo", text: "Stable",        tag: "Version",  accent: "#1fe8a8" },
  { slug: "version-rc",          collection: "repo", text: "Release Candidate", tag: "Version", accent: "#69C9D0" },
  // Language
  { slug: "lang-python",         collection: "repo", text: "Python",        tag: "Lang",     accent: "#3776AB" },
  { slug: "lang-go",             collection: "repo", text: "Go",            tag: "Lang",     accent: "#00ADD8" },
  { slug: "lang-rust",           collection: "repo", text: "Rust",          tag: "Lang",     accent: "#CE422B" },
  { slug: "lang-nodejs",         collection: "repo", text: "Node.js",       tag: "Lang",     accent: "#539E43" },
  { slug: "lang-c",              collection: "repo", text: "C / C++",       tag: "Lang",     accent: "#6295CB" },
  // Platform
  { slug: "platform-linux",      collection: "repo", text: "Linux",         tag: "Platform", accent: "#1fe8a8" },
  { slug: "platform-wasm",       collection: "repo", text: "WebAssembly",   tag: "Platform", accent: "#654FF0" },
  { slug: "platform-fpga",       collection: "repo", text: "FPGA / ASIC",   tag: "Platform", accent: "#1fe8a8" },
];

// ── Status (standalone) ──────────────────────────────────────────────────────
export const STATUS_PRESETS: Preset[] = [
  { slug: "status-passing",     collection: "status", text: "Passing",      tag: undefined, accent: "#1fe8a8" },
  { slug: "status-failing",     collection: "status", text: "Failing",      tag: undefined, accent: "#ff6b6b" },
  { slug: "status-pending",     collection: "status", text: "Pending",      tag: undefined, accent: "#ffd166" },
  { slug: "status-building",    collection: "status", text: "Building",     tag: undefined, accent: "#69C9D0" },
  { slug: "status-alpha",       collection: "status", text: "Alpha",        tag: undefined, accent: "#ff9f1c" },
  { slug: "status-beta",        collection: "status", text: "Beta",         tag: undefined, accent: "#ffd166" },
  { slug: "status-stable",      collection: "status", text: "Stable",       tag: undefined, accent: "#1fe8a8" },
  { slug: "status-deprecated",  collection: "status", text: "Deprecated",   tag: undefined, accent: "#888888" },
  { slug: "status-archived",    collection: "status", text: "Archived",     tag: undefined, accent: "#aaaaaa" },
  { slug: "status-wip",         collection: "status", text: "In Progress",  tag: undefined, accent: "#ffd166" },
  { slug: "status-maintained",  collection: "status", text: "Maintained",   tag: undefined, accent: "#1fe8a8" },
  { slug: "pq-ready",           collection: "status", text: "PQ Ready",     tag: undefined, accent: "#1fe8a8" },
  { slug: "security",           collection: "status", text: "Secure",       tag: undefined, accent: "#1fe8a8" },
  { slug: "open-source",        collection: "status", text: "Open Source",  tag: undefined, accent: "#1fe8a8" },
  { slug: "license-mit",        collection: "status", text: "MIT",          tag: undefined, accent: "#1fe8a8" },
  { slug: "license-apache",     collection: "status", text: "Apache 2.0",   tag: undefined, accent: "#1fe8a8" },
  { slug: "license-prop",       collection: "status", text: "Proprietary",  tag: undefined, accent: "#ff6b6b" },
  { slug: "sponsor",            collection: "status", text: "Sponsor",      tag: undefined, accent: "#ff6b8b" },
  { slug: "docs",               collection: "status", text: "Docs",         tag: undefined, accent: "#1fe8a8" },
  { slug: "contributing",       collection: "status", text: "Contributing", tag: undefined, accent: "#a78bfa" },
  { slug: "downloads",          collection: "status", text: "Downloads",    tag: undefined, accent: "#1fe8a8" },
  { slug: "coverage",           collection: "status", text: "Coverage",     tag: undefined, accent: "#1fe8a8" },
  { slug: "version-release",    collection: "status", text: "Release",      tag: undefined, accent: "#1fe8a8" },
  { slug: "version-prerelease", collection: "status", text: "Pre-Release",  tag: undefined, accent: "#ffd166" },
];

export const ALL_PRESETS: Preset[] = [
  ...SOCIAL_PRESETS,
  ...COMMS_PRESETS,
  ...REPO_PRESETS,
  ...STATUS_PRESETS,
];

/** Look up a preset by slug (case-insensitive). */
export function getPreset(slug: string): Preset | undefined {
  return ALL_PRESETS.find(p => p.slug.toLowerCase() === slug.toLowerCase());
}
