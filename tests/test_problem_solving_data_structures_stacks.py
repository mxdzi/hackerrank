from problem_solving.data_structures.stacks import *


def test_q1_maximum_element(capsys, monkeypatch):
    inputs = ["10",
              "1 97",
              "2",
              "1 20",
              "2",
              "1 26",
              "1 20",
              "2",
              "3",
              "1 91",
              "3"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_maximum_element.main()
    captured = capsys.readouterr()
    output = "26\n91\n"
    assert captured.out == output


def test_q2_balanced_brackets(capsys, monkeypatch):
    inputs = ["3",
              "{[()]}",
              "{[(])}",
              "{{[[(())]]}}"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_balanced_brackets.main()
    captured = capsys.readouterr()
    output = "YES\nNO\nYES\n"
    assert captured.out == output

    inputs = ["2",
              "{{([])}}",
              "{{)[](}}"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_balanced_brackets.main()
    captured = capsys.readouterr()
    output = "YES\nNO\n"
    assert captured.out == output

    inputs = ["3",
              "{(([])[])[]}",
              "{(([])[])[]]}",
              "{(([])[])[]}[]"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_balanced_brackets.main()
    captured = capsys.readouterr()
    output = "YES\nNO\nYES\n"
    assert captured.out == output
