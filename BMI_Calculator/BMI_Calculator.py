"""
Body mass index (BMI) is a value derived from the mass (weight) and 
height of a person. 
The BMI is defined as the body mass divided by 
the square of the body height, and is expressed in units of kg/m2,
resulting from mass in kilograms and height in metres.
"""

# module for color text 
# https://pypi.org/project/termcolor/
# You can  download this module from above link
from termcolor import colored, cprint
cprint(f"         BMI CALCULATOR      ","blue","on_cyan",attrs=["bold"])
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
bmi = round((weight/height),2)
if (bmi<18.5):
    print(f"Your BMI is {bmi}")
    cprint("You are "+"Underweight","red")
elif (18.5<bmi<22.9):
    cprint("Normal")
elif("23.0 < bmi < 24.9"):
    cprint("Overweight","red")
