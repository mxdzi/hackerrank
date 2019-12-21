from python.built_ins import *


def test_q1_zipped(capsys, monkeypatch):
    inputs = ["5 3",
              "89 90 78 93 80",
              "90 91 85 88 86",
              "91 92 83 89 90.5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_zipped.main()
    captured = capsys.readouterr()
    output = ("90.0\n"
              "91.0\n"
              "82.0\n"
              "90.0\n"
              "85.5\n")
    assert captured.out == output


def test_q2_input(capsys, monkeypatch):
    inputs = ["1 4", "x**3 + x**2 + x + 1"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_input.main()
    captured = capsys.readouterr()
    output = "True\n"
    assert captured.out == output


def test_q3_python_eval(capsys, monkeypatch):
    inputs = ["print(2 + 3)"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_python_eval.main()
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output


def test_q4_python_sort_sort(capsys, monkeypatch):
    inputs = ["5 3",
              "10 2 5",
              "7 1 0",
              "9 9 9",
              "1 23 12",
              "6 5 9",
              "1"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_python_sort_sort.main()
    captured = capsys.readouterr()
    output = ("7 1 0\n"
              "10 2 5\n"
              "6 5 9\n"
              "9 9 9\n"
              "1 23 12\n")
    assert captured.out == output


def test_q5_any_or_all(capsys, monkeypatch):
    inputs = ["5", "12 9 61 5 14"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_any_or_all.main()
    captured = capsys.readouterr()
    output = "True\n"
    assert captured.out == output


def test_q6_ginorts(capsys, monkeypatch):
    inputs = ["Sorting1234"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_ginorts.main()
    captured = capsys.readouterr()
    output = "ginortS1324\n"
    assert captured.out == output
