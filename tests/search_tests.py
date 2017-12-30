#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from entity.test_base import TestBase
from entity.pages.search_page import SearchPage


class SearchTests(TestBase):

    def test_search(self):
        search_results = SearchPage(self.driver).open().search("Selenium")
        self.assertEqual(10, len(search_results._results()))
        self.assertIn("Selenium", search_results._get_result_title(1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
