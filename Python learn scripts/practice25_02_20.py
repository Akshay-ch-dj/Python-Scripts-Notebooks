# Print rectangle l =x, b= y

x,y = input("Enter length and breadth: ").split()
x = int(x)
y = int(y)

for n in range(x+1):
    for z in range(y+1):
        print ('* ', end="")
    print ("")
