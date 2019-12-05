def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    s = student_marks[query_name]
    avg = sum(s)/len(s)

    print('{0:.2f}'.format(avg))
