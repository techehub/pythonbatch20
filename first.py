a= input("Enter num1#")
b=input("Enter num2#")
op= input ("Type#")

if op=='+':
    result= int (a)+ int (b)
    result = result+10
elif op=='-':
    result= int (a)- int(b)
elif op=='*':
    result= int (a)* int (b)
else:
    print ("Not defined")

print (result)

