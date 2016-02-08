def ctdn(n):
    if n > 0:
        print(n)
        ctdn(n-1)
    else:
        print('stop')

#ctdn(5)
#ctdn(-1)
#ctdn(0)
#ctdn(99)

print(list((i for i in range(5,0,-1))))

