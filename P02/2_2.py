from random import randint

possible_fighters = ['rock', 'scissors', 'paper']
computer_wins = 0
player_wins = 0

while not (computer_wins >= 3 or player_wins >= 3):
    def fighter_output():
        return possible_fighters[computer_choice].capitalize()


    computer_choice = randint(0, 2)
    user_choice_text = input("Please enter your choice for Rock, Paper and Scissors: ").lower()

    try:
        user_choice = possible_fighters.index(user_choice_text)
    except ValueError:
        print("Sorry, I dont know this thing you want to fight. Please restart and select a fair weapon.")
        quit()

    if computer_choice == user_choice:
        print("Seems I got the same thought, guess this round ends in a tie\n")
    else:
        winning_choice = (computer_choice + 1) % 3

        if user_choice == winning_choice:
            print('gg ez I won this round with my ' + fighter_output())
            computer_wins += 1
            print("Computer wins: " + str(computer_wins) + "\n")
        else:
            print("guess you won, I thought I would win this round with my " + fighter_output())
            player_wins += 1
            print("Player wins: " + str(player_wins) + "\n")

if computer_wins >= 3:
    print('Nice, I won.')
else:
    print('Good job, you won!')
