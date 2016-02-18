# file person.py written for chapter 28 of lp5e
"""
Record and process information about people.
Rund this file directly to test its classes.
"""

from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    # @rangetest(percent=(0.0,1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        

class Manager(Person):
    """
    An example for a person with special requirements.
    Implemented via inheritance
    """
    def __init__(self, name, pay): # Modifies the constructor of the superclass 
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Adams', job='dev', pay=100000)
    print(bob)
    print(sue)
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Hope', pay = 150000)
    print(tom.lastName())
    tom.giveRaise(0.1)
    print(tom.job)
    print('---All three---')
    for i in (bob, sue, tom):
        i.giveRaise(.1)
        print(i)
