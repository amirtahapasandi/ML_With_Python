from random import randint

random_number = randint(1,100)
while True:
    user_choice = input("Guss the number between 1 and 100: ")
    if int(user_choice) > random_number:
        print("Too high!")
    elif int(user_choice) < random_number:
        print("Too low!")
    elif int(user_choice) == random_number:
        print("Congratulations! You gussed the number.")
        break
    else:
        print("Enter a valid number!")