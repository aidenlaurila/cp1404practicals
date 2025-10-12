import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6
MINIMUM_QUICK_PICKS = 5

number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < MINIMUM_QUICK_PICKS:
    print(f"Quick picks must be at least {MINIMUM_QUICK_PICKS}")
    number_of_quick_picks = int(input("How many quick picks? "))

for line in range(number_of_quick_picks):
    quick_pick = []
    for i in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))