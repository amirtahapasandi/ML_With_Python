def func(char:str)-> str:
    if "0" <= char <= "9":
        print("Your char is number!")
    elif "A" <= char <= "z":
        print("Your char is a upercase letter!")
    elif "a" <= char <= "z":
        print("Your char is a lowercase letter!")
    else:
        print("Other!")

user_char = input("Enter your char:")
func(user_char)