from flask import Flask
from flask import render_template, redirect, url_for, request,flash
from flask_bootstrap import Bootstrap

import json
import devices
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def control_sensor():
    return render_template('index.html')

@app.route('/getDevices')
def get_devices():
    device= devices.get()
    #device = 'OK!'
    #print(device)
    return device

'''@app.route('/star-collect')
def start():
    r = requests.get('')
    return '''

app.run('0.0.0.0', debug=True)
