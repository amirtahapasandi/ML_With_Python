# To print sth screen in terminal window 
print("hello, Filoger!")

# Sum of two variables 
a = 5 
b = 3 
c = a + b 
print(c)

# Get 2 inputs from user and print sum of them 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a + b
print(c)

# Get temp from user 
temp = float(input("what is the temp? "))

# Suggest what to wear 
# Less than 5 : Hat  
# 5 - 15 : Hoodie 
# 15 - 25 : shirt 
# 25 - 35 : T-Shirt 

if temp <= 5:
    print("Wear a hat!")
elif 5 <= temp <= 15:
    print("wear a hoodie!")
elif 15 <= temp <= 25:
    print("Wear a shirt!")
elif 25 <= temp <= 35:
    print("Wear a T-Shirt")