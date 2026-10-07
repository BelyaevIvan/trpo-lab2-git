"""Формирование текстового отчёта об успеваемости."""

from grades import average, count_debts


def make_report(students):
    """Возвращает отчёт по группе в виде строки."""
    lines = ["Отчёт об успеваемости группы", "-" * 44]
    for name, marks in students.items():
        lines.append(f"{name:<12} ср. балл {average(marks):.2f}   задолженностей: {count_debts(marks)}")
    return "\n".join(lines)
