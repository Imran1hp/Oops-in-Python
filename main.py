class Student:
    college_name ="Luand University"
    def __init__(self,fullname, age,gender, class_, id,rollno):
        self.name=fullname
        self.age=age
        self.gender=gender
        self.class_ =class_
        self.id=id
        self.rollno=rollno
        print("New student added.....")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Class:",self.class_)
        print("ID:",self.id)
        print("Roll no:",self.rollno)
       


s1=Student(fullname="Imran",age='23',class_="C",id="98",rollno=38,gender="Male")
s2=Student(fullname="Ali",age='22',class_="A",id="48",rollno=98,gender="Male")

