import logging
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_HELLO_LOGIN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.ID, 'create-btn')
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST_ADDED = (By.CSS_SELECTOR, 'h1')


class OperationsHelper(BasePage):
    with open('testdata.yaml') as f:
        info = yaml.safe_load(f)

    def enter_bad_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['x_selector1'])
        if input1:
            input1.send_keys(self.info['bad_login'])
        else:
            logging.error('The login field was not found')

    def enter_bad_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['x_selector2'])
        if input2:
            input2.send_keys(self.info['bad_login'])
        else:
            logging.error('The password field was not found')

    def enter_good_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['x_selector1'])
        if input1:
            input1.send_keys(self.info['username'])
        else:
            logging.error('The login field was not found')

    def enter_good_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['x_selector2'])
        if input2:
            input2.send_keys(self.info['password'])
        else:
            logging.error('The password field was not found')

    def click_login_button(self):
        logging.debug('Click login button ')
        btn = self.find_element(self.ids['btn_selector'])
        if btn:
            btn.click()
        else:
            logging.error('Button not found')

    def get_error_text(self):
        err_label = self.find_element(self.ids['x_selector3'])
        if err_label:
            text = err_label.text
            logging.debug(f'Error {text} while loging')
            return text
        else:
            logging.error('The element with the error was not found')
            return None

    def get_hello_user(self):
        hello = self.find_element(self.ids['x_selector4'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('The user has not logged in')
            return None

    def click_contact_button(self):
        logging.debug('Click contact button ')
        cont_btn = self.find_element(self.ids['contact_btn'])
        if cont_btn:
            cont_btn.click()
        else:
            logging.error('The contact button was not found')

    def enter_name(self):
        logging.debug('Enter name ')
        name_field = self.find_element(self.ids['name_field'])
        if name_field:
            name_field.send_keys(self.info['name'])
        else:
            logging.error('The field for entering the name was not found')

    def enter_email(self):
        logging.debug('Enter email ')
        email_field = self.find_element(self.ids['email_field'])
        if email_field:
            email_field.send_keys(self.info['email'])
        else:
            logging.error('The field for entering the email was not found')

    def enter_content(self):
        logging.debug('Enter content ')
        content_field = self.find_element(self.ids['content_field'])
        if content_field:
            content_field.send_keys(self.info['content'])
        else:
            logging.error('The content input field was not found')

    def click_contact_us_button(self):
        logging.debug('Click contact us button ')
        cont_us_btn = self.find_element(self.ids['contact_us_btn'])
        if cont_us_btn:
            cont_us_btn.click()
        else:
            logging.error('The contact us button was not found')

    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text