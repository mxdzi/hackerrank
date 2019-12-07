from contests.projecteuler import *


def test_013_large_sum(capsys, monkeypatch):
    inputs = ["5",
              "37107287533902102798797998220837590246510135740250",
              "46376937677490009712648124896970078050417018260538",
              "74324986199524741059474233309513058123726617309629",
              "91942213363574161572522430563301811072406154908250",
              "23067588207539346171171980310421047513778063246676"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    p013_large_sum.main()
    captured = capsys.readouterr()
    output = "2728190129\n"
    assert captured.out == output
