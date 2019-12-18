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


def test_q4_py_set_add(capsys, monkeypatch):
    inputs = ["7", "UK", "China", "USA", "France", "New Zealand", "UK", "France"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_py_set_add.main()
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output


def test_q5_py_set_discard_remove_pop(capsys, monkeypatch):
    inputs = ["9", "1 2 3 4 5 6 7 8 9", "10", "pop", "remove 9", "discard 9", "discard 8", "remove 7", "pop",
              "discard 6", "remove 5", "pop", "discard 5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_py_set_discard_remove_pop.main()
    captured = capsys.readouterr()
    output = "4\n"
    assert captured.out == output


def test_q6_py_set_union(capsys, monkeypatch):
    inputs = ["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_py_set_union.main()
    captured = capsys.readouterr()
    output = "13\n"
    assert captured.out == output


def test_q7_py_set_intersection_operation(capsys, monkeypatch):
    inputs = ["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_py_set_intersection_operation.main()
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output


def test_q8_py_set_difference_operation(capsys, monkeypatch):
    inputs = ["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q8_py_set_difference_operation.main()
    captured = capsys.readouterr()
    output = "4\n"
    assert captured.out == output


def test_q9_py_set_symmetric_difference_operation(capsys, monkeypatch):
    inputs = ["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q9_py_set_symmetric_difference_operation.main()
    captured = capsys.readouterr()
    output = "8\n"
    assert captured.out == output
