def square_number(number):
    for i in range(1,10):
        power_of_numbers = i * i
        if number == power_of_numbers:
            return f"{number} is a square number!"

print(square_number(number = int(input("Num: "))))