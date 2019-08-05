import random
def outer (a, b):
    c= random.randint(143765836587435, 1003475683459798798)
    print ("c=",c)

    x=33
    y=444

    def inner ():
        return a+b +c

    return inner


f1= outer (10,20)
f2= outer (100,200)
print (f1)
print (f1())
print (f2())

print (f1.__closure__[0].cell_contents)
print (f1.__closure__[1].cell_contents)
print (f1.__closure__[2].cell_contents)

