#for i in range (1,11): 
 #   print ("%d * 5 = %d" %(i,i*5))

# Printing Pattern

for i in range (1,5):
    for j in range (0,i):
        print ( " * ", end = '' )

    print ('')     #NExt line

# For - Else loop
for i in range (5,1,-1):
    for j in range(0,i):
         print ( " * ", end = '' )

    print ('')     #NExt line

for i in range(50, 100, 2):
    
    print (i)
else:
    print (" No breaks")

print (" Values")

#While loop

i = 10
while i < 25:
    print (i)
    i = i+1
    
# Displaying Date and time current
# The continue statement

i =1
while i < 20:
    if i == 6:
        print ('Hai')
        continue
    print (i)
    i = i+2
