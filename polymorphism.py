class Complex:
    def __init__(self, real,img):
        self.real =real
        self.img =img

    def show_number(self):
        print(self.real,"i"," + ",self.img ,"j")


    def __add__(self , other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal,newImg)
    def __sub__(self ,other):
        newReal = self.real - other.real
        newImg = self.img - other.img
        return Complex(newReal,newImg)

num1 = Complex(2,3)
num2 = Complex(4,5)

num3 = num1+num2
num4 = num1 - num2

num3.show_number()
num4.show_number()