"""
print("Enter the marks of five subjects in 100: ")


myList = []
for mark in range(0,5):
    myList.append(int(input()))
print("The subjects which passed: ")

for item in range(0,5):
    if myList[item] >= 40:
        print(myList[item])    
""" 

print("Enter the marks of five subjects in 100: ")

m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

Total = m1+m2+m3+m4+m5
print("Total Marks: ", Total)

if (m1 < 40 or m2< 40 or m3< 40 or m4< 40 or m5< 40):
    print("Failed!")
else:
    if Total >= (500*0.9):
        print ("All Pass with grade: A+")
    elif (500*0.8) <= Total <= (500*0.9):
        print ("All Pass with grade: A")
    elif (500*0.7) <= Total <= (500*0.8):
        print ("All Pass with grade: B+")  
    elif (500*0.6) <= Total <= (500*0.7):
        print ("All Pass with grade: B")
    elif (500*0.5) <= Total <= (500*0.6):
        print ("All Pass with grade: C+")
    elif (500*0.4) <= Total <= (500*0.5):
        print ("All Pass with grade: C")
