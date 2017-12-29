import requests

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
s = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-01&end=2017-12-29')
print('The Current Price of Bitcoin: $' + r.json()['bpi']['USD']['rate'])
mylist = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-01&end=2017-12-29')
for x in mylist:
    print(x)
