from random import choice

list_of_names = ["Amir","Taha","Amirtaha","Sorena","Radman","Hirad","Mazdak","Soroush","Ario","Arash"]
print(f"Our list: {list_of_names}")

while True:
    user_choice = input("What's your choice? ").capitalize()
    computer_choice = choice(list_of_names)
    print(f"This is computer choice >>> {computer_choice}")

    user_comment = input("Did the computer guess right? (Yes,No): ").capitalize()
    if user_comment == "No":
        continue
    else:
        print("Greaaaaat it was right!")
        break
