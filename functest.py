def add (a,b):
    return a+b

def diff (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    return a/b

def calc(func, a,b):
        res=func(a,b)
        return res

def main ():
    x = int (input("Num1#"))
    y = int (input("Num2#"))
    op = input("Ops#")

    if (op == '+'):
        logic = add
    elif (op == "-"):
        logic = diff
    elif (op == '*'):
        logic = mul
    elif(op== '/'):
        logic = div
    else:
        print ("Invalid  Ops")

    if (logic !=None ):
        res = calc(logic, x, y)
        print(res)

main ()
