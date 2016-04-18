def oops():
    raise IndexError
def oops2():
    raise TypeError

def oopser(func):
    try:
        func()
    except IndexError:
        print('Catched the error!')

if __name__ == '__main__':
    oopser(oops)
    print('finished p1')
    oopser(oops2)
    print('finished p2')
