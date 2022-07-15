import requests
import json

# obtaining BTC price from Binance
url = 'https://fapi.binance.com/fapi/v1/ticker/price'
param = {'symbol': 'BTCUSDT'}
r = requests.get(url, params=param)
if r.status_code == 200:
    # data = json.dumps(r.json()) - error
    data = r.json()
else:
    print('error')
bpbtc = float(data['price'])
print(bpbtc)  # bpbtc = b -binance + p-price + btc - ticker

# obtaining BTC price from Huobi
url2 = 'https://api.huobi.pro/market/detail/merged?symbol=btcusdt'
param = {'symbol': 'BTCUSDT'}
r2 = requests.get(url2, params=param)
if r2.status_code == 200:
    data2 = r2.json()
    # print(data2)
else:
    print('error2')
hpbtc0 = data2['tick']
hpbtc00 = hpbtc0['bid']
hpbtc = float(hpbtc00[0])
print(hpbtc)

# compairing prices and counting a percent difference
if float(hpbtc) > float(bpbtc):
    hbpd = hpbtc - bpbtc
    hbpdpercent = hbpd / hpbtc * 100
    print(hbpdpercent)
else:
    hbpd = bpbtc - hpbtc
    hbpdpercent = hbpd / hpbtc * 100
    print(hbpdpercent)
