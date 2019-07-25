def add (a,b):
    sum =a+b
    return sum


s= add(10,10)


def calc(abc, a,b):
        res=abc(a,b)
        return res

def main ():
    a = int (input("Num1#"))
    b = int (input("Num2#"))
    op = input("Ops#")

    if (op == '+'):
        logic = lambda x,y : x+y
    elif (op == "-"):
        logic = lambda x,y : x-y
    elif (op == '*'):
        logic = lambda x,y : x*y
    elif(op== '/'):
        logic = lambda x,y : x/y
    else:
        print ("Invalid  Ops")

    res = logic (a,b)
    print (res)

    '''
    if (logic !=None ):
        res = calc(logic, x, y)
        print(res)
   '''
main ()
