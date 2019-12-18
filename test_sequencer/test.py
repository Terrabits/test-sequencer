from .axes_iterator import AxesIterator
from .helpers       import has_begin_tests, has_end_tests, has_test, is_constant
from .results       import Results

class Test:
    def __init__(self, name, test_obj, axes):
        self.name     = name
        self.test_obj = test_obj
        self.axes     = axes

    @property
    def constant_inputs(self):
        constant_inputs = dict()
        for axis, value in self.axes.items():
            if is_constant(value):
                constant_inputs[axis] = value
        return constant_inputs

    def execute_phase(self, phase):
        phase = phase.strip().lower()
        if phase == 'begin_tests' and has_begin_tests(self.test_obj):
            self.test_obj.begin_tests(self.constant_inputs)
        elif phase == 'end_tests' and has_end_tests(self.test_obj):
            self.test_obj.end_tests  (self.constant_inputs)
        elif phase == 'test':
            return self.execute_test()

    def execute_test(self):
        # handle test_obj.
        # It could be a Test instance or a function
        test_fn = None
        if callable(self.test_obj):
            test_fn = self.test_obj
        elif has_test(self.test_obj):
            test_fn = self.test_obj.test
        if not test_fn:
            return Results()

        results_dicts = []
        for point in AxesIterator(self.axes):
            results_dict = point.copy()
            data_dict    = test_fn(point)
            results_dict.update(data_dict)
            results_dicts.append(results_dict)
        return Results(results_dicts)
