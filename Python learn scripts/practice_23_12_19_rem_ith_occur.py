#Remove the i'th occurence of a Given word from list

myList = input("Enter the words: ").split()

print (myList)

rWord, i = input("Enter the word to remove and its iteration: ").split()
i = int(i)

newList = []
count = 0
for word in myList:
    if word == rWord:
        count += 1
        if count == i:
            continue
        newList.append(word)
        
    else:
        newList.append(word)

print (newList)

