import json
import logging
import pywhatkit
import requests
import random
import time

with open('config.json') as config_file:
    config = json.load(config_file)


def get_phone_number():
    try:
        resp = requests.get(config['api'])
    except requests.exceptions.RequestException:
        logging.error("Error retrieving phone number, retrying in 30s")
        time.sleep(30)
        return get_phone_number()

    return resp.text


while True:
    number = get_phone_number()

    text = random.choice(config['messages'])

    try:
        pywhatkit.sendwhatmsg_instantly(f'+{number}',
                                        text,
                                        config['wait_time'] + random.randint(-2, 2),
                                        config['tab_close'],
                                        config['close_time'] + random.randint(-2, 2))

        logging.info("Successful, moving on.")
    except:
        logging.error("Unable to send message, trying next number")



