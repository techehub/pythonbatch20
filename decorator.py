def outer (f):
    def inner (*x,**y):
        print ("=========")
        f(*x, **y)
        print ("=========")
    return inner

@outer
def hello():
    print ("Hello")

@outer
def hai ():
    print ("Hai")

@outer
def calc (a,b):
    print (a+b)

@outer
def greet ( **data ):
    print ( data["message"] , data["name"])

hello()
hai()
calc(20,30)
greet(name="Kumar", message="Good morning")


'''
f1= outer (calc)
f2= outer (greet)
f1(10,10)
f2("Kumar")
'''

