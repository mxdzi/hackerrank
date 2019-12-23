from python.itertools import *


def test_q1_itertools_product(capsys, monkeypatch):
    inputs = ["1 2", "3 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_itertools_product.main()
    captured = capsys.readouterr()
    output = "(1, 3) (1, 4) (2, 3) (2, 4)\n"
    assert captured.out == output
