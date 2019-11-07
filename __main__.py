from random         import random
from test_sequencer import TestSequencer
from time           import sleep

# aclr
aclr_axes = {
    'waveform': ['4g', '5g', '6g', 'all-the-gs'],
    'freq':  [1, 2, 3],
    'power': [4, 5, 6]
}
def aclr(waveform, freq, power):
    print(f'aclr called with ({waveform}, {freq}, {power})')
    sleep(random())
    return {'aclr': random()}

# ac power compatibility test
ac_power_axes = {
    'volts_rms': [100, 110, 120, 127, 220, 240],
    'freq_Hz':   [50, 60]
}
def ac_power(volts_rms, freq_Hz):
    print(f'ac_power called with {volts_rms} V / {freq_Hz} Hz AC')
    sleep(random())
    return {'ac_power': random() > 0.8}

# sequence tests
sequencer = TestSequencer()
sequencer.add_test('aclr',     aclr,     **aclr_axes)
sequencer.add_test('ac_power', ac_power, **ac_power_axes)
sequencer.run()
