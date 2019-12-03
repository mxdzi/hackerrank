from problem_solving.algorithms.warmup import *


def test_solve_me_first():
    assert 5 == q1_solve_me_first.solveMeFirst(2, 3)
    assert 1100 == q1_solve_me_first.solveMeFirst(100, 1000)


def test_simple_array_sum():
    assert 31 == q2_simple_array_sum.simpleArraySum([1, 2, 3, 4, 10, 11])


def test_compare_the_triplets():
    assert [1, 1] == q3_compare_the_triplets.compareTriplets((5, 6, 7), (3, 6, 10))
    assert [2, 1] == q3_compare_the_triplets.compareTriplets((17, 28, 30), (99, 16, 8))


def test_a_very_big_sum():
    assert 5000000015 == q4_a_very_big_sum.aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])


def test_diagonal_difference():
    assert 15 == q5_diagonal_difference.diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
