people_ages = 0
how_many_people = int(input("How many people are in this group? "))

count = 1
while count <= how_many_people:
    people_ages += int(input("Enter the age of person " + str(count) + ": "))
    count += 1

print("The average age of this group is " + str(people_ages / how_many_people))
