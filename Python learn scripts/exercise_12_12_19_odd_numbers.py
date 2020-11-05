l,u = input("Enter the lower and upper limits: ").split()

l = int(l)
u = int(u)

if l%2 == 0:
    l = l+1
for num in range (l,u,2):
    print ("{}, ".format(num),end = '')

print(1%10)
