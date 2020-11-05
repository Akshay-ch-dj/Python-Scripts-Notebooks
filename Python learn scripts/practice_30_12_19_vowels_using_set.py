str1 = input("Enter a string:")

vowels = set('aeiou')

count = 0
for letter in str1:
    if letter.lower() in vowels:
        count += 1
        
print ("no of vowels:", count)
