from problem_solving.data_structures.arrays import *


def test_q1_arrays_ds():
    assert "2 3 4 1" == ' '.join(map(str, q1_arrays_ds.reverseArray([1, 4, 3, 2])))


def test_q4_array_left_rotation(capsys):
    q4_array_left_rotation.arr_left_rotate([1, 2, 3, 4, 5], 4)
    captured = capsys.readouterr()
    output = "5 1 2 3 4\n"
    assert captured.out == output
