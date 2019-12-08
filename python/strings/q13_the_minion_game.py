def minion_game(string):
    vowels = set('AIUEO')

    score_stuart = 0
    score_kevin = 0

    for i in range(len(string)):
        if string[i] in vowels:
            score_kevin += len(string) - i
        else:
            score_stuart += len(string) - i

    if score_stuart > score_kevin:
        print("Stuart {}".format(score_stuart))
    elif score_stuart < score_kevin:
        print("Kevin {}".format(score_kevin))
    else:
        print("Draw")
