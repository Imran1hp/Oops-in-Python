## Single Inheritance
class Car:
   @staticmethod
   def start():
       print("started")

   @staticmethod
   def stop():
       print("stopped")     



class Handa(Car):
    def __init__(self,name):
        self.name = name



car1= Handa("Honda City")
car2 = Handa("Honda Civic")

print(car1.name)
car1.start()



## Multiple Inheritance 

class A :
    varA ="Welcome of class A"

class B:
    varB = "Welcome of class B"


class C(A,B):
    varC = "Welcome of class C"




c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)



class Person:
    name = "Imran"
    def change_name(self,name):
        self.__class__.name = name


p1 = Person()
p1.change_name("ALi")
print(p1.name)
print(Person.name)