from problem_solving.data_structures.arrays import *


def test_q1_arrays_ds():
    assert "2 3 4 1" == ' '.join(map(str, q1_arrays_ds.reverseArray([1, 4, 3, 2])))


def test_q4_array_left_rotation(capsys):
    q4_array_left_rotation.arr_left_rotate([1, 2, 3, 4, 5], 4)
    captured = capsys.readouterr()
    output = "5 1 2 3 4\n"
    assert captured.out == output


def test_q5_sparse_arrays():
    assert [2, 1, 0] == q5_sparse_arrays.matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
    assert [1, 0, 1] == q5_sparse_arrays.matchingStrings(['def', 'de', 'fgh'], ['de', 'lmn', 'fgh'])
    assert [1, 3, 4, 3, 2] == q5_sparse_arrays.matchingStrings(['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn',
                                                                'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn',
                                                                'sdaklfj', 'asdjf'],
                                                               ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn'])
