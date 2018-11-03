import time

user_countdown = int(input("Please enter a number for the countdown: "))
for_loop_countdown = user_countdown + 1
while_loop_countdown = user_countdown

while while_loop_countdown > 0:
    print(while_loop_countdown)
    while_loop_countdown -= 1
    time.sleep(1)

for x in reversed(range(for_loop_countdown)):
    print(x)
    time.sleep(1)
