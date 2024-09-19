from random import choice

while True:
    list_of_elements = ["Rock","Paper","Scissors"]
    computer_choice = choice(list_of_elements)
    user_choice = input("Rock, Paper, Scissors: (r/p/s): ").lower()
    valid_choices = ["r","p","s"]
    if user_choice not in valid_choices:
        print("Invalid choice.")
    elif user_choice == "r":
        print("You chosed Rock.")
        if computer_choice == "Rock":
            print("computer chosed Rock.")
            print("Equal")
        elif computer_choice == "Paper":
            print("computer chosed Paper.")
            print("Computer won the game.")
        elif computer_choice == "scissors":
            print("computer chosed scissors.")
            print("You won the game.")
    elif user_choice == "p":
        print("You chosed Paper.")
        if computer_choice == "Rock":
            print("computer chosed Rock.")
            print("You won the game.")
        elif computer_choice == "Paper":
            print("computer chosed Paper.")
            print("Equal")
        elif computer_choice == "scissors":
            print("computer chosed scissors.")
            print("Computer won the game.")
    elif user_choice == "s":
        print("You chosed Scissors.")
        if computer_choice == "Rock":
            print("computer chosed Rock.")
            print("Computer won the game.")
        elif computer_choice == "Paper":
            print("computer chosed Paper.")
            print("You won the game.")
        elif computer_choice == "scissors":
            print("computer chosed scissors.")
            print("Equal.")