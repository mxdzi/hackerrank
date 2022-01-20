import pytest

from python.py_regex import *


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["4",
                 "4.0O0",
                 "-1.00",
                 "+4.54",
                 "SomeRandomStuff"],
                "False\nTrue\nTrue\nFalse\n",
        ),
        (
                ["5",
                 "1.414",
                 "+.5486468",
                 "0.5.0",
                 "1+1.0",
                 "0"],
                "True\nTrue\nFalse\nFalse\nFalse\n",
        ),
    ],
)
def test_q1_introduction_to_regex(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q1_introduction_to_regex.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["100,000,000.000"],
                "100\n000\n000\n000\n",
        ),
    ],
)
def test_q2_re_split(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q2_re_split.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["..12345678910111213141516171820212223"],
                "1\n",
        ),
        (
                ["__commit__"],
                "m\n",
        ),
    ],
)
def test_q3_re_group_groups(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q3_re_group_groups.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["rabcdeefgyYhFjkIoomnpOeorteeeeet"],
                "ee\nIoo\nOeo\neeeee\n",
        ),
        (
                ["match a single character not present in the list below"],
                "-1\n",
        ),
        (
                ["abaabaabaabaae"],
                "aa\naa\naa\n",
        )
    ],
)
def test_q4_re_findall_re_finditer(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q4_re_findall_re_finditer.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["aaadaa", "aa"],
                "(0, 1)\n(1, 2)\n(4, 5)\n",
        ),
    ],
)
def test_q5_re_start_re_end(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q5_re_start_re_end.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["11",
                 "a = 1;",
                 "b = input();",
                 "",
                 "if a + b > 0 && a - b < 0:",
                 "    start()",
                 "elif a*b > 10 || a/b < 1:",
                 "    stop()",
                 "print set(list(a)) | set(list(b))",
                 "#Note do not change &&& or ||| or & or |",
                 "#Only change those '&&' which have space on both sides.",
                 "#Only change those '|| which have space on both sides."],
                ("a = 1;\n"
                 "b = input();\n"
                 "\n"
                 "if a + b > 0 and a - b < 0:\n"
                 "    start()\n"
                 "elif a*b > 10 or a/b < 1:\n"
                 "    stop()\n"
                 "print set(list(a)) | set(list(b))\n"
                 "#Note do not change &&& or ||| or & or |\n"
                 "#Only change those '&&' which have space on both sides.\n"
                 "#Only change those '|| which have space on both sides.\n"),
        ),
        (
                ["1",
                 r"x&& &&& && && x || | ||\|| x"],
                 r"x&& &&& and and x or | ||\|| x" + "\n"
        )
    ],
)
def test_q6_re_sub_regex_substitution(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q6_re_sub_regex_substitution.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["CDXXI"], "True\n"
        ),
        (
                ["DXXVIIII"], "False\n"
        )
    ],
)
def test_q7_validate_a_roman_number(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q7_validate_a_roman_number.main()
    captured = capsys.readouterr()
    assert captured.out == output
