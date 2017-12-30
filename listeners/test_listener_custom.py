from unittest.result import TestResult


class TestListener2(TestResult):

    separator1 = '=' * 70
    separator2 = '-' * 70

    def startTestRun(self):
        super(TestListener2, self).startTestRun()
        print(self.separator2)
        print(" Starting Test Run!!!")
        print(self.separator1)

    def startTest(self, test):
        super(TestListener2, self).startTest(test)
        print(self.separator2)
        print("TEST: {} started".format(test))
        print(" ... ")
        print(self.separator2)

    def stopTest(self, test):
        super(TestListener2, self).stopTest(test)
        pass

    def addSuccess(self, test):
        super(TestListener2, self).addSuccess(test)
        print(self.separator2)
        print("PASSED")

    def addError(self, test, err):
        super(TestListener2, self).addError(test, err)
        print(self.separator1)
        print("FAILED")

    def addFailure(self, test, err):
        super(TestListener2, self).addFailure(test, err)
        print(err)
        print("FAIL")

    def addSkip(self, test, reason):
        super(TestListener2, self).addSkip(test, reason)
        print("skipped {0!r}".format(reason))

    def addExpectedFailure(self, test, err):
        super(TestListener2, self).addExpectedFailure(test, err)
        print("expected failure")

    def addUnexpectedSuccess(self, test):
        super(TestListener2, self).addUnexpectedSuccess(test)
        print("unexpected success")

    def printErrors(self):
        super(TestListener2, self).printErrors()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def stopTestRun(self):
        super(TestListener2, self).stopTestRun()
        print(self.separator1)
        print("Finishing Test Run with results: ")
        print(self.separator2)
        print("Passed tests: {}".format(self.testsRun - len(self.errors)))
        print("Failed tests: {}".format(len(self.errors)))
        print("Skipped tests: {}".format(len(self.skipped)))

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            print(self.separator1)
            print("%s: %s" % (flavour, test))
            print(self.separator2)
            print("%s" % err)
