'''
list1= [1,2,3,4,5]
list2= [3,3,2,4,2, 5]
list3= [3,3,2,4,2]

x = zip (list1,list2, list3)
print (x)
for x, y, z in zip (list1,list2,list3):
    print (x,y,z)


mysum = [ (x , y ) for x,y in zip(list1, list2) ]
#print (mysum)
'''
keys = ["name", "age", "mark"]
values =["Anil", 23, [22,33,55]]

'''
z= zip (keys, values)
print (z)
for x in z :
   print (x)

'''

mydic = { key: value for key,value in zip(keys,values) }
print (mydic)

