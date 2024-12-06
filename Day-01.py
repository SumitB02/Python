
# Input :
print(" Hello World! ")

print('\n')
'''

Output :
Hello World!

Day-01 Exercise :
Write a program that prints the some notes from the previous lesson using what you have learnt about the Python print function.

Warning : The output in your program should match the example output shown below exactly,character ,
          even spaces and symbols should be identical ,otherwise the tests won’t pass.

Example Output
When you run your program, it should print the following:
Day 1 – Python Print Function
The function is declared like this:
print(‘ what to print ’)
e.g. When you hit run,this is what should happen:

'''

# Write your code below this line:
print("Day 1 – Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print('\n')
# String Manipulation and Code Intelligence



# Input:
print("Hello World!\nHello World!\nHello World!")
print('\n')
'''
Output:
Hello World!
Hello World!
Hello World!
'''

# Input:
print("Hello" + "Sumit")
print('\n')
'''
Output:
HelloSumit
'''


# Input:
print("Hello"+ " " + "Sumit")
print('\n')
'''
Output:
Hello Sumit
'''

# String Concatenation:

# Input
#  print("Hello" + " " + "Sumit")
#  ^

# Output
# IndentationError: unexpected indent

# Input
# print("Hello" + " " + "Sumit)
#                            ^

'''
Output
SyntaxError: EOL while scanning string literal
'''

'''
# Input:
prnt("Hello" + " " + "Sumit")
^
Output:
IndentationError: unexpected indent

'''


'''

Day 1.2 Debugging Exercise

Instructions:
Look at the code editor on the left.There are errors in all of the line of code.Fix the code so that it runs without errors.

Warning: The output in your program should match the example output shown below exactly,
         character for character,even spaces and symbols should be identical,otherwise the tests won’t pass.


Example Output:
When you run your program it should print the following:
Day 1 – String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "World")
New lines can be created with a backslash and n.


# Fix the code below:
print(Day 1 – String Manipulation")
print("String Concatenation is done with "+" sign.")
print('e.g. print("Hello" + "world")')
print(("New lines can be created with a backslash and n.")

Output:
print(Day 1 – String Manipulation")  # line 1
         ^
SyntaxError : invalid syntax
print('e.g. print("Hello " + "world")') # line 3
IndentationError : unexpected indent


SyntaxError: unexpected EOF while parsing # line 7

'''

#Output :-
# 1. Missing double quotes before the word Day.
print("Day 1 – String Manipulation")
# 2. Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+ " sign.')
# 3. Extra indentation removed
print('e.g. print("Hello " + "world")')
# 4. Extra ( in print function removed.
print("New lines can be created with a backslash and n.")

# Input Function:

# input() function
# input(“A prompt for the user”)

# Single Line Comment
# input() will get user input in console
# Then print() will print the word “Hello” and the user input

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
Write a program that prints the number of characters in a user’s name. 
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
# If input was “Jack”
# 1st: print(len(“Jack”))
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

# Variable :

name = "Jack"
print(name)
print('\n')

# Output: Jack

name = "Apple"
print(name)
print('\n')

# Output: Apple

name = input("What is your name?")
length = len(name)
print(length)
print('\n')

'''

Output:
What is your name?Sumit
5


Day 1.4 Variable Exercise

Instructions: Write a program that switch the value stored in the variable a and b

Warning: Do not change the code on lines 1-4 and 15-18.Your program should work for different inputs
e.g. any value of a and b

Example Input
a: 3
b: 5

Example Output
a: 5
b: 3

e.g. When you hit run,this is what should happen:
a: 6
b: 9
a:9
b:6

Hint:
1.You should not have to type any numbers in your code.
2. You might need to make some more variables.

Output :

'''

# Don’t change the code below
a = input("a:")
b = input("b:")
# Don’t change the code above

###############################
# Write your code below this line
c = a
a = b
b = c

print("a:", a)
print("b:", b)
print('\n')

# Day 1 Project : Band Name Generator

# 1. Create a greeting for your program.
print("Welcome the band name Generator:")

# 2. Ask the user for the city that they grew up in.
city = input("Which city did you grew up in?\n")
print(city)

# 3. Ask the user for the name of a pet.
pet = input("What is the name of a pet?\n")

# 4. Combine the name of their city and pet and show them their band name
print("Your band name could be " + city + " " + pet)

# 5.Make sure the input cursor shows on a new line, see the example at:

'''

Output:
Welcome to the band name Generator.
Which city did you grew up in?
Belgium
What is the name of a pet?
King
Your band name could be Belgium King

'''