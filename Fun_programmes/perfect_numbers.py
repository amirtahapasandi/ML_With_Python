x = int(input("Enter your number: "))
i = 1
list_of_numbers = []

while i < x:
    if x % i == 0:
        list_of_numbers.append(i)
    i += 1

if sum(list_of_numbers) == x:
    print("It's a perfect number!")
else:
    print("It's not a perfect number!")
