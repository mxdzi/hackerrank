from problem_solving.algorithms.debugging import *


def test_q1_prime_date(capsys, monkeypatch):
    inputs = ["02-08-2025 04-09-2025"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_prime_date.main()
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output


def test_q3_strings_xor(capsys, monkeypatch):
    inputs = ["10101", "00101"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_strings_xor.main()
    captured = capsys.readouterr()
    output = "10000\n"
    assert captured.out == output


def test_q4_zig_zag_sequence(capsys, monkeypatch):
    inputs = ["1", "7", "1 2 3 4 5 6 7"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_zig_zag_sequence.main()
    captured = capsys.readouterr()
    output = "1 2 3 7 6 5 4\n"
    assert captured.out == output


def test_q5_smart_number(capsys, monkeypatch):
    inputs = ["4", "1", "2", "7", "169"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_smart_number.main()
    captured = capsys.readouterr()
    output = "YES\nNO\nNO\nYES\n"
    assert captured.out == output
