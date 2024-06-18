# maximum
def max(x):
    maximum = x[0]
    for i in range (1, len(x)):
        if x[i] > maximum:
            maximum = x[i]
    return maximum

the_list_of_number = [1,2,3,3422654,82,939]
maximum_number = max(the_list_of_number)
print(maximum_number)

# minimum
def min(x):
    minimum = x[0]
    for i in range (1, len(x)):
        if x[i] < minimum:
            minimum = x[i]
    return minimum

the_list_of_number = [1,2,3,3422654,82,939]
minimum_number = min(the_list_of_number)
print(minimum_number)