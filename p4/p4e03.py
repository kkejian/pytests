def adder(*varargs):
    tmp = list(varargs)
    for i in tmp[1:]: tmp[0] += i
    return tmp[0]

print(adder(2,3))
print(adder(2.5,3.14))
print(adder('Exper','Teach'))
