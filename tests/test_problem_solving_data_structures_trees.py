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


def test_q3_tree_inorder_traversal(capsys, monkeypatch):
    inputs = ["6", "1 2 5 3 6 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_tree_inorder_traversal.main()
    captured = capsys.readouterr()
    output = "1 2 3 4 5 6 "
    assert captured.out == output

    inputs = ["15", "1 14 3 7 4 5 15 6 13 10 11 2 12 8 9"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_tree_inorder_traversal.main()
    captured = capsys.readouterr()
    output = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 "
    assert captured.out == output


def test_q4_tree_height_of_a_binary_tree(capsys, monkeypatch):
    inputs = ["7", "3 5 2 1 4 6 7"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_tree_height_of_a_binary_tree.main()
    captured = capsys.readouterr()
    output = "3\n"
    assert captured.out == output

    inputs = ["1", "15"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_tree_height_of_a_binary_tree.main()
    captured = capsys.readouterr()
    output = "0\n"
    assert captured.out == output

    inputs = ["5", "3 1 7 5 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_tree_height_of_a_binary_tree.main()
    captured = capsys.readouterr()
    output = "3\n"
    assert captured.out == output


def test_q6_tree_level_order_traversal(capsys, monkeypatch):
    inputs = ["6", "1 2 5 3 6 4"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_tree_level_order_traversal.main()
    captured = capsys.readouterr()
    output = "1 2 5 3 6 4 "
    assert captured.out == output
