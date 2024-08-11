from requests import get
from csv import writer
from datetime import datetime, date

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
date = date.today()
time = datetime.now().time()

with open("csv_file.csv", "w", newline = "") as cf:
    writer = writer(cf)
    writer.writerow(["name", "time", "date", "price"])
    data = [["bitcoin", f"{time}", f"{date}", f"{price_of_bitcoin}"],
            ["etherum", f"{time}", f"{date}", f"{price_of_ethereum}"],
            ["tether", f"{time}", f"{date}", f"{price_of_tether}"],
            ["binancecoin", f"{time}", f"{date}", f"{price_of_binancecoin}"]]
    writer.writerows(data)