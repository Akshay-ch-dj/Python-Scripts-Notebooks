"""
x = int(input("The number to be Factorized: "))

myList = []
for num in range (2,(x//2)): 
    if x % num == 0:
        print("The Factors are: ")
        while                                                                                 
        break
else:
    print ("The No. is Prime")
"""

x = int(input("The number to be Factorized: "))

myList = []

if x % 2 == 0:
    num = 2
    while x != 1:
        if x % num == 0:
            myList.append(num)
            num = x/num
    print(myList)
    
