
'''
# Pass command

for i in range (0,9):
    if i == 3:
        pass
        print (" Pass Here", end = '')
    else:
        print (f" {i}", end = '')
'''
# String Commands

myString = "India is my country"
myString2 = "I love my India"

print (myString.index("is"))
print (myString.find("is"))
print (myString.isalpha())
print (myString.isalnum())
print (myString.isdecimal())
print (myString.islower())
print (myString.isupper())
print (myString.isdigit())
print (myString.isspace())
print (myString.isidentifier())
print (myString.isnumeric())
print (myString.istitle())
print (myString.join(myString2))

S1 = "Kerivada Makkale"
S2 = "Anjooran"

print(S1.join(S2))
print (len(S1))
print (S1.lower())
print (S1.upper())

print (S1.replace("Kerivada","Odivada"))
print (S1.strip())
print (S1.split())
print (S1.startswith("Kerivada"))
print (S1.swapcase())
