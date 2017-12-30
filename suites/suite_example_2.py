import unittest
from tests.test_example_1 import ExampleTests1
from tests.test_example_2 import ExampleTests2
from listeners.test_listener_custom import TestListener2


test_loader = unittest.TestLoader()
test_results = TestListener2()
# get all ui_tests from SearchProductTest and HomePageTest class

suite_1 = test_loader.loadTestsFromTestCase(ExampleTests1)
suite_2 = test_loader.loadTestsFromTestCase(ExampleTests2)
# create a test suite combining search_test and home_page_test
suite = unittest.TestSuite([suite_1, suite_2])
suite.run(test_results)
