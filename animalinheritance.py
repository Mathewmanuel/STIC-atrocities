class animal:
    def __init__(self,name,isalive,habitat,sleepytime):
        self.name=name
        self.isalive=isalive
        self.habitat=habitat
        self.sleepytime=sleepytime
    def eat(self):
        print(f"{self.name} loves to hunt for food")
    def sleep(self):
        print(f"{self.name} sleeps on average {self.sleepytime} hours a day")
class wilddogs(animal):
    def speak(self):
        print("BOW BOW")
class bigcat(animal):
    def speak(self):
        print("purrr")
    
class rodents(animal):
    def speak(self):
        print("grrrrr")
    
cat1=bigcat("Bobcats",True,"Global",16)
dog=wilddogs("Hyenas",True,"Savannah",8)
rat=rodents("Hamster",True,"Caucaus",14)
cat1.eat()
cat1.sleep()
cat1.speak()
dog.eat()
dog.sleep()
dog.sleep()
dog.speak()
rat.eat()
rat.sleep()
rat.speak()


