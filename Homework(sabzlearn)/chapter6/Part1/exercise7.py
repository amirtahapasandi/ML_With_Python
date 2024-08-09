user_str = input("str>>> ")

check_user_str = map(lambda x: x.isnumeric(), user_str)
print(list(check_user_str))