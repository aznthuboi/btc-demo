from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def btc():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return('The Current Price of Bitcoin: $' + r.json()['bpi']['USD']['rate'])


@app.route("/history")
def btc_history():
    r = requests.get(
        'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-0')
    # dictionary
    history = r.json()['bpi']
    # render #1
    return '<br>'.join(['Date {}, Price {}'.format(i, history.get(i)) for i in history])


if __name__ == "__main__":
    app.run()
