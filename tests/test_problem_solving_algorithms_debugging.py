from problem_solving.algorithms.debugging import *


def test_q3_strings_xor(capsys, monkeypatch):
    inputs = ["10101", "00101"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_strings_xor.main()
    captured = capsys.readouterr()
    output = "10000\n"
    assert captured.out == output
