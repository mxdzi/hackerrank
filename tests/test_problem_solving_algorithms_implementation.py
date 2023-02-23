import pytest

from problem_solving.algorithms.implementation import *


def test_q1_grading_students():
    assert [75, 67, 40, 33] == q1_grading_students.gradingStudents(
        [73, 67, 38, 33])


@pytest.mark.parametrize(
    "inputs, outputs", [
        ((7, 11, 5, 15, [-2, 2, 1], [5, -6]), "1\n1\n"),
    ],
    ids=['Test case 0']
)
def test_q2_apple_and_orange(inputs, outputs, capsys):
    q2_apple_and_orange.countApplesAndOranges(*inputs)
    captured = capsys.readouterr()
    assert captured.out == outputs


def test_q3_kangaroo():
    assert "YES" == q3_kangaroo.kangaroo(0, 3, 4, 2)
    assert "NO" == q3_kangaroo.kangaroo(0, 2, 5, 3)


@pytest.mark.parametrize(
    "inputs, outputs", [
        (([2, 4], [16, 32, 96]), 3),
        (([3, 4], [24, 48]), 2),
    ],
    ids=['Test case 0', 'Test case 1']
)
def test_q4_between_two_sets(inputs, outputs):
    assert outputs == q4_between_two_sets.getTotalX(*inputs)


def test_q7_divisible_sum_pairs():
    assert 5 == q7_divisible_sum_pairs.divisibleSumPairs(6, 3,
                                                         [1, 3, 2, 6, 1, 2])


@pytest.mark.parametrize(
    "inputs, outputs", [
        ([1, 4, 4, 4, 5, 3], 4),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4], 3),
    ],
    ids=['Test case 0', 'Test case 5']
)
def test_q8_migratory_birds(inputs, outputs):
    assert outputs == q8_migratory_birds.migratoryBirds(inputs)


def test_q11_sock_merchant():
    assert q11_sock_merchant.sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10,
                                              20]) == 3
    assert q11_sock_merchant.sockMerchant(10,
                                          [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]) == 4


@pytest.mark.parametrize(
    "inputs, outputs", [
        ([(1, 2, 3), (1, 3, 2)], ["Cat B", "Mouse C"])
    ],
    ids=['Test case 0']
)
def test_q15_cats_and_a_mouse(inputs, outputs):
    for i, o in zip(inputs, outputs):
        assert o == q15_cats_and_a_mouse.catAndMouse(*i)


def test_q12_drawing_book():
    assert 1 == q12_drawing_book.pageCount(6, 2)
    assert 0 == q12_drawing_book.pageCount(5, 4)


@pytest.mark.parametrize(
    "inputs, outputs",
    [
        ([0, 1], [1, 2]),
        ([4, 3], [7, 6]),
        ([54, 52, 47, 48, 49, 53, 46, 50, 51, 55],
         [268435455, 134217727, 33554430, 33554431, 67108862, 268435454,
          16777215, 67108863, 134217726, 536870910])
    ],
    ids=['Test case 0', 'Test case 1', 'Test case 9']
)
def test_q21_utopian_tree(inputs, outputs):
    for i, o in zip(inputs, outputs):
        assert o == q21_utopian_tree.utopianTree(i)


@pytest.mark.parametrize(
    "inputs, outputs",
    [
        (3, 9),
        (4, 15),
        (50, 2068789129),
    ],
    ids=['Test case 0', 'Test case 1', 'Test case 2']
)
def test_q24_strange_advertising(inputs, outputs):
    assert outputs == q24_strange_advertising.viralAdvertising(inputs)


@pytest.mark.parametrize(
    "inputs, outputs", [
        (25, "15511210043330985984000000\n"),
        (45, "119622220865480194561963161495657715064383733760000000000\n")
    ], ids=['Test case 0', 'Test case 12']
)
def test_q30_extra_long_factorials(inputs, outputs, capsys):
    q30_extra_long_factorials.extraLongFactorials(inputs)
    captured = capsys.readouterr()
    assert captured.out == outputs


@pytest.mark.parametrize(
    "inputs, outputs", [
        (["aba", 10], 7),
        (["a", 1000000000000], 1000000000000)
    ], ids=['Test case 0', 'Test case 1']
)
def test_q36_repeated_string(inputs, outputs):
    assert q36_repeated_string.repeatedString(inputs[0], inputs[1]) == outputs


@pytest.mark.parametrize(
    "inputs, outputs", [
        ([(10, 2, 5), (12, 4, 4), (6, 2, 2)], [6, 3, 5]),
        ([(7, 3, 2)], [3])
    ], ids=['Test case 0', 'Test case 10']
)
def test_q50_chocolate_feast(inputs, outputs):
    for i, o in zip(inputs, outputs):
        assert o == q50_chocolate_feast.chocolateFeast(*i)
