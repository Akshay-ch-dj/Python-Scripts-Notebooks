class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def showbook(self):
        print ("Name:", self.name)
        print("Price:", self.price)

Va = Book("JavaCompletePet", 480.5)        
Va.showbook()

class Reactangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area_of_rectangle(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.length * self.breadth)

Ar = Reactangle( 5, 4)
Ar. area_of_rectangle()

Va = Book("JavaCompletePet", 480.5)
Va.showbook()

setattr( Va, 'name', "Cool Book")
setattr( Va, 'price', 550)

Va.showbook()


print (hasattr( Va, 'name'))

print (Va.__dict__)
print(Va.__doc__)

print(Va.__module__)

