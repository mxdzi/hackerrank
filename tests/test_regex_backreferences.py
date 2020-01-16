from regex.backreferences import *


def test_q1_matching_same_text_again_again(capsys, monkeypatch):
    inputs = ["ab #1?AZa$ab #1?AZa$"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_same_text_again_again.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q2_backreferences_to_failed_groups(capsys, monkeypatch):
    inputs = ["12-34-56-78"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_backreferences_to_failed_groups.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output

    inputs = ["12345678"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_backreferences_to_failed_groups.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output
