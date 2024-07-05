l1 = [1, 2, ["A", "B"]]
l2 = l1.copy()

print(id(l1))
print(id(l2))

l2[2][0] = "0"
print(l1)
print(l2)

# Shallow copy
# Deep copy  