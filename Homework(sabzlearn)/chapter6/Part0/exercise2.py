def max_of_numbers(*user_numbers:int):
    max_num = float("-inf")
    for i in user_numbers:
        if i > max_num:
            max_num = i
    return max_num

# user_input = int(input("Enter yout number or numbers: "))
print(max_of_numbers(1,2,3,5,15,3,2534657,6365,2652,636356))
