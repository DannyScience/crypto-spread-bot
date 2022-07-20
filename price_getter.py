import requests


def getprice_bin(coin1="btc", coin2="usdt"):
    url = 'https://fapi.binance.com/fapi/v1/ticker/price'
    param = {'symbol': f'{coin1.upper()}{coin2.upper()}'}
    response = requests.get(url, params=param)
    price = float(response.json()['price'])
    return price


def getprice_huo(coin1="btc", coin2="usdt"):
    url = f'https://api.huobi.pro/market/detail/merged?symbol={coin1}{coin2}'
    response = requests.get(url)
    price = float(response.json()['tick']['bid'][0])
    return price


def getprice_yob(coin1="btc", coin2="usdt"):
    url = f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1'
    response = requests.get(url)
    price = float(response.json()[f'{coin1}_{coin2}']['last'])
    return price


def main():
    print(getprice_bin())
    print(getprice_huo())
    print(getprice_yob())


if __name__ == "__main__":
    main()
