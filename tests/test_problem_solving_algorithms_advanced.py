from problem_solving.data_structures.advanced import *


def test_q2_cube_summation(capsys, monkeypatch):
    inputs = ["2",
              "4 5",
              "UPDATE 2 2 2 4",
              "QUERY 1 1 1 3 3 3",
              "UPDATE 1 1 1 23",
              "QUERY 2 2 2 4 4 4",
              "QUERY 1 1 1 3 3 3",
              "2 4",
              "UPDATE 2 2 2 1",
              "QUERY 1 1 1 1 1 1",
              "QUERY 1 1 1 2 2 2",
              "QUERY 2 2 2 2 2 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_cube_summation.main()
    captured = capsys.readouterr()
    output = "4\n4\n27\n0\n1\n1\n"
    assert captured.out == output
