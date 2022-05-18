from flask import Flask, render_template, request, flash, make_response
import requests, json

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/charts', methods=['POST', 'GET'])
def charts():
	#flash(str(request.form['name_input']))
	return render_template('indexx.html')

@app.route('/api', methods=['POST', 'GET'])
def api():
    payload = {}
    headers = {}
    #url = "https://demo-live-data.highcharts.com/"+str(request.form['name_input'])+"-ohlcv.json"
    url = "https://demo-live-data.highcharts.com/aapl-ohlcv.json"
    r = requests.get(url, headers=headers, data ={})
    r = r.json()
    return {"res":r}

#print(request.form['name_input'])

if __name__ == '__main__':
	flask.run(debug=True)
