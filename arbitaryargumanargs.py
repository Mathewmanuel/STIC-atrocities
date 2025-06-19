def add(*nums):
    total=""
    for num in nums:
        total+=num
    return total
print(add("nbrff","efreverf","ff"))

def baptism(*names):
    fullname=""
    for name in names:
        fullname+=name
    return fullname
print(baptism("Tarun","John","ranadheeran"))

def address(**addie):
    print("where the fuck the function")
    for key,values in addie.items():
        print(f"{key}:{values}")
print(address(street="Sri Nagar",Area="Mayiladuthurai", state="Tamil Nadu",country="India"))

def shippinglabel(*args,**kwargs):
    fullname=""
    for arg in args:
        fullname+=arg
    print(fullname)
    for key,value in kwargs.items():
        print(f"{key}:{value}\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
shippinglabel("Dr","Caroline","Victoria",
              homenum="12/54",street="Old State Bank Colony",Area="West Tambaram",City="Chennai",State="Tamil Nadu")

