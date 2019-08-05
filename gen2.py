
def myrange (start,end, incr):
    num= start
    while (num <end):
        num = num +incr
        yield num

itr = iter(myrange(0,100,2))
print (next (itr))
print (next (itr))
print (next (itr))
print (next (itr))
print (next (itr))


'''
for x in myrange(0,100,2):
    print (x)

'''