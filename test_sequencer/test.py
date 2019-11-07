from .axes_iterator import AxesIterator
from .results       import Results

class Test:
    def __init__(self, name, fn, **axes):
        self.name = name
        self.fn   = fn
        self.axes = axes

    def run(self):
        results_dicts = []
        for point in AxesIterator(**self.axes):
            results_dict = point.value_dict.copy()
            data_dict    = self.fn(*point.values)
            results_dict.update(data_dict)
            results_dicts.append(results_dict)
        return Results(results_dicts)
