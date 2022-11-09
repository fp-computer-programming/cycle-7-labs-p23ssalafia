# Author: Sean Salafia  11.9.22

# set a list equal to x
x = [ "45", "54", "22"]

#check the length of x
#if the length is greater than 1, execute the code
#else, print an error message.
if len(x) > 2:
    x.sort ()
    print(x)

    print ("Printed below is the largest number in the sequence:")
    print (x[-1])

    print ("Printed below is the smallest number for the sequence:")
    print (x[0])
else:
    print("Error! This list is too short")