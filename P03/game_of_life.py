from random import randint
import time
from colorama import init
init()

def check_cell_state(x_corr, y_corr):
    if not(x_corr < 0 or x_corr >= length or y_corr < 0 or y_corr >= height):
        return cell_thingy[y_corr][x_corr]
    else:
        return False


length = int(input("Enter the length of your Game of Life (e.g. 90): "))
height = int(input("Enter the height (e.g. 5): "))
alive_cells = int(input("Enter amount of alive cells (e.g. 90): "))
wished_generations = int(input("Enter your wished amount of generations: "))

cell_thingy = []

count = 0
for x in range(0, height):
    cell_thingy.append([False] * length)
    count += 1

# now activate some cells
# lazy implementation ofc
for x in range(0, alive_cells):
    cell_x = randint(0, length - 1)
    cell_y = randint(0, height - 1)
    cell_thingy[cell_y][cell_x] = True

generation = 1

# now let's roll the game
while generation <= wished_generations:
    print("Generation " + str(generation))
    for cell_y_index, cell_row in enumerate(cell_thingy):
        # find all true values
        for cell_x_index, e in enumerate(cell_row):
            # collect the state around our cell
            state_around_cell = []
            state_around_cell.append(check_cell_state(cell_x_index - 1, cell_y_index + 1))
            state_around_cell.append(check_cell_state(cell_x_index, cell_y_index + 1))
            state_around_cell.append(check_cell_state(cell_x_index + 1, cell_y_index + 1))
            state_around_cell.append(check_cell_state(cell_x_index -1, cell_y_index))
            state_around_cell.append(check_cell_state(cell_x_index + 1, cell_y_index))
            state_around_cell.append(check_cell_state(cell_x_index - 1, cell_y_index - 1))
            state_around_cell.append(check_cell_state(cell_x_index, cell_y_index - 1 ))
            state_around_cell.append(check_cell_state(cell_x_index + 1, cell_y_index -1))

            count_of_alive_cells = state_around_cell.count(True)

            # now apply the rules and probably flip some things around
            if cell_thingy[cell_y_index][cell_x_index] == True:
                if count_of_alive_cells < 2:
                    cell_thingy[cell_y_index][cell_x_index] = False
                elif 2 <= count_of_alive_cells <= 3:
                    cell_thingy[cell_y_index][cell_x_index] = True
                else:
                    cell_thingy[cell_y_index][cell_x_index] = False
            else:
                if count_of_alive_cells >= 3:
                    cell_thingy[cell_y_index][cell_x_index] = True

            if cell_thingy[cell_y_index][cell_x_index] == True:
                print('█', end=' ')
            else:
                print("   ", end=' ')
        print("\n")
    print("\n\n")
    generation += 1
    time.sleep(1)
