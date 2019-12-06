from python.strings import *


def test_q1_swap_case():
    assert 'hACKERrANK.COM PRESENTS "pYTHONIST 2".' == q1_swap_case.swap_case('HackerRank.com presents "Pythonist 2".')


def test_q2_python_string_split_and_join():
    assert "this-is-a-string" == q2_python_string_split_and_join.split_and_join("this is a string")


def test_q3_whats_your_name(capsys):
    q3_whats_your_name.print_full_name("Ross", "Taylor")
    captured = capsys.readouterr()
    output = "Hello Ross Taylor! You just delved into python.\n"
    assert captured.out == output


def test_q4_python_mutations():
    assert "abrackdabra" == q4_python_mutations.mutate_string("abracadabra", 5, 'k')


def test_q5_find_a_string():
    assert 2 == q5_find_a_string.count_substring("ABCDCDC", "CDC")


def test_q6_string_validators(capsys, monkeypatch):
    inputs = ["qA2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_string_validators.main()
    captured = capsys.readouterr()
    output = "True\nTrue\nTrue\nTrue\nTrue\n"
    assert captured.out == output
