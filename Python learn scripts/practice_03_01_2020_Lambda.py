# Lambda Exercise

def table(n):
    return lambda a:a * n
n = int(input("Enter a number: "))
b = table(n)  # Now b gets the lambda value
for i in range(1,11):
    print (n," x ",i," = ", b(i))
