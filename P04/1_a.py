import math


# calculate distance between two aircrafts

def calculate_distance():
    return math.sqrt((aircrafts[0]['x'] - aircrafts[0]['y']) ** 2 + (aircrafts[1]['x'] - aircrafts[1]['y']) ** 2)


def read_aircraft_positions():
    aircrafts[index]['x'] = read_int_from_user("Enter X-Position of Aircraft " + str(index + 1) + ": ")
    aircrafts[index]['y'] = read_int_from_user("Enter Y-Position of Aircraft " + str(index + 1) + ": ")


def read_int_from_user(text):
    return int(input(text))


aircrafts = [
    {"x": 1, "y": 1},
    {"x": 1, "y": 1}
]

for index, aircraft in enumerate(aircrafts):
    read_aircraft_positions()

print("\nThe distance between the aircrafts is " + str(calculate_distance()))
