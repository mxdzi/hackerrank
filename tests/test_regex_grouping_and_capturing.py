from regex.grouping_and_capturing import *


def test_q1_matching_word_boundaries(capsys, monkeypatch):
    inputs = ["Found any match?"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_word_boundaries.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q2_capturing_non_capturing_groups(capsys, monkeypatch):
    inputs = ["okokok! cya"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_capturing_non_capturing_groups.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q3_alternative_matching(capsys, monkeypatch):
    inputs = ["Mr.DOSHI"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_alternative_matching.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output

    inputs = ["Ms._underscore"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_alternative_matching.main()
    captured = capsys.readouterr()
    output = "false\n"
    assert captured.out == output
