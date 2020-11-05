#Default Arguments

def showme(name,age = 25):
    print ("name: {0}, Age: {1}".format(name,age))

name = "Akshay"
showme (name)

#Variable Length Arguments

def Listname(*name):
    for i in name:
        print (i)
   

Listname(input("name: "))
