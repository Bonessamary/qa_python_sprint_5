import data
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestingGoProfileToConstructor:
    # Переход из личного кабинета в конструктор
    def test_go_profile_to_constructor(self, webdriver_chrome):
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

        # Найди кнопку "Конструктор" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/'

        webdriver_chrome.quit()

    # Переход из личного кабинета по лого
    def test_go_profile_to_logo(self, webdriver_chrome):
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

        # Найди кнопку "Конструктор" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_LOGO).click()

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/'

        webdriver_chrome.quit()


