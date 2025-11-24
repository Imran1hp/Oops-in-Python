class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,other):
        
        return self.price>other.price


ord1 = Order("Laptop",10000)
ord2 = Order("Mobile",50000)        

print(ord1>ord2)