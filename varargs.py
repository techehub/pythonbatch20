'''
def  add ( x,y ,*a):
    sum = 0
    for val in a:
        sum= sum +val
    return x+y+sum

'''

def add (a,*b,**val):
    print (a)
    print (b)
    print (val)
    return val['x'] + val ['y']

def greet (**val):
    print ( val ['message'], " ", val ['name'] )


def greeting (message, name):
    print (message, name)

res = add (10, 20, x=100, y=200)

greet (name= "Vijeesh", message= "Hello")
greeting ("Vijeesh", "Hello")
print (res)