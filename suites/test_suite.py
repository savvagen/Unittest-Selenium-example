import unittest
from listeners.test_listener_custom import TestListener2
from tests.search_tests import SearchTests
from tests.login_tests import LoginTests
import os
import HTML_Test_Runner

test_loader = unittest.TestLoader()
test_results = TestListener2()
# get all ui_tests from SearchProductTest and HomePageTest class

login_suite = test_loader.loadTestsFromTestCase(LoginTests)
search_suite = test_loader.loadTestsFromTestCase(SearchTests)
# create a test suite combining search_test and home_page_test
suite = unittest.TestSuite([login_suite])
unittest.TextTestRunner(verbosity=2, resultclass=TestListener2).run(suite)

#HTML REPORT GENERATION
#dir = os.getcwd()
# open the report file
#outfile = open(dir + "\TestReport.html", "w")
# configure HTMLTestRunner options
#runner = HTML_Test_Runner.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Tests', verbosity=2)
#runner.run(suite)