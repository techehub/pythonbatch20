class Student ():

    def __init__(self,name, rollNo, mark):
        self.name=name
        self.rollNo=rollNo
        self.mark=mark

    def __mul__(self, other):
        return Student ( self.name+ "," + other.name,
                         self.rollNo+ "," + other.rollNo,
                         self.mark - other.mark)


    def __gt__(self, other):
        return  self.mark > other.mark

    def __eq__(self, other):
        if self.rollNo == other.rollNo and self.name== other.name :
            return True
        else :
            return False



s1= Student("Tom",  "111", 120)
s2= Student ("Tom",  "111", 150)
s3= Student ("Kumar","333", 150)

total = s1 * s2 * s3
print (total.name)
print (total.rollNo)
print (total.mark)


if (s1==s2):
    print (s1.name , "is grater")

else :
    print (s2.name , "is grater")


if (s1==s2):
    print ("BOTH are same")