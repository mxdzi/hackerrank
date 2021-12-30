from problem_solving.algorithms.implementation import *


def test_q3_kangaroo():
    assert "YES" == q3_kangaroo.kangaroo(0, 3, 4, 2)
    assert "NO" == q3_kangaroo.kangaroo(0, 2, 5, 3)


def test_q7_divisible_sum_pairs():
    assert 5 == q7_divisible_sum_pairs.divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])


def test_q10_drawing_book():
    assert 1 == q10_drawing_book.pageCount(6, 2)
    assert 0 == q10_drawing_book.pageCount(5, 4)
