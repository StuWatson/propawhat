import pywhatkit
import json
import requests
import random

with open('config.json') as config_file:
    config = json.load(config_file)

while True:
    resp = requests.get(config.api)

    number = resp.text

    text = random.choice(config['messages']);

    try:
        pywhatkit.sendwhatmsg_instantly(f'+{number}', text, config['wait_time'], config['tab_close'], config['close_time'])
    except:
        print("Error with this phone number, moving on.")



