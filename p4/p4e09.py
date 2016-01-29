L = [2,4,9,16,25]

import math

def sqrFOR(L):
    ret = []
    for i in L:
        ret.append(math.sqrt(i))
    return ret

def sqrMAP(L):
    ret = L[:]
    return map(math.sqrt,ret)

def sqrCOM(L):
    return [math.sqrt(i) for i in L]

def sqrGEN(L):
    return (math.sqrt(i) for i in L)

print(list(sqrFOR(L)))
print(list(sqrMAP(L)))
print(list(sqrCOM(L)))
print(list(sqrGEN(L)))
