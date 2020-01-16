from regex.assertions import *


def test_q1_positive_lookahead(capsys, monkeypatch):
    inputs = ["gooooo!"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_positive_lookahead.main()
    captured = capsys.readouterr()
    output = "Number of matches : 3\n"
    assert captured.out == output


def test_q2_negative_lookahead(capsys, monkeypatch):
    inputs = ["gooooo"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_negative_lookahead.main()
    captured = capsys.readouterr()
    output = "Number of matches : 2\n"
    assert captured.out == output
