x = int(input("The first side of your triangle: "))
y = int(input("The second side of your triangle: "))
z = int(input("The third side of your triangle: "))


def main():
    if x + y >= z or x + z >= y or y + z >= x:
        if x == y == z:
            print(equilateral())
        if x == y or x == z or y == z:
            print(isosceles())
        if x != y or x != z or y != z:
            print(scalene())

def equilateral():
        return "This triangle is equilateral"

def isosceles():
        return "This triangle is isosceles"

def scalene():
        return "This triangle is scalene"


if __name__ == "__main__":
    main()
