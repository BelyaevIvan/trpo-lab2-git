from data import students
from grades import average, grade_name, is_passed

print(f"Студентов в группе: {len(students)}")

# студенты выводятся по убыванию среднего балла
for name, marks in sorted(students.items(), key=lambda s: average(s[1]), reverse=True):
    avg = round(average(marks), 2)
    status = "аттестован" if is_passed(marks) else "не аттестован"
    print(f"{name}: средний балл {avg}, {status}")
    print("  оценки:", ", ".join(grade_name(m) for m in marks))
