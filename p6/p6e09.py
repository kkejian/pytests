class Statement:
    def __init__(self):
        self.line = ''
    def state(self):
        print('%s:\t%s' % (self.__class__.__name__, self.line))

class Parrot(Statement):
    def __init__(self):
        self.line = None
class Customer(Statement):
    def __init__(self):
        self.line = '"That\'s one ex-bird!"'
class Clerk(Statement):
    def __init__(self):
        self.line = '"No it isn\'t..."'

class Scene(Parrot,Customer,Clerk):
    def __init__(self):
        self.parrot = Parrot()
        self.customer = Customer()
        self.clerk = Clerk()
    def action(self):
        self.customer.state()
        self.clerk.state()
        self.parrot.state()

if __name__ == '__main__':
    Scene().action()



