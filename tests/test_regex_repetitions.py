from regex.repetitions import *


def test_q1_matching_x_repetitions(capsys, monkeypatch):
    inputs = ["2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_x_repetitions.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output

    inputs = ["x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo13957"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_x_repetitions.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output

    inputs = ["x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_x_repetitions.main()
    captured = capsys.readouterr()
    output = "false\n"
    assert captured.out == output


def test_q2_matching_x_y_repetitions(capsys, monkeypatch):
    inputs = ["3threeormorealphabets."]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_matching_x_y_repetitions.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q3_matching_zero_or_more_repetitions(capsys, monkeypatch):
    inputs = ["14"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_matching_zero_or_more_repetitions.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q4_matching_one_or_more_repititions(capsys, monkeypatch):
    inputs = ["1Qa"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_matching_one_or_more_repititions.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output
