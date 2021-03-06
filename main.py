import requests
from flask import Flask, Blueprint, jsonify, send_from_directory
from flask import render_template, make_response, request, url_for
from flask_cors import cross_origin
import os

app = Flask(__name__)

iotDeviceURI = 'http://192.168.29.48/'

def getStatus() -> dict:
    """
        ### getStatus
        returns the status of LED
    """
    r = requests.get(iotDeviceURI)
    status = r.json()
    if(status):
        return status
    else:
        return None

def toggleLED() -> dict:
    """
        ### toggleLED
        toggle the LED on/off and returns the status
    """
    r = requests.get(iotDeviceURI + 'ledtoggle')
    status = r.json()
    if(status):
        return status
    else:
        return dict()

def toggleLEDBlinking() -> dict:
    """
        ### toggleLEDBlinking
        toggles the blinking of LED
    """
    r = requests.get(iotDeviceURI + 'ledblinking')
    status = r.json()
    if(status):
        return status
    else:
        return dict()

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/led')
@cross_origin()
def get_led_status():
    status = getStatus()
    response = make_response(jsonify(status), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@api.route('/led', methods=['POST'])
@cross_origin()
def set_led_status():
    status = getStatus()
    if request.json:
        if 'ledOn' in request.json:
            status = toggleLED()
        if 'blinking' in request.json:
            status = toggleLEDBlinking()
    else:
        status["failed"] = True

    #print(status)
    response = make_response(jsonify(status), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

app.register_blueprint(api)

@app.route('/')
def index():
    response = make_response(render_template('index.html'), 200)
    response.headers['content-type'] = 'text/html'
    return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)