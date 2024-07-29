while True:
    print("Choose your option:\n\t1)Encrypt\n\t2)Decoding\n\t3)Exit")
    user_choice = input("\nWhat's your choice? (1/2/3): ")

    if user_choice == "1":
        user_txt = input("txt>>> ")
        encrypted_txt = ""
        for c in user_txt:
            ord_of_char = ord(c) * 5 + 6
            encrypted_txt += chr(ord_of_char)
        print(f"Encrypted text: {encrypted_txt}")
        print("-" * 89)

    elif user_choice == "2":
        user_code = input("code>>> ")
        encoded = ""
        for c in user_code:
            ord_of_char = (ord(c) - 6 )// 5
            encoded += chr(ord_of_char)
        print(f"Encoded text: {encoded}")
        print("-" * 89)

    elif user_choice == "3":
        break
    else:
        print("-" * 89)
        print("Your choice was wrong!")
        print("-" * 89)
