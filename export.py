"""Выгрузка результатов в CSV-файл."""

import csv

from grades import average, is_passed


def export_csv(students, path="results.csv"):
    """Сохраняет средний балл и статус аттестации каждого студента."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Студент", "Средний балл", "Аттестован"])
        for name, marks in students.items():
            writer.writerow([name, round(average(marks), 2), "да" if is_passed(marks) else "нет"])
    return path
