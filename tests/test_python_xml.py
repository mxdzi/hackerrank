from python.xml import *


def test_q1_xml_1_find_the_score(capsys, monkeypatch):
    inputs = ["6",
              ("<feed xml:lang='en'>"
               "    <title>HackerRank</title>"
               "    <subtitle lang='en'>Programming challenges</subtitle>"
               "    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>"
               "    <updated>2013-12-25T12:00:00</updated>"
               "</feed>")]
    monkeypatch.setattr('sys.stdin.readline', lambda: inputs.pop(0))
    monkeypatch.setattr('sys.stdin.read', lambda: inputs.pop(0))

    q1_xml_1_find_the_score.main()
    captured = capsys.readouterr()
    output = "5\n"
    assert captured.out == output

    inputs = ["11",
              ("<feed xml:lang='en'>"
               "  <title>HackerRank</title>"
               "  <subtitle lang='en'>Programming challenges</subtitle>"
               "  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>"
               "  <updated>2013-12-25T12:00:00</updated>"
               "  <entry>"
               "  	<author gender='male'>Harsh</author>"
               "    <question type='hard'>XML 1</question>"
               "    <description type='text'>This is related to XML parsing</description>"
               "  </entry>"
               "</feed>")]
    monkeypatch.setattr('sys.stdin.readline', lambda: inputs.pop(0))
    monkeypatch.setattr('sys.stdin.read', lambda: inputs.pop(0))

    q1_xml_1_find_the_score.main()
    captured = capsys.readouterr()
    output = "8\n"
    assert captured.out == output


def test_q2_xml2_find_the_maximum_depth(capsys, monkeypatch):
    inputs = ["6",
              "<feed xml:lang='en'>",
              "  <title>HackerRank</title>",
              "  <subtitle lang='en'>Programming challenges</subtitle>",
              "  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
              "  <updated>2013-12-25T12:00:00</updated>",
              "</feed>"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_xml2_find_the_maximum_depth.main()
    captured = capsys.readouterr()
    output = "1\n"
    assert captured.out == output

    inputs = ["11",
              "<feed xml:lang='en'>",
              "  <title>HackerRank</title>",
              "  <subtitle lang='en'>Programming challenges</subtitle>",
              "  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
              "  <updated>2013-12-25T12:00:00</updated>",
              "  <entry>",
              "  	<author gender='male'>Harsh</author>",
              "    <question type='hard'>XML 1</question>",
              "    <description type='text'>This is related to XML parsing</description>",
              "  </entry>",
              "</feed>"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q2_xml2_find_the_maximum_depth.main()
    captured = capsys.readouterr()
    output = "2\n"
    assert captured.out == output
