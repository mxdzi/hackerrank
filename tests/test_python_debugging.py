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


def test_q2_default_arguments(capsys, monkeypatch):
    inputs = ["3",
              "odd 2",
              "even 3",
              "odd 5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_default_arguments.main()
    captured = capsys.readouterr()
    output = "1\n3\n0\n2\n4\n1\n3\n5\n7\n9\n"
    assert captured.out == output
