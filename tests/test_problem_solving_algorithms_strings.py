from problem_solving.algorithms.strings import *


def test_q2_camelcase():
    assert 5 == q2_camelcase.camelcase("saveChangesInTheEditor")


def test_q3_strong_password():
    assert q3_strong_password.minimumNumber("3", "Ab1") == 3
    assert q3_strong_password.minimumNumber("11", "#HackerRank") == 1
    assert q3_strong_password.minimumNumber("100", "dq!17+#qh*x-@s8x563og01154o*^9)7c*9-1y9o2a(^1g6(xi^m@u!6y7%v7y8mzj$t48j#rxuj22w4@6&3fr7!5*1+@l$661t)") == 1


def test_q6_mars_exploration(capsys, monkeypatch):
    inputs = ["SOSSPSSQSSOR"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_mars_exploration.main()
    captured = capsys.readouterr()
    output = "3\n"
    assert captured.out == output

    inputs = ["SOSSOT"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_mars_exploration.main()
    captured = capsys.readouterr()
    output = "1\n"
    assert captured.out == output


def test_q7_hackerrank_in_a_string(capsys, monkeypatch):
    inputs = ["2",
              "hereiamstackerrank",
              "hackerworld"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_hackerrank_in_a_string.main()
    captured = capsys.readouterr()
    output = "YES\nNO\n"
    assert captured.out == output

    inputs = ["2",
              "hhaacckkekraraannk",
              "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_hackerrank_in_a_string.main()
    captured = capsys.readouterr()
    output = "YES\nNO\n"
    assert captured.out == output


def test_q11_funny_string():
    assert q11_funny_string.funnyString("acxz") == "Funny"
    assert q11_funny_string.funnyString("bcxz") == "Not Funny"
    assert q11_funny_string.funnyString("ivvkxq") == "Not Funny"
    assert q11_funny_string.funnyString("ivvkx") == "Not Funny"


def test_q18_anagram():
    assert q18_anagram.anagram("aaabbb") == 3
    assert q18_anagram.anagram("ab") == 1
    assert q18_anagram.anagram("abc") == -1
    assert q18_anagram.anagram("mnop") == 2
    assert q18_anagram.anagram("xyyx") == 0
    assert q18_anagram.anagram("xaxbbbxx") == 1
    assert q18_anagram.anagram("asdfjoieufoa") == 3
    assert q18_anagram.anagram("fdhlvosfpafhalll") == 5
    assert q18_anagram.anagram("mvdalvkiopaufl") == 5

    with open("tests/tests_data/q18_anagram_input10.txt") as input_file, \
            open("tests/tests_data/q18_anagram_output10.txt") as output_file:

        test_cases = int(input_file.readline())
        for _ in range(test_cases):
            _in, _out = input_file.readline().rstrip(), output_file.readline().rstrip()
            assert q18_anagram.anagram(_in) == int(_out)


def test_q21_two_strings(capsys, monkeypatch):
    inputs = ["2",
              "hello",
              "world",
              "hi",
              "world"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q21_two_strings.main()
    captured = capsys.readouterr()
    output = "YES\nNO\n"
    assert captured.out == output

    inputs = ["4",
              "wouldyoulikefries",
              "abcabcabcabcabcabc",
              "hackerrankcommunity",
              "cdecdecdecde",
              "jackandjill",
              "wentupthehill",
              "writetoyourparents",
              "fghmqzldbc"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q21_two_strings.main()
    captured = capsys.readouterr()
    output = "NO\nYES\nYES\nNO\n"
    assert captured.out == output
