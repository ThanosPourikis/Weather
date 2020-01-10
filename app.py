import requests
import json
import os 
from flask import Flask, render_template
import time
import config

PATRAS = str([38.245965, 21.735061]).replace('[','').replace(']','')
EXCLUDE = str(['currently','flags','daily']).replace('[','').replace(']','')
KEY = config.ApiKey

def darkskyapicall(key,loc,exclude):
	responce = requests.get("https://api.darksky.net/forecast/{}/{}?exclude={}".format(key,loc,exclude))
	with open('data.json','w') as json_file:
			json.dump(json.loads(responce.content),json_file,indent=4)


def weather_data():
	if(not(os.path.exists('data.json'))):
		darkskyapicall(KEY,PATRAS,EXCLUDE)
	else:
		with open('data.json','r') as json_file:
			try:
				data = json.load(json_file)
				if(time.time() - data['hourly']['data'][0]['time'] > 3600):
					darkskyapicall(KEY,PATRAS,EXCLUDE)
				return json.loads(json_file)
			except:
				darkskyapicall(KEY,PATRAS,EXCLUDE)
		
	
	with open('data.json','r') as json_file:
		return json.load(json_file)

app = Flask(__name__)

def ctime(tim):
	return time.ctime(tim)
app.jinja_env.globals.update(ctime=ctime)

@app.route('/')
def index():
	data=weather_data()
	return render_template('index.html',data=data)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)
	
 