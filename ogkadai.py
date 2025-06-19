class Item:
    payrate=0.8 #global attribute
    def __init__(self,name,price,discount:float,quantity=0):
        #run validations with assert statement
        assert price>0, f"this {price} sucks ass"
        print("AN object created")
        self.name= name
        self.price= price
        self.discount=discount
    def applydisc(self):
        return self.price*self.payrate
    def calcobj(self):
        return self.price*self.discount;
item1=Item("blender",44,0.25)
item1.payrate=0.7
print(item1.price)
print(item1.name)
print(item1.__dict__)
print(Item.__dict__)
print(item1.calcobj())
print(item1.applydisc())