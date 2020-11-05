num = int(input("Enter The number to be Prime Factorized: "))

myList = []
while num % 2 == 0:
    myList.append(2)
    num = num / 2
    
for i in range(3, int(num ** (1/2))+1, 2):
    while num % i == 0:
        myList.append(i)
        num = num/i

if num > 2:
    myList.append(num)
print (myList)

