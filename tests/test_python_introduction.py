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


def test_q4_python_division(capsys):
    q4_python_division.main(4, 3)
    captured = capsys.readouterr()
    output = "1\n1.3333333333333333\n"
    assert captured.out == output


def test_q5_python_loops(capsys):
    q5_python_loops.main(5)
    captured = capsys.readouterr()
    output = "0\n1\n4\n9\n16\n"
    assert captured.out == output


def test_q6_write_a_function():
    assert False == q6_write_a_function.is_leap(1990)


def test_q7_python_print(capsys):
    q7_python_print.main(3)
    captured = capsys.readouterr()
    output = "123"
    assert captured.out == output
