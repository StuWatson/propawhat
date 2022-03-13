import json
import logging
import smtplib
import sys
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium.webdriver.common.by import By
import time
import undetected_chromedriver.v2 as uc

logger = logging.getLogger("Propamail")
logger.setLevel(logging.INFO)


class Propaemail():
    def __init__(self):
        with open('mail_config.json', "r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)

        self.smtpObj = smtplib.SMTP(self.config['smtp_host'])

        if 'smtp_username' in self.config and 'smtp_password' in self.config:
            self.smtpObj.login(self.config['smtp_username'], self.config['smtp_password'])

        chrome_options = uc.ChromeOptions()
        self.driver = uc.Chrome(options=chrome_options)
        url = "https://mail.1920.in"
        self.driver.get(url)
        time.sleep(self.config['page_load_wait_time'])

    def get_email(self):
        refresh_button = self.driver.find_element(By.XPATH, '//img[@id="buttonReload"]')
        refresh_button.click()
        time.sleep(9)
        email = self.driver.find_element(By.XPATH, '//a[@id="email"]')

        return email.text

    def send_email(self, email_addresss):
        text = random.choice(self.config['messages'])
        subject = random.choice(self.config['subjects'])

        msg = MIMEMultipart()
        msg['From'] = self.config['sender']
        msg['To'] = email_addresss
        msg['Subject'] = subject
        message = text
        msg.attach(MIMEText(message))

        try:
            self.smtpObj.sendmail(self.config['sender'], [email_addresss], msg.as_string())
            logger.info("Successfully sent email")
        except smtplib.SMTPException:
            logger.error("Error: unable to send email")

    def run_loop(self):
        while True:
            try:
                email = self.get_email()
            except Exception as e:
                logger.error(e)
                logger.error("Error retrieving phone number, ending process")
                sys.exit()
            self.send_email(email)

if __name__ == '__main__':
    prop = Propaemail()
    prop.run_loop()
