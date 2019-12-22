from python.classes import *


def test_q1_class_1_dealing_with_complex_numbers(capsys, monkeypatch):
    inputs = ["2 1", "5 6"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_class_1_dealing_with_complex_numbers.main()
    captured = capsys.readouterr()
    output = ("7.00+7.00i\n"
              "-3.00-5.00i\n"
              "4.00+17.00i\n"
              "0.26-0.11i\n"
              "2.24+0.00i\n"
              "7.81+0.00i\n")
    assert captured.out == output


def test_q2_class_2_find_the_torsional_angle(capsys, monkeypatch):
    inputs = ["0 4 5",
              "1 7 6",
              "0 5 9",
              "1 7 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_class_2_find_the_torsional_angle.main()
    captured = capsys.readouterr()
    output = "8.19\n"
    assert captured.out == output
