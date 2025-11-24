class Employ:
    def __init__(self,roll,dept,salary):
        self.roll = roll
        self.dept= dept
        self.salary=salary
    def details(self):
     print("Roll: ",self.roll)
     print("dept: ",self.dept)
     print("salary: ",self.salary)

class Engineer(Employ):
    def __init__(self,name,age,dept,salary):
        self.name=name
        self.age=age
        super().__init__("Engineer",dept,salary,)


emp1 = Employ("imran","IT",50000)

emp2 = Engineer("imran",23,"Sales",400000)
emp2.details()     