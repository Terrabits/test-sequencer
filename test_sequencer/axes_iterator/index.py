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
    def is_empty(self):
        return self.axis_count == 0

    @property
    def is_last(self):
        return self == self.last

    def increment(self):
        if self.is_empty or self.is_last:
            return

        # copy the current index values
        index_values = self.index_values.copy()

        # seed carry with our increment
        carry =  1

        # For each position,
        # starting with least significant bit (LSB)...
        for pos in range(-1, -self.axis_count - 1, -1):
            # break if no carry
            # (nothing to do)
            if not carry:
                break

            # get current value and add carry
            index_value  = index_values[pos]
            index_value += carry

            # calculate the remainder
            axis_length       = self.axis_lengths[pos]
            index_values[pos] = index_value  % axis_length

            # calculate carry to next position
            carry             = index_value // axis_length

        # set new index values
        self.index_values = index_values

    def to_list(self):
        if self.is_empty:
            return []

        # take the first point
        points = []
        index  = Index(self.axis_lengths)
        points.append(index.index_values)

        # take each additional point
        while not index.is_last:
            index.increment()
            points.append(index.index_values)

        return points
