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


def test_q4_itertools_combinations_with_replacement(capsys, monkeypatch):
    inputs = ["HACK 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_itertools_combinations_with_replacement.main()
    captured = capsys.readouterr()
    output = "AA\nAC\nAH\nAK\nCC\nCH\nCK\nHH\nHK\nKK\n"
    assert captured.out == output


def test_q5_compress_the_string(capsys, monkeypatch):
    inputs = ["1222311"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_compress_the_string.main()
    captured = capsys.readouterr()
    output = "(1, 1) (3, 2) (1, 3) (2, 1)\n"
    assert captured.out == output


def test_q6_iterables_and_iterators(capsys, monkeypatch):
    inputs = ["4",
              "a a c d",
              "2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_iterables_and_iterators.main()
    captured = capsys.readouterr()
    output = "0.8333\n"
    assert captured.out == output


def test_q7_maximize_it(capsys, monkeypatch):
    inputs = ["3 1000",
              "2 5 4",
              "3 7 8 9",
              "5 5 7 8 9 10"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_maximize_it.main()
    captured = capsys.readouterr()
    output = "206\n"
    assert captured.out == output
