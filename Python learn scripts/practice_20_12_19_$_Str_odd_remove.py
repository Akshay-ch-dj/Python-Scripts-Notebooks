myStr = input("Enter a String: ")

Str = ""

for ind in range (2, len(myStr)):
    if ind%2 == 0:
        Str = Str  + myStr[ind]

print (myStr[0] + Str)
