from python.basic_data_types import *


def test_q1_list_comprehensions(capsys):
    q1_list_comprehensions.main(1, 1, 1, 2)
    captured = capsys.readouterr()
    output = "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n"
    assert captured.out == output

    q1_list_comprehensions.main(2, 2, 2, 2)
    captured = capsys.readouterr()
    output = "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]\n"
    assert captured.out == output


def test_q2_find_the_runner_up_score(capsys):
    q2_find_the_runner_up_score.main([2, 3, 6, 6, 5])
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output
