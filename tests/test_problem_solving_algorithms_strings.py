from problem_solving.algorithms.strings import *


def test_q2_camelcase():
    assert 5 == q2_camelcase.camelcase("saveChangesInTheEditor")


def test_q7_hackerrank_in_a_string(capsys, monkeypatch):
    inputs = ["2",
              "hereiamstackerrank",
              "hackerworld"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_hackerrank_in_a_string.main()
    captured = capsys.readouterr()
    output = "YES\nNO\n"
    assert captured.out == output

    inputs = ["2",
              "hhaacckkekraraannk",
              "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_hackerrank_in_a_string.main()
    captured = capsys.readouterr()
    output = "YES\nNO\n"
    assert captured.out == output
