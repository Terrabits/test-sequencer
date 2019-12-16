from   ddt import ddt, data
from   test_sequencer.axes_iterator import AxesIterator
import unittest

@ddt
class TestAxesIterator(unittest.TestCase):
    @data({'axes': {'string': 'my string'},                   'index': [0], 'point': {'string': 'my string'}},
          {'axes': {'gain':   0          },                   'index': [0], 'point': {'gain':   0          }},
          {'axes': {'waveform': {'modulation_type': '5GNR'}}, 'index': [0], 'point': {'waveform': {'modulation_type':   '5GNR'}}},
          {'axes': {'waveform': [{'modulation_type': '5GNR'}]}, 'index': [0], 'point': {'waveform': {'modulation_type':   '5GNR'}}},
          {'axes': {'waveform': [{'modulation_type': '5GNR'}, {'modulation_type': '4G'}]}, 'index': [0], 'point': {'waveform': {'modulation_type':   '5GNR'}}},
          {'axes': {'waveform': [{'modulation_type': '5GNR'}, {'modulation_type': '4G'}]}, 'index': [1], 'point': {'waveform': {'modulation_type':   '4G'}}})
    def test_increment_count(self, data):
        axes = data['axes']
        index = data['index']
        point = data['point']

        iterator = AxesIterator(axes)
        self.assertEqual(iterator.point_at(index), point)
