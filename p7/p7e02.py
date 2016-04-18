class MyError(Exception):
    pass
def oops():
    raise IndexError
def oops2():
    I = MyError()
    raise I

def oopser(func):
    try:
        func()
    except (IndexError, MyError) as var:
        print('Catched the error')
        import sys
        print(var.__class__.__name__)

if __name__ == '__main__':
    oopser(oops)
    print('finished p1')
    oopser(oops2)
    print('finished p2')
