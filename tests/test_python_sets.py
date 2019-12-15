from python.sets import *


def test_q1_py_introduction_to_sets():
    assert 169.375 == q1_py_introduction_to_sets.average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])


def test_q2_no_idea(capsys, monkeypatch):
    inputs = ["3 2", "1 5 3", "3 1", "5 7"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_no_idea.main()
    captured = capsys.readouterr()
    output = "1\n"
    assert captured.out == output


def test_q3_symmetric_difference(capsys, monkeypatch):
    inputs = ["4", "2 4 5 9", "4", "2 4 11 12"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_symmetric_difference.main()
    captured = capsys.readouterr()
    output = "5\n9\n11\n12\n"
    assert captured.out == output
