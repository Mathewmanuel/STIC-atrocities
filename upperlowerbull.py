class Item:
    def calculatesum(self,x,y):
        return x*y;

item1= Item()
#assigning attributes to objectitem1 of Item class
item1.name="phone"
item1.price=100
item1.quantity=5
print(item1.calculatesum(item1.price,item1.quantity))
item2 = Item()
item2.name="iphone"
item2.price=1000
item2.quantity=13

print(type(item1))
randomstr="aaaa"
print(randomstr.upper())
