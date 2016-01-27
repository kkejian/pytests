def adder(*args,**kargs):
    tmp = list(args) + list(kargs.values())
    for i in tmp[1:]: tmp[0] += i
    return tmp[0]

print(adder(2,3))
print(adder(2.5,3.14))
print(adder('Exper','Teach'))
print(adder(2,3,a=4,b=100))
print(adder('Ich',' habe',a=' Hunger',b='!'))
#print(adder(1,' habe',a=' Hunger',b='!'))
