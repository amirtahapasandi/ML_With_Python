# Multiples of 3 or 5

sum_of_all_the_multiples_of_three_and_five = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_all_the_multiples_of_three_and_five += i
print(f"sum_of_all_the_multiples_of_three_and_five: {sum_of_all_the_multiples_of_three_and_five}")