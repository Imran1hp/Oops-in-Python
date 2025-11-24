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


    def marks(self,Eng_marks,Maths_marks,Science_marks):
        self.eng_marks=Eng_marks
        self.maths_marks=Maths_marks
        self.science_marks=Science_marks
        self.precentage =((self.eng_marks+self.maths_marks+self.science_marks)/300)*100
        print("Stuent name", self.name)
        print("English:",self.eng_marks,"Maths:",self.maths_marks,"Science:",self.eng_marks,self.maths_marks,self.science_marks)
        print("Precentage:",self.precentage)

       


s1=Student(fullname="Imran",age='23',class_="C",id="98",rollno=38,gender="Male")
s1.marks(90,89,50)