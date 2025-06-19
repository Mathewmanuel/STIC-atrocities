#dundnermethod are also known as magic methods
#often automatically called by python builtins
# to get values
class book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
# to print the values instead of the locatioin of an object
    def __str__(self):
        return f"{self.title} by {self.author}"
# to help python check if 2 objects are equal
    def __eq__(self,other):
        return self.title==other.title and self.author==other.author
    def __lt__(self,other):
        return self.pages<other.pages
    def __gt__(self,other):
        return self.pages<other.pages
    def __add__(self,other):
        return f"{self.pages+ other.pages} pages"
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self,key):
        if key=='Title':
            return self.title
        elif key =='Author':
            return self.author
        elif key == 'Pages':
            return self.pages
        else:
            return f"{key} not found"

book1=book("God of Small Things","Arundhati Roy",300)
book2=book("The Power of the Subconcious mind","Thomas moore",400)
book3=book("Animal Farm","George Orwell",65)
book4=book("Animal Farm","George Orwell",56)

print(book1)
print(book2)
print(book1==book2)
print(book3==book4)
print(book2<book3)
print(book2>book3)
print(book1+book2)
print("God" in book1)
print("Animal" in book2)
print(book1['Author'])
