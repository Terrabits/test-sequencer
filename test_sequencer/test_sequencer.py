from .test import Test

class TestSequencer:
    def __init__(self):
        self.tests = []
    def add_test(self, name, fn, **axes):
        self.tests.append(Test(name, fn, **axes))
    def run(self):
        for test in self.tests:
            test.run().write_csv(f'{test.name}.csv')
