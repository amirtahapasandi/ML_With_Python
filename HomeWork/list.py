n1 = [x for x in range(10) if x % 2 == 0]
n2 = [x for x in range(10) if x % 2 != 0]

zipped = list(zip(n1, n2))

zipped_2 = zipped[::-1]

zipped_2.extend(n2[::-1])

n1[-5:-5] = [999]

n1[1:4] = ['a', 'b', 'c']

lst = sorted(n1, key=lambda x: (isinstance(x, int), x), reverse=True)

print(lst)
print(type(lst[0]))
print(type(lst[3]))
