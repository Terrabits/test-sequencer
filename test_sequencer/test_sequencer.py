from .test   import Test
from pathlib import Path

class TestSequencer:
    def __init__(self, output_path='.'):
        self.tests  = []
        self.output_path = Path(output_path)
    def add_test(self, name, fn, axes={}):
        self.tests.append(Test(name, fn, axes))
    def run(self):
        # mkdir -p output path
        self.output_path.mkdir(parents=True, exist_ok=True)

        # begin tests
        print('PHASE: BEGIN_TESTS')
        for test in self.tests:
            test.execute_phase('begin_tests')

        # test
        print('PHASE: TEST')
        for test in self.tests:
            filename = str(self.output_path / f'{test.name}.csv')
            results  = test.execute_test()
            if not results.is_empty:
                results.write_csv(filename)

        # end tests
        print('PHASE: END_TESTS')
        for test in self.tests:
            test.execute_phase('end_tests')
