# Multiples of 3 or 5

sum_of_all_the_multiples_of_three = 0
for i in range(1,1001):
    sum_of_all_the_multiples_of_three = sum_of_all_the_multiples_of_three + (3*i)
print(f"sum of all the multiples of three: {sum_of_all_the_multiples_of_three}")

print(90 * "-")

sum_of_all_the_multiples_of_five = 0
for j in range(1,1001):
    sum_of_all_the_multiples_of_five = sum_of_all_the_multiples_of_five + (5*i)
print(f"Sum of all the multiples of five: {sum_of_all_the_multiples_of_five}")

print(90 * "-")

sum_of_all_the_multiples_of_three_and_five = sum_of_all_the_multiples_of_three + sum_of_all_the_multiples_of_five
print(f"Sum of all the multiples of three and five: {sum_of_all_the_multiples_of_three_and_five}")
