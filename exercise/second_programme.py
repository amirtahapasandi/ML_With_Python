x = int(input("Enter your number: "))
f = 1

for i in range(x):
    f = f * (i + 1)
    print("i+1 is:", i+1)
    print("f is:", f)
print(x,"!=", f)
