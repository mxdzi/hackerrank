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
