class MyList:
    def __init__(self, init_val=[]):
        self.data = list(init_val)

    def __getitem__(self, index):
        #print('MyList.__getitem__ called')
        return self.data[index]

    def __setitem__(self, index, obj):
        #print('MyList__setitem__ called')
        self.data[index] = obj

    def __add__(self, x):
        #print('MyList.__add__ called')
        return MyList(self.data + x)

    def __radd__(self, x):
        #print('MyList.__radd__ called')
        return MyList(x + self.data)

    def __iter__(self):
        #print('MyList.__iter__ called')
        for i in range(0, len(self.data)):
            yield self.data[i]

    def __repr__(self):
        #print('MyList.__repr__ called')
        return '[' + ', '.join([str(x) for x in self]) + ']' 

    def append(self, obj):
        #print('MyList.append called')
        self.data = self.data + [obj]

    def extend(self, iterable):
        #print('MyList.extend called')
        for i in iterable: self.append(i)

class MyListExt(MyList):
    glb_ctr = 0
    def __init__(self,init_val=[]):
        self.ctr = 0
        glb_ctr = 0
        MyList.__init__(self, init_val)

    def __add__(self, x):
        print('MyListExt.__add__ called')
        self.ctr += 1
        MyListExt.glb_ctr += 1
        return MyList.__add__(self, x)

    def get_ctr(self): return self.ctr
    def get_glb_ctr(self): return MyListExt.glb_ctr
