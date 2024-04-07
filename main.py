from flask import Flask
from markupsafe import escape
from SentimentAnalysis import SentimentAnalysis
from sip import get_data
from wallstreet import Stock, Call, Put
import yfinance as yf
import requests
from flask_cors import CORS, cross_origin


app = Flask(__name__)


CORS(app, support_credentials=True)


def get_ticker(company_name):
    url = "https://s.yimg.com/aq/autoc"
    parameters = {'query': company_name, 'lang': 'en-US'}
    response = requests.get(url=url, params=parameters)
    data = response.json()
    print(data)
    # Extract the ticker symbol from the API response
    ticker_symbol = data['ResultSet']['Result'][0]['symbol']
    return ticker_symbol

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/getsentiment/<company_name>')
@cross_origin(supports_credentials=True)
def hello_world(company_name):
    obj = SentimentAnalysis()
    response = obj.lol(escape(company_name))
    return {
        "positive" : response[0],
        "negative" : response[1],
        "neutral" : response[2]
    }

@app.route('/newone')
def tf():
    return 'tf'


@app.route('/getsipreturns/<amt>/<fund_id>/<months>')
def get_sip_returns(amt, fund_id, months):
    response = get_data(int(escape(amt)), int(escape(fund_id)), int(escape(months)))
    return {
        "meta" : response[0],
        "current_amt" : response[1]
    }

@app.route('/gethistoricaldata/<company_name>')
@cross_origin(supports_credentials=True)
def get_live_data(company_name):
    s = Stock(company_name)
    df = s.historical(days_back=30, frequency='d')
    print(df['Date'].iloc[-1])
    return {
        "stockName": s.name,
        "basePrice": s.price,
        "lastPrice": s.last_trade,
        "pChange": s.cp,
        "closePrice": df['Close'].tolist(),
        "date": df['Date'].tolist(),
        "historicalData": df.to_dict(),
    }