from problem_solving.data_structures.trees import *


def test_q1_tree_preorder_traversal(capsys, monkeypatch):
    inputs = ["6", "1 2 5 3 6 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_tree_preorder_traversal.main()
    captured = capsys.readouterr()
    output = "1 2 5 3 4 6 "
    assert captured.out == output


def test_q2_tree_postorder_traversal(capsys, monkeypatch):
    inputs = ["6", "1 2 5 3 6 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_tree_postorder_traversal.main()
    captured = capsys.readouterr()
    output = "4 3 6 5 2 1 "
    assert captured.out == output

    inputs = ["15", "1 14 3 7 4 5 15 6 13 10 11 2 12 8 9"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_tree_postorder_traversal.main()
    captured = capsys.readouterr()
    output = "2 6 5 4 9 8 12 11 10 13 7 3 15 14 1 "
    assert captured.out == output
