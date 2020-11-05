L1 = [ 20, "And", 34, 56 ]
L2 = [ 1, 2, 3, 4, 5 ]
L3 = [ "Run", "Baby", "Run" ]

print (L1[0])
L2.append(L1[0] + L1[2])
print (L1 + L2)
NewList = L2 * 3
print(NewList)

for item in L2:
    print(f"{item} " , end = '')
print()
print(len(L3))
print (max(L2))
Lnew = L1.copy()
print (Lnew)
n = NewList.count(1)
print (n)
L2.insert(5,55)
print (L2)
L2.pop()
print (L2)

#Reversing The List

L1.reverse()
print(L1)

#Sorting List

L3.sort()
print (L3)

#Checking in List

if 20 in L1:
    print("Value Exists")

#Creating A List Using List Constructor(Converts String to Lists)

L4 = list("Anaconda")
print (L4)

L5 = list(("and" , "python", 34, "Nos"))
print(L5)
