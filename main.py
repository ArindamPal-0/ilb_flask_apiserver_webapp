import requests
from flask import Flask

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



@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)

    print(toggleLED())