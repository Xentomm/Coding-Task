import requests
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_values(data, key):
    res = []
    for value in data:
        if key in value:
            res.append(value[key])
    return res


def calculate_max_difference(bid, ask):
    result = []
    for i in range(len(bid)):
        result.append(ask[i] - bid[i])
    return max(result)

def abort_if_wrong_input(quotations, code):
    url = f'http://api.nbp.pl/api/exchangerates/tables/a/'
    response = requests.get(url)
    data = response.json()[0]['rates']
    codes = get_values(data, 'code')
    if 1 <= int(quotations) <= 255 and code.upper() in codes:
        return
    else:
        abort(400, 'Invaid data')

def abort_wrong_code(code):
    url = f'http://api.nbp.pl/api/exchangerates/tables/a/'
    response = requests.get(url)
    data = response.json()[0]['rates']
    codes = get_values(data, 'code')
    if code.upper() in codes:
        return
    else:
        abort(400, 'Invaid data')


@app.route('/')
def home():
    message = ['1. To see average exchange rate provide /average/{code}/{date} in the url', \
               '2. To see min and max average value provide /minmax/{code}/{quotations} in the url', \
                '3. To see major difference provide /buyask/{code}/{quotations} in the url']
    return render_template('index.html', message = message)

@app.route('/average/<code>/<date>')
def average(code, date):
    abort_wrong_code(code)
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}'

    response = requests.get(url)
    data = response.json()['rates'][0]['mid']
    message = [f'Average exchange rate for {code} in {date}: {data}']
    return render_template('index.html', message = message)

@app.route('/minmax/<code>/<quotations>')
def max_min(quotations, code):
    abort_if_wrong_input(quotations, code)
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/last/{quotations}/'
    response = requests.get(url)
    data = response.json()['rates']
    result = get_values(data, 'mid')
    message = [f'Maximum average value of {code} in last {quotations} quotations: {max(result)}.',
            f'Mininmum average value of {code} in last {quotations} quotations: {min(result)}.']
    return render_template('index.html', message = message)

@app.route('/buyask/<code>/<quotations>')
def buy_ask(code, quotations):
    abort_if_wrong_input(quotations, code)
    url = f'http://api.nbp.pl/api/exchangerates/rates/c/{code}/last/{quotations}/'
    response = requests.get(url)
    data = response.json()['rates']
    bid = get_values(data, 'bid')
    ask = get_values(data, 'ask')
    result = calculate_max_difference(bid, ask)
    message = [f'Maximum difference between the buy and ask rate for {code} in {quotations} quotations is: {result:.6f}']
    return render_template('index.html', message = message)