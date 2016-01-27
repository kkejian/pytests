def prime(p):
    if p <= 1:
        print('Only numbers larger than 1 are consideres to be prime.')
        return False
    else:
        for i in range(2,y//2):
            if y%i == 0:
                print(y, ' has factor ', i,'.')
                return i
        print(y, 'is prime.')
        return 1
