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
