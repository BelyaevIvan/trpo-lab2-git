"""Модуль учёта успеваемости студентов."""

PASS_MARK = 3  # минимальная положительная оценка

# TODO: добавить подсчёт задолженностей


def average(marks):
    """Средний балл по списку оценок."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def grade_name(mark):
    """Текстовое название оценки."""
    names = {5: "отлично", 4: "хорошо", 3: "удовлетворительно", 2: "неудовлетворительно"}
    return names[mark]


def is_passed(marks):
    """Студент аттестован, если нет оценок ниже PASS_MARK."""
    return all(m >= PASS_MARK for m in marks)
