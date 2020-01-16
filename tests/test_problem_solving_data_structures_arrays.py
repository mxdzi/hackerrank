from problem_solving.data_structures.arrays import *


def test_q1_arrays_ds():
    assert "2 3 4 1" == ' '.join(map(str, q1_arrays_ds.reverseArray([1, 4, 3, 2])))
