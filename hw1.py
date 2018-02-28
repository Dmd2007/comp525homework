"""This program calculates the area of a circle given the radius"""

radius = float(input('Enter Radius: '))
PI = 3.14159265359
area = PI * radius * radius

print("The area of your circle is= %.2f" %area)

print(" ")


"""This program calculates the miles per gallon of a car given miles and gallons"""

miles = input("Enter amount of miles: ")
miles = float(miles)
 
gallons = input("Enter amount of gallons: ")
gallons = float(gallons)
 
milesper = miles / gallons
print("You get: ", milesper, "mpg")

print(" ")


"""This program calculates the sum of odd numbers given n"""

oddnumbers = int(input("Insert a number to calculate the sum: "))
total = sum(range(1, oddnumbers+1, 2))

print("The sum of the odd numbers in your range is: ", sum)

print(" ")

"""This program tells whether a number is odd or not"""

n = int(input("Enter a number to determine if it is odd or even: "))
if (n % 2) == 0:
   print("{0} True".format(n))
else:
   print("{0} False".format(n))

print(" ")



"""This program prints 10 random numbers from 0 to 9"""

import random
print(random.randint(0,9), random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

print(" ")

"""This program calculates the average of 10 randome numbers.
    How many times it does this is entered by the user.  
    The program then returns the integer of how many random numbers are averaged"""

import random
n=int(input("Enter the amount of numbers to be averaged: "))
a=[]
for i in range(0,n):
    rand=random.randint(0,9)
    a.append(rand)
avg=sum(a)/n
print("The average of your random numbers are: ",round(avg,2))

print(" ")
