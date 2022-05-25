import pytest

from problem_solving.algorithms.implementation import *


def test_q1_grading_students():
    assert [75, 67, 40, 33] == q1_grading_students.gradingStudents(
        [73, 67, 38, 33])


def test_q3_kangaroo():
    assert "YES" == q3_kangaroo.kangaroo(0, 3, 4, 2)
    assert "NO" == q3_kangaroo.kangaroo(0, 2, 5, 3)


def test_q7_divisible_sum_pairs():
    assert 5 == q7_divisible_sum_pairs.divisibleSumPairs(6, 3,
                                                         [1, 3, 2, 6, 1, 2])


def test_q11_sock_merchant():
    assert q11_sock_merchant.sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10,
                                              20]) == 3
    assert q11_sock_merchant.sockMerchant(10,
                                          [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]) == 4


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
