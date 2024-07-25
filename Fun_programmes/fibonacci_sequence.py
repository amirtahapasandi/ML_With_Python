i = 0
first_number,second_number = 0,1
last_sentence = int(input("Enter last sentence(number): "))

while i <= last_sentence:
    first_number, second_number = second_number, first_number + second_number
    print(second_number)
    i += 1
