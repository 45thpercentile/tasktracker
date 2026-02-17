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


def search_tasks(tasks, query, case_sensitive=False):
    """Search tasks by title or description."""
    results = []
    for task in tasks:
        if case_sensitive:
            if query in task.title:
                results.append(task)
            elif query in task.description:
                results.append(task)
        else:
            if query.lower() in task.title.lower():
                results.append(task)
            elif query.lower() in task.description.lower():
                results.append(task)
    return results
