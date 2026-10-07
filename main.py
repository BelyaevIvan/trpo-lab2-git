from grades import average

students = {
    "Иванов": [5, 4, 5],
    "Петров": [3, 4, 4],
    "Сидоров": [4, 2, 3],
}

for name, marks in students.items():
    print(name, average(marks))
