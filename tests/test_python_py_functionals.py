from python.py_functionals import *


def test_q1_map_and_lambda_expression(capsys, monkeypatch):
    inputs = ["5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_map_and_lambda_expression.main()
    captured = capsys.readouterr()
    output = "[0, 1, 1, 8, 27]\n"
    assert captured.out == output

    inputs = ["6"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_map_and_lambda_expression.main()
    captured = capsys.readouterr()
    output = "[0, 1, 1, 8, 27, 125]\n"
    assert captured.out == output


def test_q2_validate_list_of_email_address_with_filter(capsys, monkeypatch):
    inputs = ["3",
              "lara@hackerrank.com",
              "brian-23@hackerrank.com",
              "britts_54@hackerrank.com"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_validate_list_of_email_address_with_filter.main()
    captured = capsys.readouterr()
    output = "['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']\n"
    assert captured.out == output

    inputs = ["2",
              "harsh@gmail",
              "iota_98@hackerrank.com"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_validate_list_of_email_address_with_filter.main()
    captured = capsys.readouterr()
    output = "['iota_98@hackerrank.com']\n"
    assert captured.out == output

    inputs = ["5",
              "its@gmail.com1",
              "mike13445@yahoomail9.server",
              "rase23@ha_ch.com",
              "daniyal@gmail.coma",
              "thatisit@thatisit"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_validate_list_of_email_address_with_filter.main()
    captured = capsys.readouterr()
    output = "[]\n"
    assert captured.out == output


def test_q3_reduce_function(capsys, monkeypatch):
    inputs = ["3",
              "1 2",
              "3 4",
              "10 6"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_reduce_function.main()
    captured = capsys.readouterr()
    output = "5 8\n"
    assert captured.out == output
