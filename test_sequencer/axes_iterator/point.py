class Point:
    def __init__(self, **value_dict):
        self.value_dict = value_dict

    @property
    def parameters(self):
        return list(self.value_dict.keys())

    @property
    def values(self):
        return list(self.value_dict.values())
