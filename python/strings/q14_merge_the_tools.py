def merge_the_tools(string, k):
    [print(''.join(n)) for n in [dict.fromkeys(s) for s in zip(*[iter(string)] * k)]]
