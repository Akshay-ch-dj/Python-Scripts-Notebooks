a = ["1", 1, "1", 2]

# ex-14: Remove duplicates from list a
a = list(set(a))
print(a)

# ex-15: Create a dictionary that contains the keys a  and b  and their respec
# tive values 1  and 2 .

my_dict = {"a":1, "b":2}
print(my_dict)
print(type(my_dict))
# Add "c":3 to dictionary
my_dict["c"] = 3
print(my_dict)
my_dict2 = dict([("a",1), ("b",2)])
print(my_dict2)

# ex-16: Please complete the script so that it prints out the value of key b .
d = {"a": 1, "b": 2}

print(d["b"])

# ex-17: Calculate the sum of the values of keys a  and b .
d = {"a": 1, "b": 2, "c": 3}

sum = d["a"] + d["b"]
print(sum)

# ex-19: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary 
# and print out the new dictionary.

d = {"a": 1, "b": 2}

d["c"] = 3
print(d)

# ex-20: Calculate the sum of all dictionary values.
d = {"a": 1, "b": 2, "c": 3}

sum = 0
for keys in d.keys():
    sum += d[keys]
print(sum)

## There is simple oneliner
# print(sum(d.values()))
# print(sum(d.values()))

d = {'key1': 1, 'key2': 14, 'key3': 47}
sum1 = [d[key] for key in d.keys()]
print(sum1)
