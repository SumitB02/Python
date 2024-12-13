
# List

# It is the way of organising and storing data in Python.

states_of_america = ['Delaware','Pennsylvania','New Jersey','Georgia','Connecticut',
                     'Massachusetts','Maryland','South Carolina']

print(states_of_america)
# ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina']


print(states_of_america[0]) # +ve indexing
# Delaware

print(states_of_america[1])
# Pennsylvania

print(states_of_america[-1])# -ve indexing it will print item from the end of list
# South Carolina

print(states_of_america[-2])
# Maryland

states_of_america[1] = "Pencilvania"
print(states_of_america)
# ['Delaware', 'Pencilvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina']

states_of_america.append('Angelaland') # add item at the end of the list
print(states_of_america)
# ['Delaware', 'Pencilvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'Angelaland']

states_of_america.extend(['Jack Bauer Land',"Land"])
print(states_of_america)
# ['Delaware', 'Pencilvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts',
#  'Maryland', 'South Carolina', 'Angelaland', 'Jack Bauer Land', 'Land']


# Index Errors and Working with Nested Lists

# print(states_of_america[15])
# IndexError: list index out of range

# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states])
# IndexError: list index out of range

num_of_states = len(states_of_america)
print(states_of_america[num_of_states-1])
# Land

# dirty_dozen = ['Strawberries','Spinach','Kale','Nectarines','Apples','Grapes','Peaches','Cherries','Pears','Tomatoes','Celery','Potatoes']

fruits = ['Strawberries','Nectarines','Apples','Grapes','Peaches','Cherries','Pears']
vegetables = ['Spinach','Kale','Tomatoes','Celery','Potatoes']

dirty_dozen = [fruits,vegetables]
print(dirty_dozen)
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'],
#  ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]



'''
Instructions

You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everyone's food bill.

Important : You are not allowed to use the choice() function.

Splits the string name_string into individual names and put them inside a List called names.
this to work,you must enter all the names as name followed by comma then space e.g. name,name,name

Example Input

Ben, Jenny, Michael, Chloe

Example Output

Michael is going to buy the meal today!

e.g. When you hit run,this is what should happen :
     Give me everybody names,seperated by a comma.
     Ben is going to buy a meal today!
     

Hint

You might need the help of the len() function.
Remember the list starts from 0

'''

import random

# Split string method

names_string = input('Give me everybody names,seperated by a comma.')
names = names_string.split(',')
# Don't change the code above

# Write your code below this line

# Get the total number of items in list
num_items = len(names)

# Generate random numbers between 0 and the last index
random_choice = random.randint(0,num_items-1)
person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")