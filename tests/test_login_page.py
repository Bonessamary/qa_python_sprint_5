import data
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestingLoginPage:
    # вход по кнопке "Войти в аккаунт" на главной
    def test_login_page_log_account(self, webdriver_chrome):
        webdriver_chrome.get(data.website)

        # Найди кнопку "Войти в аккаунт" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_LOG_ACCOUNT).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(
            expected_conditions.presence_of_element_located((TestLocators.BUTTON_ORDER)))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/'

        webdriver_chrome.quit()

    # вход через кнопку "личный кабинет"
    def test_login_page_profile(self, webdriver_chrome):
        webdriver_chrome.get(data.website)

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

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/'

        webdriver_chrome.quit()

# вход через кнопку в форме регистрации
    def test_login_page_registration(self, webdriver_chrome):
        webdriver_chrome.get(data.website)

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди слово "Зарегистрироваться" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.WORD_REGISTRATION).click()

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER_LOG).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.presence_of_element_located((TestLocators.BUTTON_ORDER)))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/'

        webdriver_chrome.quit()

    # вход через кнопку в форме восстановления пароля
    def test_login_page_forgot_password(self, webdriver_chrome):
        webdriver_chrome.get(data.website)

        # Найди кнопку "Личный кабинет" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        # Найди слово "Восстановить пароль" и кликни по нему
        webdriver_chrome.find_element(*TestLocators.BUTTON_FORGOT_PASSWORD).click()

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER_LOG).click()

        # Найди поле "Email" и заполни его
        webdriver_chrome.find_element(*TestLocators.EMAIL).send_keys(data.login)

        # Найди поле "Пароль" и заполни его
        webdriver_chrome.find_element(*TestLocators.PASSWORD).send_keys(data.password)

        # Найди кнопку "Войти" и кликни по ней
        webdriver_chrome.find_element(*TestLocators.BUTTON_ENTER).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(webdriver_chrome, 5).until(expected_conditions.presence_of_element_located((TestLocators.BUTTON_ORDER)))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/'
        assert webdriver_chrome.current_url == 'https://stellarburgers.nomoreparties.site/'

        webdriver_chrome.quit()