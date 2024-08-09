user_str = input("str>>> ")

check_user_str = lambda x: x.replace(".","",1).isdigit()
print(check_user_str(user_str))
