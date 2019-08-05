class MyRange():

    def __init__(self, start, end , increment):
        self.start= start
        self.end =end
        self.increment = increment
        self.current = start

    def __iter__(self):
        print ("Iter is called")
        return self

    def __next__(self):
        print ("Self called")
        self.current = self.current+ self.increment
        if self.current <= self.end:
            return self.current
        else :
            raise StopIteration()


o = MyRange (0,100,5)
#itr= o.__iter__()
#print (next(o))
#print (next(o))

for x in o:
    print (x)
