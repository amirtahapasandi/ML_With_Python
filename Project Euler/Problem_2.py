def is_even(n:int):
    if n % 2 == 0:
        return True
    return False

first_num = 1
second_num = 2
new_num = 0
sum_of_numbers = 0
while new_num < 4000000:
    new_num = first_num + second_num
    first_num = second_num
    second_num = new_num
    if is_even(first_num):
       sum_of_numbers = sum_of_numbers + first_num
print(sum_of_numbers)
