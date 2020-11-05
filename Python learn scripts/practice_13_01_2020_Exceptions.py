# Exception handling

try:
    fp = open("C:\\Users\\User1\\Desktop\\PYTHON Lrn\\IDLE FILES _AESTER\\abch.txt","r")
except:
    print ("File doesn't exists")
else:
    print ("File opened")
finally:
    print (" HE He Hu")
