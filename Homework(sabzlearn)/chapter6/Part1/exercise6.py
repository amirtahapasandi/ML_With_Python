user_str = input("str>>> ").capitalize()

check_user_str = map(lambda x: x.startswith("A"), user_str)
print(list(check_user_str))
