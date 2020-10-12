import json
from flask import Flask, render_template
import config
import time
from call import weather_data




app = Flask(__name__)



def ctime(tim):
	return time.ctime(tim)


@app.route('/')
def index():
	data=weather_data()
	return render_template('index.html',data=data,ctime = ctime)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)
	
 