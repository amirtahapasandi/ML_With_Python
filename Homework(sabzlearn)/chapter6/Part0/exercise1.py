def lenght_of_string(string:str)-> int:
    lenght = 0
    for _ in string:
        lenght += 1
    return lenght

user_str = input("str: ")
print(lenght_of_string(user_str))
