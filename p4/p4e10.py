import time, math
start = time.time()
def timetotal(func, *args, _rep=1000, **kargs):
    start = time.time()
    for i in range(_rep):
        ret = func(*args, **kargs)
    return (time.time() - start, ret)


#def timebest(func, *args, _rep=5, **kargs):
#    best = 2 ** 32
#    for i in range(_rep):
#        start = time.time()
#        ret = func(*args, **kargs)
#        elapsed = start - time.time()
#        if elapsed < best: best = elapsed
#    return (best, ret)
    
def timebesttotal(func, *args, _reppr=10000, _rounds=10, **kargs):
    return min([timetotal(func, *args, _rep=_reppr, **kargs) for i in range(_rounds)])

res = timebesttotal(math.sqrt, 9345)
print(list(res))
res2 = timebesttotal(pow, 9345, .5)
print(list(res2))
res3 = timebesttotal(lambda x: x ** 0.5, 9345)
print(list(res3))

