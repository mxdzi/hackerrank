def print_formatted(number):
    width = str(len("{0:b}".format(number)))
    lines = ["{0: >{width}d} {0: >{width}o} {0: >{width}X} {0: >{width}b}".format(n, width=width) for n in
             range(1, number + 1)]
    for line in lines:
        print(line)
