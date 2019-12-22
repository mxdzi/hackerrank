from python.errors_and_exceptions import *


def test_q1_exceptions(capsys, monkeypatch):
    inputs = ["3",
              "1 0",
              "2 $",
              "3 1"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_exceptions.main()
    captured = capsys.readouterr()
    output = ("Error Code: integer division or modulo by zero\n"
              "Error Code: invalid literal for int() with base 10: '$'\n"
              "3\n")
    assert captured.out == output


def test_q2_incorrect_regex(capsys, monkeypatch):
    inputs = ["2",
              ".*\+",
              ".*+"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_incorrect_regex.main()
    captured = capsys.readouterr()
    output = "True\nFalse\n"
    assert captured.out == output
