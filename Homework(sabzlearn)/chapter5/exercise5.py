n = int(input("Num: "))

if n < 10:
    print("It's a single digit.")
elif 10 <= n <= 99:
    print("It's a two digit.")
elif 100 <= n <= 999:
    print("It's a three digit.")
elif 1000 <= n <= 9999:
    print("It's a four digit.")
elif 10000 <= n <= 99999:
    print("It's a five digit.")
elif 100000 <= n <= 999999:
    print("It's a six digit.")
elif 100000 <= n <= 999999:
    print("It's a seven digit.")
elif 1000000 <= n <= 9999999:
    print("It's a eight digit.")
elif 10000000 <= n <= 99999999:
    print("It's a nine digit.")
elif 100000000 <= n <= 999999999:
    print("It's a ten digit.")
