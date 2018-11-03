# set the aircraft weight as a static variable, for readability and because it is always the same weight
aircraft_weight = 900
pilot_weight = int(input("Please enter the weight of the pilot in kg without any decimals: "))
passengers_weight = int(input("Please enter the weight of all passengers in kg without any decimals: "))
baggage_weight = int(input("Please enter the weight of any baggage's in kg without any decimals: "))
fuel_weight = int(input("Please enter the estimated fuel in kg without any decimals: "))

weight_sum = aircraft_weight + pilot_weight + passengers_weight + baggage_weight + fuel_weight

if weight_sum > 1280:
    print(
        "Sorry, the aircraft is currently too heavy.")
else:
    print(
        "The Aircraft is good to go!")

print("Calculated weight is " + str(weight_sum) + ", allowed weight: 1280 kg")
