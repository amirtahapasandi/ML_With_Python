a = 2
b = 330

if a > b: print("a is greater than b")

print("A") if a > b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.

print("A") if a > b else print("=") if a == b else print("B")

# Get some input from the user and store it in a list.
l = [int(x) for x in input("x,y,z: ").split(",")]
print(30*"-")
print(l)