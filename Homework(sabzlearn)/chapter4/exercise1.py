user_number = input("Enter your number: ")

if user_number[-1] == "0" and "5":
    if int(user_number) % 2 == 0:
        print(f"{user_number} it is divisible by 2 and 5.")
    else:
        pritn(f"{user_number} it is not divisible by 2 or 5.")