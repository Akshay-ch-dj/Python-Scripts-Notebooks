n = int(input("Enter a number:"))

count = 1
while n >= 10:
    n = n//10
    count += 1

print("The number of digits: ",count)
    
