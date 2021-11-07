import requests
from flask import Flask, Blueprint, jsonify, make_response, request

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
def get_led_status():
    status = getStatus()
    response = make_response(jsonify(status), 200)
    response.headers['content-type'] = 'application/json'
    return response

@api.route('/led', methods=['POST'])
def set_led_status():
    if 'ledOn' in request.json:
        status = toggleLED()
    if 'blinking' in request.json:
        status = toggleLEDBlinking()
    response = make_response(jsonify(status), 200)
    response.headers['content-type'] = 'application/json'
    return response

app.register_blueprint(api)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)