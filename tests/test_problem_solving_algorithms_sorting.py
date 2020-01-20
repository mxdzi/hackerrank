from problem_solving.algorithms.sorting import *


def test_q12_find_the_median(capsys, monkeypatch):
    inputs = ["7",
              "0 1 2 4 6 5 3"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q12_find_the_median.main()
    captured = capsys.readouterr()
    output = "3\n"
    assert captured.out == output
