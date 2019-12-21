from python.date_and_time import *


def test_q1_calendar_module(capsys, monkeypatch):
    inputs = ["08 05 2015"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_calendar_module.main()
    captured = capsys.readouterr()
    output = "WEDNESDAY\n"
    assert captured.out == output


def test_q2_python_time_delta():
    assert '25200' == q2_python_time_delta.time_delta("Sun 10 May 2015 13:54:36 -0700",
                                                      "Sun 10 May 2015 13:54:36 -0000")
    assert '88200' == q2_python_time_delta.time_delta("Sat 02 May 2015 19:54:36 +0530",
                                                      "Fri 01 May 2015 13:54:36 -0000")
