from flask import Flask, request, render_template
app = Flask(__name__)
import flask_monitoringdashboard as dashboard
import logging
logging.basicConfig(level=logging.DEBUG)
dashboard.bind(app)
import requests
import json

#API endpoint
url = "http://web3:5000/sentiment"

def check(key):
    real = "lol"
    if key == real:
        return True
    else:
        return False

@app.before_request
def before_request():
    response = app.logger.info("before request")
    return response

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    app.logger.info('%s logged in successfully')
    return render_template("index.html", name="zak")

@app.route('/photo', methods=['GET','POST'])
def photo():
    try:
        if request.method == 'POST':
            print("RQ", request)
            text = request.form['sentence']
            print(text)
            params = {"text":text, "key":"lol"}
            response = requests.post(url, params)
            print("response", response)
            result = response.json()['prediction']

    except:
        result = "no value"

    return render_template("photo.html", result=result)

@app.after_request
def after_request(response):
    app.logger.info("after request")
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
