def breakingRecords(scores):
    max_min_scores = [scores[0], scores[0]]
    max_min_count = [0, 0]
    for score in scores:
        if score > max_min_scores[0]:
            max_min_scores[0] = score
            max_min_count[0] += 1
        elif score < max_min_scores[1]:
            max_min_scores[1] = score
            max_min_count[1] += 1
    return max_min_count
