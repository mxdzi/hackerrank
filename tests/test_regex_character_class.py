from regex.character_class import *


def test_q1_matching_specific_characters(capsys, monkeypatch):
    inputs = ["1203x."]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_specific_characters.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output

    inputs = ["3000s.."]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_specific_characters.main()
    captured = capsys.readouterr()
    output = "false\n"
    assert captured.out == output

    inputs = ["13000u."]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_specific_characters.main()
    captured = capsys.readouterr()
    output = "false\n"
    assert captured.out == output


def test_q2_excluding_specific_characters(capsys, monkeypatch):
    inputs = ["think?"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_excluding_specific_characters.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q3_matching_range_of_characters(capsys, monkeypatch):
    inputs = ["h4CkR"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_matching_range_of_characters.main()
    captured = capsys.readouterr()
    output = "true\n"

    assert captured.out == output
    inputs = ["h4CkRank"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_matching_range_of_characters.main()
    captured = capsys.readouterr()
    output = "true\n"

    assert captured.out == output
    inputs = ["hh4CkRank"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_matching_range_of_characters.main()
    captured = capsys.readouterr()
    output = "false\n"
    assert captured.out == output

