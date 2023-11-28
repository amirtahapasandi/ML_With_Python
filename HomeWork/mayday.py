string: str  = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"

list_of_string: list = string.split(" ")

num: dict = {"Zero" : 0,
             "One" : 1,
             "Two" : 2,
             "Three" : 3,
             "Four" : 4,
             "Five" : 5,
             "Six" : 6,
             "Seven" : 7,
             "Eight" : 8,
             "Nine" : 9,
             "Dash" : "-"}

for i in list_of_string:
    print(num.get(i, i[0]), end="")
