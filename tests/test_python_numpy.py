import pytest

from python.numpy import *


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["1 2 3 4 -8 -10"],
                "[-10.  -8.   4.   3.   2.   1.]\n",
        ),
    ],
    ids=['Test case 0']
)
def test_q1_np_arrays(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q1_np_arrays.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["1 2 3 4 5 6 7 8 9"],
                ("[[1 2 3]\n"
                 " [4 5 6]\n"
                 " [7 8 9]]\n"),
        ),
    ],
    ids=['Test case 0']
)
def test_q2_np_shape_reshape(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q2_np_shape_reshape.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2 2", "1 2", "3 4"],
                ("[[1 3]\n"
                 " [2 4]]\n"
                 "[1 2 3 4]\n"),
        ),
    ],
    ids=['Test case 0']
)
def test_q3_np_transpose_and_flatten(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q3_np_transpose_and_flatten.main()
    captured = capsys.readouterr()
    assert captured.out == output
