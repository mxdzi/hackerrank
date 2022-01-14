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
