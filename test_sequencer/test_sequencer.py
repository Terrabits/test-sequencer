from .test import Test

class TestSequencer:
    def __init__(self):
        self.tests = []
    def add_test(self, name, fn, axes={}):
        self.tests.append(Test(name, fn, axes))
    def run(self):
        # begin tests
        for test in self.tests:
            test.execute_phase('begin_tests')
        # test
        for test in self.tests:
            filename = f'{test.name}.csv'
            test.execute_test().write_csv(filename)
        # end tests
        for test in self.tests:
            test.execute_phase('end_tests')
