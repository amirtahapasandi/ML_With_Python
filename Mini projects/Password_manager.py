import string
import random

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all_string = letters + digits + punctuation

while True:
    print("Choose your option:\n\t1)Create a Password\n\t2)Exit")
    user_choice = input("What's your choice? (1 or 2): ").capitalize()
    if user_choice == "1":
        length_of_password = int(input("Enter the lenght of password: "))
        password = "".join(random.sample(all_string, length_of_password))
        print(f"It's your password: {password}")
        break
    elif user_choice == "2":
        break
    else:
        print("Your choice was wrong!\n")