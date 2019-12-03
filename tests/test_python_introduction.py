from python.introduction import *


def test_q1_py_hello_world(capsys):
    q1_py_hello_world.main()
    captured = capsys.readouterr()
    output = "Hello, World!\n"
    assert captured.out == output
