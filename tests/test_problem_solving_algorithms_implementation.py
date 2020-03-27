from problem_solving.algorithms.implementation import *


def test_kangaroo():
    assert "YES" == q3_kangaroo.kangaroo(0, 3, 4, 2)
    assert "NO" == q3_kangaroo.kangaroo(0, 2, 5, 3)


def test_divisible_sum_pairs():
    assert 5 == q7_divisible_sum_pairs.divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
