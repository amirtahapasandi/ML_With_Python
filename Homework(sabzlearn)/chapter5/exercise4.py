n1 = int(input("Num: "))
n2 = int(input("Num: "))
min_num = min(n1, n2)
max_num = max(n1, n2)

for i in range(1, min_num+1):
    if (max_num * i) % min_num == 0:
        print(max_num * i)
        break
