#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ddt import ddt, data, unpack
from entity.pages.login_page import LoginPage
from entity.pages.main_page import MainPage
from entity.test_base import TestBase
from entity.users.user import User
from tests.test_data.login_controller import *
import allure
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from listeners.event_listener_example import EventListener

cwd = os.path.dirname(os.path.realpath(__file__))


# cwd = os.getcwd()


@ddt
class LoginTests(TestBase):

    def setUp(self):
        LoginPage(self.driver).open()

    def tearDown(self):
        MainPage(self.driver).logout()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_login(self):
        user = User('genchevskiy', 'gepur.retail.buyer')
        main_page = LoginPage(self.driver).login_as(user)
        self.assertTrue(main_page._account_button().is_displayed())
        self.assertEqual(self.driver.current_url, main_page.url)
        self.assertEqual(main_page._account_button().text, "Buyer")

    # @data(*get_csv_data("{}/test_data/login_data.csv".format(cwd)))
    # @unpack
    # def test_02_invalid_login(self, email, password, message):
    #     login_page = LoginPage(self.driver).invalid_login(email, password)
    #     self.assertTrue(login_page._error_message().is_displayed())
    #     self.assertEqual(login_page._error_message().text, message)


if __name__ == '__main__':
    unittest.main(verbosity=2)
