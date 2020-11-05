str1 = input("Enter string 1:").lower()
str2 = input("Enter string 2:").lower()

CLetter = set()

for letter in str1:
    if letter not in str2:
        CLetter.add(letter)

print (CLetter)
