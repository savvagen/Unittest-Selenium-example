from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from entity.users.user import User
from entity.test_base import base_url
from selenium.webdriver.common.action_chains import ActionChains




search_field = "q"
search_results = ".srg .g"
search_result_link = "h3 a"


class SearchPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://google.com"

    def open(self):
        self.driver.get(self.url)
        return self

    def _search_field(self):
        return self.driver.find_element_by_name(search_field)

    def search(self, text):
        self._search_field().send_keys(text, Keys.ENTER)
        return SearchResults(self.driver)


class SearchResults(object):
    def __init__(self, driver):
        self.driver = driver

    def _results(self):
        return self.driver.find_elements_by_css_selector(search_results)

    def _get_result_title(self, number):
        results = self._results()[number - 1]
        return results.find_element_by_css_selector(search_result_link).text
        # for result in results:
        #     return result.find_element_by_css_selector(search_result_link).text