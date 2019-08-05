class A :
 def display(self):
     print ("A")

class B:
   def display(self):
       print("B")

class C (A,B):
   def display(self):
       print("C")

class D (A,B):
   def display(self):
       print("C")


class X (C,D):
   pass

obj= X()
obj.display()
print (X.mro())


