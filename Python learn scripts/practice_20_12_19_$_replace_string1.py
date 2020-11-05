myStr = input("Enter a sentance containing letter 'a': ").lower()

print(myStr)
start = 0
for ind in range(0,len(myStr)):
    print (myStr[ind])
    if myStr[ind] == "a":
        L1 = myStr[start:ind]+ "$" 
        start = ind + 1

L1 = L1 + myStr[start::]
print (L1)
        
    
