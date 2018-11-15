from random import randint

cell_thingy = []

for x in range(0, 10):
    cell_thingy.append(['█'] * 15)

cell_x = randint(0, 14)
cell_y = randint(0, 9)

guesses = 0

while guesses <= 10:
    guess_x = int(input("Enter a guess for the X coordination from 0 to 14: "))
    guess_y = int(input("Enter a guess for the Y coordination from 0 to 9: "))

    if guess_x == cell_x and guess_y == cell_y:
        print("Your god, you were correct!")
        quit()
    else:
        print("Wrong call boi")
        cell_thingy[guess_y][guess_x] = 'O'

    for y_index, y in enumerate(cell_thingy):
        for x_index, x in enumerate(cell_thingy[y_index]):
            print(cell_thingy[y_index][x_index], end='')

        print("\n")

    guesses += 1
