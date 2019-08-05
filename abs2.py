class Person ():

    def __init__(self, name, age):
        self.__name=name
        self._age= age
        self.mark =100


    def setName(self,name):
        self.__ name=name


class Student (Person):
    def display(self):
        #print (self.__name)
        print (self._age)


p1= Student("Anil", 22)
print (p1.__dict__)

p1._age= 34
p1.mark=120
p1.setName("Anand")


print (p1.__dict__)