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
product = 1
for keys in D1:
    sum = sum * D1[keys]
print ("Product: ",product)
