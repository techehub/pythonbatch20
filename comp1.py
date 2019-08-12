list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]

new_data = {x:y for x,y in zip (list1,list2)}
print (new_data)


'''

newlist =[]
for x in list:
   if x%2==0:
       newlist.append(x)

print (newlist)

'''

newlist = ((x,y) for x in range(10000000) if x%2!=0   for y in range (1000000) if y%2==0  )
print (newlist)

'''
for x in newlist:
    print (x)
'''

