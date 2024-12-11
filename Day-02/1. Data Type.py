
print(len("Hello"))
# 5

# print(len(12345))
# TypeError : object of type ‘int’ has no len()

# Data Type

# Strings

"Hello"
print("Hello"[0])

# Output
# H

print("Hello"[4])
# o

print("123" + "345")
# 123345

print("hello" + "world")
# helloworld

# Integer

print(123 + 345)

# Output
# 468

# Large Integers

'''
342,654,896
123_456_789

'''

# Float
print(3.14159)

# Output
# 3.14159

# Boolean

'''
True
False

'''


'''

Day 2.1 Data Types Exercise

Data Types
Instructions:
Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35,then the output should be 3+5=8

Warning :
Do not change the code on line 1-3. Your program should work for different inputs.
e.g. any two-digit number.

Example Input
39

Example Output
3+9 = 12
12

e.g. When you hit run, this is what should happen:
Type a two digit number: 26
8

Hint:
1.Try to find out the data type of two_digit_number.
2. Think about what you learnt about subscipting.
3. Think about type conversion.

'''

# Don’t change the code below
two_digit_number =input("Type a two digit number")
# Don’t change the code above

###################################
# Write your code below this line

# Check the data type of two_digit_number
print(type(two_digit_number))

#  Output:
#  <class 'str'>

# Get the first and second digit using subscripting then convert string to int

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(type(first_digit))
print(type(second_digit))

# Add the two digit together
result = first_digit + second_digit
print(result)

'''
Output:
Type a two digit number: 87
15

'''

# new_num_char =str(num_char)
# print(“Your name contains ” + new_num_char + “characters”)

a=float(123)
print(type(a))
# Output: <class 'float'>

print(70 + float(100.5))
# Output : 170.5

print(str(70) + str(100))
# Output : 70100

print(3+5)
print(7-4)
print(3*2)
print(6/3)
print(2**3)

'''
PEMDAS
()
**
*   /
+   -

'''

print( 3 * 3 + 3 / 3 - 3)
# Output : 7.0

print(3 * (3 + 3) / 3 - 3)
# Output : 3.0
