s1 = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday'}
s2 = {'Monday', 'Wednesday', 'June'}

print (s1 | s2)
print (s1 & s2)

print (s1.intersection(s2))

s3 = {2, 3, 4, 5}
s4 = {4, 5}

if s3 > s4:
    print (s3 - s4)
    
print (s4.issubset(s3))
myList = [1,2,3,4,5,6]

mySet = set(myList)

print (mySet)

mySet.update([8])# Pass elements as list


mySet.add(7)
print (mySet)
mySet.remove(7)
print (mySet)

mySet.discard(6)# Error shows when there is no element
mySet.pop()
print (mySet)

s = "amma"

Se3 = set(s)

print (Se3)
