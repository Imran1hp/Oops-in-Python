class Account:

    def __init__(self,name,account_no,balance):
        self.name= name
        self.account_no = account_no
        self.balance = balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Rs",amount,"Deposited Successfully")


    def withdraw(self,amount):
        self.balance = self.balance - amount
        print("Rs",amount,"Withdraw Successfully")  


    def balance_(self):
        print("Your Current Balance is Rs",self.balance)
    

customer1 = Account("Imran",1234,1000)

customer1.deposit(1000)
customer1.withdraw(500)
customer1.balance_()
customer1.deposit(500)