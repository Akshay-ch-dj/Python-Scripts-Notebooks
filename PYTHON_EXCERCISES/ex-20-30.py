# d = {'key1': 1, 'key2': 14, 'key3': 47}
# # sum1 = sum([d[key] for key in d])
# # sum1 = sum(d.values())
# # print(sum1)

# # for i in d:
# #     print(i)
# print(type(d.values()))
# print(type([d[key] for key in d]))

my_dict = {"A": [1, 2, 3], "B": [9, -4, 2], "C": [3, 99, 1]}

my_dict = {key : sum(my_dict[key]) for key in my_dict}

print(my_dict)