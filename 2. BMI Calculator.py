
'''

Day 2.2 BMI Calculator Exercise

BMI Calculator

Instructions :
Write a program that calculates the Body Mass Index (BMI) from a user’s weight and height.

The BMI’s is a measure of some’s weight into account their height.
e.g. If a tall person and a short person both weight the same amount,the short person is usually more overweight.

The BMI is calculated by dividing a person’s weight (in kg) by the square of their height (in m):
   BMI = weight(kg)/ height2(m2)

Warning you should convert the result to a whole number.

Example Input:
Weight =80
Height =1.75

Example Output:
80 / 1.75 * 1.75 = 26.122448979591837

e.g. When you hit run, this is what should happen

enter your height: 1.8
enter your weight: 65
20

Hint:

1.	Check the data type of the inputs
2.	Try to use the exponent operator in your code.
3.	Remember PEMDAS
4.	Remember to round your result to the nearest whole number

'''

# Don’t change the code below
height = input("Enter the height in m: ")
weight =input("Enter the weight in kg: ")
# Don’t change the code above

# Write your code below this line
weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = int(weight)/float(height) **2

# or using multiplication and PEMDAS
bmi_as_int = int(bmi)
print(bmi_as_int)
