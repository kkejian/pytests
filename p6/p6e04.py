class Attr:
    def __getattr__(self, name):
        print('called __getattr__')
        if name in self.__dict__.keys(): return self.__dict__[name]
        else: raise AttributeError(name)

    def __setattr__(self, name, value):
        print('called __setattr__')
        self.__dict__[name] = value
