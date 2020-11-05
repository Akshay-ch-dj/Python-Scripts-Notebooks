#Occurance of a word in text file

Text = open("abc.txt","r")
d = dict()    #Dictionary to store words(keys) and its iterations(values)
# iterate through each line in txt file
for line in Text:
    line = line.strip() #remove leading space and \n chrtr
    line = line.lower() #convert to lower case
    words = line.split(" ") # Spilit line with space
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print (key, ":", d[key])
