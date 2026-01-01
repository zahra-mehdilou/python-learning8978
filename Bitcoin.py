import requests
import time

while True:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = float(data["bitcoin"]["usd"])
    print("current price is:", price)
    if price<800000:
        print("Time to buy")
    elif price>90000:
        print("Wait!")
    elif price>100000:
        break
    time.sleep(600)
