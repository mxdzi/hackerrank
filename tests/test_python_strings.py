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


def test_q7_text_alignment(capsys, monkeypatch):
    inputs = ["5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_text_alignment.main()
    captured = capsys.readouterr()
    output = ("    H    \n"
              "   HHH   \n"
              "  HHHHH  \n"
              " HHHHHHH \n"
              "HHHHHHHHH\n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n"
              "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n"
              "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "  HHHHH               HHHHH             \n"
              "                    HHHHHHHHH \n"
              "                     HHHHHHH  \n"
              "                      HHHHH   \n"
              "                       HHH    \n"
              "                        H     \n")
    assert captured.out == output


def test_q8_text_wrap(capsys):
    output = "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ"
    assert output == q8_text_wrap.wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)


def test_q9_designer_door_mat(capsys, monkeypatch):
    inputs = ["7 21"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q9_designer_door_mat.main()
    captured = capsys.readouterr()
    output = ("---------.|.---------\n"
              "------.|..|..|.------\n"
              "---.|..|..|..|..|.---\n"
              "-------WELCOME-------\n"
              "---.|..|..|..|..|.---\n"
              "------.|..|..|.------\n"
              "---------.|.---------\n")
    assert captured.out == output


def test_q10_python_string_formatting(capsys):
    q10_python_string_formatting.print_formatted(2)
    captured = capsys.readouterr()
    output = " 1  1  1  1\n 2  2  2 10\n"
    assert captured.out == output


def test_q11_alphabet_rangoli(capsys):
    q11_alphabet_rangoli.print_rangoli(5)
    captured = capsys.readouterr()
    output = ("--------e--------\n"
              "------e-d-e------\n"
              "----e-d-c-d-e----\n"
              "--e-d-c-b-c-d-e--\n"
              "e-d-c-b-a-b-c-d-e\n"
              "--e-d-c-b-c-d-e--\n"
              "----e-d-c-d-e----\n"
              "------e-d-e------\n"
              "--------e--------\n")
    assert captured.out == output


def test_q12_capitalize():
    assert "Hello World" == q12_capitalize.solve("hello world")


def test_q13_the_minion_game(capsys):
    q13_the_minion_game.minion_game("BANANA")
    captured = capsys.readouterr()
    output = "Stuart 12\n"
    assert captured.out == output

    q13_the_minion_game.minion_game(
        ("NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN"
         "ANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
         "NNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNA"
         "NANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
         "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNAN"
         "ANNANANNANANNANANNANANNANANNANAN")
    )

    captured = capsys.readouterr()
    output = "Stuart 7501500\n"
    assert captured.out == output


def test_q14_merge_the_tools(capsys):
    q14_merge_the_tools.merge_the_tools("AABCAAADA", 3)
    captured = capsys.readouterr()
    output = "AB\nCA\nAD\n"
    assert captured.out == output
