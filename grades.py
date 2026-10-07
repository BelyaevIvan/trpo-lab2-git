"""Модуль учёта успеваемости студентов."""

PASS_MARK = 4  # минимальная положительная оценка


def average(marks):
    """Средний балл по списку оценок (0 для пустого списка)."""
    return sum(marks) / len(marks) if marks else 0


def grade_name(mark):
    """Текстовое название оценки."""
    names = {5: "отлично", 4: "хорошо", 3: "удовлетворительно", 2: "неудовлетворительно", 1: "плохо"}
    return names.get(mark, "нет оценки")


def is_passed(marks):
    """Студент аттестован, если нет оценок ниже PASS_MARK."""
    return all(m >= PASS_MARK for m in marks)


def count_debts(marks):
    """Количество задолженностей (оценок ниже PASS_MARK)."""
    return sum(1 for m in marks if m < PASS_MARK)
