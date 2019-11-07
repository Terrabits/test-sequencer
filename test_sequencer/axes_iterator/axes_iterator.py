from .index import Index
from .point import Point

class AxesIterator:
    def __init__(self, **axes):
        self.axes = axes

    @property
    def is_empty(self):
        return not bool(self.axes)

    @property
    def axes_count(self):
        return len(self.axes)

    @property
    def axis_lengths(self):
        return [len(values) for values in self.axes_values]

    @property
    def axis_names(self):
        return list(self.axes.keys())

    @property
    def axes_values(self):
        return list(self.axes.values())

    def point_at(self, index):
        index_values = index.index_values if type(index) == Index else list(index)
        point_values = [self.axes_values[pos][i] for pos, i in enumerate(index_values)]
        value_dict   = dict(zip(self.axis_names, point_values))
        return Point(**value_dict)

    def __iter__(self):
        index = Index(self.axis_lengths)
        def generator():
            if self.is_empty:
                return
            while not index.is_last:
                yield self.point_at(index)
                index.increment()
            yield self.point_at(index)
        return generator()
