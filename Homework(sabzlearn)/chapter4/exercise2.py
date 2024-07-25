x,y,z = input("Enter the angles of the triangle: ").split(" ")
a,b,c = input("Enter the lenght of the sides of the triangle: ").split(" ")

if int(x) + int(y) + int(z) == 180:
    print("It's a triangle!")
    if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
        print("It's a Isosceles triangle!")
    if int(x) == 90 or int(y) == 90 or int(z) == 90:
        print("It's a right triangle!")
    if int(a) == int(b) == int(c) and (int(x) and int(y) and int(z)) == 60:
        print("It's a equilateral triangle!")
    if int(a) != int(b) and int(a) != int(c) and int(b) != int(c) and int(x) != int(y) and int(x) != int(z) and int(y) != int(z):
        print("It's a scalene triangle!")
else:
    print("It's not triangle!")