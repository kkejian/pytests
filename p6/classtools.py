# classtools.py written for chapter 28 of lp5e
"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provides an inheritable diplay overload method that shows instances with
    their class names an a name=value pair for each attribute stored on the
    instance itself (but nor attrs inherited from its classes). Can be mixed
    into any class and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self,key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
