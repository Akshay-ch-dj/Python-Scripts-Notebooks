n = int(input("Enter a number:"))

count = 0
for num in range (1,n+1):
    count += num

print(f"The sum of first {n} numbers is {count}")
