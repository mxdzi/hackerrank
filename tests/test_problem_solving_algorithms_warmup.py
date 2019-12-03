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


def test_plus_minus(capsys):
    q6_plus_minus.plusMinus([-4, 3, -9, 0, 4, 1])
    captured = capsys.readouterr()
    output = "0.500000\n0.333333\n0.166667\n"
    assert captured.out == output


def test_staircase(capsys):
    q7_staircase.staircase(6)
    captured = capsys.readouterr()
    output = "     #\n    ##\n   ###\n  ####\n #####\n######\n"
    assert captured.out == output


def test_mini_max_sum(capsys):
    q8_mini_max_sum.miniMaxSum([1, 2, 3, 4, 5])
    captured = capsys.readouterr()
    output = "10 14\n"
    assert captured.out == output

    q8_mini_max_sum.miniMaxSum([7, 69, 2, 221, 8974])
    captured = capsys.readouterr()
    output = "299 9271\n"
    assert captured.out == output


def test_birthday_cake_candles():
    assert 2 == q9_birthday_cake_candles.birthdayCakeCandles([3, 2, 1, 3])


def test_time_conversion():
    assert "19:05:45" == q10_time_conversion.timeConversion("07:05:45PM")
