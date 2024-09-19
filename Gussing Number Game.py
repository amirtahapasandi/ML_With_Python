from random import randint

random_number = randint(1,100)
while True:
    user_choice = int(input("Guss the number between 1 and 100: "))
    if user_choice > random_number:
        print("Too high!")
    elif user_choice < random_number:
        print("Too low!")
    elif user_choice == random_number:
        print("Congratulations! You gussed the number.")
        break
    else:
        print("Enter a valid number!")