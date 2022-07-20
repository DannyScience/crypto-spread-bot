import requests
import json
import telebot
import time
import config


def getprice_kra():
    url = 'https://fapi.binance.com/fapi/v1/ticker/price'
    r = requests.get('https://api.kraken.com/0/public/AssetPairs?pair=ADAUSDT')
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print('error')


getprice_kra()
