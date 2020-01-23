def matchingStrings(strings, queries):
    d = {}
    for s in strings:
        d[s] = d.get(s, 0) + 1

    result = []
    for q in queries:
        result.append(d.get(q, 0))

    return result
