import json
import logging
import os
import sys
import random
import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ChromeOptions


class Propawhatsapp():
    def __init__(self):
        with open('config.json', "r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f'--user-data-dir={self.config["user_data_path"]}')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument(f'--profile-directory={self.config["profile_directory"]}')
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_phone_number(self):
        resp = requests.get("https://api.1920.in")

        number = resp.text

        return number

    def attach_image(self):
        attach_button = self.driver.find_element(By.XPATH, '//span[@data-icon="clip"]')
        attach_button.click()
        time.sleep(self.config['click_wait'])

        image_button = self.driver.find_element(By.XPATH, '//span[@data-icon="attach-image"]')
        image_button.click()
        time.sleep(self.config['click_wait'])

        image_box = self.driver.find_element(By.XPATH,
                                             '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')

        img_path = random.choice(os.listdir("./img"))
        file_path = os.path.abspath(f'./img/{img_path}')
        image_box.send_keys(file_path)
        time.sleep(self.config['click_wait'])

    def send_message(self, number):
        text = random.choice(self.config['messages'])

        try:
            url = "https://web.whatsapp.com/send?phone=" + number + "&text=" + text

            self.driver.get(url)
            time.sleep(self.config['open_wait'] + random.randint(-2, 2))

            if self.config['img_enabled']:
                self.attach_image()

            send_button = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            send_button.click()
            time.sleep(self.config['click_wait'])

            logging.info("Successful, moving on.")
        except Exception as e:
            logging.error(e)
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


if __name__ == '__main__':
    prop = Propawhatsapp()
    prop.run_loop()
