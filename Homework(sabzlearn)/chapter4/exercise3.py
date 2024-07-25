import string
user_char = input("Enter some char: ")

def has_punctuation(input_string):
    for char in input_string:
        if char in string.punctuation:
            return True
    return False


print("Is the enterd character a number? ", user_char.isnumeric())
print("Is the enterd character a alphabetic? ", user_char.isalpha())
print("Is the enterd character a punctuation? ", has_punctuation(user_char))
