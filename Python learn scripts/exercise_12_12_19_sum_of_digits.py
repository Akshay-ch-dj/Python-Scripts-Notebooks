#For finding the sum of digits in a number
n = int(input("Enter a number"))

n1 = 0

while n != 0:
    r = n%10
    n1 = n1 + r
    n = n//10

print (n1)
