from python.strings import *


def test_q1_swap_case():
    assert 'hACKERrANK.COM PRESENTS "pYTHONIST 2".' == q1_swap_case.swap_case('HackerRank.com presents "Pythonist 2".')


def test_q2_python_string_split_and_join():
    assert "this-is-a-string" == q2_python_string_split_and_join.split_and_join("this is a string")
