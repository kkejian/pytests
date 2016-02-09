def facRec(n):
    if n==0: return 1
    else: return n*facRec(n-1)

def facRed(n):
    from functools import reduce
    return (reduce(lambda x,y: x*y, range(1,n+1)) if n else 1)

def facLoop(n):
    start = 1
    for i in range(1,n+1): start *= i
    return start

def facLib(n):
    from math import factorial
    return factorial(n)

#print(facRec(3))
#print(facRed(3))
#print(facLoop(3))
#print(facLib(3))
#print(facRec(0))
#print(facRed(0))
#print(facLoop(0))
#print(facLib(0))
#print(facRec(1))
#print(facRed(1))
#print(facLoop(1))
#print(facLib(1))

import timeit
#min(timeit.repeat(stmt="[facRec(n) for n in range(100)]", number = 1000, repeat = 5))
print(min(timeit.repeat('[facRec(i) for i in range(100)]', number = 1000, repeat =5, globals=globals())))
print(min(timeit.repeat('[facRed(i) for i in range(100)]', number = 1000, repeat =5, globals=globals())))
print(min(timeit.repeat('[facLoop(i) for i in range(100)]', number = 1000, repeat =5, globals=globals())))
print(min(timeit.repeat('[facLib(i) for i in range(100)]', number = 1000, repeat =5, globals=globals())))
