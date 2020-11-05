n = int(input("Enter the number:"))

fact = 1
for num in range (1,n+1):
    fact *= num

print("The factorial is: ",fact)
