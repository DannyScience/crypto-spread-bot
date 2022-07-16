import requests
import json
import telebot
bot = telebot.TeleBot('5542493071:AAGDxcIF-kKpFs8GuJCBeipr8DBHNCVlx3A')

# obtaining BTC price from Binance

bot.send_message(492639112, 'launching', parse_mode='html')


def dbpbtc():
    url = 'https://fapi.binance.com/fapi/v1/ticker/price'
    param = {'symbol': 'BTCUSDT'}
    r = requests.get(url, params=param)
    if r.status_code == 200:
        # data = json.dumps(r.json()) - error
        data = r.json()
    else:
        print('error')
    bpbtc = float(data['price'])  # bpbtc = b -binance + p-price + btc - ticker
    return bpbtc


bpbtc = dbpbtc()
print(bpbtc)


# obtaining BTC price from Huobi
def dhpbtc():
    url2 = 'https://api.huobi.pro/market/detail/merged?symbol=btcusdt'
    param = {'symbol': 'BTCUSDT'}
    r2 = requests.get(url2, params=param)
    if r2.status_code == 200:
        data2 = r2.json()
    else:
        print('error2')
    hpbtc0 = data2['tick']
    hpbtc00 = hpbtc0['bid']
    hpbtc = float(hpbtc00[0])
    return hpbtc


hpbtc = dhpbtc()
print(hpbtc)


# compairing prices and counting a percent difference nonstop
while 1 == 1:
    bpbtc = dbpbtc()
    hpbtc = dhpbtc()
    if float(hpbtc) > float(bpbtc):
        hbpd = hpbtc - bpbtc
        hbpdpercent = hbpd / hpbtc * 100
        hbpdpercent = round(hbpdpercent, 3)
        if hbpdpercent > 0.06:
            print('huobi - binance btcusdt spread is ' +
                  str(hbpdpercent) + '%')
            bot.send_message(492639112, 'huobi - binance btcusdt spread is ' +
                             str(hbpdpercent) + '%', parse_mode='html')
    else:
        hbpd = bpbtc - hpbtc
        hbpdpercent = hbpd / hpbtc * 100
        hbpdpercent = round(hbpdpercent, 3)
        if hbpdpercent > 0.05:
            print('binance - huobi btcusdt spread is ' +
                  str(hbpdpercent) + '%')
            bot.send_message(492639112, 'binance - huobi btcusdt spread is ' +
                             str(hbpdpercent) + '%', parse_mode='html')

bot.polling(non_stop=True)
