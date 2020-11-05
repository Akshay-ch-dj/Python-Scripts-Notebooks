a = int(input('number 1: '))
b = int(input('number 2: '))
c = int(input('number 3: '))
if a > b and a > c:
    print ('{} is larger'.format(a))

elif b > c and b > a:
    print ('{} is larger'.format(b))

else:
    print ('{} is larger'.format(c))
