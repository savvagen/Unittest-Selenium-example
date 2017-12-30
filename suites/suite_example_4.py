import unittest
from tests.test_example_1 import ExampleTests1
from tests.test_example_2 import ExampleTests2
from listeners.test_listener_example import TestListener



def suite():
    suite = unittest.TestSuite()
    suite.addTest(ExampleTests1('test_1_passing'))
    suite.addTest(ExampleTests2('test_1_passing'))
    suite.addTest(ExampleTests2('test_2_passing'))
    return suite

unittest.TextTestRunner(resultclass=TestListener, verbosity=2).run(suite())