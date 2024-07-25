n1 = int(input("Num:"))
n2 = int(input("Num:"))

min_num = n1 < n2 or n2 < n1
max_num = n1 > n2 or n2 > n1
for i in range(min_num, max_num):
    print(i)
