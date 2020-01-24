from problem_solving.data_structures.trees import *


def test_q1_tree_preorder_traversal(capsys, monkeypatch):
    inputs = ["6", "1 2 5 3 6 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_tree_preorder_traversal.main()
    captured = capsys.readouterr()
    output = "1 2 5 3 4 6 "
    assert captured.out == output
