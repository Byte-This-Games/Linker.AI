# /version.py
# /_dev/

import os
from datetime import datetime, timezone
from typing import Final

# ────────────────────────────────────────────────────────────────
#          OFFICIAL IDENTITY
# ────────────────────────────────────────────────────────────────
# Accordoding to Grok, this has no conflicts on any app stores in this field.
# Needs to be checked again properly before release.
APP_NAME: Final[str] = "Linker.ai"
APP_TAGLINE: Final[str] = "Hack your heart. Link your soul."

# ────────────────────────────────────────────────────────────────
#          VERSIONING
# ────────────────────────────────────────────────────────────────

ALPHA_MAJOR: Final[int] = 1
ALPHA_MINOR: Final[int] = 0
ALPHA_PATCH: Final[int] = 0
ALPHA_RELEASE: Final[str] = "Closed Alpha version"

# BETA_MAJOR: Final[int] = 1
# BETA_MINOR: Final[int] = 0
# BETA_PATCH: Final[int] = 0
# BETA_RELEASE: Final[str] = "Open Beta version"

# RELEASE_MAJOR: Final[int] = 1
# RELEASE_MINOR: Final[int] = 0
# RELEASE_PATCH: Final[int] = 0
# RELEASE_RELEASE: Final[str] = "Release version"

ALPHA_VERSION_CODENAMES = {
    "1.0.0": "Linker AI"
}

# ────────────────────────────────────────────────────────────────
#          CODENAME RESOLUTION
# ────────────────────────────────────────────────────────────────


def resolve_codename(version: str) -> str:
    if version in ALPHA_VERSION_CODENAMES:
        return ALPHA_VERSION_CODENAMES[version]

    # 2️⃣ Fallback to major.minor arc (e.g. 1.5.x → Behemoth)
    major_minor = ".".join(version.split(".")[:2]) + ".0"
    return ALPHA_VERSION_CODENAMES.get(major_minor, "Unknown Unit")

# ────────────────────────────────────────────────────────────────
#          ENVIRONMENT FLAGS
# ────────────────────────────────────────────────────────────────

DEBUG: Final[bool] = os.getenv("LINKER_AI_DEBUG", "0") == "1"
DETERMINISTIC: Final[bool] = os.getenv("LINKER_AI_DETERMINISTIC", "0") == "1"
OFFLINE_MODE: Final[bool] = os.getenv(
    "LINKER_AI_OFFLINE", "0") == "1"

# ────────────────────────────────────────────────────────────────
#          BUILD / RUNTIME METADATA
# ────────────────────────────────────────────────────────────────

BUILD_TIMESTAMP: Final[str] = datetime.now(
    timezone.utc).isoformat(timespec="seconds") + "Z"

# ────────────────────────────────────────────────────────────────
#          __all__ for clean imports
# ────────────────────────────────────────────────────────────────

__all__ = [
    "APP_NAME", "APP_TAGLINE",
    "DEBUG", "DETERMINISTIC", "OFFLINE_MODE",
    "BUILD_TIMESTAMP", "PROJECT_SLOGAN",
]