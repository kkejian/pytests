import time, math
start = time.time()
def timetotal(func, *args, _rep=1000, **kargs):
    start = time.time()
    for i in range(_rep):
        ret = func(*args, **kargs)
    return (time.time() - start, ret)

res = timetotal(math.sqrt, 9345)
print(list(res))

def timebest(func, *args, _rep=5, **kargs):
    best = 


