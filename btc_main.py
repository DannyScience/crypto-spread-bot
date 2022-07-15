import requests
import json

# получаем цену биткоина на бинанс фьючерсах
url = 'https://fapi.binance.com/fapi/v1/ticker/price'
param = {'symbol': 'BTCUSDT'}
r = requests.get(url, params=param)
if r.status_code == 200:
    # data = json.dumps(r.json()) - дает ошибку при обращении к словарю
    data = r.json()
    print(data)
else:
    print('error')
a = data['price']
print(a)

# получаем цену биткоина на huobi
url2 = 'https://api.huobi.pro/v1/common/symbols'
r2 = requests.get(url2, params=param)
if r2.status_code == 200:
    data2 = r2.json()
    print(data2)
else:
    print('error2')
a2 = data2['price']
print(a2)
