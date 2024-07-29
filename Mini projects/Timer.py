from time import sleep
from os import system,name


while True:
    user_choice = input("Do you want to start?(Y/N): ").capitalize()
    if user_choice == "Y":
        hour = int(input("Enter amount of hour: "))
        minutes = int(input("Enter amount of minutes: "))
        seconds = int(input("Enter amount of seconds: "))
        total = (hour * 3600) + (minutes * 60) + seconds
        print("Start...")
        while total >= 0:
            if name == "nt":
                system("cls")
            else:
                system("clear")
            print(f"Timer>>> {total}")
            sleep(1)
            total -= 1
            print("Finished.")
    elif user_choice == "N":
        break
    else:
        print("Invalid choice.")
