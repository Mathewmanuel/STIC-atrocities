import csv

class Item:
    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    def calcobj(self):
        return self.price*self.quantity
class Phone(Item):
    all=[]
    def __init__(self, name, price, quantity,brokenphone):
        #super function nukku vanakkam
        super().__init__(
            name,price,quantity
        )
        assert brokenphone>= 0,f" broken {brokenphone} is not greater than or equal to zero!"
        
        self.brokenphone= brokenphone

        Phone.all.append(self)
        

phone1=Phone("jscphonev10",500,5,1)
print(phone1.calcobj())
phone2=Phone("jscphonev10",700,5,1)
print(Phone.all)