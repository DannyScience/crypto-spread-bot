import json
from pydoc import resolve
import requests


response = requests.get('https://api.huobi.pro/v2/settings/common/symbols')
json_str = json.dumps(response.json()['data'])
a = response.json()['data']['0']
print(a)

with open('symbols.txt', 'w') as file:
    file.write(json_str)
    # print(response.json())
