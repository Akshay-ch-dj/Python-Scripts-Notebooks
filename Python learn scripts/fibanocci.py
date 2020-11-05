n = int(input('Enter the number of terms'))

t1 = 0
t2 = 1

for i in range (1,n):
    print (t1 , end ='')
    next = t1 + t2
    t1 = t2
    t2 = next
