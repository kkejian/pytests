from testmixin import tester

from listinstance  import ListInstance
from listinherited import ListInherited
from listtree      import ListTree

class SuperLister:
    def __attrnames(self): print('To Be implemented')
    def __str__(self):
        return '<Instance of %s(%s), address %s:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           self.__class__.__bases__,        # Names of superclasses
                           id(self),                        # My address
                           self.attrnames())              # name=value list

class SLInstance(SuperLister,ListInstance):
    def attrnames(self):
        return ListInstance.__attrnames(self)
    def __str__(self):
        return SuperLister.__str__(self)

class SLInherited(ListInherited, SuperLister):
    def attrnames(self):
        return ListInherited.__attrnames(self)
    def __str__(self):
        return SuperLister.__str__(self)

class SLTree(ListTree, SuperLister):
    def __attrnames(self):
        return ListTree.__attrnames(self)
    def __str__(self):
        return SuperLister.__str__(self)

tester(SLInstance)
tester(SLInherited)
tester(SLTree)
