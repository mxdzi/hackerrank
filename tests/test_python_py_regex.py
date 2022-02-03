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
    ids=['Test case 0', 'Test case 1']
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
    ids=['Test case 0']
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
    ids=['Test case 0', 'Test case 1']
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
    ids=['Test case 0', 'Test case 2', 'Test case 3']
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
    ids=['Test case 0']
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
    ids=['Test case 0', 'Test case 6']
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
    ids=['Test case 0', 'Test case 1']
)
def test_q7_validate_a_roman_number(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q7_validate_a_roman_number.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2",
                 "9587456281",
                 "1252478965"], "YES\nNO\n"
        ),
        (
                ["3",
                 "8F54698745",
                 "9898959398",
                 "879546242"], "NO\nYES\nNO\n"
        )
    ],
    ids=['Test case 0', 'Test case 1']
)
def test_q8_validating_the_phone_number(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q8_validating_the_phone_number.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2",
                 "DEXTER <dexter@hotmail.com>",
                 "VIRUS <virus!@variable.:p>"], "DEXTER <dexter@hotmail.com>\n"
        ),
        (
                ["7",
                 "dheeraj <dheeraj-234@gmail.com>",
                 "crap <itsallcrap>",
                 "harsh <harsh_1234@rediff.in>",
                 "kumal <kunal_shin@iop.az>",
                 "mattp <matt23@@india.in>",
                 "harsh <.harsh_1234@rediff.in>",
                 "harsh <-harsh_1234@rediff.in>"],
                ("dheeraj <dheeraj-234@gmail.com>\n"
                 "harsh <harsh_1234@rediff.in>\n"
                 "kumal <kunal_shin@iop.az>\n")
        ),
        (
                ["4",
                 "this <is@valid.com>",
                 "this <is_som@radom.stuff>",
                 "this <is_it@valid.com>",
                 "this <_is@notvalid.com>"],
                ("this <is@valid.com>\n"
                 "this <is_it@valid.com>\n")
        )

    ],
    ids=['Test case 0', 'Test case 1', 'Test case 3']
)
def test_q9_validating_named_email_addresses(capsys, monkeypatch, inputs,
                                             output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q9_validating_named_email_addresses.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                [11,
                 "#BED",
                 "{",
                 "    color: #FfFdF8; background-color:#aef;",
                 "11",
                 "    font-size: 123px;",
                 "    background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
                 "}",
                 "#Cab",
                 "{",
                 "    background-color: #ABC;",
                 "    border: 2px dashed #fff;",
                 "}"
                 ],
                ("#FfFdF8\n"
                 "#aef\n"
                 "#f9f9f9\n"
                 "#fff\n"
                 "#ABC\n"
                 "#fff\n")
        ),
    ],
    ids=['Test case 0']
)
def test_q10_hex_color_code(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q10_hex_color_code.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2",
                 "<html><head><title>HTML Parser - I</title></head>",
                 "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"
                 ],
                ("Start : html\n"
                 "Start : head\n"
                 "Start : title\n"
                 "End   : title\n"
                 "End   : head\n"
                 "Start : body\n"
                 "-> data-modal-target > None\n"
                 "-> class > 1\n"
                 "Start : h1\n"
                 "End   : h1\n"
                 "Empty : br\n"
                 "End   : body\n"
                 "End   : html\n")
        ),
    ],
    ids=['Test case 0']
)
def test_q11_html_parser_part_1(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q11_html_parser_part_1.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["4",
                 "<!--[if IE 9]>IE9-specific content",
                 "<![endif]-->",
                 "<div> Welcome to HackerRank</div>",
                 "<!--[if IE 9]>IE9-specific content<![endif]-->"
                 ],
                (">>> Multi-line Comment\n"
                 "[if IE 9]>IE9-specific content\n"
                 "<![endif]\n"
                 ">>> Data\n"
                 " Welcome to HackerRank\n"
                 ">>> Single-line Comment\n"
                 "[if IE 9]>IE9-specific content<![endif]\n")
        ),
    ],
    ids=['Test case 0']
)
def test_q12_html_parser_part_2(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q12_html_parser_part_2.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["9",
                 '<head>\n',
                 '<title>HTML</title>\n',
                 '</head>\n',
                 '<object type="application/x-flash" \n',
                 '  data="your-file.swf" \n',
                 '  width="0" height="0">\n',
                 '  <!-- <param name="movie" value="your-file.swf" /> -->\n',
                 '  <param name="quality" value="high"/>\n',
                 '</object>\n'
                 ],
                ("head\n"
                 "title\n"
                 "object\n"
                 "-> type > application/x-flash\n"
                 "-> data > your-file.swf\n"
                 "-> width > 0\n"
                 "-> height > 0\n"
                 "param\n"
                 "-> name > quality\n"
                 "-> value > high\n")
        ),
    ],
    ids=['Test case 0']
)
def test_q13_detect_html_tags_attributes_and_attribute_values(capsys,
                                                              monkeypatch,
                                                              inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q13_detect_html_tags_attributes_and_attribute_values.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["2",
                 "B1CD102354",
                 "B1CDEF2354"],
                ("Invalid\n"
                 "Valid\n")
        ),
    ],
    ids=['Test case 0']
)
def test_q14_validating_uid(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q14_validating_uid.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["6",
                 "4123456789123456",
                 "5123-4567-8912-3456",
                 "61234-567-8912-3456",
                 "4123356789123456",
                 "5133-3367-8912-3456",
                 "5123 - 3567 - 8912 - 3456"],
                ("Valid\n"
                 "Valid\n"
                 "Invalid\n"
                 "Valid\n"
                 "Invalid\n"
                 "Invalid\n")
        ),
    ],
    ids=['Test case 0']
)
def test_q15_validating_credit_card_number(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q15_validating_credit_card_number.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["110000"], "False\n"
        ),
        (
                ["111456"], "True\n"
        ),
        (
                ["101201"], "True\n"
        ),
        (
                ["4542867"], "False\n"
        ),
    ],
    ids=['Test case 0', 'Test case 1', 'Test case 3', 'Test case 5']
)
def test_q16_validating_postalcode(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q16_validating_postalcode.main()
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "inputs, output",
    [
        (
                ["7 3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"],
                "This is Matrix#  %!\n"
        ),
        (
                ["4 6", "T%Mic&", "h%axr%", "iit#p!", "ssrst&"],
                "This isMatrix scrpt&%!&\n"
        ),
    ],
    ids=['Test case 0', 'Test case 1']
)
def test_q17_matrix_script(capsys, monkeypatch, inputs, output):
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    q17_matrix_script.main()
    captured = capsys.readouterr()
    assert captured.out == output
