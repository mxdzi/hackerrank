def migratoryBirds(arr):
    birds = [0, 0, 0, 0, 0]
    for bird in arr:
        birds[bird-1] += 1
    return birds.index(max(birds)) + 1
