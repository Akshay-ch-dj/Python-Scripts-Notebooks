myStr = input("Enter a sentance containing letter 'a': ").lower()

print(myStr)
start = 0
for ind in range(0,len(myStr)):
    print (myStr[ind])
    if myStr[ind] == 'a':
        L1 = myStr[start:ind]
        L2 = L1 + "$"
        start = ind + 1

L2 = L2 + myStr[start::]
print (L2)
        
    
