if __name__ == '__main__':
    import json
    import logging
    import sys
    import random
    import time
    import undetected_chromedriver.v2 as uc
    from selenium.webdriver.common.by import By



    with open('config.json', "r", encoding="utf-8") as config_file:
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
                url = "https://web.whatsapp.com/send?phone=" + number + "&text=" + text

                options = uc.ChromeOptions()
                options.add_argument(config['user_data_path'])
                options.add_argument('--profile-directory=Default')
                driver = uc.Chrome(options=options)
                driver.get(url)
                time.sleep(config['open_wait'] + random.randint(-2, 2))

                # attach_button = driver.find_element(By.XPATH, '//span[@data-icon="clip"]')
                # attach_button.click()
                # time.sleep(config['click_wait'])

                # image_button = driver.find_element(By.XPATH, '//span[@data-icon="attach-image"]')
                # image_button.click()
                # time.sleep(config['click_wait'])

                # image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                # image_box.send_keys(config['img_path'])
                # time.sleep(config['click_wait'])

                send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                send_button.click()
                time.sleep(config['click_wait'])

                driver.close()

                logging.info("Successful, moving on.")
            except Exception as e:
                # logging.error(e)
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


