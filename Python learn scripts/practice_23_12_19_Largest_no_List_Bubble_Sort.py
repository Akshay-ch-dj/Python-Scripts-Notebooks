#Entering Input

n = int(input("Enter the no of elements in List: "))
print(f"Enter the List of {n} numbers: ")

myList = []
for num in range (n):
    myList.append(int(input())) 

print (myList)

#Finding the largest Number

larNo = myList[0]

for num in range(0,n-1):
    if larNo < myList[num+1]:
        larNo = myList[num+1]

print ("The Largest Number: ", larNo)

    
#Finding the Second largest Number

myNList = myList.copy()

myNList.pop(myNList.index(larNo))

n = len(myNList)

slarNo = myNList[0]

for num in range(0,n -1):
    if slarNo < myNList[num+1]:
        slarNo = myNList[num+1]

print ("The Second-Largest Number: ",slarNo)
 
#Sorting

n = len(myList)
for i in range(n):
    for j in range (0, n-i-1):
        if myList[j] > myList[j + 1]:
            myList[j], myList[j+1] = myList[j+1], myList[j]
            
print ("Sorted List: ", myList)
print ("Largest Number : ",myList[-1],", Second-Largest Number: ",myList[-2])
