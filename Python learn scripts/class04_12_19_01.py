#Functions

def showtxt (name):
    print ( "My Name is",name)

showtxt ("Kerala")

#Sum function

def sum_of (a,b):
    print ("The sum is:", a+b)
    return (a + b)

sum_of (5,6)

print (sum_of (5,6))

class Display_and_invert (text):

    def __init__ (self, name):
        self.name = name
    def showtxt (self):
        print ( "My Name is",self.name)
        

    
