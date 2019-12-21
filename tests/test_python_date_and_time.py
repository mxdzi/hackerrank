from python.date_and_time import *


def test_q1_calendar_module(capsys, monkeypatch):
    inputs = ["08 05 2015"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_calendar_module.main()
    captured = capsys.readouterr()
    output = "WEDNESDAY\n"
    assert captured.out == output
