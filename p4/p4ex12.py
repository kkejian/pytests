def facRec(n):
    if n==1: return 1
    else: return n*facRec(n-1)

def facRed(n):
    from functools import reduce
    return reduce(lambda x,y: x*y, range(1,n+1))

#def facLoop(n):

#def facLib(n):

print(facRec(3))
print(facRed(3))
