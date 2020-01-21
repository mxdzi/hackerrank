from mathematics.fundamentals import *


def test_q3_handshake(capsys, monkeypatch):
    inputs = ["2", "1", "2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_handshake.main()
    captured = capsys.readouterr()
    output = "0\n1\n"
    assert captured.out == output
