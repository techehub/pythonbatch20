x=10
y=100

def something ():
    global x
    x=20
    y=200
    print ("something x-", x)
    print("something y-", y)

    def other ():
        nonlocal y
        y =300
        print ("other y", y)

    other ()
    print("something y-", y)



print ("global", x)
something()
print ("global", x)
