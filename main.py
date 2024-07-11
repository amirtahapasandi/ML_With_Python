user_number = int(input("Enter some number: "))
sum_of_user_number = 0
count = 0


while user_number != -1:
    sum_of_user_number += user_number
    print(user_number)
    print(sum_of_user_number)
    count = count + 1
    user_number = int(input("Enter some number: "))
    if user_number == -1:
        break


print(count)
print(sum_of_user_number / count)