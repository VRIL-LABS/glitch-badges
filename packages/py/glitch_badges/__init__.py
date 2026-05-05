"""
glitch_badges — Python SDK
VRIL LABS animated glitch badge generator.
"""

from .core import make_badge, badge_url, badge_img
from .presets import (
    ALL_PRESETS,
    SOCIAL_PRESETS,
    COMMS_PRESETS,
    REPO_PRESETS,
    STATUS_PRESETS,
    get_preset,
    Preset,
)

__version__ = "1.0.0"
__all__ = [
    "make_badge",
    "badge_url",
    "badge_img",
    "ALL_PRESETS",
    "SOCIAL_PRESETS",
    "COMMS_PRESETS",
    "REPO_PRESETS",
    "STATUS_PRESETS",
    "get_preset",
    "Preset",
]
