import pytest
from selenium import webdriver

#Возвращает webdriver
@pytest.fixture()
def webdriver_chrome():
    driver = webdriver.Chrome()
    return driver