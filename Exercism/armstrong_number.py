user_number = input("Number: ")
length_of_user_number = len(user_number)


for i in user_number:
    new_user_number = int(i) ** length_of_user_number
    
print(new_user_number) 