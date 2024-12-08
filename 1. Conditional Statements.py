
'''

Conditional Statements

if-else statements

if-else :

if condition:
    do this
else:
    do this

'''


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry ,you have to grow taller before you can ride.")

'''
Comparision Operator

   Operator                  Meaning

     >                       Greater than
     <                       Less than
     >=                      Greater than or equal to
     <=                      Less than or equal to
     ==                      Equal to
     !=                      Not Equal to

'''

# Day 3.1 Odd or Even Exercise

'''

Odd or Even

Instructions

Write a program that works out whether if a given number is an odd or even number.

Even number can be divided by 2 with no remainder.
e.g. 86 is even because 86/2 = 43

43 does not have any decimal places.Therefore the division is clean.
e.g. 59 is odd because 59/2 = 36.875
36.875 is not a whole number,it has decimal places.
Therefore there is a remainder of 0.875,so the division is not clean.

The module is written as a percentage sign (%) in Python.It gives you the remainder after a division.
e.g.

6 / 2 = 3 with no remainder
6 % 2 = 0 

5 / 2 = 2 * 2 + 1 , remainder is 1.
5 % 2 = 1

14 / 4 = 3 * 4 + 2, remainder is 2
14 % 4 =2

Warning your output should match the Example Output format exactly even the positions of the commas and full stops.

Example Input 1
43

Example Output 1
This is an Odd number.

Example Input 2
94

Example Output 2
This is an Even number.

e.g. When you hit run,this is what should happen.
Which number do you want to check? 35
This is an odd number.

'''

# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

# Write your code below this line

if number % 2 == 0:
    print("This is a even number.")
else:
    print("This is a odd number.")
