class student :
    def __init__(self,name,roll):
        self.name =name
        self.roll = roll




s1 = student("imran",39)
del s1.name
print(s1.name)
print(s1.roll)

# private and  public

class person:
    def __init__(self,name):
        self.name = name

    def __hello(self):
        print("hello",self.name)

    def welcome(self):
        self.__hello()    

p1 =person("imran")
print(p1.name)
p1.__hello()
p1.welcome()       