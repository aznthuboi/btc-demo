from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route("/")
def btc():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return('The Current Price of Bitcoin: $' + r.json()['bpi']['USD']['rate'])

def btc_history():
    mylist = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-01&end=2017-12-29')
    for x in mylist:
        return(x)

if __name__ == "__main__":
    app.run()
