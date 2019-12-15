# to compliment `callable`:
def iterable(value):
    return hasattr(value, '__iter__')
def is_str(value):
    return type(value) == str
def is_dict(value):
    return type(value) == dict

def prefix_keys(indexable_obj, prefix, separator='.'):
    new_obj = {}
    for key in indexable_obj:
        new_key          = f'{prefix}{separator}{key}'
        new_obj[new_key] = indexable_obj[key]
    return new_obj

# value(s) that will not be swept are "constant"
def is_constant(value):
    return is_str(value) or is_dict(value) or not iterable(value)

def has_begin_tests(test_obj):
    return hasattr(test_obj, 'begin_tests')
def has_test(test_obj):
    return hasattr(test_obj, 'test')
def has_end_tests(test_obj):
    return hasattr(test_obj, 'begin_tests')
