def print_and_quit(text):
    print(text)
    quit()


def checksum(only_numbers_list):
    sum = 0
    for digit in only_numbers_list:
        sum += digit
    return sum % 10 == 0


def check(card_number):
    list_of_number_blocks = card_number.split(' ')
    only_numbers_list = []

    if len(list_of_number_blocks) < 4:
        print_and_quit(
            "Invalid format of credit number. Check that your card number has four blocks with four digits each.")

    for number_block in list_of_number_blocks:
        if len(list(number_block)) != 4:
            print_and_quit(
                "Sorry, one of blocks in your credit number does not contain four digits. Please check the number and try again.")

        if not (number_block.isdigit()):
            print_and_quit(
                "Sorry, credit cards number can only contain numbers. Please check your input and try again.")

        for digit in list(number_block):
            only_numbers_list.append(int(digit))

    if checksum(only_numbers_list):
        print("Your MeisterCard is valid.")
    else:
        print_and_quit("The checksum check for this number failed. Please try again.")


check(input("Enter your MeisterCard credit number: "))
