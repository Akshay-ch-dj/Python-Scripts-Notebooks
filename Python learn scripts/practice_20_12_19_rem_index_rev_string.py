myStr = input("Enter a String: ")
n = int(input("Enter The index to remove: "))

print ("index Removed: ", myStr[0:n] + myStr[n+1::])

# To Change First and Last Charactr

print ("First and Last interchanged:", myStr[-1] + myStr[1:-1] + myStr[0])
