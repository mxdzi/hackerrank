def utopianTree(n):
    height = 1
    for i in range(n):
        if i % 2:
            height += 1
        else:
            height *= 2
    return height
