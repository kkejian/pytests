class Adder:
    def __init__(self, start=[]):
        self.data = start
    def __add__(self, y):
        return self.add(self.data, y)
    def add(self, x, y):
        print('not implemented')

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        new_dict = {}
        for k in x.keys(): new_dict[k] = x[k]
        for k in y.keys(): new_dict[k] = y[k]
        return new_dict
