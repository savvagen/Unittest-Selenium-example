import unittest
import unittest.result as result


class TestListener(result.TestResult):
    separator1 = '=' * 70
    separator2 = '-' * 70

    def __init__(self, stream, descriptions, verbosity):
        super(TestListener, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def startTestRun(self):
        super(TestListener, self).startTestRun()
        self.stream.writeln(self.separator2)
        self.stream.writeln(" Starting Test Run!!!")
        self.stream.writeln(self.separator1)

    def startTest(self, test):
        super(TestListener, self).startTest(test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" ... ")
            self.stream.flush()

    def stopTest(self, test):
        super(TestListener, self).startTest(test)
        pass

    def addSuccess(self, test):
        super(TestListener, self).addSuccess(test)
        if self.showAll:
            self.stream.writeln("ok")
        elif self.dots:
            self.stream.write('.')
            self.stream.flush()

    def addError(self, test, err):
        super(TestListener, self).addError(test, err)
        if self.showAll:
            self.stream.writeln("ERROR")
        elif self.dots:
            self.stream.write('E')
            self.stream.flush()

    def addFailure(self, test, err):
        super(TestListener, self).addFailure(test, err)
        if self.showAll:
            self.stream.writeln("FAIL")
        elif self.dots:
            self.stream.write('F')
            self.stream.flush()

    def addSkip(self, test, reason):
        super(TestListener, self).addSkip(test, reason)
        if self.showAll:
            self.stream.writeln("skipped {0!r}".format(reason))
        elif self.dots:
            self.stream.write("s")
            self.stream.flush()

    def addExpectedFailure(self, test, err):
        super(TestListener, self).addExpectedFailure(test, err)
        if self.showAll:
            self.stream.writeln("expected failure")
        elif self.dots:
            self.stream.write("x")
            self.stream.flush()

    def addUnexpectedSuccess(self, test):
        super(TestListener, self).addUnexpectedSuccess(test)
        if self.showAll:
            self.stream.writeln("unexpected success")
        elif self.dots:
            self.stream.write("u")
            self.stream.flush()

    def printErrors(self):
        super(TestListener, self).printErrors()
        if self.dots or self.showAll:
            self.stream.writeln()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def stopTestRun(self):
        super(TestListener, self).stopTestRun()
        self.stream.writeln(self.separator1)
        self.stream.writeln("Finishing Test Run with results: ")
        self.stream.writeln(self.separator2)
        self.stream.writeln("Passed tests: {}".format(self.testsRun - len(self.failures)))
        self.stream.writeln("Failed tests: {}".format(len(self.failures)))
        self.stream.writeln("Skipped tests: {}".format(len(self.skipped)))


    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln("%s: %s" % (flavour, self.getDescription(test)))
            self.stream.writeln(self.separator2)
            self.stream.writeln("%s" % err)

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return str(test)

# class _WritelnDecorator(object):
#     """Used to decorate file-like objects with a handy 'writeln' method"""
#
#     def __init__(self, stream):
#         self.stream = stream
#
#     def __getattr__(self, attr):
#         if attr in ('stream', '__getstate__'):
#             raise AttributeError(attr)
#         return getattr(self.stream, attr)
#
#     def writeln(self, arg=None):
#         if arg:
#             self.write(arg)
#         self.write('\n')  # text-mode streams translate to \r\n if needed
#
#
# class TestListener(result.TestResult):
#     separator1 = '=' * 70
#     separator2 = '-' * 70
#
#     def __init__(self, stream, descriptions, verbosity):
#         super(TestListener, self).__init__(stream, descriptions, verbosity)
#         self.stream = stream
#         self.showAll = verbosity > 1
#         self.dots = verbosity == 1
#         self.descriptions = descriptions
#
#     def startTest(self, test):
#         super(TestListener, self).startTest(test)
#         if self.showAll:
#             self.stream.write(self.getDescription(test))
#             self.stream.write(" ... ")
#             self.stream.flush()
#             print(self.getDescription(test))
#             print(" ... ")
#
#     def addSuccess(self, test):
#         super(TestListener, self).addSuccess(test)
#         if self.showAll:
#             self.stream.writeln("ok")
#             print("ok")
#         elif self.dots:
#             self.stream.write('.')
#             self.stream.flush()
#             print(".")
#
#     def addError(self, test, err):
#         super(TestListener, self).addError(test, err)
#         if self.showAll:
#             self.stream.writeln("ERROR")
#             print("ERROR")
#         elif self.dots:
#             self.stream.write('E')
#             self.stream.flush()
#             print("E")
#
#     def addFailure(self, test, err):
#         super(TestListener, self).addFailure(test, err)
#         if self.showAll:
#             self.stream.writeln("FAIL")
#             print("FAIL")
#         elif self.dots:
#             self.stream.write('F')
#             self.stream.flush()
#             print("F")
#
#     def addSkip(self, test, reason):
#         super(TestListener, self).addSkip(test, reason)
#         if self.showAll:
#             self.stream.writeln("skipped {0!r}".format(reason))
#             print("skipped {0!r}".format(reason))
#         elif self.dots:
#             self.stream.write("s")
#             self.stream.flush()
#             print("s")
#
#     def addExpectedFailure(self, test, err):
#         super(TestListener, self).addExpectedFailure(test, err)
#         if self.showAll:
#             self.stream.writeln("expected failure")
#             print("expected failure")
#         elif self.dots:
#             self.stream.write("x")
#             self.stream.flush()
#             print("x")
#
#     def addUnexpectedSuccess(self, test):
#         super(TestListener, self).addUnexpectedSuccess(test)
#         if self.showAll:
#             self.stream.writeln("unexpected success")
#         elif self.dots:
#             self.stream.write("u")
#             self.stream.flush()
#
#     def printErrors(self):
#         super(TestListener, self).printErrors()
#         if self.dots or self.showAll:
#             self.stream.writeln()
#         self.printErrorList('ERROR', self.errors)
#         self.printErrorList('FAIL', self.failures)
#         self.showErrorList('ERROR', self.errors)
#         self.showErrorList('FAIL', self.failures)
#
#     def stopTestRun(self):
#         super(TestListener, self).stopTestRun()
#         print(self.separator1)
#         print(self.separator1)
#         print("Passed tests: {}".format(self.testsRun - len(self.failures)))
#         print("Failed tests: {}".format(len(self.failures)))
#         print("Skipped tests: {}".format(len(self.skipped)))
#         print(self.separator1)
#         print(self.separator1)
#
#     def printErrorList(self, flavour, errors):
#         for test, err in errors:
#             self.stream.writeln(self.separator1)
#             self.stream.writeln("%s: %s" % (flavour, self.getDescription(test)))
#             self.stream.writeln(self.separator2)
#             self.stream.writeln("%s" % err)
#
#     def showErrorList(self, flavour, errors):
#         for test, err in errors:
#             print(self.separator1)
#             print("%s: %s" % (flavour, self.getDescription(test)))
#             print(self.separator2)
#             print("%s" % err)
#
#     def getDescription(self, test):
#         doc_first_line = test.shortDescription()
#         if self.descriptions and doc_first_line:
#             return '\n'.join((str(test), doc_first_line))
#         else:
#             return str(test)
