# Author: Sean Salafia  11.9.22

#user inputs numeric values

a = int(input("Input a numeric value: "))
b = int(input("Input a numeric value: "))
c = int(input("Input a numeric value: "))

x = [a, b, c]
#check if all statements are even, if not, check if all are odd, if neither, print mixed
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("All of your numbers are even numbers!")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("All of your numbers are odd numbers!")
else:
    print("Your list of numbers is mixed")
