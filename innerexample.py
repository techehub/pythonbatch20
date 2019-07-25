

def calc (a,b,op):

    def add ():
        print ( "sum is ", a+b)

    def diff ():
        print ("diff is ", a-b)

    if op =='+':
        add ()

    elif op=='-':
        diff()

def main ():
    x = int (input("Num1#"))
    y = int (input("Num2#"))
    op = input("Ops#")
    calc (x,y,op)

main ()





