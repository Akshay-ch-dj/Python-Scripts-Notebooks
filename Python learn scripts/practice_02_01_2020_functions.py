def mc():
    msg = "Has to Python"
    print (msg)
    return msg
print (mc())

# Global scope

def calc(*arg):
    sum = 0
    for i in arg:
        sum += i
        print ("sum: ",sum)

sum = 0
sum = calc(10,20,30)
print (sum)
