import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Only for chrome setup
# @pytest.fixture()
# def setup():
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     yield driver
#     driver.quit()

# This is for all Browser

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        service=Service(EdgeChromiumDriverManager().install())
        driver= webdriver.Edge(service=service)
        print("Launching Edge browser.........")
    elif browser=='firefox':
        service = Service(GeckoDriverManager().install())
        driver=webdriver.Firefox(service=service)
        print("Launching firefox browser.........")
    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("Launching chrome browser.........")
    yield driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['QA'] = 'Ajit Devkar'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
