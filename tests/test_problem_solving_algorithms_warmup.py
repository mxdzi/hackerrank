from problem_solving.algorithms.warmup import *


def test_solve_me_first():
    assert 5 == q1_solve_me_first.solveMeFirst(2, 3)
    assert 1100 == q1_solve_me_first.solveMeFirst(100, 1000)


def test_simple_array_sum():
    assert 31 == q2_simple_array_sum.simpleArraySum([1, 2, 3, 4, 10, 11])
