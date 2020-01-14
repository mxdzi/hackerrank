from regex.introduction import *


def test_q1_matching_specific_string(capsys, monkeypatch):
    inputs = [("The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on "
               "the planet. We rank programmers based on their coding skills, helping companies source great "
               "programmers and reduce the time to hire. As a result, we are revolutionizing the way companies "
               "discover and evaluate talented engineers. The hackerrank platform is the destination for the best "
               "engineers to hone their skills and companies to find top engineers.")]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_matching_specific_string.main()
    captured = capsys.readouterr()
    output = "Number of matches : 2\n"
    assert captured.out == output


def test_q2_matching_anything_but_new_line(capsys, monkeypatch):
    inputs = ["123.456.abc.def"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_matching_anything_but_new_line.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output

    inputs = ["1123.456.abc.def"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_matching_anything_but_new_line.main()
    captured = capsys.readouterr()
    output = "false\n"
    assert captured.out == output


def test_q3_matching_digits_non_digit_character(capsys, monkeypatch):
    inputs = ["06-11-2015"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_matching_digits_non_digit_character.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q4_matching_whitespace_non_whitespace_character(capsys, monkeypatch):
    inputs = ["12 11 15"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_matching_whitespace_non_whitespace_character.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q5_matching_word_non_word(capsys, monkeypatch):
    inputs = ["www.hackerrank.com"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_matching_word_non_word.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output


def test_q6_matching_start_end(capsys, monkeypatch):
    inputs = ["0qwer."]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_matching_start_end.main()
    captured = capsys.readouterr()
    output = "true\n"
    assert captured.out == output
