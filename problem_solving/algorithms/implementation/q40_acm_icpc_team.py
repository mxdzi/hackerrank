import itertools


def acmTeam(topic):
    num_people = len(topic)
    teams = itertools.combinations(range(num_people), 2)
    team_knowledge = map(
        lambda x: tuple(filter(lambda y: '1' in y, (''.join(i) for i in zip(topic[x[0]], topic[x[1]])))), teams)
    known_subjects = list(map(len, team_knowledge))
    maximum = max(known_subjects)
    amount = known_subjects.count(maximum)
    return [maximum, amount]
