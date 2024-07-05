import copy

# Shallow copy
l1 = [1, 2, ["A", "B"]]
l2 = copy.copy(l1)

print(id(l1))
print(id(l2))

l2[2][0] = "0"
print(l1)
print(l2)


# Deep copy
l1 = [1, 2, ["A", "B"]]
l2 = copy.copy(l1)

print(id(l1))
print(id(l2))

l2[2][0] = "0"
print(l1)
print(l2)