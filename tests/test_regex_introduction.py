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
