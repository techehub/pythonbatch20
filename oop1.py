class Student(object):
    def __init__(self, name, rollNo, m1,m2,m3,m4):
        self.name= name
        self.rollNo=rollNo
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
        self.mark4=m4

    def total (self):
        return self.mark1 + self.mark2 + self.mark3 + self.mark4

    def avg (self):
        return self.total()/4

    def display(self):
        print("Name ::", self.name)
        print("Roll No ::", self.rollNo)
        print("Mark1 ::", self.mark1)
        print("Mark2 ::", self.mark2)
        print("Mark3 ::", self.mark3)
        print("Mark4 ::", self.mark4)
        print("Total ::", self.total())
        print("Average ::", self.avg())
        print ("===============================")

    def __str__(self):
        return self.name + ":" + self.rollNo


class OnlineStudent (Student):
    def __init__(self, name, rollNo, m1, m2, m3, m4, coupon):
        super().__init__(name, rollNo, m1, m2, m3, m4,)
        self.coupon= coupon

    def display(self):
        print ("Coupon ::", self.coupon)
        super().display()



s1= Student("Kumar","1111", 22,33,44,55)
s2= Student("Anil", "2222", 23,33,43,53)
s3= Student("Sunny", "333", 25,35,45,56)
s4= OnlineStudent("AAAA", "5555", 66,77,88,44,"ABCD")

s4.display()
