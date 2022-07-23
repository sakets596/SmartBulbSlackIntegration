#pip install tuya-connector-python
from tuya_connector import TuyaOpenAPI
import os
# pip install python-dotenv
import dotenv
from pathlib import Path


ENV_PATH = Path('auth/.env')
dotenv.load_dotenv(ENV_PATH)
ACCESS_ID = os.environ['ACCESS_ID']
ACCESS_KEY = os.environ['ACCESS_KEY']


ENDPOINT = 'https://openapi.tuyaus.com'
FINGUREBOT_DEVICE_ID = os.environ['FINGUREBOT_DEVICE_ID']

def bulb_on():

    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
    print(openapi.connect())
    commands = {'commands': [{'code': 'switch_led', 'value': True}]}
    result = openapi.post(f'/v1.0/iot-03/devices/{FINGUREBOT_DEVICE_ID}/commands', commands)
    print(commands)

def bulb_off():

    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
    print(openapi.connect())
    commands = {'commands': [{'code': 'switch_led', 'value': False}]}
    result = openapi.post(f'/v1.0/iot-03/devices/{FINGUREBOT_DEVICE_ID}/commands', commands)
    print(commands)