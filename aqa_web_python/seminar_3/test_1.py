import logging
import time
import yaml
from testpage import OperationsHelper


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

def test_hw(browser):
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('Kondrat')
    testpage.enter_pass('7901dbec72')
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(3)
    testpage.enter_name('Kondrat')
    testpage.enter_email('gdc5kyznfric@mail.ru')
    testpage.enter_content('Test content')
    time.sleep(3)
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.alert() == 'Form successfully submitted'


def test_step1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test1 failed'


def test_step2(browser):
    logging.info('Test2 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username"]}', 'test2 failed'


def test_step3(browser):
    logging.info('Test3 Starting')
    testpage = OperationsHelper(browser)
    testpage.click_create_post_btn()
    time.sleep(1)
    testpage.enter_post_title(testdata['test_title'])
    testpage.enter_post_description(testdata['test_description'])
    testpage.enter_post_content(testdata['test_content'])
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_added_post_title() == testdata['test_title'], 'test3 failed'
