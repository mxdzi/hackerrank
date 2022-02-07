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
