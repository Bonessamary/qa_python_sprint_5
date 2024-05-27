import data
import pytest
from selenium import webdriver

#Возвращает webdriver
@pytest.fixture()
def webdriver_chrome():
    webdriver_chrome = webdriver.Chrome()
    webdriver_chrome.get(data.website)
    yield webdriver_chrome
    webdriver_chrome.quit()