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


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["4 3 2", "1 2", "1 2", "1 2", "1 2", "3 4", "3 4", "3 4"],
                ("[[1 2]\n"
                 " [1 2]\n"
                 " [1 2]\n"
                 " [1 2]\n"
                 " [3 4]\n"
                 " [3 4]\n"
                 " [3 4]]\n"),
        ),
    ],
    ids=['Test case 0']
)
def test_q4_np_concatenate(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q4_np_concatenate.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["3 3 3"],
                ("[[[0 0 0]\n"
                 "  [0 0 0]\n"
                 "  [0 0 0]]\n"
                 "\n"
                 " [[0 0 0]\n"
                 "  [0 0 0]\n"
                 "  [0 0 0]]\n"
                 "\n"
                 " [[0 0 0]\n"
                 "  [0 0 0]\n"
                 "  [0 0 0]]]\n"
                 "[[[1 1 1]\n"
                 "  [1 1 1]\n"
                 "  [1 1 1]]\n"
                 "\n"
                 " [[1 1 1]\n"
                 "  [1 1 1]\n"
                 "  [1 1 1]]\n"
                 "\n"
                 " [[1 1 1]\n"
                 "  [1 1 1]\n"
                 "  [1 1 1]]]\n"
                 ),
        ),
        (
                ["3 2 3"],
                ("[[[0 0 0]\n"
                 "  [0 0 0]]\n"
                 "\n"
                 " [[0 0 0]\n"
                 "  [0 0 0]]\n"
                 "\n"
                 " [[0 0 0]\n"
                 "  [0 0 0]]]\n"
                 "[[[1 1 1]\n"
                 "  [1 1 1]]\n"
                 "\n"
                 " [[1 1 1]\n"
                 "  [1 1 1]]\n"
                 "\n"
                 " [[1 1 1]\n"
                 "  [1 1 1]]]\n"
                 ),
        ),
    ],
    ids=['Test case 0', 'Test case 1']
)
def test_q5_np_zeros_and_ones(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q5_np_zeros_and_ones.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["3 3"],
                ("[[1. 0. 0.]\n"
                 " [0. 1. 0.]\n"
                 " [0. 0. 1.]]\n"),
        ),
    ],
    ids=['Test case 0']
)
def test_q6_np_eye_and_identity(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q6_np_eye_and_identity.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["1 4",
                 "1 2 3 4",
                 "5 6 7 8"],
                ("[[ 6  8 10 12]]\n"
                 "[[-4 -4 -4 -4]]\n"
                 "[[ 5 12 21 32]]\n"
                 "[[0 0 0 0]]\n"
                 "[[1 2 3 4]]\n"
                 "[[    1    64  2187 65536]]\n"),
        ),
    ],
    ids=['Test case 0']
)
def test_q7_np_array_mathematics(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q7_np_array_mathematics.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"],
                ("[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n"
                 "[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n"
                 "[  1.   2.   3.   4.   6.   7.   8.   9.  10.]\n"),
        ),
    ],
    ids=['Test case 0']
)
def test_q8_floor_ceil_and_rint(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q8_floor_ceil_and_rint.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2 2", "1 2", "3 4"],
                "24\n"
        ),
    ],
    ids=['Test case 0']
)
def test_q9_np_sum_and_prod(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q9_np_sum_and_prod.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["4 2", "2 5", "3 7", "1 3", "4 0"],
                "3\n"
        ),
    ],
    ids=['Test case 0']
)
def test_q10_np_min_and_max(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q10_np_min_and_max.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2 2", "1 2", "3 4"],
                "[1.5 3.5]\n"
                "[1. 1.]\n"
                "1.11803398875\n"
        ),
        (
                ["2 2", "1 2", "3 3"],
                "[1.5 3. ]\n"
                "[1.   0.25]\n"
                "0.82915619759\n"
        ),
    ],
    ids=['Test case 0', 'Test case 1']
)
def test_q11_np_mean_var_and_std(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q11_np_mean_var_and_std.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2", "1 2", "3 4", "1 2", "3 4"],
                "[[ 7 10]\n"
                " [15 22]]\n"
        ),
    ],
    ids=['Test case 0']
)
def test_q12_np_dot_and_cross(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q12_np_dot_and_cross.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["0 1", "2 3"],
                "3\n"
                "[[0 0]\n"
                " [2 3]]\n"
        ),
    ],
    ids=['Test case 0']
)
def test_q13_np_inner_and_outer(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q13_np_inner_and_outer.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["1.1 2 3", "0"],
                "3.0\n"
        ),
    ],
    ids=['Test case 0']
)
def test_q14_np_polynomials(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q14_np_polynomials.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2", "1.1 1.1", "1.1 1.1"],
                "0.0\n"
        ),
        (
                ["2", "1.1 1.1", "1.1 1.2"],
                "0.11\n"
        ),
    ],
    ids=['Test case 0', 'Test case 1']
)
def test_q15_np_linear_algebra(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q15_np_linear_algebra.main()
    captured = capsys.readouterr()
    assert captured.out == output
