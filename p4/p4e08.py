def prime(x):
    if x <= 1:
        print('Only numbers larger than 1 are considered to be prime.')
        return False
    else:
        for i in range(2,int(x//2)):
            if x%i == 0:
                print(x, 'has factor', i,'.')
                return i
        print(x, 'is prime.')
        return 1

prime(8)
prime(3)
prime(13.0)
prime(-5)
