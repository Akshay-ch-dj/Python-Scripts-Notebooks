# Concatinate 2 dictionary

def Dic_input():
    my_dict = dict()
    n = int(input("Enter the number of items in the dictionary: "))
    while n != 0:
        key = input("Enter Key: ")
        value = input("Enter value: ")
        my_dict[key] = value
        n = n-1
    return (my_dict)

print ("Enter Dictionary 1:")
D1 = Dic_input()
print ("Enter Dictionary 2:")
D2 = Dic_input()
D1.update(D2)
print (D1)
