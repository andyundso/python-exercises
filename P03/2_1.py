domino_stones = []

first_number = 0
second_number = 0

while True:
    current_combination = str(first_number) + "|" + str(second_number)
    reversed_combination = str(second_number) + "|" + str(first_number)

    try:
        existing_combination = domino_stones.index(reversed_combination)
    except ValueError:
        domino_stones.append(current_combination)

    if second_number >= 6:
        if first_number >= 6:
            break
        else:
            first_number += 1
            second_number = 0
    else:
        second_number += 1

print("here is the domino: " + ', '.join(domino_stones))
