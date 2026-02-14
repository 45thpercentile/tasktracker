import re
from datetime import datetime


def validate_email(email):
    """Check if an email address is valid."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def format_date(dt):
    """Format a datetime object for display."""
    return dt.strftime("%Y-%m-%d %H:%M")


def truncate(text, max_length=50):
    """Truncate text to a maximum length."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def generate_id(prefix, counter):
    """Generate a simple ID string."""
    return f"{prefix}-{counter:04d}"


def parse_priority(priority_str):
    """Convert a priority string to a numeric value."""
    priorities = {"low": 1, "medium": 2, "high": 3}
    return priorities.get(priority_str.lower(), 0)
