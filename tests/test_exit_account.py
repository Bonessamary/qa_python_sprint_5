import data
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestingExitAccount:

    def test_exit_account(self, webdriver_chrome):
        webdriver_chrome.get(data.website)

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.presence_of_element_located((TestLocators.BUTTON_EXIT)))

        # Найди кнопку "Выход" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_EXIT).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_ENTER)))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/login'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/login'

        webdriver_chrome.quit()