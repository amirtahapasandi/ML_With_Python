my_list = [0,1,2,3,4,5,6,7,8,9,10]

even = filter(lambda x: x % 2 == 0, my_list)
print(list(even))

odd = filter(lambda x: (x % 2 == 0 + 1), my_list)
print(list(odd))
