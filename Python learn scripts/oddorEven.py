n = int(input('Enter a number'))



if n == 2 or n == 3:
    print (f'The number {n} is Prime')
    
else:
    i = 2
    while i < n/2:
        if n % i == 0:
            b = False
            break
        else:
            b = True
            i = i+1

    if b == True:
        print (f'The number {n} is Prime')
    else:
        print (f'The number {n} is not prime')
