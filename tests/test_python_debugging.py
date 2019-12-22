from python.debugging import *


def test_q1_words_score(capsys, monkeypatch):
    inputs = ["2", "hacker book"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_words_score.main()
    captured = capsys.readouterr()
    output = "4\n"
    assert captured.out == output

    inputs = ["3", "programming is awesome"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_words_score.main()
    captured = capsys.readouterr()
    output = "4\n"
    assert captured.out == output
