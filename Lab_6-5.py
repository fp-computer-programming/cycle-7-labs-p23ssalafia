# Author: Sean Salafia  11.9.22

# set a list equal to x


x = ["23", "20", "10"]
#check the length of x
#if the length is greater than 1, execute the code
#else, print an error message.
x.sort (reverse = True)

if len(x) > 2:
      print ("Printed below is the smallest number in the sequence:")
      print (x[-1])
      print ("Printed below is the largest number for the sequence:")
      print (x[0])
else:
    print("Error! This list is too short")

if x[-1] != x[0]:
   print("List meets specifications!")
else:
   print("Error! List does not meet specification!")


