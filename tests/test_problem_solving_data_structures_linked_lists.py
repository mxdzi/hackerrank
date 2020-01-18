from problem_solving.data_structures.linked_lists import *


def test_q1_print_the_elements_of_a_linked_list(capsys, monkeypatch):
    inputs = ["2",
              "16",
              "13"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_print_the_elements_of_a_linked_list.main()
    captured = capsys.readouterr()
    output = "16\n13\n"
    assert captured.out == output

    inputs = ["4",
              "17",
              "19",
              "5",
              "12"]
    monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

    q1_print_the_elements_of_a_linked_list.main()
    captured = capsys.readouterr()
    output = "17\n19\n5\n12\n"
    assert captured.out == output
