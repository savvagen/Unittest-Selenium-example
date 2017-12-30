from selenium import webdriver
from selenium.webdriver.support.events import AbstractEventListener
import allure


class EventListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        print("Navigating to: {}".format(url))

    def after_navigate_to(self, url, driver):
        print("Page: {} is opened".format(url))

    def before_navigate_forward(self, driver):
        pass

    def after_navigate_forward(self, driver):
        pass

    def before_navigate_back(self, driver):
        pass

    def after_navigate_back(self, driver):
        pass

    def before_find(self, by, value, driver):
        print("Finding element By: {} , value: {}".format(by, value))

    def after_find(self, by, value, driver):
        print("Element found.")

    def before_click(self, element, driver):
        print("Clicking element.")

    def after_click(self, element, driver):
        print("Preformed click on element: {}".format(element))

    def before_change_value_of(self, element, driver):
        print("Typing value to element: ".format(element))

    def after_change_value_of(self, element, driver):
        print("Value have been set. ")

    def before_execute_script(self, script, driver):
        pass

    def after_execute_script(self, script, driver):
        pass

    def before_close(self, driver):
        print("Closing browser.")

    def after_close(self, driver):
        print("Browser is closed.")

    def before_quit(self, driver):
        print("Quit from driver")

    def after_quit(self, driver):
        pass

    def on_exception(self, exception, driver):
        print("Exception found: \n{}", format(exception))
        allure.attach(driver.get_screenshot_as_png(), "Screenshot")
