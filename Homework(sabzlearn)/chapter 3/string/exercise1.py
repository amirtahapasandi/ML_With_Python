str_of_user = input("str: ")

count_of_sentence_in_str = str_of_user.count(".") + str_of_user.count("!") + str_of_user.count("?")
print(f"Count of sentence in str's user: {count_of_sentence_in_str}")


count_of_word_in_str = str_of_user.count(" ")
print(f"Count of word in str's user: {count_of_word_in_str + 1}")


len_of_str = len(str_of_user)
print(f"length of string's user: {len_of_str}")