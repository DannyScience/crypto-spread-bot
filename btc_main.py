import requests
import json
import telebot
import time
import config

bot = telebot.TeleBot(config.bot1tocken)
bot2 = telebot.TeleBot(config.bot2tocken)

bot.send_message(492639112, 'launching', parse_mode='html')


class Pair:    # the class recieves pair name and link for api requests to return price using certain method
    def __init__(self, coin1, coin2):
        self.coin1 = coin1
        self.coin2 = coin2

# get a price from binance
    def getprice_bin(self):
        url = 'https://fapi.binance.com/fapi/v1/ticker/price'
        param = {'symbol': f'{self.coin1.upper()}{self.coin2.upper()}'}
        try:
            response = requests.get(url, params=param)
            price = float(response.json()['price'])
            return price
        except:
            pass

# get a price from huobi
    def getprice_huo(self):
        url = f'https://api.huobi.pro/market/detail/merged?symbol={self.coin1}{self.coin2}'
        try:
            response = requests.get(url)
            price = float(response.json()['tick']['bid'][0])
            return price
        except:
            pass


# get a price from yobit

    def getprice_yob(self):
        url = f'https://yobit.net/api/3/ticker/{self.coin1}_{self.coin2}?ignore_invalid=1'
        try:
            response = requests.get(url)
            price = float(response.json()[
                          f'{self.coin1}_{self.coin2}']['last'])
            return price
        except:
            pass

# get a price from multiple exchanges 1 per day


def compare(arg1, arg2):    # function to compare prices
    if arg1 == None or arg2 == None:
        pass
    else:
        percent = round(abs(arg1-arg2) / arg1 * 100, 3)
        if percent > 0.0001:
            print('ticker' + ' ' + 'exchange' + ' ' + str(percent) + '%')
            #bot.send_message(492639112, ticker + ' ' + exchange + ' ' + str(percent) + '%')


# alert triggers
maxprice = 25000
minprice = 18500


def alert_check(price):   # alert function
    global maxprice
    global minprice
    if price > maxprice:
        bot2.send_message(492639112, 'BTC above alert line!')
        maxprice += 500
    elif price < minprice:
        bot2.send_message(492639112, 'BTC below alert line!')
        minprice -= 500


# defining pairs
btc = Pair('btc', 'usdt')


# compairing process nonstop
def main():
    while True:
        compare(btc.getprice_bin(), btc.getprice_huo())
        compare(btc.getprice_bin(), btc.getprice_yob())
        compare(btc.getprice_huo(), btc.getprice_yob())
        alert_check(btc.getprice_bin())
        time.sleep(10)


if __name__ == '__main__':
    main()
