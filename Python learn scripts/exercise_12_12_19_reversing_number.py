"""
#2 Reversing a Given number

num = int(input("Enter a three digit number"))
  ##Reversing
n1 = num % 10
n2 = (num // 10) % 10
n3 = num // 100

print (n1 * 100 + n2 *10 + n3)
print (num // 10)

"""
#For any number better logic
n = int(input("Enter a number"))

n1 = 0

while n != 0:
    r = n%10
    n1 = n1*10 + r
    n = n//10

print (n1)

