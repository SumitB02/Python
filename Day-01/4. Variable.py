
# Variable :

name = "Jack"
print(name)

# Output: Jack

name = "Apple"
print(name)

# Output: Apple

name = input("What is your name?")
length = len(name)
print(length)

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

