Dict1 = {'100':"Kerala", "200":"Karnadaka"}
print (Dict1)

imp = {"name":"Alen", "Age":20, "Salary":2000}

for i in imp:
    print (i)

print ("______________")
for i in imp.values():
    print (i)

for a,b in imp.items():
    print (a, ":", b)

print (len(imp))

print (str(imp))

dic2 = imp.copy()

print (imp.get('name'))

imp.pop('Age')

print (imp)

print (set(dic2)| set(imp))
