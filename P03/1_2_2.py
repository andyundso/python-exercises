# Choice guessing game simulation
from random import randint

rounds = 0
attemps = 0

while rounds < 10000:
    computer_choice = randint(1, 10)
    computer_guess = 5

    while True:
        if computer_guess < computer_choice:
            computer_guess += 1
        elif computer_guess > computer_choice:
            computer_guess -= 1
        else:
            break
        attemps += 1

    attemps += 1
    rounds += 1

print('Average amounts of guesses was ' + str(attemps / rounds))
