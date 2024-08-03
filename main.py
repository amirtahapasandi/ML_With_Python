import requests as req

query : str = input("Enter your question: ")
token : str = "703612:669d0ed0dec8a"
URL : str = f"https://one-api.ir/chatgpt/?token={token}&action=gpt4o&q={query}"
response : dict = req.get(URL).json()
result = response["result"]

with open("response.txt", "W") as f:
    f.write(result)
print("Wrote to response.txt!")