from flask import Flask
from markupsafe import escape
from SentimentAnalysis import SentimentAnalysis
from sip import get_data


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/getsentiment/<company_name>')
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