from python.closures_and_decorators import *


def test_q1_standardize_mobile_number_using_decorators(capsys, monkeypatch):
    inputs = ["3",
              "07895462130",
              "919875641230",
              "9195969878"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_standardize_mobile_number_using_decorators.main()
    captured = capsys.readouterr()
    output = ("+91 78954 62130\n"
              "+91 91959 69878\n"
              "+91 98756 41230\n")
    assert captured.out == output

    inputs = ["3",
              "09191919191",
              "9100256236",
              "+919593621456"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_standardize_mobile_number_using_decorators.main()
    captured = capsys.readouterr()
    output = ("+91 91002 56236\n"
              "+91 91919 19191\n"
              "+91 95936 21456\n")
    assert captured.out == output


def test_q2_decorators_2_name_directory(capsys, monkeypatch):
    inputs = ["3",
              "Mike Thomson 20 M",
              "Robert Bustle 32 M",
              "Andria Bustle 30 F"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_decorators_2_name_directory.main()
    captured = capsys.readouterr()
    output = ("Mr. Mike Thomson\n"
              "Ms. Andria Bustle\n"
              "Mr. Robert Bustle\n")
    assert captured.out == output

    inputs = ["5",
              "Laura Moser 50 F",
              "Ted Moser 50 M",
              "Yena Dixit 50 F",
              "Diya Mirza 50 F",
              "Rex Dsouza 51 M"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_decorators_2_name_directory.main()
    captured = capsys.readouterr()
    output = ("Ms. Laura Moser\n"
              "Mr. Ted Moser\n"
              "Ms. Yena Dixit\n"
              "Ms. Diya Mirza\n"
              "Mr. Rex Dsouza\n")
    assert captured.out == output
