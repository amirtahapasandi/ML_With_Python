from requests import get
from csv import writer
from datetime import date

token : str = "703612:669d0ed0dec8a"
URL : str = f"https://one-api.ir/DigitalCurrency/?token={token}"
response : dict = get(URL).json()
result = response["result"]
bitcoin = result[0]
price_of_bitcoin = bitcoin["price"]
ethereum = result[1]
price_of_ethereum = ethereum["price"]
tether = result[2]
price_of_tether = tether["price"]
binancecoin = result[3]
price_of_binancecoin = binancecoin["price"]

print(price_of_bitcoin)
print(price_of_ethereum)
print(price_of_tether)
print(price_of_binancecoin)

with open("my_csv_file.csv", "w") as mcf:
    writer = csv.writer(mcf)
    writer.writerow(["name", "time", "date", "price"])
    data = [["bitcoin", ],[],[],[]]