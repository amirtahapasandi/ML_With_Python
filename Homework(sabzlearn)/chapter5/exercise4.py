n1 = int(input("Num: "))
n2 = int(input("Num: "))
common_denominators = []
min_num = min(n1, n2)

for i in range(1, min_num+1):
    if n1 % i == 0 and n2 % i == 0:
        common_denominators.append(i)
print(min(common_denominators))