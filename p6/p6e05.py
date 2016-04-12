class Set:
    def __init__(self, val = []):
        self.data = []
        self.concat(list(val))

    def intersect(self, other):
        res = []
        for i in self.data:
            if i in other: res.append(i)
        return res

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return res

    def concat(self, val):
        for x in val:
            if not x in self.data: self.data.append(x)

    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __and__(self, other):
        return self.intersect(other)
    def __or__(self, other):
        return self.union(other)
    def __repr__(self):
        return 'Set: ' + repr(self.data)
    def __iter__(self):
        return iter(self.data)

class SetSub(Set):
    def __init__(self, *args):
        self.data = []
        for i in args:
            self.concat(list(i))
    def union(self, other):
        return Set(Set.union(self, other))
    def intersect(self, other):
        return Set(Set.intersect(self, other))
    def __and__(self, other):
        return self.intersect(other)
    def __rand__(self, other):
        return self.intersect(other)
    def __or__(self,other):
        return self.union(other)
    def __ror__(self,other):
        return self.union(other)
    
