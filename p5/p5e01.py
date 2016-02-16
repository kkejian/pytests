import io

def countLines(fo):
    ctr = 0
    if not isinstance(fo, io.TextIOWrapper):
        fo = open(fo)
    else:
        fo.seek(0)
    for i in fo: ctr += 1
    return ctr

def countChars(fo):
    ctr = 0 
    if not isinstance(fo, io.TextIOWrapper):
        fo = open(fo)
    else:
        fo.seek(0)
    for i in fo: ctr += len(i)
    return ctr

def test(name):
    fo = open(name)
    return countLines(fo), countChars(fo)

if __name__ == '__main__':
    import sys
    if len(sys.argv) is 1:
        print(test(input("Please enter a filename: ")))
    else:
        for i in sys.argv[1:]:
            print(test(i))
