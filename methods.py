
class Employee():
    DEFAULT_DEPT="HR"
    DEFAULT_SALARY= 10000
    DEFAULT_AGE=18
    DEFAULT_DA=200

    def __init__(self, id, name, dept, basicSalary, da, age):
        self.id=id
        self.name=name
        self.department=dept
        self.basic=basicSalary
        self.da=da
        self.age=age

    def totalSalary(self):
        return self.basic+ ( self.da*30)

    @staticmethod
    def computeGaratvity(noYear, basic):
        return noYear*basic+ Employee.DEFAULT_DA

    @classmethod
    def createEmplyeeWithIdAndName(cls, id,name):
        print(cls)
        return cls(id,name, cls.DEFAULT_DEPT, cls.DEFAULT_SALARY ,cls.DEFAULT_DA,cls.DEFAULT_AGE)

    @classmethod
    def createEmplyeeWithIdAndNameAndDept(cls, id, name,dept):
       return cls(id, name, dept, 0, 0, 18)


e1= Employee.createEmplyeeWithIdAndName("123", "Kumar")
e2= Employee.createEmplyeeWithIdAndNameAndDept("222", "Tom", "HR")


print (e1.department)
print (e2.department)
print (e1.totalSalary())
print (Employee.computeGaratvity(10,20000))




