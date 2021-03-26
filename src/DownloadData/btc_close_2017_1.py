import json

filename='btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data=json.load(f)
#打印每天的信息
for btc_dict in btc_data:
    date=btc_dict['date']
    month=int(btc_dict['month'])
    week=int(btc_dict['week'])
    weekday=btc_dict['weekday']
    close=int(float(btc_dict['close']))
    print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))