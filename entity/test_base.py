from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from listeners.event_listener_example import EventListener


def base_url():
    return "https://gepur.com"


class TestBase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver = EventFiringWebDriver(cls.d, EventListener())
        cls.driver.implicitly_wait(10)
        cls.driver.wrapped_driver.maximize_window()
        cls.driver.get(base_url())
        cls.driver.wrapped_driver.add_cookie({
            'domain': 'gepur.com',  # note the dot at the beginning
            'name': 'subscribe_popup',
            'value': 'true',
            'path': '/',
            'expires': None
        })
        cls.driver.wrapped_driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
