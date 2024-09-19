import random

def dice(n:int):
    x = 0
    while True:
        first_dice = random.randrange(1,7)
        second_dice = random.randrange(1,7)
        print(f"{first_dice, second_dice}")
        x += 1
        if x == n:
            break

while True:
    user_choice = input("Roll the dice? (y/n): ").upper()
    if user_choice == "Y":
        number_of_dice = int(input("How many times do you want tp roll the dice? (1,...): "))
        dice(number_of_dice)
        print(f"You rolled the dice {number_of_dice} times.")
    elif user_choice == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
