import requests
import json
import telebot
import time
bot = telebot.TeleBot('5542493071:AAGDxcIF-kKpFs8GuJCBeipr8DBHNCVlx3A')
bot2 = telebot.TeleBot('5517949323:AAGLO_ezhvbw_loJuOgtPOKi-6_2W2JJsTw')

bot.send_message(492639112, 'launching', parse_mode='html')


class Price:    # the class recieves pair name and link for api requests to return price using certain method
    def __init__(self, pair, source):
        self.pair = pair
        self.source = source

# get a price from binance
    def getprice_bin(self):
        url = self.source
        param = {'symbol': self.pair}
        r = requests.get(url, params=param)
        if r.status_code == 200:
            data = r.json()
        else:
            print('error')
            # bpbtc = b -binance + p-price + btc - ticker
        price = float(data['price'])
        return price

# get a price from huobi
    def getprice_huo(self):
        url = self.source
        param = {'symbol': self.pair}
        r = requests.get(url, params=param)
        if r.status_code == 200:
            data = r.json()
        else:
            print('error')
        hpbtc0 = data['tick']
        hpbtc00 = hpbtc0['bid']
        price = float(hpbtc00[0])
        return price


def compare(ticker, exchange, arg1, arg2):    # function to compare prices
    percent = round(abs(arg1-arg2) / arg1 * 100, 3)
    if percent > 0.0001:
        print(ticker + ' ' + exchange + ' ' + str(percent) + '%')
        bot.send_message(492639112, ticker + ' ' +
                         exchange + ' ' + str(percent) + '%')


def alert_check(price):   # alert function
    if price > 22500:
        bot2.send_message(492639112, 'BTC above alert line!!!!!!!!!!!!!!!')
    elif price < 18500:
        bot2.send_message(492639112, 'BTC below alert line!!!!!!!!!!!!!!!')


# defining pairs and api links
bbtc = Price('BTCUSDT', 'https://fapi.binance.com/fapi/v1/ticker/price')
hbtc = Price(
    'BTCUSDT', 'https://api.huobi.pro/market/detail/merged?symbol=btcusdt')
beth = Price('ETHUSDT', 'https://fapi.binance.com/fapi/v1/ticker/price')
heth = Price(
    'ETHUSDT', 'https://api.huobi.pro/market/detail/merged?symbol=ethusdt')


# compairing process nonstop
while True:
    compare('BTCUSDT', 'Binance-Huobi',
            bbtc.getprice_bin(), hbtc.getprice_huo())
    compare('ETHUSDT', 'Binance-Huobi',
            beth.getprice_bin(), heth.getprice_huo())
    alert_check(bbtc.getprice_bin())
    time.sleep(10)
