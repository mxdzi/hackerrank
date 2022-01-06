from problem_solving.algorithms.implementation import *


def test_q1_grading_students():
    assert [75, 67, 40, 33] == q1_grading_students.gradingStudents([73, 67, 38, 33])


def test_q3_kangaroo():
    assert "YES" == q3_kangaroo.kangaroo(0, 3, 4, 2)
    assert "NO" == q3_kangaroo.kangaroo(0, 2, 5, 3)


def test_q7_divisible_sum_pairs():
    assert 5 == q7_divisible_sum_pairs.divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])


def test_q12_drawing_book():
    assert 1 == q12_drawing_book.pageCount(6, 2)
    assert 0 == q12_drawing_book.pageCount(5, 4)
