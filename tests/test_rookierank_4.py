from contests.rookierank_4 import *


def test_c1_exam_rush(capsys, monkeypatch):
    inputs = ["2 2", "1", "2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    c1_exam_rush.main()
    captured = capsys.readouterr()
    output = "1\n"
    assert captured.out == output
