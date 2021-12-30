def gradingStudents(grades):
    g = lambda x: (x // 5 + 1) * 5 if x > 37 and x % 5 > 2 else x
    return list([g(x) for x in grades])
