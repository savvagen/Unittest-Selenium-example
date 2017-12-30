import unittest
from tests.test_example_1 import ExampleTests1
from tests.test_example_2 import ExampleTests2




# get all ui_tests from SearchProductTest and HomePageTest class
suite_1 = unittest.TestLoader().loadTestsFromTestCase(ExampleTests1)
suite_2 = unittest.TestLoader().loadTestsFromTestCase(ExampleTests2)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([suite_1, suite_2])
# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)