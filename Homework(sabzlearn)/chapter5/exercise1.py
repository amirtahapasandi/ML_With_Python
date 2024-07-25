n1 = int(input("Num:"))
n2 = int(input("Num:"))

if n1 < n2:
    min_num = n1
else:
    min_num = n2
if n1 > n2:
    max_num = n1
else:
    mac_num = n2 

for i in range(min_num, max_num):
    print(i)
