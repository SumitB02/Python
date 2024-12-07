
# Mathematical Operation

print(int(8 / 3))
# Output: 2

print(round(8 / 3))
# Output: 2.6666666667

print(int(8 / 3))
# Output: 2

print(round(8 / 3, 2))
# Output: 2.67

print(round(2.6666666666,2))
# Output: 2.66

print(8 // 3)
# Output: 2

print(type(8 // 3))
# Output: < class 'int' >


print(type(8 / 3))
# Output: < class 'float' >


print(type(4 / 2))
# Output: < class 'float' >


result = 4 / 2
result /= 2
print(result)
Output: 1.0

# Number Manipulation and F Strings

score = 0
height = 1.8
isWinning = True

# User scores a point

score += 1
print(score)
print("Your score is " + str(score))

# f-string

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

'''

Day 2.3 Life in Weeks

Exercise

Your Life in Weeks

Instructions

I was reading this article by Tim Urban Your Life in Weeks and realised just how
little time we actually have.Create a program using maths and f-strings that
tells us how many days,months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time
left in this format.You have x days,y weeks,and z month left.Where x, y and z
are replaced with the actual calculated numbers.

Warning

your output should match the 

Example Output

format exactly,even the positions of the comments and full stops.

Example Input:
56

Example Output:

You have 12410 days, 1768 weeks, and 408 months left

e.g.When you hit run, this is what should happen.

# 1 year = 365 days
# 1 year = 52 weeks
# 1 years = 12 month

'''

# Don’t chane the code below
age = input("What is your current age ?")
# Don’t change the code above

# Write your code below this line

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(months_remaining)
message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months"
print(message)

