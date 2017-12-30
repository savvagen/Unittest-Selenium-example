import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from entity.users.user import User
from entity.test_base import base_url
from selenium.webdriver.common.action_chains import ActionChains
from entity.pages.main_page import MainPage

email_field = "#loginform-email"
password_field = "#loginform-password"
submit_button = "login-button"
error_message = "p[class='help-block help-block-error']"


class LoginPage(object):


    def __init__(self, driver):
        self.url = base_url() + "/auth/login"
        self.driver = driver
        self.wait = WebDriverWait(driver, 1000)
        self.title = "Введите свой логин и пароль на Gepur"

    def _email_field(self):
        return self.driver.find_element_by_css_selector(email_field)

    def _password_field(self):
        return self.driver.find_element_by_css_selector(password_field)

    def _submit_button(self):
        return self.driver.find_element_by_name(submit_button)

    def _error_message(self):
        return self.driver.find_element_by_css_selector(error_message)

    @allure.step
    def open(self):
        self.driver.get(self.url)
        self.wait.until(expected_conditions.title_is(self.title))
        return self

    @allure.step
    def login_as(self, user):
        self._email_field().send_keys(user.email)
        self._password_field().send_keys(user.password)
        self._submit_button().click()
        return MainPage(self.driver)

    @allure.step
    def invalid_login(self, login, password):
        self._email_field().send_keys(login, Keys.TAB)
        self._password_field().send_keys(password, Keys.TAB)
        self._submit_button().click()
        self.wait.until(expected_conditions.visibility_of(self._error_message()))
        return self