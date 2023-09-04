import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from email_log import send_log_via_email

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_type = testdata['browser']
    log_email = testdata['log_email']
    log_pass = testdata['log_email_pass']
    log_file = testdata['log_name']
    report = testdata['report_name']


@pytest.fixture(scope='session')
def browser():
    driver = None
    if browser_type == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_type == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_type == 'edge':
        service = Service(executable_path=EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    yield driver
    send_log_via_email(log_email, log_email, log_pass, log_file, report)
    driver.quit()