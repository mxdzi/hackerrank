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


def test_q4_python_mod_divmod(capsys, monkeypatch):
    inputs = ["177", "10"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_python_mod_divmod.main()
    captured = capsys.readouterr()
    output = ("17\n"
              "7\n"
              "(17, 7)\n")
    assert captured.out == output


def test_q5_python_power_mod_power(capsys, monkeypatch):
    inputs = ["3", "4", "5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_python_power_mod_power.main()
    captured = capsys.readouterr()
    output = ("81\n"
              "1\n")
    assert captured.out == output


def test_q6_python_integers_come_in_all_sizes(capsys, monkeypatch):
    inputs = ["9", "29", "7", "27"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_python_integers_come_in_all_sizes.main()
    captured = capsys.readouterr()
    output = "4710194409608608369201743232\n"
    assert captured.out == output


def test_q7_python_quest_1(capsys, monkeypatch):
    inputs = ["5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_python_quest_1.main()
    captured = capsys.readouterr()
    output = ("1\n"
              "22\n"
              "333\n"
              "4444\n")
    assert captured.out == output
