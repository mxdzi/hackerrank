from python.collections import *


def test_q1_collections_counter(capsys, monkeypatch):
    inputs = ["10",
              "2 3 4 5 6 8 7 6 5 18",
              "6",
              "6 55",
              "6 45",
              "6 55",
              "4 40",
              "18 60",
              "10 50"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_collections_counter.main()
    captured = capsys.readouterr()
    output = "200\n"
    assert captured.out == output


def test_q2_defaultdict_tutorial(capsys, monkeypatch):
    inputs = ["5 2",
              "a", "a", "b", "a", "b",
              "a", "b"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_defaultdict_tutorial.main()
    captured = capsys.readouterr()
    output = "1 2 4\n3 5\n"
    assert captured.out == output

    inputs = ["1 1",
              "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxx",
              "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxx"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_defaultdict_tutorial.main()
    captured = capsys.readouterr()
    output = "-1\n"
    assert captured.out == output


def test_q3_py_collections_namedtuple(capsys, monkeypatch):
    inputs = ["5",
              "ID         MARKS      NAME       CLASS",
              "1          97         Raymond    7",
              "2          50         Steven     4",
              "3          91         Adrian     9",
              "4          72         Stewart    5",
              "5          80         Peter      6"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_py_collections_namedtuple.main()
    captured = capsys.readouterr()
    output = "78.00\n"
    assert captured.out == output

    inputs = ["5",
              "MARKS      CLASS      NAME       ID",
              "92         2          Calum      1",
              "82         5          Scott      2",
              "94         2          Jason      3",
              "55         8          Glenn      4",
              "82         2          Fergus     5"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q3_py_collections_namedtuple.main()
    captured = capsys.readouterr()
    output = "81.00\n"
    assert captured.out == output


def test_q4_py_collections_ordereddict(capsys, monkeypatch):
    inputs = ["9",
              "BANANA FRIES 12",
              "POTATO CHIPS 30",
              "APPLE JUICE 10",
              "CANDY 5",
              "APPLE JUICE 10",
              "CANDY 5",
              "CANDY 5",
              "CANDY 5",
              "POTATO CHIPS 30"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q4_py_collections_ordereddict.main()
    captured = capsys.readouterr()
    output = ("BANANA FRIES 12\n"
              "POTATO CHIPS 60\n"
              "APPLE JUICE 20\n"
              "CANDY 20\n")
    assert captured.out == output


def test_q5_word_order(capsys, monkeypatch):
    inputs = ["4",
              "bcdef",
              "abcdefg",
              "bcde",
              "bcdef"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q5_word_order.main()
    captured = capsys.readouterr()
    output = ("3\n2 1 1\n")
    assert captured.out == output


def test_q6_py_collections_deque(capsys, monkeypatch):
    inputs = ["6",
              "append 1",
              "append 2",
              "append 3",
              "appendleft 4",
              "pop",
              "popleft"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q6_py_collections_deque.main()
    captured = capsys.readouterr()
    output = "1 2\n"
    assert captured.out == output


def test_q7_most_commons(capsys, monkeypatch):
    inputs = ["aabbbccde"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_most_commons.main()
    captured = capsys.readouterr()
    output = "b 3\na 2\nc 2\n"
    assert captured.out == output

    inputs = ["szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q7_most_commons.main()
    captured = capsys.readouterr()
    output = "o 12\nm 11\nn 11\n"
    assert captured.out == output


def test_q8_piling_up(capsys, monkeypatch):
    inputs = ["2",
              "6",
              "4 3 2 1 3 4",
              "3",
              "1 3 2"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q8_piling_up.main()
    captured = capsys.readouterr()
    output = "Yes\nNo\n"
    assert captured.out == output
