import random 

number = random.randint(1,100)
while True:
    user_number = int(input("Please enter yout number(between 1 to 100): "))
    
    if user_number == number:
        print("Great!!! you guss right!")
        print(f"This was number: {number}")
        break
    elif user_number >= number:
        print("Upper! you must guees lower number.")
    else:
        print("Lower! you must guees upper number.")
        