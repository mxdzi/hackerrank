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
