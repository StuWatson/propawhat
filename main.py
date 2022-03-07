import json
import logging
import sys

import pywhatkit
import random
import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

with open('config.json') as config_file:
    config = json.load(config_file)


class Propawhatsapp():
    def __init__(self):
        self.driver = uc.Chrome()
        self.driver.get(config['url'])
        time.sleep(config['page_load_wait_time'])

    def get_phone_number(self):
        refreshButton = self.driver.find_element(By.ID, 'buttonReload')
        refreshButton.click()
        time.sleep(config['number_refresh_wait'])

        number_tag = self.driver.find_element(By.ID, 'phoneNumber')
        number_text = number_tag.text
        number = number_text[1:]

        return number

    def send_message(self, number):
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

    def run_loop(self):
        while True:
            try:
                number = self.get_phone_number()
            except Exception as e:
                logging.error(e)
                logging.error("Error retrieving phone number, ending process")
                sys.exit()
            self.send_message(number)



prop = Propawhatsapp()
prop.run_loop()


