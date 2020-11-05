x,y,z = input("Enter the Amount, Period and Rate :").split()
print ("The interest Rate for {} years for an amount {} at a rate of {} is:".format(int(y),int(x),float(z)))
print ("{}".format(int(x)*int(y)*int(z)/100))
