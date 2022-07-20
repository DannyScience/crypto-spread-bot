import requests
import json


def getBitcoinPrice():
    url = "https://www.bitstamp.net/api/v2/ticker/BTCUSDT/"
    r = requests.get(url)
    data = r.json()
    a = data[0]['last']
    print(a)


getBitcoinPrice()
