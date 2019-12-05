def main():
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        grades.append(score)
        students.append([name, score])

    second_lowest = sorted(set(grades))[1]

    for student in sorted(students, key=lambda x: x[0]):
        if student[1] == second_lowest:
            print(student[0])
