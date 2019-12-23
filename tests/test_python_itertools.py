from python.itertools import *


def test_q1_itertools_product(capsys, monkeypatch):
    inputs = ["1 2", "3 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_itertools_product.main()
    captured = capsys.readouterr()
    output = "(1, 3) (1, 4) (2, 3) (2, 4)\n"
    assert captured.out == output


def test_q2_itertools_permutations(capsys, monkeypatch):
    inputs = ["HACK 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_itertools_permutations.main()
    captured = capsys.readouterr()
    output = "AC\nAH\nAK\nCA\nCH\nCK\nHA\nHC\nHK\nKA\nKC\nKH\n"
    assert captured.out == output


def test_q3_itertools_combinations(capsys, monkeypatch):
    inputs = ["HACK 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_itertools_combinations.main()
    captured = capsys.readouterr()
    output = "A\nC\nH\nK\nAC\nAH\nAK\nCH\nCK\nHK\n"
    assert captured.out == output
