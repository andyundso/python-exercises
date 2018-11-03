def print_budget_slice(name_of_part, percent_number):
    print("Based on your budget, the " + name_of_part + " would cost " + str(
        round(percent_number * 100, 2)) + "% of your budget.\n")
    return


machine_a = {"materials": [
    {"name": "a1", "price_per_unit": 335, "required": 47},
    {"name": "a2", "price_per_unit": 1520, "required": 119},
], "base_costs": 25000, "specialist_per_hour": 150}

machine_b = {"materials": [
    {"name": "b1", "price_per_unit": 865, "required": 159},
], "base_costs": 40000, "specialist_per_hour": 175}

# important to note
# project manager works 42 hours per month and costs 200 per hour (means 42 * 200 cost per month)
# project management costs are between 8 and 12% of the total costs for the labour
# material and machine costs need to be below 25% of the budget

wished_machine = input("Please enter the machine name (A or B) you wish to rent: ")

if wished_machine == 'A':
    selected_machine = machine_a
elif wished_machine == 'B':
    selected_machine = machine_b
else:
    print("Unknown machine selected, please restart the program and type either A or B.")
    quit()

budget = int(input("Please enter your budget without any decimals: "))
wished_months = int(input("Please enter your wished duration of the project: "))

material_costs = 0
for material in selected_machine['materials']:
    material_costs += material['price_per_unit'] * material['required']

machine_costs = material_costs + selected_machine['base_costs']

machine_costs_percent = machine_costs / budget
if machine_costs_percent > 0.25:
    print("\nSorry, the costs for the machine would exceed 25%.")
    print_budget_slice("machine", machine_costs_percent)
    quit()
else:
    print("\nGreat, the costs for the machine do not exceed 25%.")
    print_budget_slice("machine", machine_costs_percent)

# lets see if the project manager is not too expense (or too cheap?)
project_management_costs = wished_months * 42 * 200
project_management_percent = project_management_costs / budget
if project_management_percent < 0.08:
    print("Sorry, the costs for the project manager would be below 8%.")
    print_budget_slice("project manager", project_management_percent)
    quit()
elif project_management_percent > 0.12:
    print("Sorry, the costs for the project manager would be over 12%.")
    print_budget_slice("project manager", project_management_percent)
    quit()
else:
    print("Great, the costs for the project manager would be between 8% and 12%.")
    print_budget_slice("project manager", project_management_percent)

# lets see how many hours we can run the specialist.
specialist_budget = budget - project_management_costs - machine_costs
specialist_hours = specialist_budget / selected_machine['specialist_per_hour']
print("The specialist can be rented for " + str(round(specialist_hours, 2)) + ", which equals " + str(round(
    specialist_hours / wished_months, 2)) + " hours per month")
