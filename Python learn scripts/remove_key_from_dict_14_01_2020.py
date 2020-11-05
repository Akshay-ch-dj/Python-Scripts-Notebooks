# Concatinate 2 dictionary

def Dic_input():
    my_dict = dict()
    n = int(input("Enter the number of items in the dictionary: "))
    while n != 0:
        key = input("Enter Key: ")
        value = int(input("Enter value: "))
        my_dict[key] = value
        n = n-1
    return (my_dict)

print ("Enter Dictionary:")
D1 = Dic_input()

while True:
    try:
        K = input("Enter the key you want to remove: ")
        del D1[K]
        print ("Updated Dictionary: ", D1)
        break
    except:
        print ("The key entered not valid: ")
