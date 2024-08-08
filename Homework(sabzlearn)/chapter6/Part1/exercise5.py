my_list = [1,2,3,4,5,6,7,8,9]

new_list = map(lambda x: x ** 2, my_list)
print(list(new_list))

new_list2 = map(lambda x: x ** 3, my_list)
print(list(new_list2))
