def copyDict(d): return dict(zip(d.keys(),d.values()))
D = dict(zip('abc',range(3)))
D2 = copyDict(D)
D['a'] = 99

def addDict(d1,d2):
    if type(d1) == type(dict()):
        D=copyDict(d1)
        for i in d2.keys(): D[i] = d2[i]
        return D
    else:
        return d1[:] + d2[:]

print(list(D.items()))
print(list(D2.items()))

D3 = dict(zip('cde',range(1,4)))
print(list(addDict(D,D3).items()))
l1, l2 = list(range(3)), list(range(1,4)) 
print(list(addDict(l1,l2)))
print(l1)
print(l2)
