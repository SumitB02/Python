
'''
Treasure Map

Instructions

You are going to write a program which will mark a spot with an X.
The map is made of 3 rows of blank squares.

     1    2    3
1 ["⬜","⬜","⬜"]
2 ["⬜","⬜","⬜"]
3 ["⬜","⬜","⬜"]

Your program should allow you to enter the position of the treasure using a two-digit system.
The first digit is the verical column number and the second digit is the horizontal row number.

e.g.
Example Input 1

column 2,row 3 would be entered as:

23

Example Output 1

["⬜","⬜","⬜"]
["⬜","⬜","⬜"]
["⬜","X","⬜"]

Example Input 2

column 3,row 1 would be entered as:

31

Example Output 2

["⬜","⬜","X"]
["⬜","⬜","⬜"]
["⬜","⬜","⬜"]

e.g. When you hit run,this is what should happen:

["⬜","⬜","⬜"]
["⬜","⬜","⬜"]
["⬜","⬜","⬜"]
Where do you want to put the treasure? 32
["⬜","⬜","⬜"]
["⬜","⬜","X"]
["⬜","⬜","⬜"]

'''

# Don't change the code below

row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
position = input("Where do you want to put the treasure? ")
# Don't change the code above

# 23
# Write the code below this row

horizontal = int(position[0]) #2
vertical = int(position[1]) #3

selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"

# Write your code above this row

# Don't change the code below
print(f'{row1}\n{row2}\n{row3}')

# Output

'''

['⬜', '⬜', '⬜']
['⬜', '⬜', '⬜']
['⬜', '⬜', '⬜']
Where do you want to put the treasure? 23
['⬜', '⬜', '⬜']
['⬜', '⬜', '⬜']
['⬜', 'X', '⬜']

'''