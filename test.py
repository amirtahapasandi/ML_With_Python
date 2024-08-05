data = open("response.txt", "r")

for i in data.readline():
    print(i)
data.close()