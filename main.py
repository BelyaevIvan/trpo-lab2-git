from data import students
from grades import average, grade_name, is_passed

print(f"Студентов в группе: {len(students)}")

for name, marks in students.items():
    avg = round(average(marks), 2)
    status = "аттестован" if is_passed(marks) else "не аттестован"
    print(f"{name}: средний балл {avg}, {status}")
    print("  оценки:", ", ".join(grade_name(m) for m in marks))
