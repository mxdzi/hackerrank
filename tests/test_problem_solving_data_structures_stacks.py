from problem_solving.data_structures.stacks import *


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
