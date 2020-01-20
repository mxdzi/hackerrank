from problem_solving.algorithms.sorting import *


def test_q1_big_sorting(capsys, monkeypatch):
    inputs = ["6",
              "31415926535897932384626433832795",
              "1",
              "3",
              "10",
              "3",
              "5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_big_sorting.main()
    captured = capsys.readouterr()
    output = ("1\n"
              "3\n"
              "3\n"
              "5\n"
              "10\n"
              "31415926535897932384626433832795\n")
    assert captured.out == output


def test_q12_find_the_median(capsys, monkeypatch):
    inputs = ["7",
              "0 1 2 4 6 5 3"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q12_find_the_median.main()
    captured = capsys.readouterr()
    output = "3\n"
    assert captured.out == output
