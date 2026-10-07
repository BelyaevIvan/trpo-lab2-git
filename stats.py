"""Статистические функции для оценок."""


def median(marks):
    """Медиана списка оценок."""
    if not marks:
        return 0
    s = sorted(marks)
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2
