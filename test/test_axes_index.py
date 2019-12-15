from   ddt import ddt, data
from   test_sequencer.axes_iterator.index import Index
import unittest

@ddt
class TestAxesIndex(unittest.TestCase):
    @data({'axis_lengths': [],     'index_count': 0},
          {'axis_lengths': [1],    'index_count': 1},
          {'axis_lengths': [1, 1], 'index_count': 1},
          {'axis_lengths': [2, 2], 'index_count': 4},
          {'axis_lengths': [1, 2], 'index_count': 2},
          {'axis_lengths': [9, 9], 'index_count': 81})
    def test_increment_count(self, data):
        axis_lengths = data['axis_lengths']
        index_count  = data['index_count']

        increments = 0
        index      = Index(axis_lengths)
        while not index.is_last and increments < 1000:
            index.increment()
            increments += 1
        if increments == 0 and index.is_empty:
            self.assertEqual(increments, index_count)
        else:
            self.assertEqual(increments, index_count - 1)

    @data({'axis_lengths': [],     'indexes': []},
          {'axis_lengths': [1],    'indexes': [[0]]},
          {'axis_lengths': [1, 1], 'indexes': [[0,0]]},
          {'axis_lengths': [2, 2], 'indexes': [[0,0], [0,1], [1,0], [1,1]]},
          {'axis_lengths': [1, 2], 'indexes': [[0,0], [0,1]]},
          {'axis_lengths': [9, 9], 'indexes': [
            [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [0,8],
            [1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8],
            [2,0], [2,1], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7], [2,8],
            [3,0], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [3,8],
            [4,0], [4,1], [4,2], [4,3], [4,4], [4,5], [4,6], [4,7], [4,8],
            [5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8],
            [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7], [6,8],
            [7,0], [7,1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7], [7,8],
            [8,0], [8,1], [8,2], [8,3], [8,4], [8,5], [8,6], [8,7], [8,8],
          ]})
    def test_index_sequence(self, data):
        axis_lengths = data['axis_lengths']
        indexes      = data['indexes']
        self.assertEqual(indexes, Index(axis_lengths).to_list())
