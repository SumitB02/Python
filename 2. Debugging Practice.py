
# String Manipulation and Code Intelligence

# Input:
print("Hello World!\nHello World!\nHello World!")

'''
Output:
Hello World!
Hello World!
Hello World!
'''

# Input:
print("Hello" + "Sumit")

'''
Output:
HelloSumit
'''


# Input:
print("Hello"+ " " + "Sumit")

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

