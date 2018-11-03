dot_start = -1
dot_end = 1
height = 0

while height <= 15:
    length = 0

    while length <= 15:
        if dot_start <= length <= dot_end:
            print('. ', end=' ')
        else:
            print('x ', end=' ')
        length += 1

    length = 0
    height += 1
    dot_start += 1
    dot_end += 1
    print("\n")
