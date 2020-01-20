from problem_solving.algorithms.bit_manipulation import *


def test_q1_lonely_integer(capsys, monkeypatch):
    inputs = ["1",
              "1"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_lonely_integer.main()
    captured = capsys.readouterr()
    output = "1\n"
    assert captured.out == output

    inputs = ["3",
              "1 1 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_lonely_integer.main()
    captured = capsys.readouterr()
    output = "2\n"
    assert captured.out == output

    inputs = ["5",
              "0 0 1 2 1"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_lonely_integer.main()
    captured = capsys.readouterr()
    output = "2\n"
    assert captured.out == output


def test_q7_flipping_bits(capsys, monkeypatch):
    inputs = ["3",
              "2147483647",
              "1",
              "0"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_flipping_bits.main()
    captured = capsys.readouterr()
    output = "2147483648\n4294967294\n4294967295\n"
    assert captured.out == output

    inputs = ["2",
              "4",
              "123456"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_flipping_bits.main()
    captured = capsys.readouterr()
    output = "4294967291\n4294843839\n"
    assert captured.out == output
