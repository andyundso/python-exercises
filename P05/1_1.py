import math


def path_length(trail):
    count = 0
    result = 0

    while (count + 1) < len(trail):
        result += math.sqrt((trail[count][0] - trail[count + 1][0]) ** 2 + (trail[count][1] - trail[count + 1][1]) ** 2)
        count += 1

    print(result)


path_length([(1, 1), (2, 1), (1, 2), (1, 1)])
