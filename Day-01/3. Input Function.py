
# Input Function:

# input() function
# input("A prompt for the user")

# Single Line Comment
# input() will get user input in console
# Then print() will print the word "Hello" and the user input

print("Hello " + input("What is your name?"))
print('\n')

'''
Output:
What is your name?Sumit
Hello Sumit

'''

'''
Day 1.3 Inputs Exercise

Instructions :
Write a program that prints the number of characters in a user's name. 
You might need to Google for a function that calculates the length of a string.

Warning : Your program should work for different inputs e.g. any name that you input.
Example Input
Sumit
Example Output
5
e.g. When you hit run, this is what should happen:
What is your name?

Hint :
1.	You can put functions inside other functions.
2.	Don’t try to print anything other than the length.

'''

# Write your code below this line
# This code prints the numbers of characters in a user’s name.

print(len(input("what is your name?")))
print('\n')

# Notes :
# If input was "Jack"
# 1st: print(len("Jack"))
# 2nd: print(4)

# Input:
name = input("What is your name?")
print(name)
print('\n')

'''
Output:
What is your name?Sumit
Sumit

'''
