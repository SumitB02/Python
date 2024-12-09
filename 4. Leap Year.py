
'''

Day 3.3 Leap Year

Instructions

Write a program that works out whether if a given year is a leap year.
A normal year has 365 days,leap year has 366 days,with an extra day in February.
The reason why we have leap years is really fascinating.

This is how you work out whether if a particular year is a leap year.
     on every year that is divisible by 4 with no remainder
     except every year that is evenly divisible by 100 with no remainder
     unless the year is also divisible by 400 with no remainder

e.g. The year 2000
2000 / 4 = 500 (Leap)
2000 / 100 = 20 (Leap)
2000 / 400 = 5 (Leap)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:
2100 / 4 = 525 (Leap)
2100 / 100 = 21 (Not Leap)
2100 / 400 = (Not Leap)

Warning your output should match the Example Output format exactly including spelling and punctuation

Example Input 1
2400

Example Output 1
Leap Year

Example Input 2
1989

Example Output
Not Leap Year

e.g. When you hit run, this is what should happen

Which year do you want to check? 1200
Leap Year

'''


# Don't change the code below
year = int(input('Which year do you want to check? '))
# Don't change the code above

# Write your code below this line

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

