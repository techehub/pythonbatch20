class Car :

    def start(self):
        print("Starting Car")

    def accelerate(self):
        print("Accelerating Car")

    def stop(self):
        print("Stopping Car")

class Nano(Car):

    def start(self):
        print ("Starting Nano")

    def accelerate(self):
        print ("Accelerating Nano")

    def stop(self):
        print ("Stopping nano")


class Alto(Car):

    def start(self):
        super().start()
        print("Starting Alto")

    def accelerate(self):
        print("Accelerating Alto")

    def stop(self):
        print("Stopping Alto")


class Cycle():

    def start(self):
        print("Starting Cycle")

    def accelerate(self):
        print("Accelerating Cycle")

    def stop(self):
        print("Stopping Cycle")

'''
class Person():
    
    def drive (self, car):
        car.start()
        car.accelerate()
        car.stop()

'''

class Person ():

    def __init__(self, n, car):
        self.__name=n
        self.car= car

    def drive(self):
        self.car.start()
        self.car.accelerate()
        self.car.stop()


def main ():

    a1= Nano()
    p1= Person("Kumar", a1)
    p1.drive()

    print (p1.__dict__)
    p1.__name = "FGDFGDGFDGFDGF"

    print (p1.__dict__)

    p1.__name= "daasdasd"

    print (p1.__dict__)


'''
    setattr(p1,"name", "Sunny")
    print (getattr(p1, "name"))
    print (hasattr(p1, "name"))
    delattr(p1,"name")
    print(hasattr(p1, "name"))


    p1= Person()
    c1= Nano()
    c2 = Alto()
    c3 = Cycle()
    p1.drive(c1)
    p1.drive(c2)
    p1.drive(c3)
    '''

main()

