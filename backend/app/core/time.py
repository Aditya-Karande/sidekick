# Always store dates and times as timezone-aware UTC timestamps to avoid timezone-related bugs.

from datetime import datetime, timezone

def utcnow() -> datetime:
    return datetime.now(timezone.utc)