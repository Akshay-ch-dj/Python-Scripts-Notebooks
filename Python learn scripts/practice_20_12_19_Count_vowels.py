myStr = input("Enter a String: ").lower()

Vowel = [ "a", "e", "i", "o", "u" ]
count = 0
for letter in myStr:
    if letter in Vowel:
        count += 1

print ("The no of Vowels: ", count)
