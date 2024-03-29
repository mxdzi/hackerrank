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

def test_q2_maximizing_xor(capsys, monkeypatch):
    inputs = ["10", "15"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_maximizing_xor.main()
    captured = capsys.readouterr()
    output = "7\n"
    assert captured.out == output


def test_q3_counter_game():
    assert "Richard" == q3_counter_game.counterGame(6)
    assert "Louise" == q3_counter_game.counterGame(132)


def test_q5_sum_vs_xor():
    assert 2 == q5_sum_vs_xor.sumXor(5)
    assert 1 == q5_sum_vs_xor.sumXor(0)
    assert 1073741824 == q5_sum_vs_xor.sumXor(1000000000000000)
    assert 4 == q5_sum_vs_xor.sumXor(10)
    assert 1 == q5_sum_vs_xor.sumXor(1)


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


def test_q11_winning_lottery_ticket(capsys, monkeypatch):
    inputs = ["5",
              "129300455",
              "5559948277",
              "012334556",
              "56789",
              "123456879"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q11_winning_lottery_ticket.main()
    captured = capsys.readouterr()
    output = "5\n\n"
    assert captured.out == output
