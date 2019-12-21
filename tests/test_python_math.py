from python.math import *


def test_q1_polar_coordinates(capsys, monkeypatch):
    inputs = ["1+2j"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_polar_coordinates.main()
    captured = capsys.readouterr()
    output = "2.23606797749979\n1.1071487177940904\n"
    assert captured.out == output


def test_q2_find_angle(capsys, monkeypatch):
    inputs = ["10", "10"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_find_angle.main()
    captured = capsys.readouterr()
    output = "45°\n"
    assert captured.out == output


def test_q3_triangle_quest_2(capsys, monkeypatch):
    inputs = ["5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_triangle_quest_2.main()
    captured = capsys.readouterr()
    output = ("1\n"
              "121\n"
              "12321\n"
              "1234321\n"
              "123454321\n")
    assert captured.out == output
