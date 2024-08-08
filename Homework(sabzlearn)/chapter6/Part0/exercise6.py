def func(char:str)-> str:
    if 48 <= ord(char) <= 57:
        print("Your char is number!")
    elif 65 <= ord(char) <= 90:
        print("Your char is a upercase letter!")
    elif 97 <= ord(char) <= 122:
        print("Your char is a lowercase letter!")
    else:
        print("Other!")

user_char = input("Enter your char:")
func(user_char)