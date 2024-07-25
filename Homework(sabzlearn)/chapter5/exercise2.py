n1 = int(input("Num: "))
n2 = int(input("Num: "))
common_denominators = []

for i in range(1,n1+1):
    if n1 % i == 0 and n2 % i == 0:
        common_denominators.append(i)
print(common_denominators)
