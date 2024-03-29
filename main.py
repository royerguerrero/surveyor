import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Surveyor:
    def __init__(self, email, password):
        print('[!] Starting execution...')
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.user_credentials = {'email': email, 'password': password}
        self.count_surveys = 0

        self.driver.get('http://34.228.175.56:8000/accounts/login/?next=/')

    def login(self):
        driver = self.driver
        email_field = driver.find_element_by_name('username')
        password_field = driver.find_element_by_name('password')
        if not self.user_credentials['email'] or not self.user_credentials['password']:
            print('[!] Please provide a credential using ENV variables')
            sys.exit(0)
            self.__del__()

        email_field.send_keys(self.user_credentials['email'])
        password_field.send_keys(self.user_credentials['password'])

        submit_btn = driver.find_element_by_xpath('//*[@id="login"]/button')
        submit_btn.click()

    def answering_surveys(self):
        driver = self.driver
        surveys = self.get_surveys()

        surveys[0].click()

        terms_and_conditions = driver.find_element_by_xpath(
            '//*[@id="terminos"]')
        terms_and_conditions.click()

        options = driver.find_elements_by_class_name('radio__survey')
        for option in options:
            value = option.get_attribute('value')
            if value == 'no':
                option.click()

        submit_survey_btn = driver.find_element_by_class_name('button__survey')
        submit_survey_btn.click()

        wait = WebDriverWait(driver, 10)
        confirm_btn = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'swal-button-container')))
        confirm_btn.click()
        self.answering_surveys()

    def get_surveys(self):
        driver = self.driver
        surveys_elements = driver.find_elements_by_class_name('card')

        if not surveys_elements:
            if self.count_surveys > 0:
                print('[!] You do not more surveys.')
            else:
                print('[!] You do not have any survey.')
            sys.exit(0)
            self.__del__()
        else:
            print('[!] Answer new survey')
            self.count_surveys += 1
            return surveys_elements

    def __del__(self):
        self.driver.close()
        print(f'[!] Completed execution, number of answered surveys: {self.count_surveys}')


if __name__ == "__main__":
    print("""
   _____
  / ___/__  ________   _____  __  ______  _____
  \__ \/ / / / ___/ | / / _ \/ / / / __ \/ ___/
 ___/ / /_/ / /   | |/ /  __/ /_/ / /_/ / /
/____/\__,_/_/    |___/\___/\__, /\____/_/
                           /____/
        by @royerguerrero (github)
    """)
    surveyor = Surveyor(email=os.environ.get('USER_MAIL'),
                        password=os.environ.get('USER_PWD'))
    surveyor.login()
    surveyor.answering_surveys()
