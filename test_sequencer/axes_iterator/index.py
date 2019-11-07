class Index:
    def __init__(self, axis_lengths):
        self.axis_lengths = axis_lengths
        self.index_values = self.first

    @property
    def axis_count(self):
        return len(self.axis_lengths)

    @property
    def first(self):
        return self.axis_count * [0]

    @property
    def last(self):
        return [i-1 for i in self.axis_lengths]

    def __eq__(self, other):
        other_values = other.index_values if type(other) == Index else list(other)
        return self.index_values == other_values

    @property
    def is_last(self):
        return self == self.last

    def increment(self):
        pos   = 0
        carry = 1
        while carry and pos < self.axis_count:
            axis_length             = self.axis_lengths[pos]
            self.index_values[pos] += carry
            carry                   = self.index_values[pos] // axis_length
            self.index_values[pos]  = self.index_values[pos]  % self.axis_lengths[pos]
            pos += 1
