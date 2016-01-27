def adder(*varargs):
    sum = varargs[:0]
    [sum +=i for i in varargs]
    return sum

print(adder(2,3))
print(adder(2.5,3.14))
print(adder('Exper','Teach'))
