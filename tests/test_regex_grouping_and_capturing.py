from regex.grouping_and_capturing import *


def test_q1_matching_word_boundaries(capsys, monkeypatch):
    inputs = ["Found any match?"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_word_boundaries.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output
