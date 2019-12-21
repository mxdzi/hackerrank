from datetime import datetime


def time_delta(t1, t2):
    d1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    d2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta = d1 - d2
    return str(int(abs(delta.total_seconds())))
