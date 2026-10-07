from grades import average, grade_name, is_passed

students = {
    "Иванов": [5, 4, 5],
    "Петров": [3, 4, 4],
    "Сидоров": [4, 2, 3],
}

for name, marks in students.items():
    avg = round(average(marks), 2)
    status = "аттестован" if is_passed(marks) else "не аттестован"
    print(f"{name}: средний балл {avg}, {status}")
    print("  оценки:", ", ".join(grade_name(m) for m in marks))
