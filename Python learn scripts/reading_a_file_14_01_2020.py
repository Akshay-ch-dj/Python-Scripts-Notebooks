# Reading a file

f = open("abc.txt","w")
# Adding Content
for i in range(5):
    f.write("How are you ahh! line number: {}\n".format(i+1))
f.close()

f = open("abc.txt","r")
print (f.read())

f.close()
# To appendthe file open in a+ mode

f = open("abc.txt","a+")
for line in range(6,9):
    f.write("This is line number: {}\n".format(line))
f.close()

f = open("abc.txt","r")
print (f.read())
