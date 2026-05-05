"""glitch_badges.presets — pre-defined badge specs for all collections."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Preset:
    slug:       str
    collection: str   # "social" | "comms" | "repo" | "status"
    text:       str
    accent:     str
    tag:        Optional[str] = None


SOCIAL_PRESETS: list[Preset] = [
    Preset("twitter",    "social", "Follow",     "#1DA1F2", "Twitter"),
    Preset("x",          "social", "Follow",     "#e7e7e7", "X"),
    Preset("instagram",  "social", "Follow",     "#E1306C", "Instagram"),
    Preset("linkedin",   "social", "Connect",    "#0A66C2", "LinkedIn"),
    Preset("youtube",    "social", "Subscribe",  "#FF0000", "YouTube"),
    Preset("tiktok",     "social", "Follow",     "#69C9D0", "TikTok"),
    Preset("mastodon",   "social", "Follow",     "#6364FF", "Mastodon"),
    Preset("bluesky",    "social", "Follow",     "#0085FF", "Bluesky"),
    Preset("share",      "social", "Share",      "#1fe8a8"),
    Preset("star",       "social", "Star",       "#1fe8a8"),
    Preset("sponsor",    "social", "Sponsor",    "#ff6b8b"),
    Preset("newsletter", "social", "Newsletter", "#1fe8a8"),
]

COMMS_PRESETS: list[Preset] = [
    Preset("discord",        "comms", "Join Server",    "#5865F2", "Discord"),
    Preset("github",         "comms", "Star Repo",      "#c8ccca", "GitHub"),
    Preset("telegram",       "comms", "Join Channel",   "#26A5E4", "Telegram"),
    Preset("slack",          "comms", "Join Workspace", "#E01E5A", "Slack"),
    Preset("matrix",         "comms", "Join Room",      "#0DBD8B", "Matrix"),
    Preset("signal",         "comms", "Message Us",     "#3A76F0", "Signal"),
    Preset("whatsapp",       "comms", "Chat",           "#25D366", "WhatsApp"),
    Preset("keybase",        "comms", "Encrypted Chat", "#FF6F21", "Keybase"),
    Preset("chat",           "comms", "Open Chat",      "#1fe8a8"),
    Preset("forum",          "comms", "Discuss",        "#1fe8a8"),
    Preset("docs",           "comms", "Docs",           "#1fe8a8"),
    Preset("support",        "comms", "Support",        "#ffd166"),
    Preset("email",          "comms", "Email Us",       "#1fe8a8"),
    Preset("secure_channel", "comms", "Secure Channel", "#1fe8a8"),
]

REPO_PRESETS: list[Preset] = [
    # Status
    Preset("status-stable",       "repo", "Stable",            "#1fe8a8", "Status"),
    Preset("status-experimental", "repo", "Experimental",      "#ff9f1c", "Status"),
    Preset("status-deprecated",   "repo", "Deprecated",        "#888888", "Status"),
    Preset("status-archived",     "repo", "Archived",          "#aaaaaa", "Status"),
    Preset("status-wip",          "repo", "In Progress",       "#ffd166", "Status"),
    Preset("status-maintained",   "repo", "Maintained",        "#1fe8a8", "Status"),
    # License
    Preset("license-mit",         "repo", "MIT",               "#1fe8a8", "License"),
    Preset("license-apache2",     "repo", "Apache 2.0",        "#1fe8a8", "License"),
    Preset("license-gpl3",        "repo", "GPL 3.0",           "#1fe8a8", "License"),
    Preset("license-proprietary", "repo", "Proprietary",       "#ff6b6b", "License"),
    Preset("license-bsl",         "repo", "BSL 1.1",           "#a78bfa", "License"),
    # Build
    Preset("build-passing",       "repo", "Passing",           "#1fe8a8", "Build"),
    Preset("build-failing",       "repo", "Failing",           "#ff6b6b", "Build"),
    Preset("build-pending",       "repo", "Pending",           "#ffd166", "Build"),
    # Security
    Preset("security-pq",         "repo", "Post-Quantum",      "#1fe8a8", "Security"),
    Preset("security-encrypted",  "repo", "E2E Encrypted",     "#1fe8a8", "Security"),
    Preset("security-audited",    "repo", "Audited",           "#1fe8a8", "Security"),
    Preset("security-cve-free",   "repo", "CVE Free",          "#1fe8a8", "Security"),
    # Contrib
    Preset("contrib-welcome",     "repo", "PRs Welcome",       "#a78bfa", "Contrib"),
    Preset("contrib-seeking",     "repo", "Seeking Contribs",  "#a78bfa", "Contrib"),
    Preset("contrib-closed",      "repo", "Closed",            "#888888", "Contrib"),
    # Version
    Preset("version-alpha",       "repo", "Alpha",             "#ff9f1c", "Version"),
    Preset("version-beta",        "repo", "Beta",              "#ffd166", "Version"),
    Preset("version-stable",      "repo", "Stable",            "#1fe8a8", "Version"),
    Preset("version-rc",          "repo", "Release Candidate", "#69C9D0", "Version"),
    # Language
    Preset("lang-python",         "repo", "Python",            "#3776AB", "Lang"),
    Preset("lang-go",             "repo", "Go",                "#00ADD8", "Lang"),
    Preset("lang-rust",           "repo", "Rust",              "#CE422B", "Lang"),
    Preset("lang-nodejs",         "repo", "Node.js",           "#539E43", "Lang"),
    Preset("lang-c",              "repo", "C / C++",           "#6295CB", "Lang"),
    # Platform
    Preset("platform-linux",      "repo", "Linux",             "#1fe8a8", "Platform"),
    Preset("platform-wasm",       "repo", "WebAssembly",       "#654FF0", "Platform"),
    Preset("platform-fpga",       "repo", "FPGA / ASIC",       "#1fe8a8", "Platform"),
]

STATUS_PRESETS: list[Preset] = [
    Preset("status-passing",     "status", "Passing",      "#1fe8a8"),
    Preset("status-failing",     "status", "Failing",      "#ff6b6b"),
    Preset("status-pending",     "status", "Pending",      "#ffd166"),
    Preset("status-building",    "status", "Building",     "#69C9D0"),
    Preset("status-alpha",       "status", "Alpha",        "#ff9f1c"),
    Preset("status-beta",        "status", "Beta",         "#ffd166"),
    Preset("status-stable",      "status", "Stable",       "#1fe8a8"),
    Preset("status-deprecated",  "status", "Deprecated",   "#888888"),
    Preset("status-archived",    "status", "Archived",     "#aaaaaa"),
    Preset("status-wip",         "status", "In Progress",  "#ffd166"),
    Preset("status-maintained",  "status", "Maintained",   "#1fe8a8"),
    Preset("pq-ready",           "status", "PQ Ready",     "#1fe8a8"),
    Preset("security",           "status", "Secure",       "#1fe8a8"),
    Preset("open-source",        "status", "Open Source",  "#1fe8a8"),
    Preset("license-mit",        "status", "MIT",          "#1fe8a8"),
    Preset("license-apache",     "status", "Apache 2.0",   "#1fe8a8"),
    Preset("license-prop",       "status", "Proprietary",  "#ff6b6b"),
    Preset("sponsor",            "status", "Sponsor",      "#ff6b8b"),
    Preset("docs",               "status", "Docs",         "#1fe8a8"),
    Preset("contributing",       "status", "Contributing", "#a78bfa"),
    Preset("downloads",          "status", "Downloads",    "#1fe8a8"),
    Preset("coverage",           "status", "Coverage",     "#1fe8a8"),
    Preset("version-release",    "status", "Release",      "#1fe8a8"),
    Preset("version-prerelease", "status", "Pre-Release",  "#ffd166"),
]

ALL_PRESETS: list[Preset] = (
    SOCIAL_PRESETS + COMMS_PRESETS + REPO_PRESETS + STATUS_PRESETS
)


def get_preset(slug: str) -> Preset | None:
    """Look up a preset by slug (case-insensitive)."""
    slug_lower = slug.lower()
    for p in ALL_PRESETS:
        if p.slug.lower() == slug_lower:
            return p
    return None
