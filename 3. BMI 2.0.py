
'''

BMI Calculator 2.0

Instructions

Write a program that interprets the Body Mass Index(BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

  Under 18.5 they are underweight.
  Over 18.5 but below 25 they have a normal weight.
  Over 25 but below 30 they are overweight.
  Over 30 but below 35 they are obese.
  Above 35 they are clinically obese.


The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

       BMI = weight (kg) / height**2 (m**2)

Warning you should round the result to the nearest whole number.
The interpretation message needs to include the words in bold from the interpretations above
e.g. underweight,normal weight,overweight,obese,clinically obese.

Example Input

weight = 80
height = 1.75

Example Output

85 / 1.75 * 1.75 = 27.755102040816325
Your BMI is 28,you are slightly overweight.

e.g. When you hit this is what should happen:

     enter your height in m: 1.8
     enter your weight in kg: 89
     Your bmi is 27, you are slightly overweight.

Hint:

Try to use the exponent operator in your code.
Remember to round your result to the nearest whole number.
Make sure you include the words in bold from the interpretations.

'''

# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

# Write your code below this line

bmi =round( weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")

'''

 Output:

enter your height in m: 1.8
enter your weight in kg: 89
Your bmi is 27, you have a normal weight.

'''



