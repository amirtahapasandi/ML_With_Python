my_list = [-1,-2,-3,-4,-5,-6,-7,-8,-9,0,1,2,3,4,5,6,7,8,9]

even_list = filter(lambda x: x % 2 == 0, my_list)
print(list(even_list))

odd_list = filter(lambda x: x % 2 == 0 + 1, my_list)
print(list(odd_list))
