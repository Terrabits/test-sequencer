from functools import wraps

def set_on_change_only(get_fn):
    def decorator(set_fn):
        @wraps(set_fn)
        def set_on_change_only(self, value):
            if value == get_fn(self):
                return
            set_fn(self, value)
        return set_on_change_only
    return decorator

# Example:
# class Instrument:
#     def __init__(self):
#         self._freq_Hz = None
#
#     # freq_Hz
#     #   note: `set_freq_Hz` only gets called
#     #   if freq is being changed!
#     @property
#     def freq_Hz(self):
#         return self._freq_Hz
#     @freq_Hz.setter
#     @set_on_change_only(freq_Hz.__get__)
#     def freq_Hz(self, value):
#         print(f'Setting freq to {value} Hz')
#         self._freq_Hz = value
