import csv
class Item:
    payrate=0.8 #global attribute
    all=[]
    def __init__(self,name,price:int,quantity:int):
        self.name= name
        self.price= price
        self.quantity=quantity
        Item.all.append(self)
        #run validations with assert statement
        if price < 0:
            raise ValueError(f"Price must be non-negative, got {price}")
        if quantity < 0:
            raise ValueError(f"Quantity must be non-negative, got {quantity}")
    print("AN object created")
    

    def applydisc(self):
        return self.price*self.payrate
    def calcobj(self):
        return self.price*self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('oop.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for i in items:
            Item(
                name=i.get('name'),
                price= int(i.get('price')),
                quantity= int(i.get('quantity')),

            )
    @staticmethod
    def isinteger(num):
        #float checkming
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

    pass

class Phone(Item):
    pass
phone1=Phone("jscphonev10",500,5)
phone1.brokenphone=1
phone2=Phone("jscphonev10",700,5)
phone2.brokenphone=1

