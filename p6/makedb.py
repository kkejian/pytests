from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Adams', job='dev', pay=100000)
tom = Manager('Tom Hope', pay = 150000)
 
import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
