from python.introduction import *


def test_q1_py_hello_world(capsys):
    q1_py_hello_world.main()
    captured = capsys.readouterr()
    output = "Hello, World!\n"
    assert captured.out == output


def test_q2_py_if_else(capsys):
    q2_py_if_else.main(3)
    captured = capsys.readouterr()
    output = "Weird\n"
    assert captured.out == output

    q2_py_if_else.main(24)
    captured = capsys.readouterr()
    output = "Not Weird\n"
    assert captured.out == output


def test_q3_python_arithmetic_operators(capsys):
    q3_python_arithmetic_operators.main(3, 2)
    captured = capsys.readouterr()
    output = "5\n1\n6\n"
    assert captured.out == output
