from python.collections import *


def test_q1_collections_counter(capsys, monkeypatch):
    inputs = ["10",
              "2 3 4 5 6 8 7 6 5 18",
              "6",
              "6 55",
              "6 45",
              "6 55",
              "4 40",
              "18 60",
              "10 50"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_collections_counter.main()
    captured = capsys.readouterr()
    output = "200\n"
    assert captured.out == output
