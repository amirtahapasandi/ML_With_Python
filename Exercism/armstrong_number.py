user_number : int=(input("Number?"))

length_of_user_number = len(user_number)
print(type(length_of_user_number))
int_of_user_number = int(user_number)
for i in int_of_user_number:
    new_number = i ** length_of_user_number

if new_number == user_number:
    print("It`s a armstrong number!")
else:
    print("It`s not a armstrong number!")