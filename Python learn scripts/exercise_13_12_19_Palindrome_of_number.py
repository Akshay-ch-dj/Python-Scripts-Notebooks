
n = int(input("Enter a number: "))

n1 = 0
n2 = n

while n2 != 0:
    r = n2%10
    n1 = n1*10 + r
    n2 = n2//10

print (n1)
print (n)
if n1 == n:
    print("The number is palindrome:")
else:
    print("The number is not palindrome")

