"""Simple calculator module for task metrics."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def percentage(part, whole):
    """Calculate what percentage 'part' is of 'whole'."""
    if whole == 0:
        return 0.0
    return (part / whole) * 100


def completion_rate(done_count, total_count):
    """Calculate task completion rate."""
    return percentage(done_count, total_count)
