
data = [1,2,3]

itr = data.__iter__()

for x in data:
    print (x)


while True:
   try :
       e= next(itr)
       print (e)
   except StopIteration:
       break

