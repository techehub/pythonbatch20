
def myfunc():
    print ("aaaaaaaa")
    yield 1

    print ("bbbbbbbb")
    yield 2

    print ("cccccccc")
    yield 3

print (myfunc())

'''
res= myfunc()
itr = iter(res)
print (next(itr))
print (next(itr))


for x in myfunc():
    print (x)
    
'''