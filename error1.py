
def div (a,b):
    return a/b


try :
    x= int(input("Num1:"))
    y= int(input("Num1:"))
    res= div (x,y)

except ValueError as e:
    print ("Please provide number as input")
    print (e)
except ZeroDivisionError as e:
    print("Please provide number grater than ZERO")
    print (e)
except Exception as e:
    print("Sorry ..somthing wrong")
    print(e)
else:
    print (res)
finally:
    print ("Completed")



