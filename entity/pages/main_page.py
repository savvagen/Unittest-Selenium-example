from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from entity.test_base import base_url
from selenium.webdriver.common.action_chains import ActionChains

account_button = "div[class='h-right__item-c h-right__item-c-js'] a"
login_button = ".h-right__item-c a"
logout_button = "a[href='/auth/logout']"


class MainPage(object):
    def __init__(self, driver):
        self.url = base_url() + "/"
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.title = "GEPUR: Женская одежда оптом и в розницу от производителя"


    def _account_button(self):
        return self.driver.find_element_by_css_selector(account_button)

    def _logout_button(self):
        return self.driver.find_element_by_css_selector(logout_button)

    def _login_button(self):
        return self.driver.find_element_by_css_selector(login_button)

    def open(self):
        self.driver.get(self.url)
        self.wait.until(expected_conditions.title_contains(self.title))
        return self

    def logout(self):
        ActionChains(self.driver).move_to_element(self._account_button()).perform()
        self._logout_button().click()
        self.wait.until(expected_conditions.visibility_of(self._login_button()))
        return self
