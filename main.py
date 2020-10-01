import unittest, os
from selenium import webdriver

class Surveyor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get('http://3.86.213.150:8000/accounts/login/')

    def test_answer_all_surveys(self):
        driver = self.driver
        email = os.environ.get('USER_MAIL')
        password = os.environ.get('USER_PWD')
        email_input = driver.find_element_by_name('username')
        password_input = driver.find_element_by_name('password')
        login_button = driver.find_element_by_xpath('//*[@id="login"]/button')

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        surveys = driver.find_elements_by_class_name('card')
        counter = 0

        while counter != len(surveys):
            survey = driver.find_element_by_class_name('button__surveyall')
            survey.click()

            terms = driver.find_element_by_class_name('radio__survey')
            terms.click()

            questions = driver.find_elements_by_class_name('input__survey')
            for question in questions:
                options = question.find_elements_by_class_name('radio__survey')
                options[1].click()

            send_survey = driver.find_element_by_class_name('button__survey')
            send_survey.click()

            confirm_btn = driver.find_element_by_class_name('swal-button--confirm')
            confirm_btn.click()

            counter += 1

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
