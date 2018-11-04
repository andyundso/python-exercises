def ask_user_for_float(text):
    return float(input(text))


def do_calc():
    return quantity * density


quantity = ask_user_for_float("Enter the quantity of your fluid in litres: ")
density = ask_user_for_float("Enter the mass peer volume of your fluid in kg / l: ")

print("\nYour fluid weights: " + str(do_calc()) + " kg.")
