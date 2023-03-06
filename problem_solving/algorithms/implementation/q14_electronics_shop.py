from itertools import product

def getMoneySpent(keyboards, drives, b):
    costs = set(filter(lambda x: x<=b, map(sum, product(keyboards, drives))))
    return max(costs) if costs else -1
