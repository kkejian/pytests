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

