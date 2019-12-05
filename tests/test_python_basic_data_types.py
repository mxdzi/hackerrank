from python.basic_data_types import *


def test_q1_list_comprehensions(capsys):
    q1_list_comprehensions.main(1, 1, 1, 2)
    captured = capsys.readouterr()
    output = "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n"
    assert captured.out == output

    q1_list_comprehensions.main(2, 2, 2, 2)
    captured = capsys.readouterr()
    output = "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]\n"
    assert captured.out == output


def test_q2_find_the_runner_up_score(capsys):
    q2_find_the_runner_up_score.main([2, 3, 6, 6, 5])
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output


def test_q3_nested_list(capsys, monkeypatch):
    inputs = ["5", "Harry", "37.21", "Berry", "37.21", "Tina", "37.2", "Akriti", "41", "Harsh", "39"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_nested_list.main()
    captured = capsys.readouterr()
    output = "Berry\nHarry\n"
    assert captured.out == output


def test_q4_finding_the_percentage(capsys, monkeypatch):
    inputs = ["3", "Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60", "Malika"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_finding_the_percentage.main()
    captured = capsys.readouterr()
    output = "56.00\n"
    assert captured.out == output

    inputs = ["2", "Harsh 25 26.5 28", "Anurag 26 28 30", "Harsh"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_finding_the_percentage.main()
    captured = capsys.readouterr()
    output = "26.50\n"
    assert captured.out == output


def test_q5_python_lists(capsys, monkeypatch):
    inputs = ["12", "insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9",
              "append 1", "sort", "print", "pop", "reverse", "print"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_python_lists.main()
    captured = capsys.readouterr()
    output = "[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n"
    assert captured.out == output


def test_q6_python_tuples(capsys, monkeypatch):
    inputs = ["2", "1 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_python_tuples.main()
    captured = capsys.readouterr()
    output = str(hash((1, 2))) + '\n'
    assert captured.out == output
