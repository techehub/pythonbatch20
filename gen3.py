def myrange (start,end, incr):
    num= start

    while (num <end):
        num = num +incr
        yield num


mylist = myrange(0,1000000000099373987938457937495739487534,2)

for x in mylist:
    print (x ,"===>>", x**x)

