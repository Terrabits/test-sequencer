from ..helpers import is_constant
from .index    import Index

class AxesIterator:
    def __init__(self, axes):
        self.axes = axes

    @property
    def is_empty(self):
        return not bool(self.axes)

    @property
    def axes_count(self):
        return len(self.axes)

    @property
    def axis_lengths(self):
        # TODO: handle str, other consts, iterables, indexables here
        lengths = []
        for values in self.axes_values:
            if is_constant(values):
                lengths.append(1)
            else:
                lengths.append(len(values))
        return lengths

    @property
    def axis_names(self):
        return list(self.axes.keys())

    @property
    def axes_values(self):
        return list(self.axes.values())

    def point_at(self, index):
        # TODO: handle str, other consts, iterables, indexables here
        index_values = index.index_values if type(index) == Index else index
        point_values = []
        for pos, i in enumerate(index_values):
            values = self.axes_values[pos]
            if is_constant(values):
                point_values.append(values)
            else:
                point_values.append(values[i])
        point = dict(zip(self.axis_names, point_values))
        return point

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
