from   ddt import ddt, data
from   test_sequencer.axes_iterator.index import Index
import unittest

@ddt
class TestAxesIndex(unittest.TestCase):
    @data({'axis_lengths': [], 'index_count': 0})
    def test_increment_count(self):
        axis_lengths = [5, 10]
        index_count  = 5 * 10
        increments   = 0
        index        = Index(axis_lengths)
        while not index.is_last and increments < 1000:
            index.increment()
            increments += 1
        self.assertEqual(increments, index_count - 1)
