# Choice guessing game with a human player
from random import randint

computer_choice = randint(1, 10)
user_choice = 0

while user_choice != computer_choice:
    user_choice = int(input("Type in your guess: "))

    if user_choice < computer_choice:
        print("My number is bigger :) \n")
    elif user_choice > computer_choice:
        print("My number is smaller :) \n")

print("Congrats, you have wonnered!")
