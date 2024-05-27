import data
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestingRegistration:
    def test_registration(self, webdriver_chrome):

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди слово "Зарегистрироваться" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.WORD_REGISTRATION).click()

        # Найди поле "Имя" и заполни его
        webdriver_chrome.find_element(*TestLocators.NAME).send_keys(data.username)

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login_random)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Зарегистрироваться" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_ENTER)))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/login'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_error(self, webdriver_chrome):

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди слово "Зарегистрироваться" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.WORD_REGISTRATION).click()

        # Найди поле "Имя" и заполни его
        webdriver_chrome.find_element(*TestLocators.NAME).send_keys(data.username)

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его некорректными данными
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.wrong_password)

        # Найди кнопку "Зарегистрироваться" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        # Проверить ошибку для некорректного пароля
        assert webdriver_chrome.find_element(*TestLocators.TEXT_INVALID_PASSWORD).text == 'Некорректный пароль'