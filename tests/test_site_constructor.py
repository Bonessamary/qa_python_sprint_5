import data
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestingSiteConstructor:
    # Переход на соусы
    def test_constructor_sauces(self, webdriver_chrome):

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.presence_of_element_located((TestLocators.BUTTON_ORDER)))

        # Найди раздел "Соусы" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.SITE_SAUCES).click()

        # Проверь, что образились соусы
        sauces = webdriver_chrome.find_element(*TestLocators.SITE_SAUCES)
        assert 'type_current' in sauces.get_attribute('class')

    # Переход на начинки
    def test_constructor_topping(self, webdriver_chrome):

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.presence_of_element_located((TestLocators.BUTTON_ORDER)))

        # Найди раздел "Начинки" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.SITE_TOPPING).click()

        # Проверь, что образились начинки
        topping = webdriver_chrome.find_element(*TestLocators.SITE_TOPPING)
        assert 'type_current' in topping.get_attribute('class')

 # Переход на булки
    def test_constructor_buns(self, webdriver_chrome):

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.presence_of_element_located((TestLocators.BUTTON_ORDER)))

        # Найди раздел "Начинки" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.SITE_TOPPING).click()

        # Найди раздел "Булки" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.SITE_BUNS).click()

        # Проверь, что образились булки
        buns = webdriver_chrome.find_element(*TestLocators.SITE_BUNS)
        assert 'type_current' in buns.get_attribute('class')