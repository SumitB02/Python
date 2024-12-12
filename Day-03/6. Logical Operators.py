
'''

Logical Operators

AND Operators
OR Operators
NOT Operators

if condition1 & condition2 & condition3:
    do this
else:
    do this

'''

# Day 3.5 Love Calculator Exercise

'''

Instructions

You are going to write a program that tests the compatibility between two people.
We're going to use the super scientific method recommended by Buzzfeed

To work out the love score between two people:
Take both people's names and check for the number of times the letters
in the world TRUE occurs.Them check for the number of times the letters 
in the word LOVE occurs.Then combine these numbers to make a 2 digit number.

This BuzzFeed article gives more details on this:

For LoveScores less than 10 or greater than 90,the message should be:
  "Your score is x, you go together like coke and mentos." 
  
For LoveScores between 40 and 50,the message should be:
  "Your score is y, you are alright together."
  
Otherwise the message
"Your score is z."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"


T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53
print: "Your score is 53."

Example Input 1

name1 = "Kanye West"
name2 = "Kim Kardashian"


Example Output1
Your score is 42, you are alright together.

Example Input2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"

Example Output

Your score is 73.


e.g. When you hit run,this is what should happen:
     
     Welcome to the Love Calculator
     What is your name?
     Kanye West
     What is their name?
     Kim Kardashian
     Your score is 42,you are alright together.


Hint :

1. The lower() function changes all the letters in a string to lower case.
2. The count() function will give you the number of times a letter occurs in a string.

'''

# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below this line

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score},you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

