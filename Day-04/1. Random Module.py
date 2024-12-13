
# Random Module

import random


# Input

random_integer = random.randint(1,10)
print(random_integer)

# Output
# 9

# Input


random_float = random.random() * 5
print(random_float)

# Output
# 3.44816365277509

# Input
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

# Output
# Your love score is 16

# Coding Exercise : Heads or Tails

'''

Instructions

You are going to write a virtual coin toss program.It will randomly tell the user "Heads" or "Tails".

Important,the first letter should be capitalised and spelt exactly like in the example 
e.g. "Heads",not "heads".

There are many ways of doing this.You should generate a random number,either 0 or 1.
Then use that number to print out "Heads" or "Tails".

Example Output

Heads 

or 

Tails

'''

# Write your code below this line
# Hint : Remember to import the random module first.

import random

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# Output
# Tails

